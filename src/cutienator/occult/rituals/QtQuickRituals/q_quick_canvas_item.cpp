//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/6.12.0/QtQuick/private/qquickcanvasitem_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtQuick/qtquickglobal.h>
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#if QT_CONFIG(quick_canvas)
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qquickcanvasitem_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qrect.h>
#include <QtCore/qsize.h>
#include <QtQuick/qquickitem.h>
#include <QtCore/qpoint.h>
#include <QtCore/qvariant.h>
#include <QtCore/qmetaobject.h>
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <private/qsgadaptationlayer_p.h>
#include "qquickcanvasitem_p.h"
#include <private/qquickitem_p.h>
#include <private/qquickcanvascontext_p.h>
#include <private/qquickcontext2d_p.h>
#include <private/qquickcontext2dtexture_p.h>
#include <private/qsgadaptationlayer_p.h>
#include <qsgtextureprovider.h>
#include <QtQuick/private/qquickpixmap_p.h>
#include <QtGui/QGuiApplication>
#include <qsgtextureprovider.h>
#include <qqmlinfo.h>
#include <private/qqmlengine_p.h>
#include <QtCore/QBuffer>
#include <QtCore/QDir>
#include <QtCore/qdatetime.h>
#include <private/qv4value_p.h>
#include <private/qv4functionobject_p.h>
#include <private/qv4scopedvalue_p.h>
#include <private/qv4jscall_p.h>
#include <private/qv4qobjectwrapper_p.h>
#include <private/qjsvalue_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtdeclarative/src/quick/items/context2d/qquickcanvasitem.cpp, line 768, as _ZNK16QQuickCanvasItem17isTextureProviderEv
inline bool QQuickCanvasItem::isTextureProvider() const
{
    return true;
}

//  from ../qtdeclarative/src/quick/items/context2d/qquickcanvasitem.cpp, line 624, as _ZN16QQuickCanvasItem14schedulePolishEv
inline void QQuickCanvasItem::schedulePolish()
{
    auto polishRequestEvent = new QEvent(QEvent::PolishRequest);
    QCoreApplication::postEvent(this, polishRequestEvent);
}

//  from ../qtdeclarative/src/quick/items/context2d/qquickcanvasitem.cpp, line 596, as _ZN16QQuickCanvasItem5eventEP6QEvent
inline bool QQuickCanvasItem::event(QEvent *event)
{
    switch (event->type()) {
    case QEvent::PolishRequest:
        polish();
        return true;
    default:
        return QQuickItem::event(event);
    }
}

//  from ../qtdeclarative/src/quick/items/context2d/qquickcanvasitem.cpp, line 1194, as _ZN16QQuickCanvasItem9tiledRectERK6QRectFRK5QSize
inline QRect QQuickCanvasItem::tiledRect(const QRectF &window, const QSize &tileSize)
{
    if (window.isEmpty())
        return QRect();

    const int tw = tileSize.width();
    const int th = tileSize.height();
    const int h1 = window.left() / tw;
    const int v1 = window.top() / th;

    const int htiles = ((window.right() - h1 * tw) + tw - 1)/tw;
    const int vtiles = ((window.bottom() - v1 * th) + th - 1)/th;

    return QRect(h1 * tw, v1 * th, htiles * tw, vtiles * th);
}
//  -----------------------------------------------------------------------

//  Only a class built on QQuickCanvasItem may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQQuickCanvasItem : QQuickCanvasItem {
  using QQuickCanvasItem::event;
};

