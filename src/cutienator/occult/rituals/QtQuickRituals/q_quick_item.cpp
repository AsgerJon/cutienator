//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/qquickitem.h, Qt 6.12.0. Changes made here are lost.
#include <QtQuick/QtQuick>
#include <QtQuick/qquickitem.h>
#include <QtCore/qstring.h>
#include <QtCore/qrect.h>
#include <QtCore/qpoint.h>
#include <QtCore/qsize.h>
#include <QtGui/qcursor.h>
#include <QtQml/QtQml>
#include <QtQml/qjsvalue.h>
#include <QtGui/qtransform.h>
#include <QtCore/qvariant.h>
#include <QtCore/qdebug.h>
#include <QtCore/qmetaobject.h>
#include <QtCore/qlist.h>
#include <cstring>

//  Only a class built on QQuickItem may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQQuickItem : QQuickItem {
  using QQuickItem::event;
  using QQuickItem::itemChange;
  using QQuickItem::geometryChange;
  using QQuickItem::classBegin;
  using QQuickItem::componentComplete;
  using QQuickItem::keyPressEvent;
  using QQuickItem::keyReleaseEvent;
  using QQuickItem::inputMethodEvent;
  using QQuickItem::focusInEvent;
  using QQuickItem::focusOutEvent;
  using QQuickItem::mousePressEvent;
  using QQuickItem::mouseMoveEvent;
  using QQuickItem::mouseReleaseEvent;
  using QQuickItem::mouseDoubleClickEvent;
  using QQuickItem::mouseUngrabEvent;
  using QQuickItem::touchUngrabEvent;
  using QQuickItem::wheelEvent;
  using QQuickItem::touchEvent;
  using QQuickItem::hoverEnterEvent;
  using QQuickItem::hoverMoveEvent;
  using QQuickItem::hoverLeaveEvent;
  using QQuickItem::dragEnterEvent;
  using QQuickItem::dragMoveEvent;
  using QQuickItem::dragLeaveEvent;
  using QQuickItem::dropEvent;
  using QQuickItem::childMouseEventFilter;
  using QQuickItem::updatePaintNode;
  using QQuickItem::releaseResources;
  using QQuickItem::updatePolish;
};

//  A QQuickItem that Python can take functions over in. Every QQuickItem
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef const QRectF * (*CuteQQuickItemCall0)(const void *, int *);
typedef const QRectF * (*CuteQQuickItemCall1)(const void *, int *);
typedef bool (*CuteQQuickItemCall2)(const void *, const QPointF *, int *);
#if QT_CONFIG(im)
typedef const QVariant * (*CuteQQuickItemCall3)(const void *, int, int *);
#endif  // QT_CONFIG(im)
typedef bool (*CuteQQuickItemCall4)(const void *, int *);
typedef void * (*CuteQQuickItemCall5)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickItemCall6)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickItemCall7)(const void *, int, const QQuickItem::ItemChangeData *, int *);
typedef void (*CuteQQuickItemCall8)(const void *, const QRectF *, const QRectF *, int *);
typedef void (*CuteQQuickItemCall9)(const void *, int *);
typedef void (*CuteQQuickItemCall10)(const void *, int *);
typedef void (*CuteQQuickItemCall11)(const void *, QKeyEvent *, int *);
typedef void (*CuteQQuickItemCall12)(const void *, QKeyEvent *, int *);
#if QT_CONFIG(im)
typedef void (*CuteQQuickItemCall13)(const void *, QInputMethodEvent *, int *);
#endif  // QT_CONFIG(im)
typedef void (*CuteQQuickItemCall14)(const void *, QFocusEvent *, int *);
typedef void (*CuteQQuickItemCall15)(const void *, QFocusEvent *, int *);
typedef void (*CuteQQuickItemCall16)(const void *, QMouseEvent *, int *);
typedef void (*CuteQQuickItemCall17)(const void *, QMouseEvent *, int *);
typedef void (*CuteQQuickItemCall18)(const void *, QMouseEvent *, int *);
typedef void (*CuteQQuickItemCall19)(const void *, QMouseEvent *, int *);
typedef void (*CuteQQuickItemCall20)(const void *, int *);
typedef void (*CuteQQuickItemCall21)(const void *, int *);
#if QT_CONFIG(wheelevent)
typedef void (*CuteQQuickItemCall22)(const void *, QWheelEvent *, int *);
#endif  // QT_CONFIG(wheelevent)
typedef void (*CuteQQuickItemCall23)(const void *, QTouchEvent *, int *);
typedef void (*CuteQQuickItemCall24)(const void *, QHoverEvent *, int *);
typedef void (*CuteQQuickItemCall25)(const void *, QHoverEvent *, int *);
typedef void (*CuteQQuickItemCall26)(const void *, QHoverEvent *, int *);
#if QT_CONFIG(quick_draganddrop)
typedef void (*CuteQQuickItemCall27)(const void *, QDragEnterEvent *, int *);
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
typedef void (*CuteQQuickItemCall28)(const void *, QDragMoveEvent *, int *);
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
typedef void (*CuteQQuickItemCall29)(const void *, QDragLeaveEvent *, int *);
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
typedef void (*CuteQQuickItemCall30)(const void *, QDropEvent *, int *);
#endif  // QT_CONFIG(quick_draganddrop)
typedef bool (*CuteQQuickItemCall31)(const void *, QQuickItem *, QEvent *, int *);
typedef void * (*CuteQQuickItemCall32)(const void *, QSGNode *, QQuickItem::UpdatePaintNodeData *, int *);
typedef void (*CuteQQuickItemCall33)(const void *, int *);
typedef void (*CuteQQuickItemCall34)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickItemCall35)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickItemCall36)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickItemCall37)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickItemCall38)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickItemCall39)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickItemCall40)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQQuickItem : public QQuickItem {
public:
  using QQuickItem::QQuickItem;
  void *taken[41] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZNK10QQuickItem12boundingRectEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK10QQuickItem8clipRectEv")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK10QQuickItem8containsERK7QPointF")) {
      taken[2] = call;
      return true;
    }
#if QT_CONFIG(im)
    if (!std::strcmp(key, "_ZNK10QQuickItem16inputMethodQueryEN2Qt16InputMethodQueryE")) {
      taken[3] = call;
      return true;
    }
