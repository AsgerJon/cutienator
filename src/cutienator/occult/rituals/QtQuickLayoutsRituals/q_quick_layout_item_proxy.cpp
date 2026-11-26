//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuickLayouts/6.12.0/QtQuickLayouts/private/qquicklayoutitemproxy_p.h,
//  Qt 6.12.0. Changes made here are lost.
#include <QtGui/qtguiglobal.h>
#include <QtQuick/qtquickglobal.h>
#include <QtQuickLayouts/6.12.0/QtQuickLayouts/private/qquicklayoutglobal_p.h>
#include <QtQuickLayouts/QtQuickLayouts>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuickLayouts/6.12.0/QtQuickLayouts/private/qquicklayoutitemproxy_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qrect.h>
#include <QtQuick/QtQuick>
#include <QtQuick/qquickitem.h>
#include <QtCore/qpoint.h>
#include <QtCore/qvariant.h>
#include <QtCore/qmetaobject.h>
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuickLayouts/private/qquicklayoutitemproxy_p.h>
#include <QtQuickLayouts/private/qquicklayout_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtdeclarative/src/quicklayouts/qquicklayoutitemproxy.cpp, line 146, as _ZN21QQuickLayoutItemProxy10itemChangeEN10QQuickItem10ItemChangeERKNS0_14ItemChangeDataE
inline void QQuickLayoutItemProxy::itemChange(ItemChange c, const ItemChangeData &d)
{
    if (c == QQuickItem::ItemVisibleHasChanged)
    {
        maybeTakeControl();
    }
    QQuickItem::itemChange(c, d);
}

//  from ../qtdeclarative/src/quicklayouts/qquicklayoutitemproxy.cpp, line 114, as _ZN21QQuickLayoutItemProxy14geometryChangeERK6QRectFS2_
inline void QQuickLayoutItemProxy::geometryChange(const QRectF &newGeom, const QRectF &oldGeom)
{
    QQuickItem::geometryChange(newGeom, oldGeom);
    if (!isVisible())
        return;

    const QSizeF sz = newGeom.size();
    QPointF pos(0., 0.);

    if (QQuickItem *t = effectiveTarget()) {
        if (QQuickLayoutItemProxyAttachedData * attachedData = target()->property("QQuickLayoutItemProxyAttachedData").value<QQuickLayoutItemProxyAttachedData*>()) {
            if (attachedData->getControllingProxy() != this)
                return;
        }

        // Should normally not be the case, except the user resets the parent
        // This is a failsave for this case and positions the item correctly
        if (t->parentItem() != this)
            pos = t->parentItem()->mapFromGlobal(mapToGlobal(0, 0));

        if (t->size() == sz && t->position() == pos && newGeom == oldGeom)
            return;

        t->setSize(sz);
        t->setPosition(pos);
    }
}

//  from ../qtdeclarative/src/quicklayouts/qquicklayoutitemproxy.cpp, line 213, as _ZNK21QQuickLayoutItemProxy6targetEv
inline QQuickItem *QQuickLayoutItemProxy::target() const
{
    Q_D(const QQuickLayoutItemProxy);
    return d->target;
}
//  -----------------------------------------------------------------------

