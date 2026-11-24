//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qquickoverlay_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtGui/qtguiglobal.h>
#include <QtQuick/qtquickglobal.h>
#include <QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qtquicktemplates2global_p.h>
#include <QtQuickTemplates2/QtQuickTemplates2>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qquickoverlay_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtQuick/QtQuick>
#include <QtQuick/qquickitem.h>
#include <QtCore/qrect.h>
#include <QtCore/qpoint.h>
#include <QtCore/qvariant.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  Only a class built on QQuickOverlay may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQQuickOverlay : QQuickOverlay {
  using QQuickOverlay::itemChange;
  using QQuickOverlay::geometryChange;
  using QQuickOverlay::mousePressEvent;
  using QQuickOverlay::mouseMoveEvent;
  using QQuickOverlay::mouseReleaseEvent;
  using QQuickOverlay::touchEvent;
  using QQuickOverlay::wheelEvent;
  using QQuickOverlay::dragEnterEvent;
  using QQuickOverlay::dragMoveEvent;
  using QQuickOverlay::dragLeaveEvent;
  using QQuickOverlay::dropEvent;
  using QQuickOverlay::childMouseEventFilter;
  using QQuickOverlay::eventFilter;
};

//  A QQuickOverlay that Python can take functions over in. Every QQuickOverlay
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQQuickOverlayCall0)(const void *, int, const QQuickItem::ItemChangeData *, int *);
typedef void (*CuteQQuickOverlayCall1)(const void *, const QRectF *, const QRectF *, int *);
typedef void (*CuteQQuickOverlayCall2)(const void *, QMouseEvent *, int *);
typedef void (*CuteQQuickOverlayCall3)(const void *, QMouseEvent *, int *);
typedef void (*CuteQQuickOverlayCall4)(const void *, QMouseEvent *, int *);
#if QT_CONFIG(quicktemplates2_multitouch)
typedef void (*CuteQQuickOverlayCall5)(const void *, QTouchEvent *, int *);
#endif  // QT_CONFIG(quicktemplates2_multitouch)
#if QT_CONFIG(wheelevent)
typedef void (*CuteQQuickOverlayCall6)(const void *, QWheelEvent *, int *);
#endif  // QT_CONFIG(wheelevent)
#if QT_CONFIG(quick_draganddrop)
typedef void (*CuteQQuickOverlayCall7)(const void *, QDragEnterEvent *, int *);
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
typedef void (*CuteQQuickOverlayCall8)(const void *, QDragMoveEvent *, int *);
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
typedef void (*CuteQQuickOverlayCall9)(const void *, QDragLeaveEvent *, int *);
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
typedef void (*CuteQQuickOverlayCall10)(const void *, QDropEvent *, int *);
#endif  // QT_CONFIG(quick_draganddrop)
typedef bool (*CuteQQuickOverlayCall11)(const void *, QQuickItem *, QEvent *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickOverlayCall12)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
typedef const QRectF * (*CuteQQuickOverlayCall13)(const void *, int *);
typedef const QRectF * (*CuteQQuickOverlayCall14)(const void *, int *);
typedef bool (*CuteQQuickOverlayCall15)(const void *, const QPointF *, int *);
#if QT_CONFIG(im)
typedef const QVariant * (*CuteQQuickOverlayCall16)(const void *, int, int *);
#endif  // QT_CONFIG(im)
typedef bool (*CuteQQuickOverlayCall17)(const void *, int *);
typedef void * (*CuteQQuickOverlayCall18)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickOverlayCall19)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickOverlayCall20)(const void *, int *);
typedef void (*CuteQQuickOverlayCall21)(const void *, int *);
typedef void (*CuteQQuickOverlayCall22)(const void *, QKeyEvent *, int *);
typedef void (*CuteQQuickOverlayCall23)(const void *, QKeyEvent *, int *);
#if QT_CONFIG(im)
typedef void (*CuteQQuickOverlayCall24)(const void *, QInputMethodEvent *, int *);
#endif  // QT_CONFIG(im)
typedef void (*CuteQQuickOverlayCall25)(const void *, QFocusEvent *, int *);
typedef void (*CuteQQuickOverlayCall26)(const void *, QFocusEvent *, int *);
typedef void (*CuteQQuickOverlayCall27)(const void *, QMouseEvent *, int *);
typedef void (*CuteQQuickOverlayCall28)(const void *, int *);
typedef void (*CuteQQuickOverlayCall29)(const void *, int *);
typedef void (*CuteQQuickOverlayCall30)(const void *, QHoverEvent *, int *);
typedef void (*CuteQQuickOverlayCall31)(const void *, QHoverEvent *, int *);
typedef void (*CuteQQuickOverlayCall32)(const void *, QHoverEvent *, int *);
typedef void * (*CuteQQuickOverlayCall33)(const void *, QSGNode *, QQuickItem::UpdatePaintNodeData *, int *);
typedef void (*CuteQQuickOverlayCall34)(const void *, int *);
typedef void (*CuteQQuickOverlayCall35)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickOverlayCall36)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickOverlayCall37)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickOverlayCall38)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickOverlayCall39)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickOverlayCall40)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQQuickOverlay : public QQuickOverlay {
public:
  using QQuickOverlay::QQuickOverlay;
  void *taken[41] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN10QQuickItem10itemChangeENS_10ItemChangeERKNS_14ItemChangeDataE")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem14geometryChangeERK6QRectFS2_")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem15mousePressEventEP11QMouseEvent")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem14mouseMoveEventEP11QMouseEvent")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem17mouseReleaseEventEP11QMouseEvent")) {
      taken[4] = call;
      return true;
    }