#endif  // QT_CONFIG(im)
    if (!std::strcmp(key, "_ZNK10QQuickItem17isTextureProviderEv")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK10QQuickItem15textureProviderEv")) {
      taken[5] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[6] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN10QQuickItem10itemChangeENS_10ItemChangeERKNS_14ItemChangeDataE")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem14geometryChangeERK6QRectFS2_")) {
      taken[8] = call;
      return true;
    }
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

  //  QRectF QQuickItem::boundingRect() const
  QRectF boundingRect() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQQuickItemCall0 call = reinterpret_cast<CuteQQuickItemCall0>(taken[0]);
      const QRectF * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QQuickItem::boundingRect();
  }

  //  QRectF QQuickItem::clipRect() const
  QRectF clipRect() const override {
    if (taken[1]) {
      int handled = 0;
      CuteQQuickItemCall1 call = reinterpret_cast<CuteQQuickItemCall1>(taken[1]);
      const QRectF * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QQuickItem::clipRect();
  }

  //  bool QQuickItem::contains(const QPointF &point) const
  bool contains(const QPointF &point) const override {
    if (taken[2]) {
      int handled = 0;
      CuteQQuickItemCall2 call = reinterpret_cast<CuteQQuickItemCall2>(taken[2]);
      bool given = call(this, &point, &handled);
      if (handled) return given;
    }
    return QQuickItem::contains(point);
  }

#if QT_CONFIG(im)
  //  QVariant QQuickItem::inputMethodQuery(Qt::InputMethodQuery query)
  //      const
  QVariant inputMethodQuery(Qt::InputMethodQuery query) const override {
    if (taken[3]) {
      int handled = 0;
      CuteQQuickItemCall3 call = reinterpret_cast<CuteQQuickItemCall3>(taken[3]);
      const QVariant * given = call(this, static_cast<int>(query), &handled);
      if (handled && given) return *given;
    }
    return QQuickItem::inputMethodQuery(query);
  }
#endif  // QT_CONFIG(im)

  //  bool QQuickItem::isTextureProvider() const
  bool isTextureProvider() const override {
    if (taken[4]) {
      int handled = 0;
      CuteQQuickItemCall4 call = reinterpret_cast<CuteQQuickItemCall4>(taken[4]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QQuickItem::isTextureProvider();
  }

  //  QSGTextureProvider *QQuickItem::textureProvider() const
  QSGTextureProvider *textureProvider() const override {
    if (taken[5]) {
      int handled = 0;
      CuteQQuickItemCall5 call = reinterpret_cast<CuteQQuickItemCall5>(taken[5]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QSGTextureProvider *>(given);
    }
    return QQuickItem::textureProvider();
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QQuickItem::event(QEvent *a0)
  bool event(QEvent *a0) override {
    if (taken[6]) {
      int handled = 0;
      CuteQQuickItemCall6 call = reinterpret_cast<CuteQQuickItemCall6>(taken[6]);
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
    if (taken[7]) {
      int handled = 0;
      CuteQQuickItemCall7 call = reinterpret_cast<CuteQQuickItemCall7>(taken[7]);
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
    if (taken[8]) {
      int handled = 0;
      CuteQQuickItemCall8 call = reinterpret_cast<CuteQQuickItemCall8>(taken[8]);
      call(this, &newGeometry, &oldGeometry, &handled);
      if (handled) return;
    }
    QQuickItem::geometryChange(newGeometry, oldGeometry);
  }

  //  void QQuickItem::classBegin()
  void classBegin() override {
    if (taken[9]) {
      int handled = 0;
      CuteQQuickItemCall9 call = reinterpret_cast<CuteQQuickItemCall9>(taken[9]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItem::classBegin();
  }

  //  void QQuickItem::componentComplete()
  void componentComplete() override {
    if (taken[10]) {
      int handled = 0;
      CuteQQuickItemCall10 call = reinterpret_cast<CuteQQuickItemCall10>(taken[10]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItem::componentComplete();
  }

  //  void QQuickItem::keyPressEvent(QKeyEvent *event)
  void keyPressEvent(QKeyEvent *event) override {
    if (taken[11]) {
      int handled = 0;
      CuteQQuickItemCall11 call = reinterpret_cast<CuteQQuickItemCall11>(taken[11]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::keyPressEvent(event);
  }

  //  void QQuickItem::keyReleaseEvent(QKeyEvent *event)
  void keyReleaseEvent(QKeyEvent *event) override {
    if (taken[12]) {
      int handled = 0;
      CuteQQuickItemCall12 call = reinterpret_cast<CuteQQuickItemCall12>(taken[12]);
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
      CuteQQuickItemCall13 call = reinterpret_cast<CuteQQuickItemCall13>(taken[13]);
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
      CuteQQuickItemCall14 call = reinterpret_cast<CuteQQuickItemCall14>(taken[14]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItem::focusInEvent(a0);
  }

  //  void QQuickItem::focusOutEvent(QFocusEvent *a0)
  void focusOutEvent(QFocusEvent *a0) override {
    if (taken[15]) {
      int handled = 0;
      CuteQQuickItemCall15 call = reinterpret_cast<CuteQQuickItemCall15>(taken[15]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItem::focusOutEvent(a0);
  }

  //  void QQuickItem::mousePressEvent(QMouseEvent *event)
  void mousePressEvent(QMouseEvent *event) override {
    if (taken[16]) {
      int handled = 0;
      CuteQQuickItemCall16 call = reinterpret_cast<CuteQQuickItemCall16>(taken[16]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::mousePressEvent(event);
  }

  //  void QQuickItem::mouseMoveEvent(QMouseEvent *event)
  void mouseMoveEvent(QMouseEvent *event) override {
    if (taken[17]) {
      int handled = 0;
      CuteQQuickItemCall17 call = reinterpret_cast<CuteQQuickItemCall17>(taken[17]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::mouseMoveEvent(event);
  }

  //  void QQuickItem::mouseReleaseEvent(QMouseEvent *event)
  void mouseReleaseEvent(QMouseEvent *event) override {
    if (taken[18]) {
      int handled = 0;
      CuteQQuickItemCall18 call = reinterpret_cast<CuteQQuickItemCall18>(taken[18]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::mouseReleaseEvent(event);
  }

  //  void QQuickItem::mouseDoubleClickEvent(QMouseEvent *event)
  void mouseDoubleClickEvent(QMouseEvent *event) override {
    if (taken[19]) {
      int handled = 0;
      CuteQQuickItemCall19 call = reinterpret_cast<CuteQQuickItemCall19>(taken[19]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::mouseDoubleClickEvent(event);
  }

  //  void QQuickItem::mouseUngrabEvent()
  void mouseUngrabEvent() override {
    if (taken[20]) {
      int handled = 0;
      CuteQQuickItemCall20 call = reinterpret_cast<CuteQQuickItemCall20>(taken[20]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItem::mouseUngrabEvent();
  }

  //  void QQuickItem::touchUngrabEvent()
  void touchUngrabEvent() override {
    if (taken[21]) {
      int handled = 0;
      CuteQQuickItemCall21 call = reinterpret_cast<CuteQQuickItemCall21>(taken[21]);
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
      CuteQQuickItemCall22 call = reinterpret_cast<CuteQQuickItemCall22>(taken[22]);
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
      CuteQQuickItemCall23 call = reinterpret_cast<CuteQQuickItemCall23>(taken[23]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::touchEvent(event);
  }

  //  void QQuickItem::hoverEnterEvent(QHoverEvent *event)
  void hoverEnterEvent(QHoverEvent *event) override {
    if (taken[24]) {
      int handled = 0;
      CuteQQuickItemCall24 call = reinterpret_cast<CuteQQuickItemCall24>(taken[24]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::hoverEnterEvent(event);
  }

  //  void QQuickItem::hoverMoveEvent(QHoverEvent *event)
  void hoverMoveEvent(QHoverEvent *event) override {
    if (taken[25]) {
      int handled = 0;
      CuteQQuickItemCall25 call = reinterpret_cast<CuteQQuickItemCall25>(taken[25]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::hoverMoveEvent(event);
  }

  //  void QQuickItem::hoverLeaveEvent(QHoverEvent *event)
  void hoverLeaveEvent(QHoverEvent *event) override {
    if (taken[26]) {
      int handled = 0;
      CuteQQuickItemCall26 call = reinterpret_cast<CuteQQuickItemCall26>(taken[26]);
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
      CuteQQuickItemCall27 call = reinterpret_cast<CuteQQuickItemCall27>(taken[27]);
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
      CuteQQuickItemCall28 call = reinterpret_cast<CuteQQuickItemCall28>(taken[28]);
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
      CuteQQuickItemCall29 call = reinterpret_cast<CuteQQuickItemCall29>(taken[29]);
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
      CuteQQuickItemCall30 call = reinterpret_cast<CuteQQuickItemCall30>(taken[30]);
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
      CuteQQuickItemCall31 call = reinterpret_cast<CuteQQuickItemCall31>(taken[31]);
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
      CuteQQuickItemCall32 call = reinterpret_cast<CuteQQuickItemCall32>(taken[32]);
      void * given = call(this, a0, a1, &handled);
      if (handled) return static_cast<QSGNode *>(given);
    }
    return QQuickItem::updatePaintNode(a0, a1);
  }

  //  void QQuickItem::releaseResources()
  void releaseResources() override {
    if (taken[33]) {
      int handled = 0;
      CuteQQuickItemCall33 call = reinterpret_cast<CuteQQuickItemCall33>(taken[33]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItem::releaseResources();
  }

  //  void QQuickItem::updatePolish()
  void updatePolish() override {
    if (taken[34]) {
      int handled = 0;
      CuteQQuickItemCall34 call = reinterpret_cast<CuteQQuickItemCall34>(taken[34]);
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
      CuteQQuickItemCall35 call = reinterpret_cast<CuteQQuickItemCall35>(taken[35]);
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
      CuteQQuickItemCall36 call = reinterpret_cast<CuteQQuickItemCall36>(taken[36]);
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
      CuteQQuickItemCall37 call = reinterpret_cast<CuteQQuickItemCall37>(taken[37]);
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
      CuteQQuickItemCall38 call = reinterpret_cast<CuteQQuickItemCall38>(taken[38]);
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
      CuteQQuickItemCall39 call = reinterpret_cast<CuteQQuickItemCall39>(taken[39]);
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
      CuteQQuickItemCall40 call = reinterpret_cast<CuteQQuickItemCall40>(taken[40]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QQuickItem::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK10QQuickItem10metaObjectEv(
    const QQuickItem *self) {
  return self->metaObject();
}

//  QString QQuickItem::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN10QQuickItem2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuickItem::tr(s, c, n));
}

//  QQuickItem::QQuickItem(QQuickItem *parent)
extern "C" Q_DECL_EXPORT
QQuickItem *ritual_ZN10QQuickItemC1EPS_(QQuickItem *parent) {
  return new CuteQQuickItem(parent);
}

//  QQuickItem::~QQuickItem()
extern "C" Q_DECL_EXPORT
void ritual_ZN10QQuickItemD1Ev(QQuickItem *self) {
  delete self;
}

//  QQuickWindow *QQuickItem::window() const
extern "C" Q_DECL_EXPORT
QQuickWindow *ritual_ZNK10QQuickItem6windowEv(const QQuickItem *self) {
  return self->window();
}

//  QQuickItem *QQuickItem::parentItem() const
extern "C" Q_DECL_EXPORT
QQuickItem *ritual_ZNK10QQuickItem10parentItemEv(const QQuickItem *self) {
  return self->parentItem();
}

//  void QQuickItem::setParentItem(QQuickItem *parent)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QQuickItem13setParentItemEPS_(
    QQuickItem *self,
    QQuickItem *parent) {
  self->setParentItem(parent);
}

//  void QQuickItem::stackBefore(const QQuickItem *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QQuickItem11stackBeforeEPKS_(
    QQuickItem *self,
    const QQuickItem *a0) {
  self->stackBefore(a0);
}

//  void QQuickItem::stackAfter(const QQuickItem *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QQuickItem10stackAfterEPKS_(
    QQuickItem *self,
    const QQuickItem *a0) {
  self->stackAfter(a0);
}

//  QRectF QQuickItem::childrenRect()
extern "C" Q_DECL_EXPORT
QRectF *ritual_ZN10QQuickItem12childrenRectEv(QQuickItem *self) {
  return new QRectF(self->childrenRect());
}

//  QList<QQuickItem *> QQuickItem::childItems() const
extern "C" Q_DECL_EXPORT
QList<QQuickItem *> *ritual_ZNK10QQuickItem10childItemsEv(
    const QQuickItem *self) {
  return new QList<QQuickItem *>(self->childItems());
}

//  bool QQuickItem::clip() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK10QQuickItem4clipEv(const QQuickItem *self) {
  return self->clip();
}

//  void QQuickItem::setClip(bool a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QQuickItem7setClipEb(QQuickItem *self, bool a0) {
  self->setClip(a0);
}

//  QString QQuickItem::state() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK10QQuickItem5stateEv(const QQuickItem *self) {
  return new QString(self->state());
}

//  void QQuickItem::setState(const QString &a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QQuickItem8setStateERK7QString(
    QQuickItem *self,
    const QString *a0) {
  self->setState(*a0);
}

//  qreal QQuickItem::baselineOffset() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK10QQuickItem14baselineOffsetEv(const QQuickItem *self) {
  return self->baselineOffset();
}

//  void QQuickItem::setBaselineOffset(qreal a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QQuickItem17setBaselineOffsetEd(QQuickItem *self, qreal a0) {
  self->setBaselineOffset(a0);
}

//  qreal QQuickItem::x() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK10QQuickItem1xEv(const QQuickItem *self) {
  return self->x();
}

//  qreal QQuickItem::y() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK10QQuickItem1yEv(const QQuickItem *self) {
  return self->y();
}

//  QPointF QQuickItem::position() const
extern "C" Q_DECL_EXPORT
QPointF *ritual_ZNK10QQuickItem8positionEv(const QQuickItem *self) {
  return new QPointF(self->position());
}

//  void QQuickItem::setX(qreal a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QQuickItem4setXEd(QQuickItem *self, qreal a0) {
  self->setX(a0);
}

//  void QQuickItem::setY(qreal a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QQuickItem4setYEd(QQuickItem *self, qreal a0) {
  self->setY(a0);
}

//  void QQuickItem::setPosition(const QPointF &a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QQuickItem11setPositionERK7QPointF(
    QQuickItem *self,
    const QPointF *a0) {
  self->setPosition(*a0);
}

//  qreal QQuickItem::width() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK10QQuickItem5widthEv(const QQuickItem *self) {
  return self->width();
}

//  void QQuickItem::setWidth(qreal a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QQuickItem8setWidthEd(QQuickItem *self, qreal a0) {
  self->setWidth(a0);
}

//  void QQuickItem::resetWidth()
extern "C" Q_DECL_EXPORT
void ritual_ZN10QQuickItem10resetWidthEv(QQuickItem *self) {
  self->resetWidth();
}

//  void QQuickItem::setImplicitWidth(qreal a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QQuickItem16setImplicitWidthEd(QQuickItem *self, qreal a0) {
  self->setImplicitWidth(a0);
}

//  qreal QQuickItem::implicitWidth() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK10QQuickItem13implicitWidthEv(const QQuickItem *self) {
  return self->implicitWidth();
}

//  qreal QQuickItem::height() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK10QQuickItem6heightEv(const QQuickItem *self) {
  return self->height();
}

//  void QQuickItem::setHeight(qreal a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QQuickItem9setHeightEd(QQuickItem *self, qreal a0) {
  self->setHeight(a0);
}

//  void QQuickItem::resetHeight()
extern "C" Q_DECL_EXPORT
void ritual_ZN10QQuickItem11resetHeightEv(QQuickItem *self) {
  self->resetHeight();
}

//  void QQuickItem::setImplicitHeight(qreal a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QQuickItem17setImplicitHeightEd(QQuickItem *self, qreal a0) {
  self->setImplicitHeight(a0);
}

//  qreal QQuickItem::implicitHeight() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK10QQuickItem14implicitHeightEv(const QQuickItem *self) {
  return self->implicitHeight();
}

//  QSizeF QQuickItem::size() const
extern "C" Q_DECL_EXPORT
QSizeF *ritual_ZNK10QQuickItem4sizeEv(const QQuickItem *self) {
  return new QSizeF(self->size());
}

//  void QQuickItem::setSize(const QSizeF &size)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QQuickItem7setSizeERK6QSizeF(
    QQuickItem *self,
    const QSizeF *size) {
  self->setSize(*size);
}

//  TransformOrigin QQuickItem::transformOrigin() const
extern "C" Q_DECL_EXPORT
QQuickItem::TransformOrigin ritual_ZNK10QQuickItem15transformOriginEv(
    const QQuickItem *self) {
  return self->transformOrigin();
}

//  void QQuickItem::setTransformOrigin(TransformOrigin a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QQuickItem18setTransformOriginENS_15TransformOriginE(
    QQuickItem *self,
    QQuickItem::TransformOrigin a0) {
  self->setTransformOrigin(a0);
}

//  QPointF QQuickItem::transformOriginPoint() const
extern "C" Q_DECL_EXPORT
QPointF *ritual_ZNK10QQuickItem20transformOriginPointEv(
    const QQuickItem *self) {
  return new QPointF(self->transformOriginPoint());
}

//  void QQuickItem::setTransformOriginPoint(const QPointF &a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QQuickItem23setTransformOriginPointERK7QPointF(
    QQuickItem *self,
    const QPointF *a0) {
  self->setTransformOriginPoint(*a0);
}

//  qreal QQuickItem::z() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK10QQuickItem1zEv(const QQuickItem *self) {
  return self->z();
}

//  void QQuickItem::setZ(qreal a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QQuickItem4setZEd(QQuickItem *self, qreal a0) {
  self->setZ(a0);
}

//  qreal QQuickItem::rotation() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK10QQuickItem8rotationEv(const QQuickItem *self) {
  return self->rotation();
}

//  void QQuickItem::setRotation(qreal a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QQuickItem11setRotationEd(QQuickItem *self, qreal a0) {
  self->setRotation(a0);
}

//  qreal QQuickItem::scale() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK10QQuickItem5scaleEv(const QQuickItem *self) {
  return self->scale();
}

//  void QQuickItem::setScale(qreal a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QQuickItem8setScaleEd(QQuickItem *self, qreal a0) {
  self->setScale(a0);
}

//  qreal QQuickItem::opacity() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK10QQuickItem7opacityEv(const QQuickItem *self) {
  return self->opacity();
}

//  void QQuickItem::setOpacity(qreal a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QQuickItem10setOpacityEd(QQuickItem *self, qreal a0) {
  self->setOpacity(a0);
}

//  bool QQuickItem::isVisible() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK10QQuickItem9isVisibleEv(const QQuickItem *self) {
  return self->isVisible();
}

//  void QQuickItem::setVisible(bool a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QQuickItem10setVisibleEb(QQuickItem *self, bool a0) {
  self->setVisible(a0);
}

//  bool QQuickItem::isEnabled() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK10QQuickItem9isEnabledEv(const QQuickItem *self) {
  return self->isEnabled();
}

//  void QQuickItem::setEnabled(bool a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QQuickItem10setEnabledEb(QQuickItem *self, bool a0) {
  self->setEnabled(a0);
}