//  A QQuickLayoutItemProxy that Python can take functions over in. Every QQuickLayoutItemProxy
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQQuickLayoutItemProxyCall0)(const void *, const QRectF *, const QRectF *, int *);
typedef void (*CuteQQuickLayoutItemProxyCall1)(const void *, int, const QQuickItem::ItemChangeData *, int *);
typedef const QRectF * (*CuteQQuickLayoutItemProxyCall2)(const void *, int *);
typedef const QRectF * (*CuteQQuickLayoutItemProxyCall3)(const void *, int *);
typedef bool (*CuteQQuickLayoutItemProxyCall4)(const void *, const QPointF *, int *);
#if QT_CONFIG(im)
typedef const QVariant * (*CuteQQuickLayoutItemProxyCall5)(const void *, int, int *);
#endif  // QT_CONFIG(im)
typedef bool (*CuteQQuickLayoutItemProxyCall6)(const void *, int *);
typedef void * (*CuteQQuickLayoutItemProxyCall7)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickLayoutItemProxyCall8)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickLayoutItemProxyCall9)(const void *, int *);
typedef void (*CuteQQuickLayoutItemProxyCall10)(const void *, int *);
typedef void (*CuteQQuickLayoutItemProxyCall11)(const void *, QKeyEvent *, int *);
typedef void (*CuteQQuickLayoutItemProxyCall12)(const void *, QKeyEvent *, int *);
#if QT_CONFIG(im)
typedef void (*CuteQQuickLayoutItemProxyCall13)(const void *, QInputMethodEvent *, int *);
#endif  // QT_CONFIG(im)
typedef void (*CuteQQuickLayoutItemProxyCall14)(const void *, QFocusEvent *, int *);
typedef void (*CuteQQuickLayoutItemProxyCall15)(const void *, QFocusEvent *, int *);
typedef void (*CuteQQuickLayoutItemProxyCall16)(const void *, QMouseEvent *, int *);
typedef void (*CuteQQuickLayoutItemProxyCall17)(const void *, QMouseEvent *, int *);
typedef void (*CuteQQuickLayoutItemProxyCall18)(const void *, QMouseEvent *, int *);
typedef void (*CuteQQuickLayoutItemProxyCall19)(const void *, QMouseEvent *, int *);
typedef void (*CuteQQuickLayoutItemProxyCall20)(const void *, int *);
typedef void (*CuteQQuickLayoutItemProxyCall21)(const void *, int *);
#if QT_CONFIG(wheelevent)
typedef void (*CuteQQuickLayoutItemProxyCall22)(const void *, QWheelEvent *, int *);
#endif  // QT_CONFIG(wheelevent)
typedef void (*CuteQQuickLayoutItemProxyCall23)(const void *, QTouchEvent *, int *);
typedef void (*CuteQQuickLayoutItemProxyCall24)(const void *, QHoverEvent *, int *);
typedef void (*CuteQQuickLayoutItemProxyCall25)(const void *, QHoverEvent *, int *);
typedef void (*CuteQQuickLayoutItemProxyCall26)(const void *, QHoverEvent *, int *);
#if QT_CONFIG(quick_draganddrop)
typedef void (*CuteQQuickLayoutItemProxyCall27)(const void *, QDragEnterEvent *, int *);
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
typedef void (*CuteQQuickLayoutItemProxyCall28)(const void *, QDragMoveEvent *, int *);
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
typedef void (*CuteQQuickLayoutItemProxyCall29)(const void *, QDragLeaveEvent *, int *);
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
typedef void (*CuteQQuickLayoutItemProxyCall30)(const void *, QDropEvent *, int *);
#endif  // QT_CONFIG(quick_draganddrop)
typedef bool (*CuteQQuickLayoutItemProxyCall31)(const void *, QQuickItem *, QEvent *, int *);
typedef void * (*CuteQQuickLayoutItemProxyCall32)(const void *, QSGNode *, QQuickItem::UpdatePaintNodeData *, int *);
typedef void (*CuteQQuickLayoutItemProxyCall33)(const void *, int *);
typedef void (*CuteQQuickLayoutItemProxyCall34)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickLayoutItemProxyCall35)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickLayoutItemProxyCall36)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickLayoutItemProxyCall37)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickLayoutItemProxyCall38)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickLayoutItemProxyCall39)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickLayoutItemProxyCall40)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQQuickLayoutItemProxy : public QQuickLayoutItemProxy {
public:
  using QQuickLayoutItemProxy::QQuickLayoutItemProxy;
  void *taken[41] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN10QQuickItem14geometryChangeERK6QRectFS2_")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem10itemChangeENS_10ItemChangeERKNS_14ItemChangeDataE")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK10QQuickItem12boundingRectEv")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK10QQuickItem8clipRectEv")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK10QQuickItem8containsERK7QPointF")) {
      taken[4] = call;
      return true;
    }
#if QT_CONFIG(im)
    if (!std::strcmp(key, "_ZNK10QQuickItem16inputMethodQueryEN2Qt16InputMethodQueryE")) {
      taken[5] = call;
      return true;
    }
#endif  // QT_CONFIG(im)
    if (!std::strcmp(key, "_ZNK10QQuickItem17isTextureProviderEv")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK10QQuickItem15textureProviderEv")) {
      taken[7] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[8] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN16QQmlParserStatus10classBeginEv")) {
      taken[9] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQmlParserStatus17componentCompleteEv")) {
      taken[10] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem13keyPressEventEP9QKeyEvent")) {
      taken[11] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem15keyReleaseEventEP9QKeyEvent")) {
      taken[12] = call;
      return true;
    }
#if QT_CONFIG(im)
    if (!std::strcmp(key, "_ZN10QQuickItem16inputMethodEventEP17QInputMethodEvent")) {
      taken[13] = call;
      return true;
    }
#endif  // QT_CONFIG(im)
    if (!std::strcmp(key, "_ZN10QQuickItem12focusInEventEP11QFocusEvent")) {
      taken[14] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem13focusOutEventEP11QFocusEvent")) {
      taken[15] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem15mousePressEventEP11QMouseEvent")) {
      taken[16] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem14mouseMoveEventEP11QMouseEvent")) {
      taken[17] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem17mouseReleaseEventEP11QMouseEvent")) {
      taken[18] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem21mouseDoubleClickEventEP11QMouseEvent")) {
      taken[19] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem16mouseUngrabEventEv")) {
      taken[20] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem16touchUngrabEventEv")) {
      taken[21] = call;
      return true;
    }
#if QT_CONFIG(wheelevent)
    if (!std::strcmp(key, "_ZN10QQuickItem10wheelEventEP11QWheelEvent")) {
      taken[22] = call;
      return true;
    }
