//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/6.12.0/QtQuick/private/qquickpincharea_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qquickpincharea_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qrect.h>
#include <QtQuick/qquickitem.h>
#include <QtCore/qpoint.h>
#include <QtCore/qvariant.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  Only a class built on QQuickPinchArea may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQQuickPinchArea : QQuickPinchArea {
  using QQuickPinchArea::childMouseEventFilter;
  using QQuickPinchArea::touchEvent;
  using QQuickPinchArea::geometryChange;
  using QQuickPinchArea::itemChange;
  using QQuickPinchArea::event;
};

//  A QQuickPinchArea that Python can take functions over in. Every QQuickPinchArea
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef bool (*CuteQQuickPinchAreaCall0)(const void *, QQuickItem *, QEvent *, int *);
typedef void (*CuteQQuickPinchAreaCall1)(const void *, QTouchEvent *, int *);
typedef void (*CuteQQuickPinchAreaCall2)(const void *, const QRectF *, const QRectF *, int *);
typedef void (*CuteQQuickPinchAreaCall3)(const void *, int, const QQuickItem::ItemChangeData *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickPinchAreaCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
typedef const QRectF * (*CuteQQuickPinchAreaCall5)(const void *, int *);
typedef const QRectF * (*CuteQQuickPinchAreaCall6)(const void *, int *);
typedef bool (*CuteQQuickPinchAreaCall7)(const void *, const QPointF *, int *);
#if QT_CONFIG(im)
typedef const QVariant * (*CuteQQuickPinchAreaCall8)(const void *, int, int *);
#endif  // QT_CONFIG(im)
typedef bool (*CuteQQuickPinchAreaCall9)(const void *, int *);
typedef void * (*CuteQQuickPinchAreaCall10)(const void *, int *);
typedef void (*CuteQQuickPinchAreaCall11)(const void *, int *);
typedef void (*CuteQQuickPinchAreaCall12)(const void *, int *);
typedef void (*CuteQQuickPinchAreaCall13)(const void *, QKeyEvent *, int *);
typedef void (*CuteQQuickPinchAreaCall14)(const void *, QKeyEvent *, int *);
#if QT_CONFIG(im)
typedef void (*CuteQQuickPinchAreaCall15)(const void *, QInputMethodEvent *, int *);
#endif  // QT_CONFIG(im)
typedef void (*CuteQQuickPinchAreaCall16)(const void *, QFocusEvent *, int *);
typedef void (*CuteQQuickPinchAreaCall17)(const void *, QFocusEvent *, int *);
typedef void (*CuteQQuickPinchAreaCall18)(const void *, QMouseEvent *, int *);
typedef void (*CuteQQuickPinchAreaCall19)(const void *, QMouseEvent *, int *);
typedef void (*CuteQQuickPinchAreaCall20)(const void *, QMouseEvent *, int *);
typedef void (*CuteQQuickPinchAreaCall21)(const void *, QMouseEvent *, int *);
typedef void (*CuteQQuickPinchAreaCall22)(const void *, int *);
typedef void (*CuteQQuickPinchAreaCall23)(const void *, int *);
#if QT_CONFIG(wheelevent)
typedef void (*CuteQQuickPinchAreaCall24)(const void *, QWheelEvent *, int *);
#endif  // QT_CONFIG(wheelevent)
typedef void (*CuteQQuickPinchAreaCall25)(const void *, QHoverEvent *, int *);
typedef void (*CuteQQuickPinchAreaCall26)(const void *, QHoverEvent *, int *);
typedef void (*CuteQQuickPinchAreaCall27)(const void *, QHoverEvent *, int *);
#if QT_CONFIG(quick_draganddrop)
typedef void (*CuteQQuickPinchAreaCall28)(const void *, QDragEnterEvent *, int *);
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
typedef void (*CuteQQuickPinchAreaCall29)(const void *, QDragMoveEvent *, int *);
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
typedef void (*CuteQQuickPinchAreaCall30)(const void *, QDragLeaveEvent *, int *);
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
typedef void (*CuteQQuickPinchAreaCall31)(const void *, QDropEvent *, int *);
#endif  // QT_CONFIG(quick_draganddrop)
typedef void * (*CuteQQuickPinchAreaCall32)(const void *, QSGNode *, QQuickItem::UpdatePaintNodeData *, int *);
typedef void (*CuteQQuickPinchAreaCall33)(const void *, int *);
typedef void (*CuteQQuickPinchAreaCall34)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickPinchAreaCall35)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickPinchAreaCall36)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickPinchAreaCall37)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickPinchAreaCall38)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickPinchAreaCall39)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickPinchAreaCall40)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQQuickPinchArea : public QQuickPinchArea {
public:
  using QQuickPinchArea::QQuickPinchArea;
  void *taken[41] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN10QQuickItem21childMouseEventFilterEPS_P6QEvent")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem10touchEventEP11QTouchEvent")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem14geometryChangeERK6QRectFS2_")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem10itemChangeENS_10ItemChangeERKNS_14ItemChangeDataE")) {
      taken[3] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[4] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZNK10QQuickItem12boundingRectEv")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK10QQuickItem8clipRectEv")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK10QQuickItem8containsERK7QPointF")) {
      taken[7] = call;
      return true;
    }