//  bool QQuickItem::smooth() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK10QQuickItem6smoothEv(const QQuickItem *self) {
  return self->smooth();
}

//  void QQuickItem::setSmooth(bool a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QQuickItem9setSmoothEb(QQuickItem *self, bool a0) {
  self->setSmooth(a0);
}

//  bool QQuickItem::activeFocusOnTab() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK10QQuickItem16activeFocusOnTabEv(const QQuickItem *self) {
  return self->activeFocusOnTab();
}

//  void QQuickItem::setActiveFocusOnTab(bool a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QQuickItem19setActiveFocusOnTabEb(
    QQuickItem *self,
    bool a0) {
  self->setActiveFocusOnTab(a0);
}

//  bool QQuickItem::antialiasing() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK10QQuickItem12antialiasingEv(const QQuickItem *self) {
  return self->antialiasing();
}

//  void QQuickItem::setAntialiasing(bool a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QQuickItem15setAntialiasingEb(QQuickItem *self, bool a0) {
  self->setAntialiasing(a0);
}

//  void QQuickItem::resetAntialiasing()
extern "C" Q_DECL_EXPORT
void ritual_ZN10QQuickItem17resetAntialiasingEv(QQuickItem *self) {
  self->resetAntialiasing();
}

//  Flags QQuickItem::flags() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK10QQuickItem5flagsEv(const QQuickItem *self) {
  return static_cast<int>(self->flags().toInt());
}