#endif  // QT_CONFIG(wheelevent)
    if (!std::strcmp(key, "_ZN10QQuickItem10touchEventEP11QTouchEvent")) {
      taken[23] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem15hoverEnterEventEP11QHoverEvent")) {
      taken[24] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem14hoverMoveEventEP11QHoverEvent")) {
      taken[25] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem15hoverLeaveEventEP11QHoverEvent")) {
      taken[26] = call;
      return true;
    }
#if QT_CONFIG(quick_draganddrop)
    if (!std::strcmp(key, "_ZN10QQuickItem14dragEnterEventEP15QDragEnterEvent")) {
      taken[27] = call;
      return true;
    }
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
    if (!std::strcmp(key, "_ZN10QQuickItem13dragMoveEventEP14QDragMoveEvent")) {
      taken[28] = call;
      return true;
    }
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
    if (!std::strcmp(key, "_ZN10QQuickItem14dragLeaveEventEP15QDragLeaveEvent")) {
      taken[29] = call;
      return true;
    }
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
    if (!std::strcmp(key, "_ZN10QQuickItem9dropEventEP10QDropEvent")) {
      taken[30] = call;
      return true;
    }
#endif  // QT_CONFIG(quick_draganddrop)
    if (!std::strcmp(key, "_ZN10QQuickItem21childMouseEventFilterEPS_P6QEvent")) {
      taken[31] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem15updatePaintNodeEP7QSGNodePNS_19UpdatePaintNodeDataE")) {
      taken[32] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem16releaseResourcesEv")) {
      taken[33] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem12updatePolishEv")) {
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

  //  void QQuickLayoutItemProxy::geometryChange(const QRectF &newGeom,
  //      const QRectF &oldGeom)
  void geometryChange(
      const QRectF &newGeom,
      const QRectF &oldGeom) override {
    if (taken[0]) {
      int handled = 0;
      CuteQQuickLayoutItemProxyCall0 call = reinterpret_cast<CuteQQuickLayoutItemProxyCall0>(taken[0]);
      call(this, &newGeom, &oldGeom, &handled);
      if (handled) return;
    }
    QQuickLayoutItemProxy::geometryChange(newGeom, oldGeom);
  }

  //  void QQuickLayoutItemProxy::itemChange(ItemChange c, const
  //      ItemChangeData &d)
  void itemChange(
      QQuickItem::ItemChange c,
      const QQuickItem::ItemChangeData &d) override {
    if (taken[1]) {
      int handled = 0;
      CuteQQuickLayoutItemProxyCall1 call = reinterpret_cast<CuteQQuickLayoutItemProxyCall1>(taken[1]);
      call(this, static_cast<int>(c), &d, &handled);
      if (handled) return;
    }
    QQuickLayoutItemProxy::itemChange(c, d);
  }

  //  QRectF QQuickItem::boundingRect() const
  QRectF boundingRect() const override {
    if (taken[2]) {
      int handled = 0;
      CuteQQuickLayoutItemProxyCall2 call = reinterpret_cast<CuteQQuickLayoutItemProxyCall2>(taken[2]);
      const QRectF * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QQuickItem::boundingRect();
  }

  //  QRectF QQuickItem::clipRect() const
  QRectF clipRect() const override {
    if (taken[3]) {
      int handled = 0;
      CuteQQuickLayoutItemProxyCall3 call = reinterpret_cast<CuteQQuickLayoutItemProxyCall3>(taken[3]);
      const QRectF * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QQuickItem::clipRect();
  }

  //  bool QQuickItem::contains(const QPointF &point) const
  bool contains(const QPointF &point) const override {
    if (taken[4]) {
      int handled = 0;
      CuteQQuickLayoutItemProxyCall4 call = reinterpret_cast<CuteQQuickLayoutItemProxyCall4>(taken[4]);
      bool given = call(this, &point, &handled);
      if (handled) return given;
    }
    return QQuickItem::contains(point);
  }

#if QT_CONFIG(im)
  //  QVariant QQuickItem::inputMethodQuery(Qt::InputMethodQuery query)
  //      const
  QVariant inputMethodQuery(Qt::InputMethodQuery query) const override {
    if (taken[5]) {
      int handled = 0;
      CuteQQuickLayoutItemProxyCall5 call = reinterpret_cast<CuteQQuickLayoutItemProxyCall5>(taken[5]);
      const QVariant * given = call(this, static_cast<int>(query), &handled);
      if (handled && given) return *given;
    }
    return QQuickItem::inputMethodQuery(query);
  }
#endif  // QT_CONFIG(im)

  //  bool QQuickItem::isTextureProvider() const
  bool isTextureProvider() const override {
    if (taken[6]) {
      int handled = 0;
      CuteQQuickLayoutItemProxyCall6 call = reinterpret_cast<CuteQQuickLayoutItemProxyCall6>(taken[6]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QQuickItem::isTextureProvider();
  }

  //  QSGTextureProvider *QQuickItem::textureProvider() const
  QSGTextureProvider *textureProvider() const override {
    if (taken[7]) {
      int handled = 0;
      CuteQQuickLayoutItemProxyCall7 call = reinterpret_cast<CuteQQuickLayoutItemProxyCall7>(taken[7]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QSGTextureProvider *>(given);
    }
    return QQuickItem::textureProvider();
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QQuickItem::event(QEvent *a0)
  bool event(QEvent *a0) override {
    if (taken[8]) {
      int handled = 0;
      CuteQQuickLayoutItemProxyCall8 call = reinterpret_cast<CuteQQuickLayoutItemProxyCall8>(taken[8]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQuickItem::event(a0);
  }
#endif  // !defined(QT_NO_QOBJECT)

  //  void QQuickItem::classBegin()
  void classBegin() override {
    if (taken[9]) {
      int handled = 0;
      CuteQQuickLayoutItemProxyCall9 call = reinterpret_cast<CuteQQuickLayoutItemProxyCall9>(taken[9]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItem::classBegin();
  }

  //  void QQuickItem::componentComplete()
  void componentComplete() override {
    if (taken[10]) {
      int handled = 0;
      CuteQQuickLayoutItemProxyCall10 call = reinterpret_cast<CuteQQuickLayoutItemProxyCall10>(taken[10]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItem::componentComplete();
  }

  //  void QQuickItem::keyPressEvent(QKeyEvent *event)
  void keyPressEvent(QKeyEvent *event) override {
    if (taken[11]) {
      int handled = 0;
      CuteQQuickLayoutItemProxyCall11 call = reinterpret_cast<CuteQQuickLayoutItemProxyCall11>(taken[11]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::keyPressEvent(event);
  }

  //  void QQuickItem::keyReleaseEvent(QKeyEvent *event)
  void keyReleaseEvent(QKeyEvent *event) override {
    if (taken[12]) {
      int handled = 0;
      CuteQQuickLayoutItemProxyCall12 call = reinterpret_cast<CuteQQuickLayoutItemProxyCall12>(taken[12]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::keyReleaseEvent(event);
  }

#if QT_CONFIG(im)
  //  void QQuickItem::inputMethodEvent(QInputMethodEvent *a0)
  void inputMethodEvent(QInputMethodEvent *a0) override {
    if (taken[13]) {
      int handled = 0;
      CuteQQuickLayoutItemProxyCall13 call = reinterpret_cast<CuteQQuickLayoutItemProxyCall13>(taken[13]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItem::inputMethodEvent(a0);
  }
#endif  // QT_CONFIG(im)

  //  void QQuickItem::focusInEvent(QFocusEvent *a0)
  void focusInEvent(QFocusEvent *a0) override {
    if (taken[14]) {
      int handled = 0;
      CuteQQuickLayoutItemProxyCall14 call = reinterpret_cast<CuteQQuickLayoutItemProxyCall14>(taken[14]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItem::focusInEvent(a0);
  }

  //  void QQuickItem::focusOutEvent(QFocusEvent *a0)
  void focusOutEvent(QFocusEvent *a0) override {
    if (taken[15]) {
      int handled = 0;
      CuteQQuickLayoutItemProxyCall15 call = reinterpret_cast<CuteQQuickLayoutItemProxyCall15>(taken[15]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItem::focusOutEvent(a0);
  }

  //  void QQuickItem::mousePressEvent(QMouseEvent *event)
  void mousePressEvent(QMouseEvent *event) override {
    if (taken[16]) {
      int handled = 0;
      CuteQQuickLayoutItemProxyCall16 call = reinterpret_cast<CuteQQuickLayoutItemProxyCall16>(taken[16]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::mousePressEvent(event);
  }

  //  void QQuickItem::mouseMoveEvent(QMouseEvent *event)
  void mouseMoveEvent(QMouseEvent *event) override {
    if (taken[17]) {
      int handled = 0;
      CuteQQuickLayoutItemProxyCall17 call = reinterpret_cast<CuteQQuickLayoutItemProxyCall17>(taken[17]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::mouseMoveEvent(event);
  }

  //  void QQuickItem::mouseReleaseEvent(QMouseEvent *event)
  void mouseReleaseEvent(QMouseEvent *event) override {
    if (taken[18]) {
      int handled = 0;
      CuteQQuickLayoutItemProxyCall18 call = reinterpret_cast<CuteQQuickLayoutItemProxyCall18>(taken[18]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::mouseReleaseEvent(event);
  }

  //  void QQuickItem::mouseDoubleClickEvent(QMouseEvent *event)
  void mouseDoubleClickEvent(QMouseEvent *event) override {
    if (taken[19]) {
      int handled = 0;
      CuteQQuickLayoutItemProxyCall19 call = reinterpret_cast<CuteQQuickLayoutItemProxyCall19>(taken[19]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::mouseDoubleClickEvent(event);
  }

  //  void QQuickItem::mouseUngrabEvent()
  void mouseUngrabEvent() override {
    if (taken[20]) {
      int handled = 0;
      CuteQQuickLayoutItemProxyCall20 call = reinterpret_cast<CuteQQuickLayoutItemProxyCall20>(taken[20]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItem::mouseUngrabEvent();
  }

  //  void QQuickItem::touchUngrabEvent()
  void touchUngrabEvent() override {
    if (taken[21]) {
      int handled = 0;
      CuteQQuickLayoutItemProxyCall21 call = reinterpret_cast<CuteQQuickLayoutItemProxyCall21>(taken[21]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItem::touchUngrabEvent();
  }

#if QT_CONFIG(wheelevent)
  //  void QQuickItem::wheelEvent(QWheelEvent *event)
  void wheelEvent(QWheelEvent *event) override {
    if (taken[22]) {
      int handled = 0;
      CuteQQuickLayoutItemProxyCall22 call = reinterpret_cast<CuteQQuickLayoutItemProxyCall22>(taken[22]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::wheelEvent(event);
  }
#endif  // QT_CONFIG(wheelevent)

  //  void QQuickItem::touchEvent(QTouchEvent *event)
  void touchEvent(QTouchEvent *event) override {
    if (taken[23]) {
      int handled = 0;
      CuteQQuickLayoutItemProxyCall23 call = reinterpret_cast<CuteQQuickLayoutItemProxyCall23>(taken[23]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::touchEvent(event);
  }

  //  void QQuickItem::hoverEnterEvent(QHoverEvent *event)
  void hoverEnterEvent(QHoverEvent *event) override {
    if (taken[24]) {
      int handled = 0;
      CuteQQuickLayoutItemProxyCall24 call = reinterpret_cast<CuteQQuickLayoutItemProxyCall24>(taken[24]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::hoverEnterEvent(event);
  }

  //  void QQuickItem::hoverMoveEvent(QHoverEvent *event)
  void hoverMoveEvent(QHoverEvent *event) override {
    if (taken[25]) {
      int handled = 0;
      CuteQQuickLayoutItemProxyCall25 call = reinterpret_cast<CuteQQuickLayoutItemProxyCall25>(taken[25]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::hoverMoveEvent(event);
  }

  //  void QQuickItem::hoverLeaveEvent(QHoverEvent *event)
  void hoverLeaveEvent(QHoverEvent *event) override {
    if (taken[26]) {
      int handled = 0;
      CuteQQuickLayoutItemProxyCall26 call = reinterpret_cast<CuteQQuickLayoutItemProxyCall26>(taken[26]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::hoverLeaveEvent(event);
  }

#if QT_CONFIG(quick_draganddrop)
  //  void QQuickItem::dragEnterEvent(QDragEnterEvent *a0)
  void dragEnterEvent(QDragEnterEvent *a0) override {
    if (taken[27]) {
      int handled = 0;
      CuteQQuickLayoutItemProxyCall27 call = reinterpret_cast<CuteQQuickLayoutItemProxyCall27>(taken[27]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItem::dragEnterEvent(a0);
  }
#endif  // QT_CONFIG(quick_draganddrop)

#if QT_CONFIG(quick_draganddrop)
  //  void QQuickItem::dragMoveEvent(QDragMoveEvent *a0)
  void dragMoveEvent(QDragMoveEvent *a0) override {
    if (taken[28]) {
      int handled = 0;
      CuteQQuickLayoutItemProxyCall28 call = reinterpret_cast<CuteQQuickLayoutItemProxyCall28>(taken[28]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItem::dragMoveEvent(a0);
  }
#endif  // QT_CONFIG(quick_draganddrop)

#if QT_CONFIG(quick_draganddrop)
  //  void QQuickItem::dragLeaveEvent(QDragLeaveEvent *a0)
  void dragLeaveEvent(QDragLeaveEvent *a0) override {
    if (taken[29]) {
      int handled = 0;
      CuteQQuickLayoutItemProxyCall29 call = reinterpret_cast<CuteQQuickLayoutItemProxyCall29>(taken[29]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItem::dragLeaveEvent(a0);
  }
#endif  // QT_CONFIG(quick_draganddrop)

#if QT_CONFIG(quick_draganddrop)
  //  void QQuickItem::dropEvent(QDropEvent *a0)
  void dropEvent(QDropEvent *a0) override {
    if (taken[30]) {
      int handled = 0;
      CuteQQuickLayoutItemProxyCall30 call = reinterpret_cast<CuteQQuickLayoutItemProxyCall30>(taken[30]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItem::dropEvent(a0);
  }
#endif  // QT_CONFIG(quick_draganddrop)

  //  bool QQuickItem::childMouseEventFilter(QQuickItem *a0, QEvent *a1)
  bool childMouseEventFilter(QQuickItem *a0, QEvent *a1) override {
    if (taken[31]) {
      int handled = 0;
      CuteQQuickLayoutItemProxyCall31 call = reinterpret_cast<CuteQQuickLayoutItemProxyCall31>(taken[31]);
      bool given = call(this, a0, a1, &handled);
      if (handled) return given;
    }
    return QQuickItem::childMouseEventFilter(a0, a1);
  }

  //  QSGNode *QQuickItem::updatePaintNode(QSGNode *a0, UpdatePaintNodeData
  //      *a1)
  QSGNode *updatePaintNode(
      QSGNode *a0,
      QQuickItem::UpdatePaintNodeData *a1) override {
    if (taken[32]) {
      int handled = 0;
      CuteQQuickLayoutItemProxyCall32 call = reinterpret_cast<CuteQQuickLayoutItemProxyCall32>(taken[32]);
      void * given = call(this, a0, a1, &handled);
      if (handled) return static_cast<QSGNode *>(given);
    }
    return QQuickItem::updatePaintNode(a0, a1);
  }

  //  void QQuickItem::releaseResources()
  void releaseResources() override {
    if (taken[33]) {
      int handled = 0;
      CuteQQuickLayoutItemProxyCall33 call = reinterpret_cast<CuteQQuickLayoutItemProxyCall33>(taken[33]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItem::releaseResources();
  }

  //  void QQuickItem::updatePolish()
  void updatePolish() override {
    if (taken[34]) {
      int handled = 0;
      CuteQQuickLayoutItemProxyCall34 call = reinterpret_cast<CuteQQuickLayoutItemProxyCall34>(taken[34]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItem::updatePolish();
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[35]) {
      int handled = 0;
      CuteQQuickLayoutItemProxyCall35 call = reinterpret_cast<CuteQQuickLayoutItemProxyCall35>(taken[35]);
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
      CuteQQuickLayoutItemProxyCall36 call = reinterpret_cast<CuteQQuickLayoutItemProxyCall36>(taken[36]);
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
      CuteQQuickLayoutItemProxyCall37 call = reinterpret_cast<CuteQQuickLayoutItemProxyCall37>(taken[37]);
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
      CuteQQuickLayoutItemProxyCall38 call = reinterpret_cast<CuteQQuickLayoutItemProxyCall38>(taken[38]);
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
      CuteQQuickLayoutItemProxyCall39 call = reinterpret_cast<CuteQQuickLayoutItemProxyCall39>(taken[39]);
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
      CuteQQuickLayoutItemProxyCall40 call = reinterpret_cast<CuteQQuickLayoutItemProxyCall40>(taken[40]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QQuickLayoutItemProxy::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK21QQuickLayoutItemProxy10metaObjectEv(
    const QQuickLayoutItemProxy *self) {
  return self->metaObject();
}

//  void *QQuickLayoutItemProxy::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN21QQuickLayoutItemProxy11qt_metacastEPKc(
    QQuickLayoutItemProxy *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QQuickLayoutItemProxy::qt_metacall(QMetaObject::Call a0, int a1, void
//      **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN21QQuickLayoutItemProxy11qt_metacallEN11QMetaObject4CallEiPPv(
    QQuickLayoutItemProxy *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QQuickLayoutItemProxy::~QQuickLayoutItemProxy()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuickLayoutItemProxyD1Ev(QQuickLayoutItemProxy *self) {
  delete self;
}

//  void QQuickLayoutItemProxy::geometryChange(const QRectF &newGeom, const
//      QRectF &oldGeom)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuickLayoutItemProxy14geometryChangeERK6QRectFS2_(
    QQuickLayoutItemProxy *self,
    const QRectF *newGeom,
    const QRectF *oldGeom) {
  self->geometryChange(*newGeom, *oldGeom);
}

//  void QQuickLayoutItemProxy::itemChange(ItemChange c, const ItemChangeData
//      &d)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuickLayoutItemProxy10itemChangeEN10QQuickItem10ItemChangeERKNS0_14ItemChangeDataE(
    QQuickLayoutItemProxy *self,
    QQuickItem::ItemChange c,
    const QQuickItem::ItemChangeData *d) {
  self->itemChange(c, *d);
}

//  QQuickItem *QQuickLayoutItemProxy::target() const
extern "C" Q_DECL_EXPORT
QQuickItem *ritual_ZNK21QQuickLayoutItemProxy6targetEv(
    const QQuickLayoutItemProxy *self) {
  return self->target();
}

//  void QQuickLayoutItemProxy::clearTarget()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuickLayoutItemProxy11clearTargetEv(
    QQuickLayoutItemProxy *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQuickLayoutItemProxy")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "clearTarget()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "clearTarget()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QQuickLayoutItemProxy::updatePos()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuickLayoutItemProxy9updatePosEv(
    QQuickLayoutItemProxy *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQuickLayoutItemProxy")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "updatePos()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "updatePos()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QQuickLayoutItemProxy::targetMinimumWidthChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuickLayoutItemProxy25targetMinimumWidthChangedEv(
    QQuickLayoutItemProxy *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQuickLayoutItemProxy")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "targetMinimumWidthChanged()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "targetMinimumWidthChanged()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QQuickLayoutItemProxy::proxyMinimumWidthChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuickLayoutItemProxy24proxyMinimumWidthChangedEv(
    QQuickLayoutItemProxy *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQuickLayoutItemProxy")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "proxyMinimumWidthChanged()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "proxyMinimumWidthChanged()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QQuickLayoutItemProxy::targetMinimumHeightChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuickLayoutItemProxy26targetMinimumHeightChangedEv(
    QQuickLayoutItemProxy *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQuickLayoutItemProxy")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "targetMinimumHeightChanged()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "targetMinimumHeightChanged()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QQuickLayoutItemProxy::proxyMinimumHeightChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuickLayoutItemProxy25proxyMinimumHeightChangedEv(
    QQuickLayoutItemProxy *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQuickLayoutItemProxy")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "proxyMinimumHeightChanged()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "proxyMinimumHeightChanged()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QQuickLayoutItemProxy::targetPreferredWidthChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuickLayoutItemProxy27targetPreferredWidthChangedEv(
    QQuickLayoutItemProxy *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQuickLayoutItemProxy")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "targetPreferredWidthChanged()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "targetPreferredWidthChanged()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QQuickLayoutItemProxy::proxyPreferredWidthChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuickLayoutItemProxy26proxyPreferredWidthChangedEv(
    QQuickLayoutItemProxy *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQuickLayoutItemProxy")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "proxyPreferredWidthChanged()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "proxyPreferredWidthChanged()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QQuickLayoutItemProxy::targetPreferredHeightChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuickLayoutItemProxy28targetPreferredHeightChangedEv(
    QQuickLayoutItemProxy *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQuickLayoutItemProxy")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "targetPreferredHeightChanged()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "targetPreferredHeightChanged()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QQuickLayoutItemProxy::proxyPreferredHeightChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuickLayoutItemProxy27proxyPreferredHeightChangedEv(
    QQuickLayoutItemProxy *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQuickLayoutItemProxy")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "proxyPreferredHeightChanged()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "proxyPreferredHeightChanged()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QQuickLayoutItemProxy::targetMaximumWidthChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuickLayoutItemProxy25targetMaximumWidthChangedEv(
    QQuickLayoutItemProxy *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQuickLayoutItemProxy")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "targetMaximumWidthChanged()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "targetMaximumWidthChanged()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QQuickLayoutItemProxy::proxyMaximumWidthChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuickLayoutItemProxy24proxyMaximumWidthChangedEv(
    QQuickLayoutItemProxy *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQuickLayoutItemProxy")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "proxyMaximumWidthChanged()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "proxyMaximumWidthChanged()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QQuickLayoutItemProxy::targetMaximumHeightChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuickLayoutItemProxy26targetMaximumHeightChangedEv(
    QQuickLayoutItemProxy *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQuickLayoutItemProxy")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "targetMaximumHeightChanged()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "targetMaximumHeightChanged()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QQuickLayoutItemProxy::proxyMaximumHeightChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuickLayoutItemProxy25proxyMaximumHeightChangedEv(
    QQuickLayoutItemProxy *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQuickLayoutItemProxy")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "proxyMaximumHeightChanged()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "proxyMaximumHeightChanged()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QQuickLayoutItemProxy::targetFillWidthChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuickLayoutItemProxy22targetFillWidthChangedEv(
    QQuickLayoutItemProxy *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQuickLayoutItemProxy")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "targetFillWidthChanged()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "targetFillWidthChanged()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QQuickLayoutItemProxy::proxyFillWidthChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuickLayoutItemProxy21proxyFillWidthChangedEv(
    QQuickLayoutItemProxy *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQuickLayoutItemProxy")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "proxyFillWidthChanged()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "proxyFillWidthChanged()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QQuickLayoutItemProxy::targetFillHeightChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuickLayoutItemProxy23targetFillHeightChangedEv(
    QQuickLayoutItemProxy *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQuickLayoutItemProxy")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "targetFillHeightChanged()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "targetFillHeightChanged()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QQuickLayoutItemProxy::proxyFillHeightChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuickLayoutItemProxy22proxyFillHeightChangedEv(
    QQuickLayoutItemProxy *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQuickLayoutItemProxy")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "proxyFillHeightChanged()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "proxyFillHeightChanged()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QQuickLayoutItemProxy::targetAlignmentChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuickLayoutItemProxy22targetAlignmentChangedEv(
    QQuickLayoutItemProxy *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQuickLayoutItemProxy")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "targetAlignmentChanged()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "targetAlignmentChanged()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QQuickLayoutItemProxy::proxyAlignmentChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuickLayoutItemProxy21proxyAlignmentChangedEv(
    QQuickLayoutItemProxy *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQuickLayoutItemProxy")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "proxyAlignmentChanged()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "proxyAlignmentChanged()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QQuickLayoutItemProxy::targetHorizontalStretchFactorChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuickLayoutItemProxy36targetHorizontalStretchFactorChangedEv(
    QQuickLayoutItemProxy *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQuickLayoutItemProxy")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "targetHorizontalStretchFactorChanged()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "targetHorizontalStretchFactorChanged()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QQuickLayoutItemProxy::proxyHorizontalStretchFactorChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuickLayoutItemProxy35proxyHorizontalStretchFactorChangedEv(
    QQuickLayoutItemProxy *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQuickLayoutItemProxy")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "proxyHorizontalStretchFactorChanged()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "proxyHorizontalStretchFactorChanged()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QQuickLayoutItemProxy::targetVerticalStretchFactorChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuickLayoutItemProxy34targetVerticalStretchFactorChangedEv(
    QQuickLayoutItemProxy *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQuickLayoutItemProxy")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "targetVerticalStretchFactorChanged()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "targetVerticalStretchFactorChanged()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QQuickLayoutItemProxy::proxyVerticalStretchFactorChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuickLayoutItemProxy33proxyVerticalStretchFactorChangedEv(
    QQuickLayoutItemProxy *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQuickLayoutItemProxy")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "proxyVerticalStretchFactorChanged()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "proxyVerticalStretchFactorChanged()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QQuickLayoutItemProxy::targetMarginsChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuickLayoutItemProxy20targetMarginsChangedEv(
    QQuickLayoutItemProxy *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQuickLayoutItemProxy")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "targetMarginsChanged()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "targetMarginsChanged()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QQuickLayoutItemProxy::proxyMarginsChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuickLayoutItemProxy19proxyMarginsChangedEv(
    QQuickLayoutItemProxy *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQuickLayoutItemProxy")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "proxyMarginsChanged()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "proxyMarginsChanged()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QQuickLayoutItemProxy::targetLeftMarginChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuickLayoutItemProxy23targetLeftMarginChangedEv(
    QQuickLayoutItemProxy *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQuickLayoutItemProxy")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "targetLeftMarginChanged()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "targetLeftMarginChanged()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QQuickLayoutItemProxy::proxyLeftMarginChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuickLayoutItemProxy22proxyLeftMarginChangedEv(
    QQuickLayoutItemProxy *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQuickLayoutItemProxy")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "proxyLeftMarginChanged()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "proxyLeftMarginChanged()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QQuickLayoutItemProxy::targetTopMarginChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuickLayoutItemProxy22targetTopMarginChangedEv(
    QQuickLayoutItemProxy *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQuickLayoutItemProxy")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "targetTopMarginChanged()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "targetTopMarginChanged()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QQuickLayoutItemProxy::proxyTopMarginChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuickLayoutItemProxy21proxyTopMarginChangedEv(
    QQuickLayoutItemProxy *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQuickLayoutItemProxy")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "proxyTopMarginChanged()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "proxyTopMarginChanged()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QQuickLayoutItemProxy::targetRightMarginChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuickLayoutItemProxy24targetRightMarginChangedEv(
    QQuickLayoutItemProxy *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQuickLayoutItemProxy")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "targetRightMarginChanged()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "targetRightMarginChanged()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QQuickLayoutItemProxy::proxyRightMarginChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuickLayoutItemProxy23proxyRightMarginChangedEv(
    QQuickLayoutItemProxy *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQuickLayoutItemProxy")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "proxyRightMarginChanged()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "proxyRightMarginChanged()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QQuickLayoutItemProxy::targetBottomMarginChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuickLayoutItemProxy25targetBottomMarginChangedEv(
    QQuickLayoutItemProxy *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQuickLayoutItemProxy")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "targetBottomMarginChanged()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "targetBottomMarginChanged()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QQuickLayoutItemProxy::proxyBottomMarginChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuickLayoutItemProxy24proxyBottomMarginChangedEv(
    QQuickLayoutItemProxy *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQuickLayoutItemProxy")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "proxyBottomMarginChanged()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "proxyBottomMarginChanged()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QQuickLayoutItemProxy::targetChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuickLayoutItemProxy13targetChangedEv(
    QQuickLayoutItemProxy *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQuickLayoutItemProxy")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "targetChanged()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "targetChanged()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  QQuickLayoutItemProxyPrivate *QQuickLayoutItemProxy::d_func()
extern "C" Q_DECL_EXPORT
QQuickLayoutItemProxyPrivate *ritual_ZN21QQuickLayoutItemProxy6d_funcEv(
    QQuickLayoutItemProxy *self) {
  return self->d_func();
}

//  const QQuickLayoutItemProxyPrivate *QQuickLayoutItemProxy::d_func() const
extern "C" Q_DECL_EXPORT
const QQuickLayoutItemProxyPrivate *ritual_ZNK21QQuickLayoutItemProxy6d_funcEv(
    const QQuickLayoutItemProxy *self) {
  return self->d_func();
}

//  a Python function taken by a CuteQQuickLayoutItemProxy, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQuickLayoutItemProxy(
    QQuickLayoutItemProxy *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQuickLayoutItemProxy *>(self)->take(key, call);
}