//  A QQuickCanvasItem that Python can take functions over in. Every QQuickCanvasItem
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if QT_CONFIG(quick_canvas)
typedef bool (*CuteQQuickCanvasItemCall0)(const void *, int *);
#endif  // QT_CONFIG(quick_canvas)
#if QT_CONFIG(quick_canvas)
typedef void * (*CuteQQuickCanvasItemCall1)(const void *, int *);
#endif  // QT_CONFIG(quick_canvas)
#if QT_CONFIG(quick_canvas)
typedef void (*CuteQQuickCanvasItemCall2)(const void *, int *);
#endif  // QT_CONFIG(quick_canvas)
#if QT_CONFIG(quick_canvas)
typedef void (*CuteQQuickCanvasItemCall3)(const void *, int, const QQuickItem::ItemChangeData *, int *);
#endif  // QT_CONFIG(quick_canvas)
#if QT_CONFIG(quick_canvas)
typedef void (*CuteQQuickCanvasItemCall4)(const void *, int *);
#endif  // QT_CONFIG(quick_canvas)
#if QT_CONFIG(quick_canvas)
typedef void * (*CuteQQuickCanvasItemCall5)(const void *, QSGNode *, QQuickItem::UpdatePaintNodeData *, int *);
#endif  // QT_CONFIG(quick_canvas)
#if QT_CONFIG(quick_canvas)
typedef void (*CuteQQuickCanvasItemCall6)(const void *, const QRectF *, const QRectF *, int *);
#endif  // QT_CONFIG(quick_canvas)
#if QT_CONFIG(quick_canvas)
typedef void (*CuteQQuickCanvasItemCall7)(const void *, int *);
#endif  // QT_CONFIG(quick_canvas)
#if !defined(QT_NO_QOBJECT)
#if QT_CONFIG(quick_canvas)
typedef bool (*CuteQQuickCanvasItemCall8)(const void *, QEvent *, int *);
#endif  // QT_CONFIG(quick_canvas)
#endif  // !defined(QT_NO_QOBJECT)
typedef const QRectF * (*CuteQQuickCanvasItemCall9)(const void *, int *);
typedef const QRectF * (*CuteQQuickCanvasItemCall10)(const void *, int *);
typedef bool (*CuteQQuickCanvasItemCall11)(const void *, const QPointF *, int *);
#if QT_CONFIG(im)
typedef const QVariant * (*CuteQQuickCanvasItemCall12)(const void *, int, int *);
#endif  // QT_CONFIG(im)
typedef void (*CuteQQuickCanvasItemCall13)(const void *, int *);
typedef void (*CuteQQuickCanvasItemCall14)(const void *, QKeyEvent *, int *);
typedef void (*CuteQQuickCanvasItemCall15)(const void *, QKeyEvent *, int *);
#if QT_CONFIG(im)
typedef void (*CuteQQuickCanvasItemCall16)(const void *, QInputMethodEvent *, int *);
#endif  // QT_CONFIG(im)
typedef void (*CuteQQuickCanvasItemCall17)(const void *, QFocusEvent *, int *);
typedef void (*CuteQQuickCanvasItemCall18)(const void *, QFocusEvent *, int *);
typedef void (*CuteQQuickCanvasItemCall19)(const void *, QMouseEvent *, int *);
typedef void (*CuteQQuickCanvasItemCall20)(const void *, QMouseEvent *, int *);
typedef void (*CuteQQuickCanvasItemCall21)(const void *, QMouseEvent *, int *);
typedef void (*CuteQQuickCanvasItemCall22)(const void *, QMouseEvent *, int *);
typedef void (*CuteQQuickCanvasItemCall23)(const void *, int *);
typedef void (*CuteQQuickCanvasItemCall24)(const void *, int *);
#if QT_CONFIG(wheelevent)
typedef void (*CuteQQuickCanvasItemCall25)(const void *, QWheelEvent *, int *);
#endif  // QT_CONFIG(wheelevent)
typedef void (*CuteQQuickCanvasItemCall26)(const void *, QTouchEvent *, int *);
typedef void (*CuteQQuickCanvasItemCall27)(const void *, QHoverEvent *, int *);
typedef void (*CuteQQuickCanvasItemCall28)(const void *, QHoverEvent *, int *);
typedef void (*CuteQQuickCanvasItemCall29)(const void *, QHoverEvent *, int *);
#if QT_CONFIG(quick_draganddrop)
typedef void (*CuteQQuickCanvasItemCall30)(const void *, QDragEnterEvent *, int *);
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
typedef void (*CuteQQuickCanvasItemCall31)(const void *, QDragMoveEvent *, int *);
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
typedef void (*CuteQQuickCanvasItemCall32)(const void *, QDragLeaveEvent *, int *);
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
typedef void (*CuteQQuickCanvasItemCall33)(const void *, QDropEvent *, int *);
#endif  // QT_CONFIG(quick_draganddrop)
typedef bool (*CuteQQuickCanvasItemCall34)(const void *, QQuickItem *, QEvent *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickCanvasItemCall35)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickCanvasItemCall36)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickCanvasItemCall37)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickCanvasItemCall38)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickCanvasItemCall39)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickCanvasItemCall40)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQQuickCanvasItem : public QQuickCanvasItem {
public:
  using QQuickCanvasItem::QQuickCanvasItem;
  void *taken[41] = {};

  bool take(const char *key, void *call) {
#if QT_CONFIG(quick_canvas)
    if (!std::strcmp(key, "_ZNK10QQuickItem17isTextureProviderEv")) {
      taken[0] = call;
      return true;
    }
#endif  // QT_CONFIG(quick_canvas)
#if QT_CONFIG(quick_canvas)
    if (!std::strcmp(key, "_ZNK10QQuickItem15textureProviderEv")) {
      taken[1] = call;
      return true;
    }
#endif  // QT_CONFIG(quick_canvas)
#if QT_CONFIG(quick_canvas)
    if (!std::strcmp(key, "_ZN16QQmlParserStatus17componentCompleteEv")) {
      taken[2] = call;
      return true;
    }
#endif  // QT_CONFIG(quick_canvas)
#if QT_CONFIG(quick_canvas)
    if (!std::strcmp(key, "_ZN10QQuickItem10itemChangeENS_10ItemChangeERKNS_14ItemChangeDataE")) {
      taken[3] = call;
      return true;
    }
#endif  // QT_CONFIG(quick_canvas)
#if QT_CONFIG(quick_canvas)
    if (!std::strcmp(key, "_ZN10QQuickItem12updatePolishEv")) {
      taken[4] = call;
      return true;
    }
#endif  // QT_CONFIG(quick_canvas)
#if QT_CONFIG(quick_canvas)
    if (!std::strcmp(key, "_ZN10QQuickItem15updatePaintNodeEP7QSGNodePNS_19UpdatePaintNodeDataE")) {
      taken[5] = call;
      return true;
    }
#endif  // QT_CONFIG(quick_canvas)
#if QT_CONFIG(quick_canvas)
    if (!std::strcmp(key, "_ZN10QQuickItem14geometryChangeERK6QRectFS2_")) {
      taken[6] = call;
      return true;
    }
#endif  // QT_CONFIG(quick_canvas)
#if QT_CONFIG(quick_canvas)
    if (!std::strcmp(key, "_ZN10QQuickItem16releaseResourcesEv")) {
      taken[7] = call;
      return true;
    }
#endif  // QT_CONFIG(quick_canvas)
#if !defined(QT_NO_QOBJECT)
#if QT_CONFIG(quick_canvas)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[8] = call;
      return true;
    }
#endif  // QT_CONFIG(quick_canvas)
#endif  // !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZNK10QQuickItem12boundingRectEv")) {
      taken[9] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK10QQuickItem8clipRectEv")) {
      taken[10] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK10QQuickItem8containsERK7QPointF")) {
      taken[11] = call;
      return true;
    }