//  void QQuickItem::setFlag(Flag flag, bool enabled)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QQuickItem7setFlagENS_4FlagEb(
    QQuickItem *self,
    QQuickItem::Flag flag,
    bool enabled) {
  self->setFlag(flag, enabled);
}

//  void QQuickItem::setFlags(Flags flags)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QQuickItem8setFlagsE6QFlagsINS_4FlagEE(
    QQuickItem *self,
    int flags) {
  self->setFlags(QFlags<QQuickItem::Flag>::fromInt(flags));
}

//  QRectF QQuickItem::boundingRect() const
extern "C" Q_DECL_EXPORT
QRectF *ritual_ZNK10QQuickItem12boundingRectEv(const QQuickItem *self) {
  return new QRectF(self->boundingRect());
}

//  QRectF QQuickItem::clipRect() const
extern "C" Q_DECL_EXPORT
QRectF *ritual_ZNK10QQuickItem8clipRectEv(const QQuickItem *self) {
  return new QRectF(self->clipRect());
}

//  QQuickItem *QQuickItem::viewportItem() const
extern "C" Q_DECL_EXPORT
QQuickItem *ritual_ZNK10QQuickItem12viewportItemEv(const QQuickItem *self) {
  return self->viewportItem();
}

//  bool QQuickItem::hasActiveFocus() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK10QQuickItem14hasActiveFocusEv(const QQuickItem *self) {
  return self->hasActiveFocus();
}

//  bool QQuickItem::hasFocus() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK10QQuickItem8hasFocusEv(const QQuickItem *self) {
  return self->hasFocus();
}

//  void QQuickItem::setFocus(bool a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QQuickItem8setFocusEb(QQuickItem *self, bool a0) {
  self->setFocus(a0);
}

//  void QQuickItem::setFocus(bool focus, Qt::FocusReason reason)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QQuickItem8setFocusEbN2Qt11FocusReasonE(
    QQuickItem *self,
    bool focus,
    Qt::FocusReason reason) {
  self->setFocus(focus, reason);
}

//  bool QQuickItem::isFocusScope() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK10QQuickItem12isFocusScopeEv(const QQuickItem *self) {
  return self->isFocusScope();
}

//  QQuickItem *QQuickItem::scopedFocusItem() const
extern "C" Q_DECL_EXPORT
QQuickItem *ritual_ZNK10QQuickItem15scopedFocusItemEv(
    const QQuickItem *self) {
  return self->scopedFocusItem();
}

//  Qt::FocusPolicy QQuickItem::focusPolicy() const
extern "C" Q_DECL_EXPORT
Qt::FocusPolicy ritual_ZNK10QQuickItem11focusPolicyEv(
    const QQuickItem *self) {
  return self->focusPolicy();
}

//  void QQuickItem::setFocusPolicy(Qt::FocusPolicy policy)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QQuickItem14setFocusPolicyEN2Qt11FocusPolicyE(
    QQuickItem *self,
    Qt::FocusPolicy policy) {
  self->setFocusPolicy(policy);
}

//  bool QQuickItem::isAncestorOf(const QQuickItem *child) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK10QQuickItem12isAncestorOfEPKS_(
    const QQuickItem *self,
    const QQuickItem *child) {
  return self->isAncestorOf(child);
}

//  Qt::MouseButtons QQuickItem::acceptedMouseButtons() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK10QQuickItem20acceptedMouseButtonsEv(const QQuickItem *self) {
  return static_cast<int>(self->acceptedMouseButtons().toInt());
}

//  void QQuickItem::setAcceptedMouseButtons(Qt::MouseButtons buttons)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QQuickItem23setAcceptedMouseButtonsE6QFlagsIN2Qt11MouseButtonEE(
    QQuickItem *self,
    int buttons) {
  self->setAcceptedMouseButtons(QFlags<Qt::MouseButton>::fromInt(buttons));
}

//  bool QQuickItem::acceptHoverEvents() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK10QQuickItem17acceptHoverEventsEv(const QQuickItem *self) {
  return self->acceptHoverEvents();
}

//  void QQuickItem::setAcceptHoverEvents(bool enabled)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QQuickItem20setAcceptHoverEventsEb(
    QQuickItem *self,
    bool enabled) {
  self->setAcceptHoverEvents(enabled);
}

//  bool QQuickItem::acceptTouchEvents() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK10QQuickItem17acceptTouchEventsEv(const QQuickItem *self) {
  return self->acceptTouchEvents();
}

//  void QQuickItem::setAcceptTouchEvents(bool accept)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QQuickItem20setAcceptTouchEventsEb(
    QQuickItem *self,
    bool accept) {
  self->setAcceptTouchEvents(accept);
}

#if QT_CONFIG(cursor)
//  QCursor QQuickItem::cursor() const
extern "C" Q_DECL_EXPORT
QCursor *ritual_ZNK10QQuickItem6cursorEv(const QQuickItem *self) {
  return new QCursor(self->cursor());
}
#endif  // QT_CONFIG(cursor)

#if QT_CONFIG(cursor)
//  void QQuickItem::setCursor(const QCursor &cursor)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QQuickItem9setCursorERK7QCursor(
    QQuickItem *self,
    const QCursor *cursor) {
  self->setCursor(*cursor);
}
#endif  // QT_CONFIG(cursor)

#if QT_CONFIG(cursor)
//  void QQuickItem::unsetCursor()
extern "C" Q_DECL_EXPORT
void ritual_ZN10QQuickItem11unsetCursorEv(QQuickItem *self) {
  self->unsetCursor();
}
#endif  // QT_CONFIG(cursor)

//  bool QQuickItem::isUnderMouse() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK10QQuickItem12isUnderMouseEv(const QQuickItem *self) {
  return self->isUnderMouse();
}

//  void QQuickItem::grabMouse()
extern "C" Q_DECL_EXPORT
void ritual_ZN10QQuickItem9grabMouseEv(QQuickItem *self) {
  self->grabMouse();
}

//  void QQuickItem::ungrabMouse()
extern "C" Q_DECL_EXPORT
void ritual_ZN10QQuickItem11ungrabMouseEv(QQuickItem *self) {
  self->ungrabMouse();
}

//  bool QQuickItem::keepMouseGrab() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK10QQuickItem13keepMouseGrabEv(const QQuickItem *self) {
  return self->keepMouseGrab();
}

//  void QQuickItem::setKeepMouseGrab(bool a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QQuickItem16setKeepMouseGrabEb(QQuickItem *self, bool a0) {
  self->setKeepMouseGrab(a0);
}

//  bool QQuickItem::filtersChildMouseEvents() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK10QQuickItem23filtersChildMouseEventsEv(
    const QQuickItem *self) {
  return self->filtersChildMouseEvents();
}

//  void QQuickItem::setFiltersChildMouseEvents(bool filter)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QQuickItem26setFiltersChildMouseEventsEb(
    QQuickItem *self,
    bool filter) {
  self->setFiltersChildMouseEvents(filter);
}

//  void QQuickItem::ungrabTouchPoints()
extern "C" Q_DECL_EXPORT
void ritual_ZN10QQuickItem17ungrabTouchPointsEv(QQuickItem *self) {
  self->ungrabTouchPoints();
}

//  bool QQuickItem::keepTouchGrab() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK10QQuickItem13keepTouchGrabEv(const QQuickItem *self) {
  return self->keepTouchGrab();
}

//  void QQuickItem::setKeepTouchGrab(bool a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QQuickItem16setKeepTouchGrabEb(QQuickItem *self, bool a0) {
  self->setKeepTouchGrab(a0);
}

//  bool QQuickItem::grabToImage(const QJSValue &callback, const QSize
//      &targetSize)
extern "C" Q_DECL_EXPORT
bool ritual_ZN10QQuickItem11grabToImageERK8QJSValueRK5QSize(
    QQuickItem *self,
    const QJSValue *callback,
    const QSize *targetSize) {
  return self->grabToImage(*callback, *targetSize);
}

//  bool QQuickItem::contains(const QPointF &point) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK10QQuickItem8containsERK7QPointF(
    const QQuickItem *self,
    const QPointF *point) {
  return self->contains(*point);
}