#if QT_CONFIG(quicktemplates2_multitouch)
    if (!std::strcmp(key, "_ZN10QQuickItem10touchEventEP11QTouchEvent")) {
      taken[5] = call;
      return true;
    }
#endif  // QT_CONFIG(quicktemplates2_multitouch)
#if QT_CONFIG(wheelevent)
    if (!std::strcmp(key, "_ZN10QQuickItem10wheelEventEP11QWheelEvent")) {
      taken[6] = call;
      return true;
    }
#endif  // QT_CONFIG(wheelevent)
#if QT_CONFIG(quick_draganddrop)
    if (!std::strcmp(key, "_ZN10QQuickItem14dragEnterEventEP15QDragEnterEvent")) {
      taken[7] = call;
      return true;
    }
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
    if (!std::strcmp(key, "_ZN10QQuickItem13dragMoveEventEP14QDragMoveEvent")) {
      taken[8] = call;
      return true;
    }
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
    if (!std::strcmp(key, "_ZN10QQuickItem14dragLeaveEventEP15QDragLeaveEvent")) {
      taken[9] = call;
      return true;
    }
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
    if (!std::strcmp(key, "_ZN10QQuickItem9dropEventEP10QDropEvent")) {
      taken[10] = call;
      return true;
    }
#endif  // QT_CONFIG(quick_draganddrop)
    if (!std::strcmp(key, "_ZN10QQuickItem21childMouseEventFilterEPS_P6QEvent")) {
      taken[11] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[12] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZNK10QQuickItem12boundingRectEv")) {
      taken[13] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK10QQuickItem8clipRectEv")) {
      taken[14] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK10QQuickItem8containsERK7QPointF")) {
      taken[15] = call;
      return true;
    }
#if QT_CONFIG(im)
    if (!std::strcmp(key, "_ZNK10QQuickItem16inputMethodQueryEN2Qt16InputMethodQueryE")) {
      taken[16] = call;
      return true;
    }
#endif  // QT_CONFIG(im)
    if (!std::strcmp(key, "_ZNK10QQuickItem17isTextureProviderEv")) {
      taken[17] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK10QQuickItem15textureProviderEv")) {
      taken[18] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[19] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN16QQmlParserStatus10classBeginEv")) {
      taken[20] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQmlParserStatus17componentCompleteEv")) {
      taken[21] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem13keyPressEventEP9QKeyEvent")) {
      taken[22] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem15keyReleaseEventEP9QKeyEvent")) {
      taken[23] = call;
      return true;
    }
#if QT_CONFIG(im)
    if (!std::strcmp(key, "_ZN10QQuickItem16inputMethodEventEP17QInputMethodEvent")) {
      taken[24] = call;
      return true;
    }