#if QT_CONFIG(im)
    if (!std::strcmp(key, "_ZNK10QQuickItem16inputMethodQueryEN2Qt16InputMethodQueryE")) {
      taken[12] = call;
      return true;
    }
#endif  // QT_CONFIG(im)
    if (!std::strcmp(key, "_ZN16QQmlParserStatus10classBeginEv")) {
      taken[13] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem13keyPressEventEP9QKeyEvent")) {
      taken[14] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem15keyReleaseEventEP9QKeyEvent")) {
      taken[15] = call;
      return true;
    }
#if QT_CONFIG(im)
    if (!std::strcmp(key, "_ZN10QQuickItem16inputMethodEventEP17QInputMethodEvent")) {
      taken[16] = call;
      return true;
    }
#endif  // QT_CONFIG(im)
    if (!std::strcmp(key, "_ZN10QQuickItem12focusInEventEP11QFocusEvent")) {
      taken[17] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem13focusOutEventEP11QFocusEvent")) {
      taken[18] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem15mousePressEventEP11QMouseEvent")) {
      taken[19] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem14mouseMoveEventEP11QMouseEvent")) {
      taken[20] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem17mouseReleaseEventEP11QMouseEvent")) {
      taken[21] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem21mouseDoubleClickEventEP11QMouseEvent")) {
      taken[22] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem16mouseUngrabEventEv")) {
      taken[23] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem16touchUngrabEventEv")) {
      taken[24] = call;
      return true;
    }