//  QObject *QQuickItem::containmentMask() const
extern "C" Q_DECL_EXPORT
QObject *ritual_ZNK10QQuickItem15containmentMaskEv(const QQuickItem *self) {
  return self->containmentMask();
}

//  void QQuickItem::setContainmentMask(QObject *mask)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QQuickItem18setContainmentMaskEP7QObject(
    QQuickItem *self,
    QObject *mask) {
  self->setContainmentMask(mask);
}

//  QTransform QQuickItem::itemTransform(QQuickItem *a0, bool *a1) const
extern "C" Q_DECL_EXPORT
QTransform *ritual_ZNK10QQuickItem13itemTransformEPS_Pb(
    const QQuickItem *self,
    QQuickItem *a0,
    bool *a1) {
  return new QTransform(self->itemTransform(a0, a1));
}

//  QPointF QQuickItem::mapToScene(const QPointF &point) const
extern "C" Q_DECL_EXPORT
QPointF *ritual_ZNK10QQuickItem10mapToSceneERK7QPointF(
    const QQuickItem *self,
    const QPointF *point) {
  return new QPointF(self->mapToScene(*point));
}

//  QRectF QQuickItem::mapRectToItem(const QQuickItem *item, const QRectF
//      &rect) const
extern "C" Q_DECL_EXPORT
QRectF *ritual_ZNK10QQuickItem13mapRectToItemEPKS_RK6QRectF(
    const QQuickItem *self,
    const QQuickItem *item,
    const QRectF *rect) {
  return new QRectF(self->mapRectToItem(item, *rect));
}

//  QRectF QQuickItem::mapRectToScene(const QRectF &rect) const
extern "C" Q_DECL_EXPORT
QRectF *ritual_ZNK10QQuickItem14mapRectToSceneERK6QRectF(
    const QQuickItem *self,
    const QRectF *rect) {
  return new QRectF(self->mapRectToScene(*rect));
}

//  QPointF QQuickItem::mapFromScene(const QPointF &point) const
extern "C" Q_DECL_EXPORT
QPointF *ritual_ZNK10QQuickItem12mapFromSceneERK7QPointF(
    const QQuickItem *self,
    const QPointF *point) {
  return new QPointF(self->mapFromScene(*point));
}

//  QRectF QQuickItem::mapRectFromItem(const QQuickItem *item, const QRectF
//      &rect) const
extern "C" Q_DECL_EXPORT
QRectF *ritual_ZNK10QQuickItem15mapRectFromItemEPKS_RK6QRectF(
    const QQuickItem *self,
    const QQuickItem *item,
    const QRectF *rect) {
  return new QRectF(self->mapRectFromItem(item, *rect));
}

//  QRectF QQuickItem::mapRectFromScene(const QRectF &rect) const
extern "C" Q_DECL_EXPORT
QRectF *ritual_ZNK10QQuickItem16mapRectFromSceneERK6QRectF(
    const QQuickItem *self,
    const QRectF *rect) {
  return new QRectF(self->mapRectFromScene(*rect));
}

//  void QQuickItem::polish()
extern "C" Q_DECL_EXPORT
void ritual_ZN10QQuickItem6polishEv(QQuickItem *self) {
  self->polish();
}

#if QT_DEPRECATED_SINCE(6, 5)
//  void QQuickItem::mapFromItem(QQmlV4FunctionPtr a0) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK10QQuickItem11mapFromItemEP14QQmlV4Function(
    const QQuickItem *self,
    QQmlV4FunctionPtr a0) {
  self->mapFromItem(a0);
}
#endif  // QT_DEPRECATED_SINCE(6, 5)

//  QPointF QQuickItem::mapFromItem(const QQuickItem *item, const QPointF
//      &point) const
extern "C" Q_DECL_EXPORT
QPointF *ritual_ZNK10QQuickItem11mapFromItemEPKS_RK7QPointF(
    const QQuickItem *self,
    const QQuickItem *item,
    const QPointF *point) {
  return new QPointF(self->mapFromItem(item, *point));
}

//  QPointF QQuickItem::mapFromItem(const QQuickItem *item, qreal x, qreal y)
extern "C" Q_DECL_EXPORT
QPointF *ritual_ZN10QQuickItem11mapFromItemEPKS_dd(
    QQuickItem *self,
    const QQuickItem *item,
    qreal x,
    qreal y) {
  return new QPointF(self->mapFromItem(item, x, y));
}

//  QRectF QQuickItem::mapFromItem(const QQuickItem *item, const QRectF
//      &rect) const
extern "C" Q_DECL_EXPORT
QRectF *ritual_ZNK10QQuickItem11mapFromItemEPKS_RK6QRectF(
    const QQuickItem *self,
    const QQuickItem *item,
    const QRectF *rect) {
  return new QRectF(self->mapFromItem(item, *rect));
}

//  QRectF QQuickItem::mapFromItem(const QQuickItem *item, qreal x, qreal y,
//      qreal width, qreal height) const
extern "C" Q_DECL_EXPORT
QRectF *ritual_ZNK10QQuickItem11mapFromItemEPKS_dddd(
    const QQuickItem *self,
    const QQuickItem *item,
    qreal x,
    qreal y,
    qreal width,
    qreal height) {
  return new QRectF(self->mapFromItem(item, x, y, width, height));
}

#if QT_DEPRECATED_SINCE(6, 5)
//  void QQuickItem::mapToItem(QQmlV4FunctionPtr a0) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK10QQuickItem9mapToItemEP14QQmlV4Function(
    const QQuickItem *self,
    QQmlV4FunctionPtr a0) {
  self->mapToItem(a0);
}
#endif  // QT_DEPRECATED_SINCE(6, 5)

//  QPointF QQuickItem::mapToItem(const QQuickItem *item, const QPointF
//      &point) const
extern "C" Q_DECL_EXPORT
QPointF *ritual_ZNK10QQuickItem9mapToItemEPKS_RK7QPointF(
    const QQuickItem *self,
    const QQuickItem *item,
    const QPointF *point) {
  return new QPointF(self->mapToItem(item, *point));
}

//  QPointF QQuickItem::mapToItem(const QQuickItem *item, qreal x, qreal y)
extern "C" Q_DECL_EXPORT
QPointF *ritual_ZN10QQuickItem9mapToItemEPKS_dd(
    QQuickItem *self,
    const QQuickItem *item,
    qreal x,
    qreal y) {
  return new QPointF(self->mapToItem(item, x, y));
}

//  QRectF QQuickItem::mapToItem(const QQuickItem *item, const QRectF &rect)
//      const
extern "C" Q_DECL_EXPORT
QRectF *ritual_ZNK10QQuickItem9mapToItemEPKS_RK6QRectF(
    const QQuickItem *self,
    const QQuickItem *item,
    const QRectF *rect) {
  return new QRectF(self->mapToItem(item, *rect));
}

//  QRectF QQuickItem::mapToItem(const QQuickItem *item, qreal x, qreal y,
//      qreal width, qreal height) const
extern "C" Q_DECL_EXPORT
QRectF *ritual_ZNK10QQuickItem9mapToItemEPKS_dddd(
    const QQuickItem *self,
    const QQuickItem *item,
    qreal x,
    qreal y,
    qreal width,
    qreal height) {
  return new QRectF(self->mapToItem(item, x, y, width, height));
}

#if QT_DEPRECATED_SINCE(6, 5)
//  void QQuickItem::mapFromGlobal(QQmlV4FunctionPtr a0) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK10QQuickItem13mapFromGlobalEP14QQmlV4Function(
    const QQuickItem *self,
    QQmlV4FunctionPtr a0) {
  self->mapFromGlobal(a0);
}
#endif  // QT_DEPRECATED_SINCE(6, 5)

//  QPointF QQuickItem::mapFromGlobal(qreal x, qreal y) const
extern "C" Q_DECL_EXPORT
QPointF *ritual_ZNK10QQuickItem13mapFromGlobalEdd(
    const QQuickItem *self,
    qreal x,
    qreal y) {
  return new QPointF(self->mapFromGlobal(x, y));
}

//  QPointF QQuickItem::mapFromGlobal(const QPointF &point) const
extern "C" Q_DECL_EXPORT
QPointF *ritual_ZNK10QQuickItem13mapFromGlobalERK7QPointF(
    const QQuickItem *self,
    const QPointF *point) {
  return new QPointF(self->mapFromGlobal(*point));
}

#if QT_DEPRECATED_SINCE(6, 5)
//  void QQuickItem::mapToGlobal(QQmlV4FunctionPtr a0) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK10QQuickItem11mapToGlobalEP14QQmlV4Function(
    const QQuickItem *self,
    QQmlV4FunctionPtr a0) {
  self->mapToGlobal(a0);
}
#endif  // QT_DEPRECATED_SINCE(6, 5)