#if QT_CONFIG(im)
    if (!std::strcmp(key, "_ZNK10QQuickItem16inputMethodQueryEN2Qt16InputMethodQueryE")) {
      taken[8] = call;
      return true;
    }
#endif  // QT_CONFIG(im)
    if (!std::strcmp(key, "_ZNK10QQuickItem17isTextureProviderEv")) {
      taken[9] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK10QQuickItem15textureProviderEv")) {
      taken[10] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQmlParserStatus10classBeginEv")) {
      taken[11] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQmlParserStatus17componentCompleteEv")) {
      taken[12] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem13keyPressEventEP9QKeyEvent")) {
      taken[13] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem15keyReleaseEventEP9QKeyEvent")) {
      taken[14] = call;
      return true;
    }
#if QT_CONFIG(im)
    if (!std::strcmp(key, "_ZN10QQuickItem16inputMethodEventEP17QInputMethodEvent")) {
      taken[15] = call;
      return true;
    }
#endif  // QT_CONFIG(im)
    if (!std::strcmp(key, "_ZN10QQuickItem12focusInEventEP11QFocusEvent")) {
      taken[16] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem13focusOutEventEP11QFocusEvent")) {
      taken[17] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem15mousePressEventEP11QMouseEvent")) {
      taken[18] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem14mouseMoveEventEP11QMouseEvent")) {
      taken[19] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem17mouseReleaseEventEP11QMouseEvent")) {
      taken[20] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem21mouseDoubleClickEventEP11QMouseEvent")) {
      taken[21] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem16mouseUngrabEventEv")) {
      taken[22] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem16touchUngrabEventEv")) {
      taken[23] = call;
      return true;
    }
#if QT_CONFIG(wheelevent)
    if (!std::strcmp(key, "_ZN10QQuickItem10wheelEventEP11QWheelEvent")) {
      taken[24] = call;
      return true;
    }
#endif  // QT_CONFIG(wheelevent)
    if (!std::strcmp(key, "_ZN10QQuickItem15hoverEnterEventEP11QHoverEvent")) {
      taken[25] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem14hoverMoveEventEP11QHoverEvent")) {
      taken[26] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem15hoverLeaveEventEP11QHoverEvent")) {
      taken[27] = call;
      return true;
    }
#if QT_CONFIG(quick_draganddrop)
    if (!std::strcmp(key, "_ZN10QQuickItem14dragEnterEventEP15QDragEnterEvent")) {
      taken[28] = call;
      return true;
    }
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
    if (!std::strcmp(key, "_ZN10QQuickItem13dragMoveEventEP14QDragMoveEvent")) {
      taken[29] = call;
      return true;
    }
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
    if (!std::strcmp(key, "_ZN10QQuickItem14dragLeaveEventEP15QDragLeaveEvent")) {
      taken[30] = call;
      return true;
    }
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
    if (!std::strcmp(key, "_ZN10QQuickItem9dropEventEP10QDropEvent")) {
      taken[31] = call;
      return true;
    }