#endif  // QT_CONFIG(im)
    if (!std::strcmp(key, "_ZN10QQuickItem12focusInEventEP11QFocusEvent")) {
      taken[25] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem13focusOutEventEP11QFocusEvent")) {
      taken[26] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem21mouseDoubleClickEventEP11QMouseEvent")) {
      taken[27] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem16mouseUngrabEventEv")) {
      taken[28] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem16touchUngrabEventEv")) {
      taken[29] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem15hoverEnterEventEP11QHoverEvent")) {
      taken[30] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem14hoverMoveEventEP11QHoverEvent")) {
      taken[31] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem15hoverLeaveEventEP11QHoverEvent")) {
      taken[32] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem15updatePaintNodeEP7QSGNodePNS_19UpdatePaintNodeDataE")) {
      taken[33] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem16releaseResourcesEv")) {
      taken[34] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem12updatePolishEv")) {
      taken[35] = call;
      return true;
    }
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

  //  void QQuickOverlay::itemChange(ItemChange change, const
  //      ItemChangeData &data)
  void itemChange(
      QQuickItem::ItemChange change,
      const QQuickItem::ItemChangeData &data) override {
    if (taken[0]) {
      int handled = 0;
      CuteQQuickOverlayCall0 call = reinterpret_cast<CuteQQuickOverlayCall0>(taken[0]);
      call(this, static_cast<int>(change), &data, &handled);
      if (handled) return;
    }
    QQuickOverlay::itemChange(change, data);
  }

  //  void QQuickOverlay::geometryChange(const QRectF &newGeometry, const
  //      QRectF &oldGeometry)
  void geometryChange(
      const QRectF &newGeometry,
      const QRectF &oldGeometry) override {
    if (taken[1]) {
      int handled = 0;
      CuteQQuickOverlayCall1 call = reinterpret_cast<CuteQQuickOverlayCall1>(taken[1]);
      call(this, &newGeometry, &oldGeometry, &handled);
      if (handled) return;
    }
    QQuickOverlay::geometryChange(newGeometry, oldGeometry);
  }

  //  void QQuickOverlay::mousePressEvent(QMouseEvent *event)
  void mousePressEvent(QMouseEvent *event) override {
    if (taken[2]) {
      int handled = 0;
      CuteQQuickOverlayCall2 call = reinterpret_cast<CuteQQuickOverlayCall2>(taken[2]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickOverlay::mousePressEvent(event);
  }

  //  void QQuickOverlay::mouseMoveEvent(QMouseEvent *event)
  void mouseMoveEvent(QMouseEvent *event) override {
    if (taken[3]) {
      int handled = 0;
      CuteQQuickOverlayCall3 call = reinterpret_cast<CuteQQuickOverlayCall3>(taken[3]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickOverlay::mouseMoveEvent(event);
  }

  //  void QQuickOverlay::mouseReleaseEvent(QMouseEvent *event)
  void mouseReleaseEvent(QMouseEvent *event) override {
    if (taken[4]) {
      int handled = 0;
      CuteQQuickOverlayCall4 call = reinterpret_cast<CuteQQuickOverlayCall4>(taken[4]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickOverlay::mouseReleaseEvent(event);
  }

#if QT_CONFIG(quicktemplates2_multitouch)
  //  void QQuickOverlay::touchEvent(QTouchEvent *event)
  void touchEvent(QTouchEvent *event) override {
    if (taken[5]) {
      int handled = 0;
      CuteQQuickOverlayCall5 call = reinterpret_cast<CuteQQuickOverlayCall5>(taken[5]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickOverlay::touchEvent(event);
  }
#endif  // QT_CONFIG(quicktemplates2_multitouch)

#if QT_CONFIG(wheelevent)
  //  void QQuickOverlay::wheelEvent(QWheelEvent *event)
  void wheelEvent(QWheelEvent *event) override {
    if (taken[6]) {
      int handled = 0;
      CuteQQuickOverlayCall6 call = reinterpret_cast<CuteQQuickOverlayCall6>(taken[6]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickOverlay::wheelEvent(event);
  }
#endif  // QT_CONFIG(wheelevent)

#if QT_CONFIG(quick_draganddrop)
  //  void QQuickOverlay::dragEnterEvent(QDragEnterEvent *event)
  void dragEnterEvent(QDragEnterEvent *event) override {
    if (taken[7]) {
      int handled = 0;
      CuteQQuickOverlayCall7 call = reinterpret_cast<CuteQQuickOverlayCall7>(taken[7]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickOverlay::dragEnterEvent(event);
  }
#endif  // QT_CONFIG(quick_draganddrop)

#if QT_CONFIG(quick_draganddrop)
  //  void QQuickOverlay::dragMoveEvent(QDragMoveEvent *event)
  void dragMoveEvent(QDragMoveEvent *event) override {
    if (taken[8]) {
      int handled = 0;
      CuteQQuickOverlayCall8 call = reinterpret_cast<CuteQQuickOverlayCall8>(taken[8]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickOverlay::dragMoveEvent(event);
  }
#endif  // QT_CONFIG(quick_draganddrop)

#if QT_CONFIG(quick_draganddrop)
  //  void QQuickOverlay::dragLeaveEvent(QDragLeaveEvent *event)
  void dragLeaveEvent(QDragLeaveEvent *event) override {
    if (taken[9]) {
      int handled = 0;
      CuteQQuickOverlayCall9 call = reinterpret_cast<CuteQQuickOverlayCall9>(taken[9]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickOverlay::dragLeaveEvent(event);
  }
#endif  // QT_CONFIG(quick_draganddrop)

#if QT_CONFIG(quick_draganddrop)
  //  void QQuickOverlay::dropEvent(QDropEvent *event)
  void dropEvent(QDropEvent *event) override {
    if (taken[10]) {
      int handled = 0;
      CuteQQuickOverlayCall10 call = reinterpret_cast<CuteQQuickOverlayCall10>(taken[10]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickOverlay::dropEvent(event);
  }
#endif  // QT_CONFIG(quick_draganddrop)

  //  bool QQuickOverlay::childMouseEventFilter(QQuickItem *item, QEvent
  //      *event)
  bool childMouseEventFilter(QQuickItem *item, QEvent *event) override {
    if (taken[11]) {
      int handled = 0;
      CuteQQuickOverlayCall11 call = reinterpret_cast<CuteQQuickOverlayCall11>(taken[11]);
      bool given = call(this, item, event, &handled);
      if (handled) return given;
    }
    return QQuickOverlay::childMouseEventFilter(item, event);
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QQuickOverlay::eventFilter(QObject *object, QEvent *event)
  bool eventFilter(QObject *object, QEvent *event) override {
    if (taken[12]) {
      int handled = 0;
      CuteQQuickOverlayCall12 call = reinterpret_cast<CuteQQuickOverlayCall12>(taken[12]);
      bool given = call(this, object, event, &handled);
      if (handled) return given;
    }
    return QQuickOverlay::eventFilter(object, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

  //  QRectF QQuickItem::boundingRect() const
  QRectF boundingRect() const override {
    if (taken[13]) {
      int handled = 0;
      CuteQQuickOverlayCall13 call = reinterpret_cast<CuteQQuickOverlayCall13>(taken[13]);
      const QRectF * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QQuickItem::boundingRect();
  }

  //  QRectF QQuickItem::clipRect() const
  QRectF clipRect() const override {
    if (taken[14]) {
      int handled = 0;
      CuteQQuickOverlayCall14 call = reinterpret_cast<CuteQQuickOverlayCall14>(taken[14]);
      const QRectF * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QQuickItem::clipRect();
  }

  //  bool QQuickItem::contains(const QPointF &point) const
  bool contains(const QPointF &point) const override {
    if (taken[15]) {
      int handled = 0;
      CuteQQuickOverlayCall15 call = reinterpret_cast<CuteQQuickOverlayCall15>(taken[15]);
      bool given = call(this, &point, &handled);
      if (handled) return given;
    }
    return QQuickItem::contains(point);
  }

#if QT_CONFIG(im)
  //  QVariant QQuickItem::inputMethodQuery(Qt::InputMethodQuery query)
  //      const
  QVariant inputMethodQuery(Qt::InputMethodQuery query) const override {
    if (taken[16]) {
      int handled = 0;
      CuteQQuickOverlayCall16 call = reinterpret_cast<CuteQQuickOverlayCall16>(taken[16]);
      const QVariant * given = call(this, static_cast<int>(query), &handled);
      if (handled && given) return *given;
    }
    return QQuickItem::inputMethodQuery(query);
  }
#endif  // QT_CONFIG(im)

  //  bool QQuickItem::isTextureProvider() const
  bool isTextureProvider() const override {
    if (taken[17]) {
      int handled = 0;
      CuteQQuickOverlayCall17 call = reinterpret_cast<CuteQQuickOverlayCall17>(taken[17]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QQuickItem::isTextureProvider();
  }

  //  QSGTextureProvider *QQuickItem::textureProvider() const
  QSGTextureProvider *textureProvider() const override {
    if (taken[18]) {
      int handled = 0;
      CuteQQuickOverlayCall18 call = reinterpret_cast<CuteQQuickOverlayCall18>(taken[18]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QSGTextureProvider *>(given);
    }
    return QQuickItem::textureProvider();
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QQuickItem::event(QEvent *a0)
  bool event(QEvent *a0) override {
    if (taken[19]) {
      int handled = 0;
      CuteQQuickOverlayCall19 call = reinterpret_cast<CuteQQuickOverlayCall19>(taken[19]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQuickItem::event(a0);
  }
#endif  // !defined(QT_NO_QOBJECT)

  //  void QQuickItem::classBegin()
  void classBegin() override {
    if (taken[20]) {
      int handled = 0;
      CuteQQuickOverlayCall20 call = reinterpret_cast<CuteQQuickOverlayCall20>(taken[20]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItem::classBegin();
  }

  //  void QQuickItem::componentComplete()
  void componentComplete() override {
    if (taken[21]) {
      int handled = 0;
      CuteQQuickOverlayCall21 call = reinterpret_cast<CuteQQuickOverlayCall21>(taken[21]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItem::componentComplete();
  }

  //  void QQuickItem::keyPressEvent(QKeyEvent *event)
  void keyPressEvent(QKeyEvent *event) override {
    if (taken[22]) {
      int handled = 0;
      CuteQQuickOverlayCall22 call = reinterpret_cast<CuteQQuickOverlayCall22>(taken[22]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::keyPressEvent(event);
  }

  //  void QQuickItem::keyReleaseEvent(QKeyEvent *event)
  void keyReleaseEvent(QKeyEvent *event) override {
    if (taken[23]) {
      int handled = 0;
      CuteQQuickOverlayCall23 call = reinterpret_cast<CuteQQuickOverlayCall23>(taken[23]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::keyReleaseEvent(event);
  }

#if QT_CONFIG(im)
  //  void QQuickItem::inputMethodEvent(QInputMethodEvent *a0)
  void inputMethodEvent(QInputMethodEvent *a0) override {
    if (taken[24]) {
      int handled = 0;
      CuteQQuickOverlayCall24 call = reinterpret_cast<CuteQQuickOverlayCall24>(taken[24]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItem::inputMethodEvent(a0);
  }
#endif  // QT_CONFIG(im)

  //  void QQuickItem::focusInEvent(QFocusEvent *a0)
  void focusInEvent(QFocusEvent *a0) override {
    if (taken[25]) {
      int handled = 0;
      CuteQQuickOverlayCall25 call = reinterpret_cast<CuteQQuickOverlayCall25>(taken[25]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItem::focusInEvent(a0);
  }

  //  void QQuickItem::focusOutEvent(QFocusEvent *a0)
  void focusOutEvent(QFocusEvent *a0) override {
    if (taken[26]) {
      int handled = 0;
      CuteQQuickOverlayCall26 call = reinterpret_cast<CuteQQuickOverlayCall26>(taken[26]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItem::focusOutEvent(a0);
  }

  //  void QQuickItem::mouseDoubleClickEvent(QMouseEvent *event)
  void mouseDoubleClickEvent(QMouseEvent *event) override {
    if (taken[27]) {
      int handled = 0;
      CuteQQuickOverlayCall27 call = reinterpret_cast<CuteQQuickOverlayCall27>(taken[27]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::mouseDoubleClickEvent(event);
  }

  //  void QQuickItem::mouseUngrabEvent()
  void mouseUngrabEvent() override {
    if (taken[28]) {
      int handled = 0;
      CuteQQuickOverlayCall28 call = reinterpret_cast<CuteQQuickOverlayCall28>(taken[28]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItem::mouseUngrabEvent();
  }

  //  void QQuickItem::touchUngrabEvent()
  void touchUngrabEvent() override {
    if (taken[29]) {
      int handled = 0;
      CuteQQuickOverlayCall29 call = reinterpret_cast<CuteQQuickOverlayCall29>(taken[29]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItem::touchUngrabEvent();
  }

  //  void QQuickItem::hoverEnterEvent(QHoverEvent *event)
  void hoverEnterEvent(QHoverEvent *event) override {
    if (taken[30]) {
      int handled = 0;
      CuteQQuickOverlayCall30 call = reinterpret_cast<CuteQQuickOverlayCall30>(taken[30]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::hoverEnterEvent(event);
  }

  //  void QQuickItem::hoverMoveEvent(QHoverEvent *event)
  void hoverMoveEvent(QHoverEvent *event) override {
    if (taken[31]) {
      int handled = 0;
      CuteQQuickOverlayCall31 call = reinterpret_cast<CuteQQuickOverlayCall31>(taken[31]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::hoverMoveEvent(event);
  }

  //  void QQuickItem::hoverLeaveEvent(QHoverEvent *event)
  void hoverLeaveEvent(QHoverEvent *event) override {
    if (taken[32]) {
      int handled = 0;
      CuteQQuickOverlayCall32 call = reinterpret_cast<CuteQQuickOverlayCall32>(taken[32]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::hoverLeaveEvent(event);
  }

  //  QSGNode *QQuickItem::updatePaintNode(QSGNode *a0, UpdatePaintNodeData
  //      *a1)
  QSGNode *updatePaintNode(
      QSGNode *a0,
      QQuickItem::UpdatePaintNodeData *a1) override {
    if (taken[33]) {
      int handled = 0;
      CuteQQuickOverlayCall33 call = reinterpret_cast<CuteQQuickOverlayCall33>(taken[33]);
      void * given = call(this, a0, a1, &handled);
      if (handled) return static_cast<QSGNode *>(given);
    }
    return QQuickItem::updatePaintNode(a0, a1);
  }

  //  void QQuickItem::releaseResources()
  void releaseResources() override {
    if (taken[34]) {
      int handled = 0;
      CuteQQuickOverlayCall34 call = reinterpret_cast<CuteQQuickOverlayCall34>(taken[34]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItem::releaseResources();
  }

  //  void QQuickItem::updatePolish()
  void updatePolish() override {
    if (taken[35]) {
      int handled = 0;
      CuteQQuickOverlayCall35 call = reinterpret_cast<CuteQQuickOverlayCall35>(taken[35]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItem::updatePolish();
  }

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[36]) {
      int handled = 0;
      CuteQQuickOverlayCall36 call = reinterpret_cast<CuteQQuickOverlayCall36>(taken[36]);
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
      CuteQQuickOverlayCall37 call = reinterpret_cast<CuteQQuickOverlayCall37>(taken[37]);
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
      CuteQQuickOverlayCall38 call = reinterpret_cast<CuteQQuickOverlayCall38>(taken[38]);
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
      CuteQQuickOverlayCall39 call = reinterpret_cast<CuteQQuickOverlayCall39>(taken[39]);
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
      CuteQQuickOverlayCall40 call = reinterpret_cast<CuteQQuickOverlayCall40>(taken[40]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QQuickOverlay::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK13QQuickOverlay10metaObjectEv(
    const QQuickOverlay *self) {
  return self->metaObject();
}

//  QString QQuickOverlay::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN13QQuickOverlay2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuickOverlay::tr(s, c, n));
}

//  void QQuickOverlay::qt_qmlMarker_attached()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QQuickOverlay21qt_qmlMarker_attachedEv(QQuickOverlay *self) {
  self->qt_qmlMarker_attached();
}

//  void QQuickOverlay::qt_qmlMarker_uncreatable()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QQuickOverlay24qt_qmlMarker_uncreatableEv(
    QQuickOverlay *self) {
  self->qt_qmlMarker_uncreatable();
}

//  QQuickOverlay::QQuickOverlay(QQuickItem *parent)
extern "C" Q_DECL_EXPORT
QQuickOverlay *ritual_ZN13QQuickOverlayC1EP10QQuickItem(QQuickItem *parent) {
  return new CuteQQuickOverlay(parent);
}

//  QQuickOverlay::~QQuickOverlay()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QQuickOverlayD1Ev(QQuickOverlay *self) {
  delete self;
}

//  QQmlComponent *QQuickOverlay::modal() const
extern "C" Q_DECL_EXPORT
QQmlComponent *ritual_ZNK13QQuickOverlay5modalEv(const QQuickOverlay *self) {
  return self->modal();
}

//  void QQuickOverlay::setModal(QQmlComponent *modal)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QQuickOverlay8setModalEP13QQmlComponent(
    QQuickOverlay *self,
    QQmlComponent *modal) {
  self->setModal(modal);
}

//  QQmlComponent *QQuickOverlay::modeless() const
extern "C" Q_DECL_EXPORT
QQmlComponent *ritual_ZNK13QQuickOverlay8modelessEv(
    const QQuickOverlay *self) {
  return self->modeless();
}

//  void QQuickOverlay::setModeless(QQmlComponent *modeless)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QQuickOverlay11setModelessEP13QQmlComponent(
    QQuickOverlay *self,
    QQmlComponent *modeless) {
  self->setModeless(modeless);
}

//  QQuickOverlay *QQuickOverlay::overlay(QQuickWindow *window, QQuickItem
//      *parent)
extern "C" Q_DECL_EXPORT
QQuickOverlay *ritual_ZN13QQuickOverlay7overlayEP12QQuickWindowP10QQuickItem(
    QQuickWindow *window,
    QQuickItem *parent) {
  return QQuickOverlay::overlay(window, parent);
}

//  QQuickOverlayAttached *QQuickOverlay::qmlAttachedProperties(QObject
//      *object)
extern "C" Q_DECL_EXPORT
QQuickOverlayAttached *ritual_ZN13QQuickOverlay21qmlAttachedPropertiesEP7QObject(
    QObject *object) {
  return QQuickOverlay::qmlAttachedProperties(object);
}

//  void QQuickOverlay::itemChange(ItemChange change, const ItemChangeData
//      &data)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QQuickOverlay10itemChangeEN10QQuickItem10ItemChangeERKNS0_14ItemChangeDataE(
    QQuickOverlay *self,
    QQuickItem::ItemChange change,
    const QQuickItem::ItemChangeData *data) {
  self->itemChange(change, *data);
}

//  void QQuickOverlay::geometryChange(const QRectF &newGeometry, const
//      QRectF &oldGeometry)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QQuickOverlay14geometryChangeERK6QRectFS2_(
    QQuickOverlay *self,
    const QRectF *newGeometry,
    const QRectF *oldGeometry) {
  self->geometryChange(*newGeometry, *oldGeometry);
}

//  void QQuickOverlay::mousePressEvent(QMouseEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QQuickOverlay15mousePressEventEP11QMouseEvent(
    QQuickOverlay *self,
    QMouseEvent *event) {
  self->mousePressEvent(event);
}

//  void QQuickOverlay::mouseMoveEvent(QMouseEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QQuickOverlay14mouseMoveEventEP11QMouseEvent(
    QQuickOverlay *self,
    QMouseEvent *event) {
  self->mouseMoveEvent(event);
}

//  void QQuickOverlay::mouseReleaseEvent(QMouseEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QQuickOverlay17mouseReleaseEventEP11QMouseEvent(
    QQuickOverlay *self,
    QMouseEvent *event) {
  self->mouseReleaseEvent(event);
}

#if QT_CONFIG(quicktemplates2_multitouch)
//  void QQuickOverlay::touchEvent(QTouchEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QQuickOverlay10touchEventEP11QTouchEvent(
    QQuickOverlay *self,
    QTouchEvent *event) {
  self->touchEvent(event);
}
#endif  // QT_CONFIG(quicktemplates2_multitouch)

#if QT_CONFIG(wheelevent)
//  void QQuickOverlay::wheelEvent(QWheelEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QQuickOverlay10wheelEventEP11QWheelEvent(
    QQuickOverlay *self,
    QWheelEvent *event) {
  self->wheelEvent(event);
}
#endif  // QT_CONFIG(wheelevent)

#if QT_CONFIG(quick_draganddrop)
//  void QQuickOverlay::dragEnterEvent(QDragEnterEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QQuickOverlay14dragEnterEventEP15QDragEnterEvent(
    QQuickOverlay *self,
    QDragEnterEvent *event) {
  self->dragEnterEvent(event);
}
#endif  // QT_CONFIG(quick_draganddrop)

#if QT_CONFIG(quick_draganddrop)
//  void QQuickOverlay::dragMoveEvent(QDragMoveEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QQuickOverlay13dragMoveEventEP14QDragMoveEvent(
    QQuickOverlay *self,
    QDragMoveEvent *event) {
  self->dragMoveEvent(event);
}
#endif  // QT_CONFIG(quick_draganddrop)

#if QT_CONFIG(quick_draganddrop)
//  void QQuickOverlay::dragLeaveEvent(QDragLeaveEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QQuickOverlay14dragLeaveEventEP15QDragLeaveEvent(
    QQuickOverlay *self,
    QDragLeaveEvent *event) {
  self->dragLeaveEvent(event);
}
#endif  // QT_CONFIG(quick_draganddrop)

#if QT_CONFIG(quick_draganddrop)
//  void QQuickOverlay::dropEvent(QDropEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QQuickOverlay9dropEventEP10QDropEvent(
    QQuickOverlay *self,
    QDropEvent *event) {
  self->dropEvent(event);
}
#endif  // QT_CONFIG(quick_draganddrop)

//  void QQuickOverlay::handleWheelAndDnDEvents(QEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QQuickOverlay23handleWheelAndDnDEventsEP6QEvent(
    QQuickOverlay *self,
    QEvent *event) {
  self->handleWheelAndDnDEvents(event);
}

//  bool QQuickOverlay::childMouseEventFilter(QQuickItem *item, QEvent
//      *event)
extern "C" Q_DECL_EXPORT
bool ritual_ZN13QQuickOverlay21childMouseEventFilterEP10QQuickItemP6QEvent(
    QQuickOverlay *self,
    QQuickItem *item,
    QEvent *event) {
  return self->childMouseEventFilter(item, event);
}

//  bool QQuickOverlay::eventFilter(QObject *object, QEvent *event)
extern "C" Q_DECL_EXPORT
bool ritual_ZN13QQuickOverlay11eventFilterEP7QObjectP6QEvent(
    QQuickOverlay *self,
    QObject *object,
    QEvent *event) {
  return self->eventFilter(object, event);
}

//  QQuickOverlayPrivate *QQuickOverlay::d_func()
extern "C" Q_DECL_EXPORT
QQuickOverlayPrivate *ritual_ZN13QQuickOverlay6d_funcEv(
    QQuickOverlay *self) {
  return self->d_func();
}

//  const QQuickOverlayPrivate *QQuickOverlay::d_func() const
extern "C" Q_DECL_EXPORT
const QQuickOverlayPrivate *ritual_ZNK13QQuickOverlay6d_funcEv(
    const QQuickOverlay *self) {
  return self->d_func();
}

//  a Python function taken by a CuteQQuickOverlay, for the function named by
//      the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQuickOverlay(
    QQuickOverlay *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQuickOverlay *>(self)->take(key, call);
}

//  void QQuickOverlay::itemChange(ItemChange change, const ItemChangeData
//      &data)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN13QQuickOverlay10itemChangeEN10QQuickItem10ItemChangeERKNS0_14ItemChangeDataE(
    QQuickOverlay *self,
    QQuickItem::ItemChange change,
    const QQuickItem::ItemChangeData *data) {
  static_cast<OwnQQuickOverlay *>(self)->OwnQQuickOverlay::itemChange(
      change,
      *data);
}

//  void QQuickOverlay::geometryChange(const QRectF &newGeometry, const
//      QRectF &oldGeometry)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN13QQuickOverlay14geometryChangeERK6QRectFS2_(
    QQuickOverlay *self,
    const QRectF *newGeometry,
    const QRectF *oldGeometry) {
  static_cast<OwnQQuickOverlay *>(self)->OwnQQuickOverlay::geometryChange(
      *newGeometry,
      *oldGeometry);
}

//  void QQuickOverlay::mousePressEvent(QMouseEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN13QQuickOverlay15mousePressEventEP11QMouseEvent(
    QQuickOverlay *self,
    QMouseEvent *event) {
  static_cast<OwnQQuickOverlay *>(self)->OwnQQuickOverlay::mousePressEvent(
      event);
}

//  void QQuickOverlay::mouseMoveEvent(QMouseEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN13QQuickOverlay14mouseMoveEventEP11QMouseEvent(
    QQuickOverlay *self,
    QMouseEvent *event) {
  static_cast<OwnQQuickOverlay *>(self)->OwnQQuickOverlay::mouseMoveEvent(
      event);
}

//  void QQuickOverlay::mouseReleaseEvent(QMouseEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN13QQuickOverlay17mouseReleaseEventEP11QMouseEvent(
    QQuickOverlay *self,
    QMouseEvent *event) {
  static_cast<OwnQQuickOverlay *>(self)->OwnQQuickOverlay::mouseReleaseEvent(
      event);
}

#if QT_CONFIG(quicktemplates2_multitouch)
//  void QQuickOverlay::touchEvent(QTouchEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN13QQuickOverlay10touchEventEP11QTouchEvent(
    QQuickOverlay *self,
    QTouchEvent *event) {
  static_cast<OwnQQuickOverlay *>(self)->OwnQQuickOverlay::touchEvent(event);
}
#endif  // QT_CONFIG(quicktemplates2_multitouch)

#if QT_CONFIG(wheelevent)
//  void QQuickOverlay::wheelEvent(QWheelEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN13QQuickOverlay10wheelEventEP11QWheelEvent(
    QQuickOverlay *self,
    QWheelEvent *event) {
  static_cast<OwnQQuickOverlay *>(self)->OwnQQuickOverlay::wheelEvent(event);
}
#endif  // QT_CONFIG(wheelevent)

#if QT_CONFIG(quick_draganddrop)
//  void QQuickOverlay::dragEnterEvent(QDragEnterEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN13QQuickOverlay14dragEnterEventEP15QDragEnterEvent(
    QQuickOverlay *self,
    QDragEnterEvent *event) {
  static_cast<OwnQQuickOverlay *>(self)->OwnQQuickOverlay::dragEnterEvent(
      event);
}
#endif  // QT_CONFIG(quick_draganddrop)

#if QT_CONFIG(quick_draganddrop)
//  void QQuickOverlay::dragMoveEvent(QDragMoveEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN13QQuickOverlay13dragMoveEventEP14QDragMoveEvent(
    QQuickOverlay *self,
    QDragMoveEvent *event) {
  static_cast<OwnQQuickOverlay *>(self)->OwnQQuickOverlay::dragMoveEvent(
      event);
}
#endif  // QT_CONFIG(quick_draganddrop)

#if QT_CONFIG(quick_draganddrop)
//  void QQuickOverlay::dragLeaveEvent(QDragLeaveEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN13QQuickOverlay14dragLeaveEventEP15QDragLeaveEvent(
    QQuickOverlay *self,
    QDragLeaveEvent *event) {
  static_cast<OwnQQuickOverlay *>(self)->OwnQQuickOverlay::dragLeaveEvent(
      event);
}
#endif  // QT_CONFIG(quick_draganddrop)

#if QT_CONFIG(quick_draganddrop)
//  void QQuickOverlay::dropEvent(QDropEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN13QQuickOverlay9dropEventEP10QDropEvent(
    QQuickOverlay *self,
    QDropEvent *event) {
  static_cast<OwnQQuickOverlay *>(self)->OwnQQuickOverlay::dropEvent(event);
}
#endif  // QT_CONFIG(quick_draganddrop)

//  bool QQuickOverlay::childMouseEventFilter(QQuickItem *item, QEvent
//      *event)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN13QQuickOverlay21childMouseEventFilterEP10QQuickItemP6QEvent(
    QQuickOverlay *self,
    QQuickItem *item,
    QEvent *event) {
  return static_cast<OwnQQuickOverlay *>(self)->OwnQQuickOverlay::childMouseEventFilter(
      item,
      event);
}

//  bool QQuickOverlay::eventFilter(QObject *object, QEvent *event)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN13QQuickOverlay11eventFilterEP7QObjectP6QEvent(
    QQuickOverlay *self,
    QObject *object,
    QEvent *event) {
  return static_cast<OwnQQuickOverlay *>(self)->OwnQQuickOverlay::eventFilter(
      object,
      event);
}