//  QPointF QQuickItem::mapToGlobal(qreal x, qreal y) const
extern "C" Q_DECL_EXPORT
QPointF *ritual_ZNK10QQuickItem11mapToGlobalEdd(
    const QQuickItem *self,
    qreal x,
    qreal y) {
  return new QPointF(self->mapToGlobal(x, y));
}

//  QPointF QQuickItem::mapToGlobal(const QPointF &point) const
extern "C" Q_DECL_EXPORT
QPointF *ritual_ZNK10QQuickItem11mapToGlobalERK7QPointF(
    const QQuickItem *self,
    const QPointF *point) {
  return new QPointF(self->mapToGlobal(*point));
}

//  void QQuickItem::forceActiveFocus()
extern "C" Q_DECL_EXPORT
void ritual_ZN10QQuickItem16forceActiveFocusEv(QQuickItem *self) {
  self->forceActiveFocus();
}

//  void QQuickItem::forceActiveFocus(Qt::FocusReason reason)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QQuickItem16forceActiveFocusEN2Qt11FocusReasonE(
    QQuickItem *self,
    Qt::FocusReason reason) {
  self->forceActiveFocus(reason);
}

//  QQuickItem *QQuickItem::nextItemInFocusChain(bool forward)
extern "C" Q_DECL_EXPORT
QQuickItem *ritual_ZN10QQuickItem20nextItemInFocusChainEb(
    QQuickItem *self,
    bool forward) {
  return self->nextItemInFocusChain(forward);
}

//  QQuickItem *QQuickItem::childAt(qreal x, qreal y) const
extern "C" Q_DECL_EXPORT
QQuickItem *ritual_ZNK10QQuickItem7childAtEdd(
    const QQuickItem *self,
    qreal x,
    qreal y) {
  return self->childAt(x, y);
}

//  void QQuickItem::ensurePolished()
extern "C" Q_DECL_EXPORT
void ritual_ZN10QQuickItem14ensurePolishedEv(QQuickItem *self) {
  self->ensurePolished();
}

//  void QQuickItem::dumpItemTree() const
extern "C" Q_DECL_EXPORT
void ritual_ZNK10QQuickItem12dumpItemTreeEv(const QQuickItem *self) {
  self->dumpItemTree();
}

#if QT_CONFIG(im)
//  QVariant QQuickItem::inputMethodQuery(Qt::InputMethodQuery query) const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK10QQuickItem16inputMethodQueryEN2Qt16InputMethodQueryE(
    const QQuickItem *self,
    Qt::InputMethodQuery query) {
  return new QVariant(self->inputMethodQuery(query));
}
#endif  // QT_CONFIG(im)

//  bool QQuickItem::isTextureProvider() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK10QQuickItem17isTextureProviderEv(const QQuickItem *self) {
  return self->isTextureProvider();
}

//  QSGTextureProvider *QQuickItem::textureProvider() const
extern "C" Q_DECL_EXPORT
QSGTextureProvider *ritual_ZNK10QQuickItem15textureProviderEv(
    const QQuickItem *self) {
  return self->textureProvider();
}

//  void QQuickItem::setMutabilityGroup(int mutabilityGroup)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QQuickItem18setMutabilityGroupEi(
    QQuickItem *self,
    int mutabilityGroup) {
  self->setMutabilityGroup(mutabilityGroup);
}

//  int QQuickItem::mutabilityGroup() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK10QQuickItem15mutabilityGroupEv(const QQuickItem *self) {
  return self->mutabilityGroup();
}

//  void QQuickItem::update()
extern "C" Q_DECL_EXPORT
void ritual_ZN10QQuickItem6updateEv(QQuickItem *self) {
  self->update();
}

//  bool QQuickItem::event(QEvent *a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN10QQuickItem5eventEP6QEvent(QQuickItem *self, QEvent *a0) {
  return self->event(a0);
}

//  bool QQuickItem::isComponentComplete() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK10QQuickItem19isComponentCompleteEv(const QQuickItem *self) {
  return self->isComponentComplete();
}

//  void QQuickItem::itemChange(ItemChange a0, const ItemChangeData &a1)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QQuickItem10itemChangeENS_10ItemChangeERKNS_14ItemChangeDataE(
    QQuickItem *self,
    QQuickItem::ItemChange a0,
    const QQuickItem::ItemChangeData *a1) {
  self->itemChange(a0, *a1);
}

//  void QQuickItem::geometryChange(const QRectF &newGeometry, const QRectF
//      &oldGeometry)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QQuickItem14geometryChangeERK6QRectFS2_(
    QQuickItem *self,
    const QRectF *newGeometry,
    const QRectF *oldGeometry) {
  self->geometryChange(*newGeometry, *oldGeometry);
}

#if QT_CONFIG(im)
//  void QQuickItem::updateInputMethod(Qt::InputMethodQueries queries)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QQuickItem17updateInputMethodE6QFlagsIN2Qt16InputMethodQueryEE(
    QQuickItem *self,
    int queries) {
  self->updateInputMethod(QFlags<Qt::InputMethodQuery>::fromInt(queries));
}
#endif  // QT_CONFIG(im)

//  bool QQuickItem::widthValid() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK10QQuickItem10widthValidEv(const QQuickItem *self) {
  return self->widthValid();
}

//  bool QQuickItem::heightValid() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK10QQuickItem11heightValidEv(const QQuickItem *self) {
  return self->heightValid();
}

//  void QQuickItem::setImplicitSize(qreal a0, qreal a1)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QQuickItem15setImplicitSizeEdd(
    QQuickItem *self,
    qreal a0,
    qreal a1) {
  self->setImplicitSize(a0, a1);
}

//  void QQuickItem::classBegin()
extern "C" Q_DECL_EXPORT
void ritual_ZN10QQuickItem10classBeginEv(QQuickItem *self) {
  self->classBegin();
}

//  void QQuickItem::componentComplete()
extern "C" Q_DECL_EXPORT
void ritual_ZN10QQuickItem17componentCompleteEv(QQuickItem *self) {
  self->componentComplete();
}

//  void QQuickItem::keyPressEvent(QKeyEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QQuickItem13keyPressEventEP9QKeyEvent(
    QQuickItem *self,
    QKeyEvent *event) {
  self->keyPressEvent(event);
}

//  void QQuickItem::keyReleaseEvent(QKeyEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QQuickItem15keyReleaseEventEP9QKeyEvent(
    QQuickItem *self,
    QKeyEvent *event) {
  self->keyReleaseEvent(event);
}

#if QT_CONFIG(im)
//  void QQuickItem::inputMethodEvent(QInputMethodEvent *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QQuickItem16inputMethodEventEP17QInputMethodEvent(
    QQuickItem *self,
    QInputMethodEvent *a0) {
  self->inputMethodEvent(a0);
}
#endif  // QT_CONFIG(im)

//  void QQuickItem::focusInEvent(QFocusEvent *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QQuickItem12focusInEventEP11QFocusEvent(
    QQuickItem *self,
    QFocusEvent *a0) {
  self->focusInEvent(a0);
}

//  void QQuickItem::focusOutEvent(QFocusEvent *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QQuickItem13focusOutEventEP11QFocusEvent(
    QQuickItem *self,
    QFocusEvent *a0) {
  self->focusOutEvent(a0);
}

//  void QQuickItem::mousePressEvent(QMouseEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QQuickItem15mousePressEventEP11QMouseEvent(
    QQuickItem *self,
    QMouseEvent *event) {
  self->mousePressEvent(event);
}

//  void QQuickItem::mouseMoveEvent(QMouseEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QQuickItem14mouseMoveEventEP11QMouseEvent(
    QQuickItem *self,
    QMouseEvent *event) {
  self->mouseMoveEvent(event);
}

//  void QQuickItem::mouseReleaseEvent(QMouseEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QQuickItem17mouseReleaseEventEP11QMouseEvent(
    QQuickItem *self,
    QMouseEvent *event) {
  self->mouseReleaseEvent(event);
}

//  void QQuickItem::mouseDoubleClickEvent(QMouseEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QQuickItem21mouseDoubleClickEventEP11QMouseEvent(
    QQuickItem *self,
    QMouseEvent *event) {
  self->mouseDoubleClickEvent(event);
}

//  void QQuickItem::mouseUngrabEvent()
extern "C" Q_DECL_EXPORT
void ritual_ZN10QQuickItem16mouseUngrabEventEv(QQuickItem *self) {
  self->mouseUngrabEvent();
}

//  void QQuickItem::touchUngrabEvent()
extern "C" Q_DECL_EXPORT
void ritual_ZN10QQuickItem16touchUngrabEventEv(QQuickItem *self) {
  self->touchUngrabEvent();
}

#if QT_CONFIG(wheelevent)
//  void QQuickItem::wheelEvent(QWheelEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QQuickItem10wheelEventEP11QWheelEvent(
    QQuickItem *self,
    QWheelEvent *event) {
  self->wheelEvent(event);
}
#endif  // QT_CONFIG(wheelevent)