#endif  // QT_CONFIG(quick_draganddrop)
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

  //  bool QQuickPinchArea::childMouseEventFilter(QQuickItem *i, QEvent *e)
  bool childMouseEventFilter(QQuickItem *i, QEvent *e) override {
    if (taken[0]) {
      int handled = 0;
      CuteQQuickPinchAreaCall0 call = reinterpret_cast<CuteQQuickPinchAreaCall0>(taken[0]);
      bool given = call(this, i, e, &handled);
      if (handled) return given;
    }
    return QQuickPinchArea::childMouseEventFilter(i, e);
  }

  //  void QQuickPinchArea::touchEvent(QTouchEvent *event)
  void touchEvent(QTouchEvent *event) override {
    if (taken[1]) {
      int handled = 0;
      CuteQQuickPinchAreaCall1 call = reinterpret_cast<CuteQQuickPinchAreaCall1>(taken[1]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickPinchArea::touchEvent(event);
  }

  //  void QQuickPinchArea::geometryChange(const QRectF &newGeometry, const
  //      QRectF &oldGeometry)
  void geometryChange(
      const QRectF &newGeometry,
      const QRectF &oldGeometry) override {
    if (taken[2]) {
      int handled = 0;
      CuteQQuickPinchAreaCall2 call = reinterpret_cast<CuteQQuickPinchAreaCall2>(taken[2]);
      call(this, &newGeometry, &oldGeometry, &handled);
      if (handled) return;
    }
    QQuickPinchArea::geometryChange(newGeometry, oldGeometry);
  }

  //  void QQuickPinchArea::itemChange(ItemChange change, const
  //      ItemChangeData &value)
  void itemChange(
      QQuickItem::ItemChange change,
      const QQuickItem::ItemChangeData &value) override {
    if (taken[3]) {
      int handled = 0;
      CuteQQuickPinchAreaCall3 call = reinterpret_cast<CuteQQuickPinchAreaCall3>(taken[3]);
      call(this, static_cast<int>(change), &value, &handled);
      if (handled) return;
    }
    QQuickPinchArea::itemChange(change, value);
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QQuickPinchArea::event(QEvent *a0)
  bool event(QEvent *a0) override {
    if (taken[4]) {
      int handled = 0;
      CuteQQuickPinchAreaCall4 call = reinterpret_cast<CuteQQuickPinchAreaCall4>(taken[4]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQuickPinchArea::event(a0);
  }
#endif  // !defined(QT_NO_QOBJECT)

  //  QRectF QQuickItem::boundingRect() const
  QRectF boundingRect() const override {
    if (taken[5]) {
      int handled = 0;
      CuteQQuickPinchAreaCall5 call = reinterpret_cast<CuteQQuickPinchAreaCall5>(taken[5]);
      const QRectF * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QQuickItem::boundingRect();
  }

  //  QRectF QQuickItem::clipRect() const
  QRectF clipRect() const override {
    if (taken[6]) {
      int handled = 0;
      CuteQQuickPinchAreaCall6 call = reinterpret_cast<CuteQQuickPinchAreaCall6>(taken[6]);
      const QRectF * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QQuickItem::clipRect();
  }

  //  bool QQuickItem::contains(const QPointF &point) const
  bool contains(const QPointF &point) const override {
    if (taken[7]) {
      int handled = 0;
      CuteQQuickPinchAreaCall7 call = reinterpret_cast<CuteQQuickPinchAreaCall7>(taken[7]);
      bool given = call(this, &point, &handled);
      if (handled) return given;
    }
    return QQuickItem::contains(point);
  }

#if QT_CONFIG(im)
  //  QVariant QQuickItem::inputMethodQuery(Qt::InputMethodQuery query)
  //      const
  QVariant inputMethodQuery(Qt::InputMethodQuery query) const override {
    if (taken[8]) {
      int handled = 0;
      CuteQQuickPinchAreaCall8 call = reinterpret_cast<CuteQQuickPinchAreaCall8>(taken[8]);
      const QVariant * given = call(this, static_cast<int>(query), &handled);
      if (handled && given) return *given;
    }
    return QQuickItem::inputMethodQuery(query);
  }
#endif  // QT_CONFIG(im)

  //  bool QQuickItem::isTextureProvider() const
  bool isTextureProvider() const override {
    if (taken[9]) {
      int handled = 0;
      CuteQQuickPinchAreaCall9 call = reinterpret_cast<CuteQQuickPinchAreaCall9>(taken[9]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QQuickItem::isTextureProvider();
  }

  //  QSGTextureProvider *QQuickItem::textureProvider() const
  QSGTextureProvider *textureProvider() const override {
    if (taken[10]) {
      int handled = 0;
      CuteQQuickPinchAreaCall10 call = reinterpret_cast<CuteQQuickPinchAreaCall10>(taken[10]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QSGTextureProvider *>(given);
    }
    return QQuickItem::textureProvider();
  }

  //  void QQuickItem::classBegin()
  void classBegin() override {
    if (taken[11]) {
      int handled = 0;
      CuteQQuickPinchAreaCall11 call = reinterpret_cast<CuteQQuickPinchAreaCall11>(taken[11]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItem::classBegin();
  }

  //  void QQuickItem::componentComplete()
  void componentComplete() override {
    if (taken[12]) {
      int handled = 0;
      CuteQQuickPinchAreaCall12 call = reinterpret_cast<CuteQQuickPinchAreaCall12>(taken[12]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItem::componentComplete();
  }

  //  void QQuickItem::keyPressEvent(QKeyEvent *event)
  void keyPressEvent(QKeyEvent *event) override {
    if (taken[13]) {
      int handled = 0;
      CuteQQuickPinchAreaCall13 call = reinterpret_cast<CuteQQuickPinchAreaCall13>(taken[13]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::keyPressEvent(event);
  }

  //  void QQuickItem::keyReleaseEvent(QKeyEvent *event)
  void keyReleaseEvent(QKeyEvent *event) override {
    if (taken[14]) {
      int handled = 0;
      CuteQQuickPinchAreaCall14 call = reinterpret_cast<CuteQQuickPinchAreaCall14>(taken[14]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::keyReleaseEvent(event);
  }

#if QT_CONFIG(im)
  //  void QQuickItem::inputMethodEvent(QInputMethodEvent *a0)
  void inputMethodEvent(QInputMethodEvent *a0) override {
    if (taken[15]) {
      int handled = 0;
      CuteQQuickPinchAreaCall15 call = reinterpret_cast<CuteQQuickPinchAreaCall15>(taken[15]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItem::inputMethodEvent(a0);
  }
#endif  // QT_CONFIG(im)

  //  void QQuickItem::focusInEvent(QFocusEvent *a0)
  void focusInEvent(QFocusEvent *a0) override {
    if (taken[16]) {
      int handled = 0;
      CuteQQuickPinchAreaCall16 call = reinterpret_cast<CuteQQuickPinchAreaCall16>(taken[16]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItem::focusInEvent(a0);
  }

  //  void QQuickItem::focusOutEvent(QFocusEvent *a0)
  void focusOutEvent(QFocusEvent *a0) override {
    if (taken[17]) {
      int handled = 0;
      CuteQQuickPinchAreaCall17 call = reinterpret_cast<CuteQQuickPinchAreaCall17>(taken[17]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItem::focusOutEvent(a0);
  }

  //  void QQuickItem::mousePressEvent(QMouseEvent *event)
  void mousePressEvent(QMouseEvent *event) override {
    if (taken[18]) {
      int handled = 0;
      CuteQQuickPinchAreaCall18 call = reinterpret_cast<CuteQQuickPinchAreaCall18>(taken[18]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::mousePressEvent(event);
  }

  //  void QQuickItem::mouseMoveEvent(QMouseEvent *event)
  void mouseMoveEvent(QMouseEvent *event) override {
    if (taken[19]) {
      int handled = 0;
      CuteQQuickPinchAreaCall19 call = reinterpret_cast<CuteQQuickPinchAreaCall19>(taken[19]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::mouseMoveEvent(event);
  }

  //  void QQuickItem::mouseReleaseEvent(QMouseEvent *event)
  void mouseReleaseEvent(QMouseEvent *event) override {
    if (taken[20]) {
      int handled = 0;
      CuteQQuickPinchAreaCall20 call = reinterpret_cast<CuteQQuickPinchAreaCall20>(taken[20]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::mouseReleaseEvent(event);
  }

  //  void QQuickItem::mouseDoubleClickEvent(QMouseEvent *event)
  void mouseDoubleClickEvent(QMouseEvent *event) override {
    if (taken[21]) {
      int handled = 0;
      CuteQQuickPinchAreaCall21 call = reinterpret_cast<CuteQQuickPinchAreaCall21>(taken[21]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::mouseDoubleClickEvent(event);
  }

  //  void QQuickItem::mouseUngrabEvent()
  void mouseUngrabEvent() override {
    if (taken[22]) {
      int handled = 0;
      CuteQQuickPinchAreaCall22 call = reinterpret_cast<CuteQQuickPinchAreaCall22>(taken[22]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItem::mouseUngrabEvent();
  }

  //  void QQuickItem::touchUngrabEvent()
  void touchUngrabEvent() override {
    if (taken[23]) {
      int handled = 0;
      CuteQQuickPinchAreaCall23 call = reinterpret_cast<CuteQQuickPinchAreaCall23>(taken[23]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItem::touchUngrabEvent();
  }

#if QT_CONFIG(wheelevent)
  //  void QQuickItem::wheelEvent(QWheelEvent *event)
  void wheelEvent(QWheelEvent *event) override {
    if (taken[24]) {
      int handled = 0;
      CuteQQuickPinchAreaCall24 call = reinterpret_cast<CuteQQuickPinchAreaCall24>(taken[24]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::wheelEvent(event);
  }
#endif  // QT_CONFIG(wheelevent)

  //  void QQuickItem::hoverEnterEvent(QHoverEvent *event)
  void hoverEnterEvent(QHoverEvent *event) override {
    if (taken[25]) {
      int handled = 0;
      CuteQQuickPinchAreaCall25 call = reinterpret_cast<CuteQQuickPinchAreaCall25>(taken[25]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::hoverEnterEvent(event);
  }

  //  void QQuickItem::hoverMoveEvent(QHoverEvent *event)
  void hoverMoveEvent(QHoverEvent *event) override {
    if (taken[26]) {
      int handled = 0;
      CuteQQuickPinchAreaCall26 call = reinterpret_cast<CuteQQuickPinchAreaCall26>(taken[26]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::hoverMoveEvent(event);
  }

  //  void QQuickItem::hoverLeaveEvent(QHoverEvent *event)
  void hoverLeaveEvent(QHoverEvent *event) override {
    if (taken[27]) {
      int handled = 0;
      CuteQQuickPinchAreaCall27 call = reinterpret_cast<CuteQQuickPinchAreaCall27>(taken[27]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::hoverLeaveEvent(event);
  }

#if QT_CONFIG(quick_draganddrop)
  //  void QQuickItem::dragEnterEvent(QDragEnterEvent *a0)
  void dragEnterEvent(QDragEnterEvent *a0) override {
    if (taken[28]) {
      int handled = 0;
      CuteQQuickPinchAreaCall28 call = reinterpret_cast<CuteQQuickPinchAreaCall28>(taken[28]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItem::dragEnterEvent(a0);
  }
#endif  // QT_CONFIG(quick_draganddrop)

#if QT_CONFIG(quick_draganddrop)
  //  void QQuickItem::dragMoveEvent(QDragMoveEvent *a0)
  void dragMoveEvent(QDragMoveEvent *a0) override {
    if (taken[29]) {
      int handled = 0;
      CuteQQuickPinchAreaCall29 call = reinterpret_cast<CuteQQuickPinchAreaCall29>(taken[29]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItem::dragMoveEvent(a0);
  }
#endif  // QT_CONFIG(quick_draganddrop)

#if QT_CONFIG(quick_draganddrop)
  //  void QQuickItem::dragLeaveEvent(QDragLeaveEvent *a0)
  void dragLeaveEvent(QDragLeaveEvent *a0) override {
    if (taken[30]) {
      int handled = 0;
      CuteQQuickPinchAreaCall30 call = reinterpret_cast<CuteQQuickPinchAreaCall30>(taken[30]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItem::dragLeaveEvent(a0);
  }
#endif  // QT_CONFIG(quick_draganddrop)

#if QT_CONFIG(quick_draganddrop)
  //  void QQuickItem::dropEvent(QDropEvent *a0)
  void dropEvent(QDropEvent *a0) override {
    if (taken[31]) {
      int handled = 0;
      CuteQQuickPinchAreaCall31 call = reinterpret_cast<CuteQQuickPinchAreaCall31>(taken[31]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItem::dropEvent(a0);
  }
#endif  // QT_CONFIG(quick_draganddrop)

  //  QSGNode *QQuickItem::updatePaintNode(QSGNode *a0, UpdatePaintNodeData
  //      *a1)
  QSGNode *updatePaintNode(
      QSGNode *a0,
      QQuickItem::UpdatePaintNodeData *a1) override {
    if (taken[32]) {
      int handled = 0;
      CuteQQuickPinchAreaCall32 call = reinterpret_cast<CuteQQuickPinchAreaCall32>(taken[32]);
      void * given = call(this, a0, a1, &handled);
      if (handled) return static_cast<QSGNode *>(given);
    }
    return QQuickItem::updatePaintNode(a0, a1);
  }

  //  void QQuickItem::releaseResources()
  void releaseResources() override {
    if (taken[33]) {
      int handled = 0;
      CuteQQuickPinchAreaCall33 call = reinterpret_cast<CuteQQuickPinchAreaCall33>(taken[33]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItem::releaseResources();
  }

  //  void QQuickItem::updatePolish()
  void updatePolish() override {
    if (taken[34]) {
      int handled = 0;
      CuteQQuickPinchAreaCall34 call = reinterpret_cast<CuteQQuickPinchAreaCall34>(taken[34]);
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
      CuteQQuickPinchAreaCall35 call = reinterpret_cast<CuteQQuickPinchAreaCall35>(taken[35]);
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
      CuteQQuickPinchAreaCall36 call = reinterpret_cast<CuteQQuickPinchAreaCall36>(taken[36]);
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
      CuteQQuickPinchAreaCall37 call = reinterpret_cast<CuteQQuickPinchAreaCall37>(taken[37]);
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
      CuteQQuickPinchAreaCall38 call = reinterpret_cast<CuteQQuickPinchAreaCall38>(taken[38]);
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
      CuteQQuickPinchAreaCall39 call = reinterpret_cast<CuteQQuickPinchAreaCall39>(taken[39]);
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
      CuteQQuickPinchAreaCall40 call = reinterpret_cast<CuteQQuickPinchAreaCall40>(taken[40]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QQuickPinchArea::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK15QQuickPinchArea10metaObjectEv(
    const QQuickPinchArea *self) {
  return self->metaObject();
}

//  QString QQuickPinchArea::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN15QQuickPinchArea2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuickPinchArea::tr(s, c, n));
}

//  QQuickPinchArea::QQuickPinchArea(QQuickItem *parent)
extern "C" Q_DECL_EXPORT
QQuickPinchArea *ritual_ZN15QQuickPinchAreaC1EP10QQuickItem(
    QQuickItem *parent) {
  return new CuteQQuickPinchArea(parent);
}

//  QQuickPinchArea::~QQuickPinchArea()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickPinchAreaD1Ev(QQuickPinchArea *self) {
  delete self;
}

//  bool QQuickPinchArea::isEnabled() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK15QQuickPinchArea9isEnabledEv(const QQuickPinchArea *self) {
  return self->isEnabled();
}

//  void QQuickPinchArea::setEnabled(bool a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickPinchArea10setEnabledEb(
    QQuickPinchArea *self,
    bool a0) {
  self->setEnabled(a0);
}

//  QQuickPinch *QQuickPinchArea::pinch()
extern "C" Q_DECL_EXPORT
QQuickPinch *ritual_ZN15QQuickPinchArea5pinchEv(QQuickPinchArea *self) {
  return self->pinch();
}

//  bool QQuickPinchArea::childMouseEventFilter(QQuickItem *i, QEvent *e)
extern "C" Q_DECL_EXPORT
bool ritual_ZN15QQuickPinchArea21childMouseEventFilterEP10QQuickItemP6QEvent(
    QQuickPinchArea *self,
    QQuickItem *i,
    QEvent *e) {
  return self->childMouseEventFilter(i, e);
}

//  void QQuickPinchArea::touchEvent(QTouchEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickPinchArea10touchEventEP11QTouchEvent(
    QQuickPinchArea *self,
    QTouchEvent *event) {
  self->touchEvent(event);
}

//  void QQuickPinchArea::geometryChange(const QRectF &newGeometry, const
//      QRectF &oldGeometry)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickPinchArea14geometryChangeERK6QRectFS2_(
    QQuickPinchArea *self,
    const QRectF *newGeometry,
    const QRectF *oldGeometry) {
  self->geometryChange(*newGeometry, *oldGeometry);
}

//  void QQuickPinchArea::itemChange(ItemChange change, const ItemChangeData
//      &value)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickPinchArea10itemChangeEN10QQuickItem10ItemChangeERKNS0_14ItemChangeDataE(
    QQuickPinchArea *self,
    QQuickItem::ItemChange change,
    const QQuickItem::ItemChangeData *value) {
  self->itemChange(change, *value);
}

//  bool QQuickPinchArea::event(QEvent *a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN15QQuickPinchArea5eventEP6QEvent(
    QQuickPinchArea *self,
    QEvent *a0) {
  return self->event(a0);
}

//  void QQuickPinchArea::clearPinch(QTouchEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickPinchArea10clearPinchEP11QTouchEvent(
    QQuickPinchArea *self,
    QTouchEvent *event) {
  self->clearPinch(event);
}

//  void QQuickPinchArea::cancelPinch(QTouchEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickPinchArea11cancelPinchEP11QTouchEvent(
    QQuickPinchArea *self,
    QTouchEvent *event) {
  self->cancelPinch(event);
}

//  void QQuickPinchArea::updatePinch(QTouchEvent *event, bool filtering)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickPinchArea11updatePinchEP11QTouchEventb(
    QQuickPinchArea *self,
    QTouchEvent *event,
    bool filtering) {
  self->updatePinch(event, filtering);
}

//  void QQuickPinchArea::updatePinchTarget()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickPinchArea17updatePinchTargetEv(QQuickPinchArea *self) {
  self->updatePinchTarget();
}

//  QQuickPinchAreaPrivate *QQuickPinchArea::d_func()
extern "C" Q_DECL_EXPORT
QQuickPinchAreaPrivate *ritual_ZN15QQuickPinchArea6d_funcEv(
    QQuickPinchArea *self) {
  return self->d_func();
}

//  const QQuickPinchAreaPrivate *QQuickPinchArea::d_func() const
extern "C" Q_DECL_EXPORT
const QQuickPinchAreaPrivate *ritual_ZNK15QQuickPinchArea6d_funcEv(
    const QQuickPinchArea *self) {
  return self->d_func();
}

//  a Python function taken by a CuteQQuickPinchArea, for the function named
//      by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQuickPinchArea(
    QQuickPinchArea *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQuickPinchArea *>(self)->take(key, call);
}

//  bool QQuickPinchArea::childMouseEventFilter(QQuickItem *i, QEvent *e)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN15QQuickPinchArea21childMouseEventFilterEP10QQuickItemP6QEvent(
    QQuickPinchArea *self,
    QQuickItem *i,
    QEvent *e) {
  return static_cast<OwnQQuickPinchArea *>(self)->OwnQQuickPinchArea::childMouseEventFilter(
      i,
      e);
}

//  void QQuickPinchArea::touchEvent(QTouchEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN15QQuickPinchArea10touchEventEP11QTouchEvent(
    QQuickPinchArea *self,
    QTouchEvent *event) {
  static_cast<OwnQQuickPinchArea *>(self)->OwnQQuickPinchArea::touchEvent(
      event);
}

//  void QQuickPinchArea::geometryChange(const QRectF &newGeometry, const
//      QRectF &oldGeometry)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN15QQuickPinchArea14geometryChangeERK6QRectFS2_(
    QQuickPinchArea *self,
    const QRectF *newGeometry,
    const QRectF *oldGeometry) {
  static_cast<OwnQQuickPinchArea *>(self)->OwnQQuickPinchArea::geometryChange(
      *newGeometry,
      *oldGeometry);
}

//  void QQuickPinchArea::itemChange(ItemChange change, const ItemChangeData
//      &value)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN15QQuickPinchArea10itemChangeEN10QQuickItem10ItemChangeERKNS0_14ItemChangeDataE(
    QQuickPinchArea *self,
    QQuickItem::ItemChange change,
    const QQuickItem::ItemChangeData *value) {
  static_cast<OwnQQuickPinchArea *>(self)->OwnQQuickPinchArea::itemChange(
      change,
      *value);
}

//  bool QQuickPinchArea::event(QEvent *a0)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN15QQuickPinchArea5eventEP6QEvent(
    QQuickPinchArea *self,
    QEvent *a0) {
  return static_cast<OwnQQuickPinchArea *>(self)->OwnQQuickPinchArea::event(
      a0);
}
