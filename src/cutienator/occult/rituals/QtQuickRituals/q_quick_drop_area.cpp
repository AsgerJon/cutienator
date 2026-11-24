//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/6.12.0/QtQuick/private/qquickdroparea_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtQuick/qtquickglobal.h>
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#if QT_CONFIG(quick_draganddrop)
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qquickdroparea_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qrect.h>
#include <QtCore/qpoint.h>
#include <QtCore/qvariant.h>
#include <QtQuick/qquickitem.h>
#include <QtCore/qmetaobject.h>
#include <QtCore/qlist.h>
#include <cstring>

//  Only a class built on QQuickDropArea may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQQuickDropArea : QQuickDropArea {
  using QQuickDropArea::dragMoveEvent;
  using QQuickDropArea::dragEnterEvent;
  using QQuickDropArea::dragLeaveEvent;
  using QQuickDropArea::dropEvent;
};

//  A QQuickDropArea that Python can take functions over in. Every QQuickDropArea
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if QT_CONFIG(quick_draganddrop)
typedef void (*CuteQQuickDropAreaCall0)(const void *, QDragMoveEvent *, int *);
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
typedef void (*CuteQQuickDropAreaCall1)(const void *, QDragEnterEvent *, int *);
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
typedef void (*CuteQQuickDropAreaCall2)(const void *, QDragLeaveEvent *, int *);
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
typedef void (*CuteQQuickDropAreaCall3)(const void *, QDropEvent *, int *);
#endif  // QT_CONFIG(quick_draganddrop)
typedef const QRectF * (*CuteQQuickDropAreaCall4)(const void *, int *);
typedef const QRectF * (*CuteQQuickDropAreaCall5)(const void *, int *);
typedef bool (*CuteQQuickDropAreaCall6)(const void *, const QPointF *, int *);
#if QT_CONFIG(im)
typedef const QVariant * (*CuteQQuickDropAreaCall7)(const void *, int, int *);
#endif  // QT_CONFIG(im)
typedef bool (*CuteQQuickDropAreaCall8)(const void *, int *);
typedef void * (*CuteQQuickDropAreaCall9)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickDropAreaCall10)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickDropAreaCall11)(const void *, int, const QQuickItem::ItemChangeData *, int *);
typedef void (*CuteQQuickDropAreaCall12)(const void *, const QRectF *, const QRectF *, int *);
typedef void (*CuteQQuickDropAreaCall13)(const void *, int *);
typedef void (*CuteQQuickDropAreaCall14)(const void *, int *);
typedef void (*CuteQQuickDropAreaCall15)(const void *, QKeyEvent *, int *);
typedef void (*CuteQQuickDropAreaCall16)(const void *, QKeyEvent *, int *);
#if QT_CONFIG(im)
typedef void (*CuteQQuickDropAreaCall17)(const void *, QInputMethodEvent *, int *);
#endif  // QT_CONFIG(im)
typedef void (*CuteQQuickDropAreaCall18)(const void *, QFocusEvent *, int *);
typedef void (*CuteQQuickDropAreaCall19)(const void *, QFocusEvent *, int *);
typedef void (*CuteQQuickDropAreaCall20)(const void *, QMouseEvent *, int *);
typedef void (*CuteQQuickDropAreaCall21)(const void *, QMouseEvent *, int *);
typedef void (*CuteQQuickDropAreaCall22)(const void *, QMouseEvent *, int *);
typedef void (*CuteQQuickDropAreaCall23)(const void *, QMouseEvent *, int *);
typedef void (*CuteQQuickDropAreaCall24)(const void *, int *);
typedef void (*CuteQQuickDropAreaCall25)(const void *, int *);
#if QT_CONFIG(wheelevent)
typedef void (*CuteQQuickDropAreaCall26)(const void *, QWheelEvent *, int *);
#endif  // QT_CONFIG(wheelevent)
typedef void (*CuteQQuickDropAreaCall27)(const void *, QTouchEvent *, int *);
typedef void (*CuteQQuickDropAreaCall28)(const void *, QHoverEvent *, int *);
typedef void (*CuteQQuickDropAreaCall29)(const void *, QHoverEvent *, int *);
typedef void (*CuteQQuickDropAreaCall30)(const void *, QHoverEvent *, int *);
typedef bool (*CuteQQuickDropAreaCall31)(const void *, QQuickItem *, QEvent *, int *);
typedef void * (*CuteQQuickDropAreaCall32)(const void *, QSGNode *, QQuickItem::UpdatePaintNodeData *, int *);
typedef void (*CuteQQuickDropAreaCall33)(const void *, int *);
typedef void (*CuteQQuickDropAreaCall34)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickDropAreaCall35)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickDropAreaCall36)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickDropAreaCall37)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickDropAreaCall38)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickDropAreaCall39)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickDropAreaCall40)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQQuickDropArea : public QQuickDropArea {
public:
  using QQuickDropArea::QQuickDropArea;
  void *taken[41] = {};

  bool take(const char *key, void *call) {
#if QT_CONFIG(quick_draganddrop)
    if (!std::strcmp(key, "_ZN10QQuickItem13dragMoveEventEP14QDragMoveEvent")) {
      taken[0] = call;
      return true;
    }
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
    if (!std::strcmp(key, "_ZN10QQuickItem14dragEnterEventEP15QDragEnterEvent")) {
      taken[1] = call;
      return true;
    }
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
    if (!std::strcmp(key, "_ZN10QQuickItem14dragLeaveEventEP15QDragLeaveEvent")) {
      taken[2] = call;
      return true;
    }
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
    if (!std::strcmp(key, "_ZN10QQuickItem9dropEventEP10QDropEvent")) {
      taken[3] = call;
      return true;
    }
#endif  // QT_CONFIG(quick_draganddrop)
    if (!std::strcmp(key, "_ZNK10QQuickItem12boundingRectEv")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK10QQuickItem8clipRectEv")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK10QQuickItem8containsERK7QPointF")) {
      taken[6] = call;
      return true;
    }
#if QT_CONFIG(im)
    if (!std::strcmp(key, "_ZNK10QQuickItem16inputMethodQueryEN2Qt16InputMethodQueryE")) {
      taken[7] = call;
      return true;
    }
#endif  // QT_CONFIG(im)
    if (!std::strcmp(key, "_ZNK10QQuickItem17isTextureProviderEv")) {
      taken[8] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK10QQuickItem15textureProviderEv")) {
      taken[9] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[10] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN10QQuickItem10itemChangeENS_10ItemChangeERKNS_14ItemChangeDataE")) {
      taken[11] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem14geometryChangeERK6QRectFS2_")) {
      taken[12] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQmlParserStatus10classBeginEv")) {
      taken[13] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQmlParserStatus17componentCompleteEv")) {
      taken[14] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem13keyPressEventEP9QKeyEvent")) {
      taken[15] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem15keyReleaseEventEP9QKeyEvent")) {
      taken[16] = call;
      return true;
    }
#if QT_CONFIG(im)
    if (!std::strcmp(key, "_ZN10QQuickItem16inputMethodEventEP17QInputMethodEvent")) {
      taken[17] = call;
      return true;
    }
#endif  // QT_CONFIG(im)
    if (!std::strcmp(key, "_ZN10QQuickItem12focusInEventEP11QFocusEvent")) {
      taken[18] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem13focusOutEventEP11QFocusEvent")) {
      taken[19] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem15mousePressEventEP11QMouseEvent")) {
      taken[20] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem14mouseMoveEventEP11QMouseEvent")) {
      taken[21] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem17mouseReleaseEventEP11QMouseEvent")) {
      taken[22] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem21mouseDoubleClickEventEP11QMouseEvent")) {
      taken[23] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem16mouseUngrabEventEv")) {
      taken[24] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem16touchUngrabEventEv")) {
      taken[25] = call;
      return true;
    }
#if QT_CONFIG(wheelevent)
    if (!std::strcmp(key, "_ZN10QQuickItem10wheelEventEP11QWheelEvent")) {
      taken[26] = call;
      return true;
    }
#endif  // QT_CONFIG(wheelevent)
    if (!std::strcmp(key, "_ZN10QQuickItem10touchEventEP11QTouchEvent")) {
      taken[27] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem15hoverEnterEventEP11QHoverEvent")) {
      taken[28] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem14hoverMoveEventEP11QHoverEvent")) {
      taken[29] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem15hoverLeaveEventEP11QHoverEvent")) {
      taken[30] = call;
      return true;
    }
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

#if QT_CONFIG(quick_draganddrop)
  //  void QQuickDropArea::dragMoveEvent(QDragMoveEvent *event)
  void dragMoveEvent(QDragMoveEvent *event) override {
    if (taken[0]) {
      int handled = 0;
      CuteQQuickDropAreaCall0 call = reinterpret_cast<CuteQQuickDropAreaCall0>(taken[0]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickDropArea::dragMoveEvent(event);
  }
#endif  // QT_CONFIG(quick_draganddrop)

#if QT_CONFIG(quick_draganddrop)
  //  void QQuickDropArea::dragEnterEvent(QDragEnterEvent *event)
  void dragEnterEvent(QDragEnterEvent *event) override {
    if (taken[1]) {
      int handled = 0;
      CuteQQuickDropAreaCall1 call = reinterpret_cast<CuteQQuickDropAreaCall1>(taken[1]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickDropArea::dragEnterEvent(event);
  }
#endif  // QT_CONFIG(quick_draganddrop)

#if QT_CONFIG(quick_draganddrop)
  //  void QQuickDropArea::dragLeaveEvent(QDragLeaveEvent *event)
  void dragLeaveEvent(QDragLeaveEvent *event) override {
    if (taken[2]) {
      int handled = 0;
      CuteQQuickDropAreaCall2 call = reinterpret_cast<CuteQQuickDropAreaCall2>(taken[2]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickDropArea::dragLeaveEvent(event);
  }
#endif  // QT_CONFIG(quick_draganddrop)

#if QT_CONFIG(quick_draganddrop)
  //  void QQuickDropArea::dropEvent(QDropEvent *event)
  void dropEvent(QDropEvent *event) override {
    if (taken[3]) {
      int handled = 0;
      CuteQQuickDropAreaCall3 call = reinterpret_cast<CuteQQuickDropAreaCall3>(taken[3]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickDropArea::dropEvent(event);
  }
#endif  // QT_CONFIG(quick_draganddrop)

  //  QRectF QQuickItem::boundingRect() const
  QRectF boundingRect() const override {
    if (taken[4]) {
      int handled = 0;
      CuteQQuickDropAreaCall4 call = reinterpret_cast<CuteQQuickDropAreaCall4>(taken[4]);
      const QRectF * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QQuickItem::boundingRect();
  }

  //  QRectF QQuickItem::clipRect() const
  QRectF clipRect() const override {
    if (taken[5]) {
      int handled = 0;
      CuteQQuickDropAreaCall5 call = reinterpret_cast<CuteQQuickDropAreaCall5>(taken[5]);
      const QRectF * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QQuickItem::clipRect();
  }

  //  bool QQuickItem::contains(const QPointF &point) const
  bool contains(const QPointF &point) const override {
    if (taken[6]) {
      int handled = 0;
      CuteQQuickDropAreaCall6 call = reinterpret_cast<CuteQQuickDropAreaCall6>(taken[6]);
      bool given = call(this, &point, &handled);
      if (handled) return given;
    }
    return QQuickItem::contains(point);
  }

#if QT_CONFIG(im)
  //  QVariant QQuickItem::inputMethodQuery(Qt::InputMethodQuery query)
  //      const
  QVariant inputMethodQuery(Qt::InputMethodQuery query) const override {
    if (taken[7]) {
      int handled = 0;
      CuteQQuickDropAreaCall7 call = reinterpret_cast<CuteQQuickDropAreaCall7>(taken[7]);
      const QVariant * given = call(this, static_cast<int>(query), &handled);
      if (handled && given) return *given;
    }
    return QQuickItem::inputMethodQuery(query);
  }
#endif  // QT_CONFIG(im)

  //  bool QQuickItem::isTextureProvider() const
  bool isTextureProvider() const override {
    if (taken[8]) {
      int handled = 0;
      CuteQQuickDropAreaCall8 call = reinterpret_cast<CuteQQuickDropAreaCall8>(taken[8]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QQuickItem::isTextureProvider();
  }

  //  QSGTextureProvider *QQuickItem::textureProvider() const
  QSGTextureProvider *textureProvider() const override {
    if (taken[9]) {
      int handled = 0;
      CuteQQuickDropAreaCall9 call = reinterpret_cast<CuteQQuickDropAreaCall9>(taken[9]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QSGTextureProvider *>(given);
    }
    return QQuickItem::textureProvider();
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QQuickItem::event(QEvent *a0)
  bool event(QEvent *a0) override {
    if (taken[10]) {
      int handled = 0;
      CuteQQuickDropAreaCall10 call = reinterpret_cast<CuteQQuickDropAreaCall10>(taken[10]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQuickItem::event(a0);
  }
#endif  // !defined(QT_NO_QOBJECT)

  //  void QQuickItem::itemChange(ItemChange a0, const ItemChangeData &a1)
  void itemChange(
      QQuickItem::ItemChange a0,
      const QQuickItem::ItemChangeData &a1) override {
    if (taken[11]) {
      int handled = 0;
      CuteQQuickDropAreaCall11 call = reinterpret_cast<CuteQQuickDropAreaCall11>(taken[11]);
      call(this, static_cast<int>(a0), &a1, &handled);
      if (handled) return;
    }
    QQuickItem::itemChange(a0, a1);
  }

  //  void QQuickItem::geometryChange(const QRectF &newGeometry, const
  //      QRectF &oldGeometry)
  void geometryChange(
      const QRectF &newGeometry,
      const QRectF &oldGeometry) override {
    if (taken[12]) {
      int handled = 0;
      CuteQQuickDropAreaCall12 call = reinterpret_cast<CuteQQuickDropAreaCall12>(taken[12]);
      call(this, &newGeometry, &oldGeometry, &handled);
      if (handled) return;
    }
    QQuickItem::geometryChange(newGeometry, oldGeometry);
  }

  //  void QQuickItem::classBegin()
  void classBegin() override {
    if (taken[13]) {
      int handled = 0;
      CuteQQuickDropAreaCall13 call = reinterpret_cast<CuteQQuickDropAreaCall13>(taken[13]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItem::classBegin();
  }

  //  void QQuickItem::componentComplete()
  void componentComplete() override {
    if (taken[14]) {
      int handled = 0;
      CuteQQuickDropAreaCall14 call = reinterpret_cast<CuteQQuickDropAreaCall14>(taken[14]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItem::componentComplete();
  }

  //  void QQuickItem::keyPressEvent(QKeyEvent *event)
  void keyPressEvent(QKeyEvent *event) override {
    if (taken[15]) {
      int handled = 0;
      CuteQQuickDropAreaCall15 call = reinterpret_cast<CuteQQuickDropAreaCall15>(taken[15]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::keyPressEvent(event);
  }

  //  void QQuickItem::keyReleaseEvent(QKeyEvent *event)
  void keyReleaseEvent(QKeyEvent *event) override {
    if (taken[16]) {
      int handled = 0;
      CuteQQuickDropAreaCall16 call = reinterpret_cast<CuteQQuickDropAreaCall16>(taken[16]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::keyReleaseEvent(event);
  }

#if QT_CONFIG(im)
  //  void QQuickItem::inputMethodEvent(QInputMethodEvent *a0)
  void inputMethodEvent(QInputMethodEvent *a0) override {
    if (taken[17]) {
      int handled = 0;
      CuteQQuickDropAreaCall17 call = reinterpret_cast<CuteQQuickDropAreaCall17>(taken[17]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItem::inputMethodEvent(a0);
  }
#endif  // QT_CONFIG(im)

  //  void QQuickItem::focusInEvent(QFocusEvent *a0)
  void focusInEvent(QFocusEvent *a0) override {
    if (taken[18]) {
      int handled = 0;
      CuteQQuickDropAreaCall18 call = reinterpret_cast<CuteQQuickDropAreaCall18>(taken[18]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItem::focusInEvent(a0);
  }

  //  void QQuickItem::focusOutEvent(QFocusEvent *a0)
  void focusOutEvent(QFocusEvent *a0) override {
    if (taken[19]) {
      int handled = 0;
      CuteQQuickDropAreaCall19 call = reinterpret_cast<CuteQQuickDropAreaCall19>(taken[19]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItem::focusOutEvent(a0);
  }

  //  void QQuickItem::mousePressEvent(QMouseEvent *event)
  void mousePressEvent(QMouseEvent *event) override {
    if (taken[20]) {
      int handled = 0;
      CuteQQuickDropAreaCall20 call = reinterpret_cast<CuteQQuickDropAreaCall20>(taken[20]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::mousePressEvent(event);
  }

  //  void QQuickItem::mouseMoveEvent(QMouseEvent *event)
  void mouseMoveEvent(QMouseEvent *event) override {
    if (taken[21]) {
      int handled = 0;
      CuteQQuickDropAreaCall21 call = reinterpret_cast<CuteQQuickDropAreaCall21>(taken[21]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::mouseMoveEvent(event);
  }

  //  void QQuickItem::mouseReleaseEvent(QMouseEvent *event)
  void mouseReleaseEvent(QMouseEvent *event) override {
    if (taken[22]) {
      int handled = 0;
      CuteQQuickDropAreaCall22 call = reinterpret_cast<CuteQQuickDropAreaCall22>(taken[22]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::mouseReleaseEvent(event);
  }

  //  void QQuickItem::mouseDoubleClickEvent(QMouseEvent *event)
  void mouseDoubleClickEvent(QMouseEvent *event) override {
    if (taken[23]) {
      int handled = 0;
      CuteQQuickDropAreaCall23 call = reinterpret_cast<CuteQQuickDropAreaCall23>(taken[23]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::mouseDoubleClickEvent(event);
  }

  //  void QQuickItem::mouseUngrabEvent()
  void mouseUngrabEvent() override {
    if (taken[24]) {
      int handled = 0;
      CuteQQuickDropAreaCall24 call = reinterpret_cast<CuteQQuickDropAreaCall24>(taken[24]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItem::mouseUngrabEvent();
  }

  //  void QQuickItem::touchUngrabEvent()
  void touchUngrabEvent() override {
    if (taken[25]) {
      int handled = 0;
      CuteQQuickDropAreaCall25 call = reinterpret_cast<CuteQQuickDropAreaCall25>(taken[25]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItem::touchUngrabEvent();
  }

#if QT_CONFIG(wheelevent)
  //  void QQuickItem::wheelEvent(QWheelEvent *event)
  void wheelEvent(QWheelEvent *event) override {
    if (taken[26]) {
      int handled = 0;
      CuteQQuickDropAreaCall26 call = reinterpret_cast<CuteQQuickDropAreaCall26>(taken[26]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::wheelEvent(event);
  }
#endif  // QT_CONFIG(wheelevent)

  //  void QQuickItem::touchEvent(QTouchEvent *event)
  void touchEvent(QTouchEvent *event) override {
    if (taken[27]) {
      int handled = 0;
      CuteQQuickDropAreaCall27 call = reinterpret_cast<CuteQQuickDropAreaCall27>(taken[27]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::touchEvent(event);
  }

  //  void QQuickItem::hoverEnterEvent(QHoverEvent *event)
  void hoverEnterEvent(QHoverEvent *event) override {
    if (taken[28]) {
      int handled = 0;
      CuteQQuickDropAreaCall28 call = reinterpret_cast<CuteQQuickDropAreaCall28>(taken[28]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::hoverEnterEvent(event);
  }

  //  void QQuickItem::hoverMoveEvent(QHoverEvent *event)
  void hoverMoveEvent(QHoverEvent *event) override {
    if (taken[29]) {
      int handled = 0;
      CuteQQuickDropAreaCall29 call = reinterpret_cast<CuteQQuickDropAreaCall29>(taken[29]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::hoverMoveEvent(event);
  }

  //  void QQuickItem::hoverLeaveEvent(QHoverEvent *event)
  void hoverLeaveEvent(QHoverEvent *event) override {
    if (taken[30]) {
      int handled = 0;
      CuteQQuickDropAreaCall30 call = reinterpret_cast<CuteQQuickDropAreaCall30>(taken[30]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::hoverLeaveEvent(event);
  }

  //  bool QQuickItem::childMouseEventFilter(QQuickItem *a0, QEvent *a1)
  bool childMouseEventFilter(QQuickItem *a0, QEvent *a1) override {
    if (taken[31]) {
      int handled = 0;
      CuteQQuickDropAreaCall31 call = reinterpret_cast<CuteQQuickDropAreaCall31>(taken[31]);
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
      CuteQQuickDropAreaCall32 call = reinterpret_cast<CuteQQuickDropAreaCall32>(taken[32]);
      void * given = call(this, a0, a1, &handled);
      if (handled) return static_cast<QSGNode *>(given);
    }
    return QQuickItem::updatePaintNode(a0, a1);
  }

  //  void QQuickItem::releaseResources()
  void releaseResources() override {
    if (taken[33]) {
      int handled = 0;
      CuteQQuickDropAreaCall33 call = reinterpret_cast<CuteQQuickDropAreaCall33>(taken[33]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItem::releaseResources();
  }

  //  void QQuickItem::updatePolish()
  void updatePolish() override {
    if (taken[34]) {
      int handled = 0;
      CuteQQuickDropAreaCall34 call = reinterpret_cast<CuteQQuickDropAreaCall34>(taken[34]);
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
      CuteQQuickDropAreaCall35 call = reinterpret_cast<CuteQQuickDropAreaCall35>(taken[35]);
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
      CuteQQuickDropAreaCall36 call = reinterpret_cast<CuteQQuickDropAreaCall36>(taken[36]);
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
      CuteQQuickDropAreaCall37 call = reinterpret_cast<CuteQQuickDropAreaCall37>(taken[37]);
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
      CuteQQuickDropAreaCall38 call = reinterpret_cast<CuteQQuickDropAreaCall38>(taken[38]);
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
      CuteQQuickDropAreaCall39 call = reinterpret_cast<CuteQQuickDropAreaCall39>(taken[39]);
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
      CuteQQuickDropAreaCall40 call = reinterpret_cast<CuteQQuickDropAreaCall40>(taken[40]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QQuickDropArea::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK14QQuickDropArea10metaObjectEv(
    const QQuickDropArea *self) {
  return self->metaObject();
}

//  QString QQuickDropArea::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN14QQuickDropArea2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuickDropArea::tr(s, c, n));
}

//  QQuickDropArea::QQuickDropArea(QQuickItem *parent)
extern "C" Q_DECL_EXPORT
QQuickDropArea *ritual_ZN14QQuickDropAreaC1EP10QQuickItem(
    QQuickItem *parent) {
  return new CuteQQuickDropArea(parent);
}

//  QQuickDropArea::~QQuickDropArea()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickDropAreaD1Ev(QQuickDropArea *self) {
  delete self;
}

//  bool QQuickDropArea::containsDrag() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK14QQuickDropArea12containsDragEv(const QQuickDropArea *self) {
  return self->containsDrag();
}

//  QStringList QQuickDropArea::keys() const
extern "C" Q_DECL_EXPORT
QList<QString> *ritual_ZNK14QQuickDropArea4keysEv(
    const QQuickDropArea *self) {
  return new QList<QString>(self->keys());
}

//  void QQuickDropArea::setKeys(const QStringList &keys)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickDropArea7setKeysERK5QListI7QStringE(
    QQuickDropArea *self,
    const QList<QString> *keys) {
  self->setKeys(*keys);
}

//  QQuickDropAreaDrag *QQuickDropArea::drag()
extern "C" Q_DECL_EXPORT
QQuickDropAreaDrag *ritual_ZN14QQuickDropArea4dragEv(QQuickDropArea *self) {
  return self->drag();
}

//  void QQuickDropArea::dragMoveEvent(QDragMoveEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickDropArea13dragMoveEventEP14QDragMoveEvent(
    QQuickDropArea *self,
    QDragMoveEvent *event) {
  self->dragMoveEvent(event);
}

//  void QQuickDropArea::dragEnterEvent(QDragEnterEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickDropArea14dragEnterEventEP15QDragEnterEvent(
    QQuickDropArea *self,
    QDragEnterEvent *event) {
  self->dragEnterEvent(event);
}

//  void QQuickDropArea::dragLeaveEvent(QDragLeaveEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickDropArea14dragLeaveEventEP15QDragLeaveEvent(
    QQuickDropArea *self,
    QDragLeaveEvent *event) {
  self->dragLeaveEvent(event);
}

//  void QQuickDropArea::dropEvent(QDropEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickDropArea9dropEventEP10QDropEvent(
    QQuickDropArea *self,
    QDropEvent *event) {
  self->dropEvent(event);
}

//  a Python function taken by a CuteQQuickDropArea, for the function named
//      by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQuickDropArea(
    QQuickDropArea *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQuickDropArea *>(self)->take(key, call);
}

//  void QQuickDropArea::dragMoveEvent(QDragMoveEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN14QQuickDropArea13dragMoveEventEP14QDragMoveEvent(
    QQuickDropArea *self,
    QDragMoveEvent *event) {
  static_cast<OwnQQuickDropArea *>(self)->OwnQQuickDropArea::dragMoveEvent(
      event);
}

//  void QQuickDropArea::dragEnterEvent(QDragEnterEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN14QQuickDropArea14dragEnterEventEP15QDragEnterEvent(
    QQuickDropArea *self,
    QDragEnterEvent *event) {
  static_cast<OwnQQuickDropArea *>(self)->OwnQQuickDropArea::dragEnterEvent(
      event);
}

//  void QQuickDropArea::dragLeaveEvent(QDragLeaveEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN14QQuickDropArea14dragLeaveEventEP15QDragLeaveEvent(
    QQuickDropArea *self,
    QDragLeaveEvent *event) {
  static_cast<OwnQQuickDropArea *>(self)->OwnQQuickDropArea::dragLeaveEvent(
      event);
}

//  void QQuickDropArea::dropEvent(QDropEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN14QQuickDropArea9dropEventEP10QDropEvent(
    QQuickDropArea *self,
    QDropEvent *event) {
  static_cast<OwnQQuickDropArea *>(self)->OwnQQuickDropArea::dropEvent(
      event);
}

#endif  // QT_CONFIG(quick_draganddrop)