//  void QQuickItem::touchEvent(QTouchEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QQuickItem10touchEventEP11QTouchEvent(
    QQuickItem *self,
    QTouchEvent *event) {
  self->touchEvent(event);
}

//  void QQuickItem::hoverEnterEvent(QHoverEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QQuickItem15hoverEnterEventEP11QHoverEvent(
    QQuickItem *self,
    QHoverEvent *event) {
  self->hoverEnterEvent(event);
}

//  void QQuickItem::hoverMoveEvent(QHoverEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QQuickItem14hoverMoveEventEP11QHoverEvent(
    QQuickItem *self,
    QHoverEvent *event) {
  self->hoverMoveEvent(event);
}

//  void QQuickItem::hoverLeaveEvent(QHoverEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QQuickItem15hoverLeaveEventEP11QHoverEvent(
    QQuickItem *self,
    QHoverEvent *event) {
  self->hoverLeaveEvent(event);
}

#if QT_CONFIG(quick_draganddrop)
//  void QQuickItem::dragEnterEvent(QDragEnterEvent *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QQuickItem14dragEnterEventEP15QDragEnterEvent(
    QQuickItem *self,
    QDragEnterEvent *a0) {
  self->dragEnterEvent(a0);
}
#endif  // QT_CONFIG(quick_draganddrop)

#if QT_CONFIG(quick_draganddrop)
//  void QQuickItem::dragMoveEvent(QDragMoveEvent *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QQuickItem13dragMoveEventEP14QDragMoveEvent(
    QQuickItem *self,
    QDragMoveEvent *a0) {
  self->dragMoveEvent(a0);
}
#endif  // QT_CONFIG(quick_draganddrop)

#if QT_CONFIG(quick_draganddrop)
//  void QQuickItem::dragLeaveEvent(QDragLeaveEvent *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QQuickItem14dragLeaveEventEP15QDragLeaveEvent(
    QQuickItem *self,
    QDragLeaveEvent *a0) {
  self->dragLeaveEvent(a0);
}
#endif  // QT_CONFIG(quick_draganddrop)

#if QT_CONFIG(quick_draganddrop)
//  void QQuickItem::dropEvent(QDropEvent *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QQuickItem9dropEventEP10QDropEvent(
    QQuickItem *self,
    QDropEvent *a0) {
  self->dropEvent(a0);
}
#endif  // QT_CONFIG(quick_draganddrop)

//  bool QQuickItem::childMouseEventFilter(QQuickItem *a0, QEvent *a1)
extern "C" Q_DECL_EXPORT
bool ritual_ZN10QQuickItem21childMouseEventFilterEPS_P6QEvent(
    QQuickItem *self,
    QQuickItem *a0,
    QEvent *a1) {
  return self->childMouseEventFilter(a0, a1);
}

//  QSGNode *QQuickItem::updatePaintNode(QSGNode *a0, UpdatePaintNodeData
//      *a1)
extern "C" Q_DECL_EXPORT
QSGNode *ritual_ZN10QQuickItem15updatePaintNodeEP7QSGNodePNS_19UpdatePaintNodeDataE(
    QQuickItem *self,
    QSGNode *a0,
    QQuickItem::UpdatePaintNodeData *a1) {
  return self->updatePaintNode(a0, a1);
}

//  void QQuickItem::releaseResources()
extern "C" Q_DECL_EXPORT
void ritual_ZN10QQuickItem16releaseResourcesEv(QQuickItem *self) {
  self->releaseResources();
}

//  void QQuickItem::updatePolish()
extern "C" Q_DECL_EXPORT
void ritual_ZN10QQuickItem12updatePolishEv(QQuickItem *self) {
  self->updatePolish();
}

#if !defined(QT_NO_DEBUG_STREAM)
//  QDebug operator<<(QDebug debug, QQuickItem *item)
extern "C" Q_DECL_EXPORT
QDebug *ritual_Zls6QDebugP10QQuickItem(
    const QDebug *debug,
    QQuickItem *item) {
  return new QDebug(operator<<(*debug, item));
}
#endif  // !defined(QT_NO_DEBUG_STREAM)

//  QQuickItemPrivate *QQuickItem::d_func()
extern "C" Q_DECL_EXPORT
QQuickItemPrivate *ritual_ZN10QQuickItem6d_funcEv(QQuickItem *self) {
  return self->d_func();
}

//  const QQuickItemPrivate *QQuickItem::d_func() const
extern "C" Q_DECL_EXPORT
const QQuickItemPrivate *ritual_ZNK10QQuickItem6d_funcEv(
    const QQuickItem *self) {
  return self->d_func();
}

//  QQuickItem as the QQmlParserStatus it is built on
extern "C" Q_DECL_EXPORT
QQmlParserStatus *ritual_cast_QQuickItem_QQmlParserStatus(QQuickItem *self) {
  return static_cast<QQmlParserStatus *>(self);
}

//  a Python function taken by a CuteQQuickItem, for the function named by
//      the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQuickItem(QQuickItem *self, const char *key, void *call) {
  return static_cast<CuteQQuickItem *>(self)->take(key, call);
}

//  QRectF QQuickItem::boundingRect() const
extern "C" Q_DECL_EXPORT
QRectF *ritual_own_ZNK10QQuickItem12boundingRectEv(const QQuickItem *self) {
  return new QRectF(self->QQuickItem::boundingRect());
}

//  QRectF QQuickItem::clipRect() const
extern "C" Q_DECL_EXPORT
QRectF *ritual_own_ZNK10QQuickItem8clipRectEv(const QQuickItem *self) {
  return new QRectF(self->QQuickItem::clipRect());
}

//  bool QQuickItem::contains(const QPointF &point) const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK10QQuickItem8containsERK7QPointF(
    const QQuickItem *self,
    const QPointF *point) {
  return self->QQuickItem::contains(*point);
}

#if QT_CONFIG(im)
//  QVariant QQuickItem::inputMethodQuery(Qt::InputMethodQuery query) const
extern "C" Q_DECL_EXPORT
QVariant *ritual_own_ZNK10QQuickItem16inputMethodQueryEN2Qt16InputMethodQueryE(
    const QQuickItem *self,
    Qt::InputMethodQuery query) {
  return new QVariant(self->QQuickItem::inputMethodQuery(query));
}
#endif  // QT_CONFIG(im)

//  bool QQuickItem::isTextureProvider() const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK10QQuickItem17isTextureProviderEv(
    const QQuickItem *self) {
  return self->QQuickItem::isTextureProvider();
}

//  QSGTextureProvider *QQuickItem::textureProvider() const
extern "C" Q_DECL_EXPORT
QSGTextureProvider *ritual_own_ZNK10QQuickItem15textureProviderEv(
    const QQuickItem *self) {
  return self->QQuickItem::textureProvider();
}

//  bool QQuickItem::event(QEvent *a0)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN10QQuickItem5eventEP6QEvent(QQuickItem *self, QEvent *a0) {
  return static_cast<OwnQQuickItem *>(self)->OwnQQuickItem::event(a0);
}

//  void QQuickItem::itemChange(ItemChange a0, const ItemChangeData &a1)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN10QQuickItem10itemChangeENS_10ItemChangeERKNS_14ItemChangeDataE(
    QQuickItem *self,
    QQuickItem::ItemChange a0,
    const QQuickItem::ItemChangeData *a1) {
  static_cast<OwnQQuickItem *>(self)->OwnQQuickItem::itemChange(a0, *a1);
}

//  void QQuickItem::geometryChange(const QRectF &newGeometry, const QRectF
//      &oldGeometry)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN10QQuickItem14geometryChangeERK6QRectFS2_(
    QQuickItem *self,
    const QRectF *newGeometry,
    const QRectF *oldGeometry) {
  static_cast<OwnQQuickItem *>(self)->OwnQQuickItem::geometryChange(
      *newGeometry,
      *oldGeometry);
}

//  void QQuickItem::classBegin()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN10QQuickItem10classBeginEv(QQuickItem *self) {
  static_cast<OwnQQuickItem *>(self)->OwnQQuickItem::classBegin();
}

//  void QQuickItem::componentComplete()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN10QQuickItem17componentCompleteEv(QQuickItem *self) {
  static_cast<OwnQQuickItem *>(self)->OwnQQuickItem::componentComplete();
}

//  void QQuickItem::keyPressEvent(QKeyEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN10QQuickItem13keyPressEventEP9QKeyEvent(
    QQuickItem *self,
    QKeyEvent *event) {
  static_cast<OwnQQuickItem *>(self)->OwnQQuickItem::keyPressEvent(event);
}