#if QT_CONFIG(wheelevent)
    if (!std::strcmp(key, "_ZN10QQuickItem10wheelEventEP11QWheelEvent")) {
      taken[25] = call;
      return true;
    }
#endif  // QT_CONFIG(wheelevent)
    if (!std::strcmp(key, "_ZN10QQuickItem10touchEventEP11QTouchEvent")) {
      taken[26] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem15hoverEnterEventEP11QHoverEvent")) {
      taken[27] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem14hoverMoveEventEP11QHoverEvent")) {
      taken[28] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem15hoverLeaveEventEP11QHoverEvent")) {
      taken[29] = call;
      return true;
    }
#if QT_CONFIG(quick_draganddrop)
    if (!std::strcmp(key, "_ZN10QQuickItem14dragEnterEventEP15QDragEnterEvent")) {
      taken[30] = call;
      return true;
    }
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
    if (!std::strcmp(key, "_ZN10QQuickItem13dragMoveEventEP14QDragMoveEvent")) {
      taken[31] = call;
      return true;
    }
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
    if (!std::strcmp(key, "_ZN10QQuickItem14dragLeaveEventEP15QDragLeaveEvent")) {
      taken[32] = call;
      return true;
    }
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
    if (!std::strcmp(key, "_ZN10QQuickItem9dropEventEP10QDropEvent")) {
      taken[33] = call;
      return true;
    }