//  void QQuickItem::keyReleaseEvent(QKeyEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN10QQuickItem15keyReleaseEventEP9QKeyEvent(
    QQuickItem *self,
    QKeyEvent *event) {
  static_cast<OwnQQuickItem *>(self)->OwnQQuickItem::keyReleaseEvent(event);
}

#if QT_CONFIG(im)
//  void QQuickItem::inputMethodEvent(QInputMethodEvent *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN10QQuickItem16inputMethodEventEP17QInputMethodEvent(
    QQuickItem *self,
    QInputMethodEvent *a0) {
  static_cast<OwnQQuickItem *>(self)->OwnQQuickItem::inputMethodEvent(a0);
}
#endif  // QT_CONFIG(im)

//  void QQuickItem::focusInEvent(QFocusEvent *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN10QQuickItem12focusInEventEP11QFocusEvent(
    QQuickItem *self,
    QFocusEvent *a0) {
  static_cast<OwnQQuickItem *>(self)->OwnQQuickItem::focusInEvent(a0);
}

//  void QQuickItem::focusOutEvent(QFocusEvent *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN10QQuickItem13focusOutEventEP11QFocusEvent(
    QQuickItem *self,
    QFocusEvent *a0) {
  static_cast<OwnQQuickItem *>(self)->OwnQQuickItem::focusOutEvent(a0);
}

//  void QQuickItem::mousePressEvent(QMouseEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN10QQuickItem15mousePressEventEP11QMouseEvent(
    QQuickItem *self,
    QMouseEvent *event) {
  static_cast<OwnQQuickItem *>(self)->OwnQQuickItem::mousePressEvent(event);
}

//  void QQuickItem::mouseMoveEvent(QMouseEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN10QQuickItem14mouseMoveEventEP11QMouseEvent(
    QQuickItem *self,
    QMouseEvent *event) {
  static_cast<OwnQQuickItem *>(self)->OwnQQuickItem::mouseMoveEvent(event);
}

//  void QQuickItem::mouseReleaseEvent(QMouseEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN10QQuickItem17mouseReleaseEventEP11QMouseEvent(
    QQuickItem *self,
    QMouseEvent *event) {
  static_cast<OwnQQuickItem *>(self)->OwnQQuickItem::mouseReleaseEvent(
      event);
}

//  void QQuickItem::mouseDoubleClickEvent(QMouseEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN10QQuickItem21mouseDoubleClickEventEP11QMouseEvent(
    QQuickItem *self,
    QMouseEvent *event) {
  static_cast<OwnQQuickItem *>(self)->OwnQQuickItem::mouseDoubleClickEvent(
      event);
}

//  void QQuickItem::mouseUngrabEvent()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN10QQuickItem16mouseUngrabEventEv(QQuickItem *self) {
  static_cast<OwnQQuickItem *>(self)->OwnQQuickItem::mouseUngrabEvent();
}

//  void QQuickItem::touchUngrabEvent()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN10QQuickItem16touchUngrabEventEv(QQuickItem *self) {
  static_cast<OwnQQuickItem *>(self)->OwnQQuickItem::touchUngrabEvent();
}

#if QT_CONFIG(wheelevent)
//  void QQuickItem::wheelEvent(QWheelEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN10QQuickItem10wheelEventEP11QWheelEvent(
    QQuickItem *self,
    QWheelEvent *event) {
  static_cast<OwnQQuickItem *>(self)->OwnQQuickItem::wheelEvent(event);
}
#endif  // QT_CONFIG(wheelevent)

//  void QQuickItem::touchEvent(QTouchEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN10QQuickItem10touchEventEP11QTouchEvent(
    QQuickItem *self,
    QTouchEvent *event) {
  static_cast<OwnQQuickItem *>(self)->OwnQQuickItem::touchEvent(event);
}

//  void QQuickItem::hoverEnterEvent(QHoverEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN10QQuickItem15hoverEnterEventEP11QHoverEvent(
    QQuickItem *self,
    QHoverEvent *event) {
  static_cast<OwnQQuickItem *>(self)->OwnQQuickItem::hoverEnterEvent(event);
}

//  void QQuickItem::hoverMoveEvent(QHoverEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN10QQuickItem14hoverMoveEventEP11QHoverEvent(
    QQuickItem *self,
    QHoverEvent *event) {
  static_cast<OwnQQuickItem *>(self)->OwnQQuickItem::hoverMoveEvent(event);
}

//  void QQuickItem::hoverLeaveEvent(QHoverEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN10QQuickItem15hoverLeaveEventEP11QHoverEvent(
    QQuickItem *self,
    QHoverEvent *event) {
  static_cast<OwnQQuickItem *>(self)->OwnQQuickItem::hoverLeaveEvent(event);
}

#if QT_CONFIG(quick_draganddrop)
//  void QQuickItem::dragEnterEvent(QDragEnterEvent *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN10QQuickItem14dragEnterEventEP15QDragEnterEvent(
    QQuickItem *self,
    QDragEnterEvent *a0) {
  static_cast<OwnQQuickItem *>(self)->OwnQQuickItem::dragEnterEvent(a0);
}
#endif  // QT_CONFIG(quick_draganddrop)

#if QT_CONFIG(quick_draganddrop)
//  void QQuickItem::dragMoveEvent(QDragMoveEvent *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN10QQuickItem13dragMoveEventEP14QDragMoveEvent(
    QQuickItem *self,
    QDragMoveEvent *a0) {
  static_cast<OwnQQuickItem *>(self)->OwnQQuickItem::dragMoveEvent(a0);
}
#endif  // QT_CONFIG(quick_draganddrop)

#if QT_CONFIG(quick_draganddrop)
//  void QQuickItem::dragLeaveEvent(QDragLeaveEvent *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN10QQuickItem14dragLeaveEventEP15QDragLeaveEvent(
    QQuickItem *self,
    QDragLeaveEvent *a0) {
  static_cast<OwnQQuickItem *>(self)->OwnQQuickItem::dragLeaveEvent(a0);
}
#endif  // QT_CONFIG(quick_draganddrop)

#if QT_CONFIG(quick_draganddrop)
//  void QQuickItem::dropEvent(QDropEvent *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN10QQuickItem9dropEventEP10QDropEvent(
    QQuickItem *self,
    QDropEvent *a0) {
  static_cast<OwnQQuickItem *>(self)->OwnQQuickItem::dropEvent(a0);
}
#endif  // QT_CONFIG(quick_draganddrop)

//  bool QQuickItem::childMouseEventFilter(QQuickItem *a0, QEvent *a1)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN10QQuickItem21childMouseEventFilterEPS_P6QEvent(
    QQuickItem *self,
    QQuickItem *a0,
    QEvent *a1) {
  return static_cast<OwnQQuickItem *>(self)->OwnQQuickItem::childMouseEventFilter(
      a0,
      a1);
}

//  QSGNode *QQuickItem::updatePaintNode(QSGNode *a0, UpdatePaintNodeData
//      *a1)
extern "C" Q_DECL_EXPORT
QSGNode *ritual_own_ZN10QQuickItem15updatePaintNodeEP7QSGNodePNS_19UpdatePaintNodeDataE(
    QQuickItem *self,
    QSGNode *a0,
    QQuickItem::UpdatePaintNodeData *a1) {
  return static_cast<OwnQQuickItem *>(self)->OwnQQuickItem::updatePaintNode(
      a0,
      a1);
}

//  void QQuickItem::releaseResources()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN10QQuickItem16releaseResourcesEv(QQuickItem *self) {
  static_cast<OwnQQuickItem *>(self)->OwnQQuickItem::releaseResources();
}

//  void QQuickItem::updatePolish()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN10QQuickItem12updatePolishEv(QQuickItem *self) {
  static_cast<OwnQQuickItem *>(self)->OwnQQuickItem::updatePolish();
}

//  QList<QQuickItem *>::QList()
extern "C" Q_DECL_EXPORT
QList<QQuickItem *> *ritual_list_make_QQuickItem_ptr() {
  return new QList<QQuickItem *>();
}

//  void QList<QQuickItem *>::append(const QQuickItem * &value)
extern "C" Q_DECL_EXPORT
void ritual_list_add_QQuickItem_ptr(
    QList<QQuickItem *> *self,
    QQuickItem *element) {
  self->append(element);
}

//  qsizetype QList<QQuickItem *>::size() const
extern "C" Q_DECL_EXPORT
long long ritual_list_size_QQuickItem_ptr(const QList<QQuickItem *> *self) {
  return self->size();
}

//  const QQuickItem * &QList<QQuickItem *>::at(qsizetype i) const
extern "C" Q_DECL_EXPORT
QQuickItem *ritual_list_at_QQuickItem_ptr(
    const QList<QQuickItem *> *self,
    long long index) {
  return self->at(index);
}

//  QList<QQuickItem *>::~QList()
extern "C" Q_DECL_EXPORT
void ritual_list_drop_QQuickItem_ptr(QList<QQuickItem *> *self) {
  delete self;
}