#endif  // QT_CONFIG(quick_draganddrop)
    if (!std::strcmp(key, "_ZN10QQuickItem21childMouseEventFilterEPS_P6QEvent")) {
      taken[34] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[35] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[36] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[37] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[38] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[39] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[40] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

#if QT_CONFIG(quick_canvas)
  //  bool QQuickCanvasItem::isTextureProvider() const
  bool isTextureProvider() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQQuickCanvasItemCall0 call = reinterpret_cast<CuteQQuickCanvasItemCall0>(taken[0]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QQuickCanvasItem::isTextureProvider();
  }
#endif  // QT_CONFIG(quick_canvas)

#if QT_CONFIG(quick_canvas)
  //  QSGTextureProvider *QQuickCanvasItem::textureProvider() const
  QSGTextureProvider *textureProvider() const override {
    if (taken[1]) {
      int handled = 0;
      CuteQQuickCanvasItemCall1 call = reinterpret_cast<CuteQQuickCanvasItemCall1>(taken[1]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QSGTextureProvider *>(given);
    }
    return QQuickCanvasItem::textureProvider();
  }
#endif  // QT_CONFIG(quick_canvas)

#if QT_CONFIG(quick_canvas)
  //  void QQuickCanvasItem::componentComplete()
  void componentComplete() override {
    if (taken[2]) {
      int handled = 0;
      CuteQQuickCanvasItemCall2 call = reinterpret_cast<CuteQQuickCanvasItemCall2>(taken[2]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickCanvasItem::componentComplete();
  }
#endif  // QT_CONFIG(quick_canvas)

#if QT_CONFIG(quick_canvas)
  //  void QQuickCanvasItem::itemChange(QQuickItem::ItemChange a0, const
  //      QQuickItem::ItemChangeData &a1)
  void itemChange(
      QQuickItem::ItemChange a0,
      const QQuickItem::ItemChangeData &a1) override {
    if (taken[3]) {
      int handled = 0;
      CuteQQuickCanvasItemCall3 call = reinterpret_cast<CuteQQuickCanvasItemCall3>(taken[3]);
      call(this, static_cast<int>(a0), &a1, &handled);
      if (handled) return;
    }
    QQuickCanvasItem::itemChange(a0, a1);
  }
#endif  // QT_CONFIG(quick_canvas)

#if QT_CONFIG(quick_canvas)
  //  void QQuickCanvasItem::updatePolish()
  void updatePolish() override {
    if (taken[4]) {
      int handled = 0;
      CuteQQuickCanvasItemCall4 call = reinterpret_cast<CuteQQuickCanvasItemCall4>(taken[4]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickCanvasItem::updatePolish();
  }
#endif  // QT_CONFIG(quick_canvas)

#if QT_CONFIG(quick_canvas)
  //  QSGNode *QQuickCanvasItem::updatePaintNode(QSGNode *a0,
  //      UpdatePaintNodeData *a1)
  QSGNode *updatePaintNode(
      QSGNode *a0,
      QQuickItem::UpdatePaintNodeData *a1) override {
    if (taken[5]) {
      int handled = 0;
      CuteQQuickCanvasItemCall5 call = reinterpret_cast<CuteQQuickCanvasItemCall5>(taken[5]);
      void * given = call(this, a0, a1, &handled);
      if (handled) return static_cast<QSGNode *>(given);
    }
    return QQuickCanvasItem::updatePaintNode(a0, a1);
  }
#endif  // QT_CONFIG(quick_canvas)

#if QT_CONFIG(quick_canvas)
  //  void QQuickCanvasItem::geometryChange(const QRectF &newGeometry,
  //      const QRectF &oldGeometry)
  void geometryChange(
      const QRectF &newGeometry,
      const QRectF &oldGeometry) override {
    if (taken[6]) {
      int handled = 0;
      CuteQQuickCanvasItemCall6 call = reinterpret_cast<CuteQQuickCanvasItemCall6>(taken[6]);
      call(this, &newGeometry, &oldGeometry, &handled);
      if (handled) return;
    }
    QQuickCanvasItem::geometryChange(newGeometry, oldGeometry);
  }
#endif  // QT_CONFIG(quick_canvas)

#if QT_CONFIG(quick_canvas)
  //  void QQuickCanvasItem::releaseResources()
  void releaseResources() override {
    if (taken[7]) {
      int handled = 0;
      CuteQQuickCanvasItemCall7 call = reinterpret_cast<CuteQQuickCanvasItemCall7>(taken[7]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickCanvasItem::releaseResources();
  }
#endif  // QT_CONFIG(quick_canvas)

#if !defined(QT_NO_QOBJECT)
#if QT_CONFIG(quick_canvas)
  //  bool QQuickCanvasItem::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[8]) {
      int handled = 0;
      CuteQQuickCanvasItemCall8 call = reinterpret_cast<CuteQQuickCanvasItemCall8>(taken[8]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QQuickCanvasItem::event(event);
  }
#endif  // QT_CONFIG(quick_canvas)
#endif  // !defined(QT_NO_QOBJECT)

  //  QRectF QQuickItem::boundingRect() const
  QRectF boundingRect() const override {
    if (taken[9]) {
      int handled = 0;
      CuteQQuickCanvasItemCall9 call = reinterpret_cast<CuteQQuickCanvasItemCall9>(taken[9]);
      const QRectF * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QQuickItem::boundingRect();
  }

  //  QRectF QQuickItem::clipRect() const
  QRectF clipRect() const override {
    if (taken[10]) {
      int handled = 0;
      CuteQQuickCanvasItemCall10 call = reinterpret_cast<CuteQQuickCanvasItemCall10>(taken[10]);
      const QRectF * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QQuickItem::clipRect();
  }

  //  bool QQuickItem::contains(const QPointF &point) const
  bool contains(const QPointF &point) const override {
    if (taken[11]) {
      int handled = 0;
      CuteQQuickCanvasItemCall11 call = reinterpret_cast<CuteQQuickCanvasItemCall11>(taken[11]);
      bool given = call(this, &point, &handled);
      if (handled) return given;
    }
    return QQuickItem::contains(point);
  }

#if QT_CONFIG(im)
  //  QVariant QQuickItem::inputMethodQuery(Qt::InputMethodQuery query)
  //      const
  QVariant inputMethodQuery(Qt::InputMethodQuery query) const override {
    if (taken[12]) {
      int handled = 0;
      CuteQQuickCanvasItemCall12 call = reinterpret_cast<CuteQQuickCanvasItemCall12>(taken[12]);
      const QVariant * given = call(this, static_cast<int>(query), &handled);
      if (handled && given) return *given;
    }
    return QQuickItem::inputMethodQuery(query);
  }
#endif  // QT_CONFIG(im)

  //  void QQuickItem::classBegin()
  void classBegin() override {
    if (taken[13]) {
      int handled = 0;
      CuteQQuickCanvasItemCall13 call = reinterpret_cast<CuteQQuickCanvasItemCall13>(taken[13]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItem::classBegin();
  }

  //  void QQuickItem::keyPressEvent(QKeyEvent *event)
  void keyPressEvent(QKeyEvent *event) override {
    if (taken[14]) {
      int handled = 0;
      CuteQQuickCanvasItemCall14 call = reinterpret_cast<CuteQQuickCanvasItemCall14>(taken[14]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::keyPressEvent(event);
  }

  //  void QQuickItem::keyReleaseEvent(QKeyEvent *event)
  void keyReleaseEvent(QKeyEvent *event) override {
    if (taken[15]) {
      int handled = 0;
      CuteQQuickCanvasItemCall15 call = reinterpret_cast<CuteQQuickCanvasItemCall15>(taken[15]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::keyReleaseEvent(event);
  }

#if QT_CONFIG(im)
  //  void QQuickItem::inputMethodEvent(QInputMethodEvent *a0)
  void inputMethodEvent(QInputMethodEvent *a0) override {
    if (taken[16]) {
      int handled = 0;
      CuteQQuickCanvasItemCall16 call = reinterpret_cast<CuteQQuickCanvasItemCall16>(taken[16]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItem::inputMethodEvent(a0);
  }
#endif  // QT_CONFIG(im)

  //  void QQuickItem::focusInEvent(QFocusEvent *a0)
  void focusInEvent(QFocusEvent *a0) override {
    if (taken[17]) {
      int handled = 0;
      CuteQQuickCanvasItemCall17 call = reinterpret_cast<CuteQQuickCanvasItemCall17>(taken[17]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItem::focusInEvent(a0);
  }

  //  void QQuickItem::focusOutEvent(QFocusEvent *a0)
  void focusOutEvent(QFocusEvent *a0) override {
    if (taken[18]) {
      int handled = 0;
      CuteQQuickCanvasItemCall18 call = reinterpret_cast<CuteQQuickCanvasItemCall18>(taken[18]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItem::focusOutEvent(a0);
  }

  //  void QQuickItem::mousePressEvent(QMouseEvent *event)
  void mousePressEvent(QMouseEvent *event) override {
    if (taken[19]) {
      int handled = 0;
      CuteQQuickCanvasItemCall19 call = reinterpret_cast<CuteQQuickCanvasItemCall19>(taken[19]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::mousePressEvent(event);
  }

  //  void QQuickItem::mouseMoveEvent(QMouseEvent *event)
  void mouseMoveEvent(QMouseEvent *event) override {
    if (taken[20]) {
      int handled = 0;
      CuteQQuickCanvasItemCall20 call = reinterpret_cast<CuteQQuickCanvasItemCall20>(taken[20]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::mouseMoveEvent(event);
  }

  //  void QQuickItem::mouseReleaseEvent(QMouseEvent *event)
  void mouseReleaseEvent(QMouseEvent *event) override {
    if (taken[21]) {
      int handled = 0;
      CuteQQuickCanvasItemCall21 call = reinterpret_cast<CuteQQuickCanvasItemCall21>(taken[21]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::mouseReleaseEvent(event);
  }

  //  void QQuickItem::mouseDoubleClickEvent(QMouseEvent *event)
  void mouseDoubleClickEvent(QMouseEvent *event) override {
    if (taken[22]) {
      int handled = 0;
      CuteQQuickCanvasItemCall22 call = reinterpret_cast<CuteQQuickCanvasItemCall22>(taken[22]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::mouseDoubleClickEvent(event);
  }

  //  void QQuickItem::mouseUngrabEvent()
  void mouseUngrabEvent() override {
    if (taken[23]) {
      int handled = 0;
      CuteQQuickCanvasItemCall23 call = reinterpret_cast<CuteQQuickCanvasItemCall23>(taken[23]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItem::mouseUngrabEvent();
  }

  //  void QQuickItem::touchUngrabEvent()
  void touchUngrabEvent() override {
    if (taken[24]) {
      int handled = 0;
      CuteQQuickCanvasItemCall24 call = reinterpret_cast<CuteQQuickCanvasItemCall24>(taken[24]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItem::touchUngrabEvent();
  }

#if QT_CONFIG(wheelevent)
  //  void QQuickItem::wheelEvent(QWheelEvent *event)
  void wheelEvent(QWheelEvent *event) override {
    if (taken[25]) {
      int handled = 0;
      CuteQQuickCanvasItemCall25 call = reinterpret_cast<CuteQQuickCanvasItemCall25>(taken[25]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::wheelEvent(event);
  }
#endif  // QT_CONFIG(wheelevent)

  //  void QQuickItem::touchEvent(QTouchEvent *event)
  void touchEvent(QTouchEvent *event) override {
    if (taken[26]) {
      int handled = 0;
      CuteQQuickCanvasItemCall26 call = reinterpret_cast<CuteQQuickCanvasItemCall26>(taken[26]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::touchEvent(event);
  }

  //  void QQuickItem::hoverEnterEvent(QHoverEvent *event)
  void hoverEnterEvent(QHoverEvent *event) override {
    if (taken[27]) {
      int handled = 0;
      CuteQQuickCanvasItemCall27 call = reinterpret_cast<CuteQQuickCanvasItemCall27>(taken[27]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::hoverEnterEvent(event);
  }

  //  void QQuickItem::hoverMoveEvent(QHoverEvent *event)
  void hoverMoveEvent(QHoverEvent *event) override {
    if (taken[28]) {
      int handled = 0;
      CuteQQuickCanvasItemCall28 call = reinterpret_cast<CuteQQuickCanvasItemCall28>(taken[28]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::hoverMoveEvent(event);
  }

  //  void QQuickItem::hoverLeaveEvent(QHoverEvent *event)
  void hoverLeaveEvent(QHoverEvent *event) override {
    if (taken[29]) {
      int handled = 0;
      CuteQQuickCanvasItemCall29 call = reinterpret_cast<CuteQQuickCanvasItemCall29>(taken[29]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::hoverLeaveEvent(event);
  }

#if QT_CONFIG(quick_draganddrop)
  //  void QQuickItem::dragEnterEvent(QDragEnterEvent *a0)
  void dragEnterEvent(QDragEnterEvent *a0) override {
    if (taken[30]) {
      int handled = 0;
      CuteQQuickCanvasItemCall30 call = reinterpret_cast<CuteQQuickCanvasItemCall30>(taken[30]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItem::dragEnterEvent(a0);
  }
#endif  // QT_CONFIG(quick_draganddrop)

#if QT_CONFIG(quick_draganddrop)
  //  void QQuickItem::dragMoveEvent(QDragMoveEvent *a0)
  void dragMoveEvent(QDragMoveEvent *a0) override {
    if (taken[31]) {
      int handled = 0;
      CuteQQuickCanvasItemCall31 call = reinterpret_cast<CuteQQuickCanvasItemCall31>(taken[31]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItem::dragMoveEvent(a0);
  }
#endif  // QT_CONFIG(quick_draganddrop)

#if QT_CONFIG(quick_draganddrop)
  //  void QQuickItem::dragLeaveEvent(QDragLeaveEvent *a0)
  void dragLeaveEvent(QDragLeaveEvent *a0) override {
    if (taken[32]) {
      int handled = 0;
      CuteQQuickCanvasItemCall32 call = reinterpret_cast<CuteQQuickCanvasItemCall32>(taken[32]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItem::dragLeaveEvent(a0);
  }
#endif  // QT_CONFIG(quick_draganddrop)

#if QT_CONFIG(quick_draganddrop)
  //  void QQuickItem::dropEvent(QDropEvent *a0)
  void dropEvent(QDropEvent *a0) override {
    if (taken[33]) {
      int handled = 0;
      CuteQQuickCanvasItemCall33 call = reinterpret_cast<CuteQQuickCanvasItemCall33>(taken[33]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItem::dropEvent(a0);
  }
#endif  // QT_CONFIG(quick_draganddrop)

  //  bool QQuickItem::childMouseEventFilter(QQuickItem *a0, QEvent *a1)
  bool childMouseEventFilter(QQuickItem *a0, QEvent *a1) override {
    if (taken[34]) {
      int handled = 0;
      CuteQQuickCanvasItemCall34 call = reinterpret_cast<CuteQQuickCanvasItemCall34>(taken[34]);
      bool given = call(this, a0, a1, &handled);
      if (handled) return given;
    }
    return QQuickItem::childMouseEventFilter(a0, a1);
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[35]) {
      int handled = 0;
      CuteQQuickCanvasItemCall35 call = reinterpret_cast<CuteQQuickCanvasItemCall35>(taken[35]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[36]) {
      int handled = 0;
      CuteQQuickCanvasItemCall36 call = reinterpret_cast<CuteQQuickCanvasItemCall36>(taken[36]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[37]) {
      int handled = 0;
      CuteQQuickCanvasItemCall37 call = reinterpret_cast<CuteQQuickCanvasItemCall37>(taken[37]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[38]) {
      int handled = 0;
      CuteQQuickCanvasItemCall38 call = reinterpret_cast<CuteQQuickCanvasItemCall38>(taken[38]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[39]) {
      int handled = 0;
      CuteQQuickCanvasItemCall39 call = reinterpret_cast<CuteQQuickCanvasItemCall39>(taken[39]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[40]) {
      int handled = 0;
      CuteQQuickCanvasItemCall40 call = reinterpret_cast<CuteQQuickCanvasItemCall40>(taken[40]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QQuickCanvasItem::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK16QQuickCanvasItem10metaObjectEv(
    const QQuickCanvasItem *self) {
  return self->metaObject();
}

//  bool QQuickCanvasItem::isTextureProvider() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK16QQuickCanvasItem17isTextureProviderEv(
    const QQuickCanvasItem *self) {
  return self->isTextureProvider();
}

//  void QQuickCanvasItem::schedulePolish()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickCanvasItem14schedulePolishEv(QQuickCanvasItem *self) {
  self->schedulePolish();
}

//  bool QQuickCanvasItem::event(QEvent *event)
extern "C" Q_DECL_EXPORT
bool ritual_ZN16QQuickCanvasItem5eventEP6QEvent(
    QQuickCanvasItem *self,
    QEvent *event) {
  return self->event(event);
}

//  QRect QQuickCanvasItem::tiledRect(const QRectF &window, const QSize
//      &tileSize)
extern "C" Q_DECL_EXPORT
QRect *ritual_ZN16QQuickCanvasItem9tiledRectERK6QRectFRK5QSize(
    const QRectF *window,
    const QSize *tileSize) {
  return new QRect(QQuickCanvasItem::tiledRect(*window, *tileSize));
}

//  a Python function taken by a CuteQQuickCanvasItem, for the function named
//      by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQuickCanvasItem(
    QQuickCanvasItem *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQuickCanvasItem *>(self)->take(key, call);
}

//  bool QQuickCanvasItem::isTextureProvider() const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK16QQuickCanvasItem17isTextureProviderEv(
    const QQuickCanvasItem *self) {
  return self->QQuickCanvasItem::isTextureProvider();
}

//  bool QQuickCanvasItem::event(QEvent *event)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN16QQuickCanvasItem5eventEP6QEvent(
    QQuickCanvasItem *self,
    QEvent *event) {
  return static_cast<OwnQQuickCanvasItem *>(self)->OwnQQuickCanvasItem::event(
      event);
}

#endif  // QT_CONFIG(quick_canvas)
