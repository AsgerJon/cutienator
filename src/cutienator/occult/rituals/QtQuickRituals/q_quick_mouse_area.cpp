//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/6.12.0/QtQuick/private/qquickmousearea_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtGui/qtguiglobal.h>
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qquickmousearea_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qrect.h>
#include <QtQuick/qquickitem.h>
#include <QtCore/qpoint.h>
#include <QtCore/qvariant.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  Only a class built on QQuickMouseArea may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQQuickMouseArea : QQuickMouseArea {
  using QQuickMouseArea::mousePressEvent;
  using QQuickMouseArea::mouseReleaseEvent;
  using QQuickMouseArea::mouseDoubleClickEvent;
  using QQuickMouseArea::mouseMoveEvent;
  using QQuickMouseArea::mouseUngrabEvent;
  using QQuickMouseArea::touchUngrabEvent;
  using QQuickMouseArea::hoverEnterEvent;
  using QQuickMouseArea::hoverMoveEvent;
  using QQuickMouseArea::hoverLeaveEvent;
  using QQuickMouseArea::wheelEvent;
  using QQuickMouseArea::childMouseEventFilter;
  using QQuickMouseArea::timerEvent;
  using QQuickMouseArea::geometryChange;
  using QQuickMouseArea::itemChange;
  using QQuickMouseArea::updatePaintNode;
};

//  A QQuickMouseArea that Python can take functions over in. Every QQuickMouseArea
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQQuickMouseAreaCall0)(const void *, QMouseEvent *, int *);
typedef void (*CuteQQuickMouseAreaCall1)(const void *, QMouseEvent *, int *);
typedef void (*CuteQQuickMouseAreaCall2)(const void *, QMouseEvent *, int *);
typedef void (*CuteQQuickMouseAreaCall3)(const void *, QMouseEvent *, int *);
typedef void (*CuteQQuickMouseAreaCall4)(const void *, int *);
typedef void (*CuteQQuickMouseAreaCall5)(const void *, int *);
typedef void (*CuteQQuickMouseAreaCall6)(const void *, QHoverEvent *, int *);
typedef void (*CuteQQuickMouseAreaCall7)(const void *, QHoverEvent *, int *);
typedef void (*CuteQQuickMouseAreaCall8)(const void *, QHoverEvent *, int *);
#if QT_CONFIG(wheelevent)
typedef void (*CuteQQuickMouseAreaCall9)(const void *, QWheelEvent *, int *);
#endif  // QT_CONFIG(wheelevent)
typedef bool (*CuteQQuickMouseAreaCall10)(const void *, QQuickItem *, QEvent *, int *);
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickMouseAreaCall11)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickMouseAreaCall12)(const void *, const QRectF *, const QRectF *, int *);
typedef void (*CuteQQuickMouseAreaCall13)(const void *, int, const QQuickItem::ItemChangeData *, int *);
typedef void * (*CuteQQuickMouseAreaCall14)(const void *, QSGNode *, QQuickItem::UpdatePaintNodeData *, int *);
typedef const QRectF * (*CuteQQuickMouseAreaCall15)(const void *, int *);
typedef const QRectF * (*CuteQQuickMouseAreaCall16)(const void *, int *);
typedef bool (*CuteQQuickMouseAreaCall17)(const void *, const QPointF *, int *);
#if QT_CONFIG(im)
typedef const QVariant * (*CuteQQuickMouseAreaCall18)(const void *, int, int *);
#endif  // QT_CONFIG(im)
typedef bool (*CuteQQuickMouseAreaCall19)(const void *, int *);
typedef void * (*CuteQQuickMouseAreaCall20)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickMouseAreaCall21)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickMouseAreaCall22)(const void *, int *);
typedef void (*CuteQQuickMouseAreaCall23)(const void *, int *);
typedef void (*CuteQQuickMouseAreaCall24)(const void *, QKeyEvent *, int *);
typedef void (*CuteQQuickMouseAreaCall25)(const void *, QKeyEvent *, int *);
#if QT_CONFIG(im)
typedef void (*CuteQQuickMouseAreaCall26)(const void *, QInputMethodEvent *, int *);
#endif  // QT_CONFIG(im)
typedef void (*CuteQQuickMouseAreaCall27)(const void *, QFocusEvent *, int *);
typedef void (*CuteQQuickMouseAreaCall28)(const void *, QFocusEvent *, int *);
typedef void (*CuteQQuickMouseAreaCall29)(const void *, QTouchEvent *, int *);
#if QT_CONFIG(quick_draganddrop)
typedef void (*CuteQQuickMouseAreaCall30)(const void *, QDragEnterEvent *, int *);
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
typedef void (*CuteQQuickMouseAreaCall31)(const void *, QDragMoveEvent *, int *);
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
typedef void (*CuteQQuickMouseAreaCall32)(const void *, QDragLeaveEvent *, int *);
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
typedef void (*CuteQQuickMouseAreaCall33)(const void *, QDropEvent *, int *);
#endif  // QT_CONFIG(quick_draganddrop)
typedef void (*CuteQQuickMouseAreaCall34)(const void *, int *);
typedef void (*CuteQQuickMouseAreaCall35)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickMouseAreaCall36)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickMouseAreaCall37)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickMouseAreaCall38)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickMouseAreaCall39)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickMouseAreaCall40)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQQuickMouseArea : public QQuickMouseArea {
public:
  using QQuickMouseArea::QQuickMouseArea;
  void *taken[41] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN10QQuickItem15mousePressEventEP11QMouseEvent")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem17mouseReleaseEventEP11QMouseEvent")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem21mouseDoubleClickEventEP11QMouseEvent")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem14mouseMoveEventEP11QMouseEvent")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem16mouseUngrabEventEv")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem16touchUngrabEventEv")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem15hoverEnterEventEP11QHoverEvent")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem14hoverMoveEventEP11QHoverEvent")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem15hoverLeaveEventEP11QHoverEvent")) {
      taken[8] = call;
      return true;
    }
#if QT_CONFIG(wheelevent)
    if (!std::strcmp(key, "_ZN10QQuickItem10wheelEventEP11QWheelEvent")) {
      taken[9] = call;
      return true;
    }
#endif  // QT_CONFIG(wheelevent)
    if (!std::strcmp(key, "_ZN10QQuickItem21childMouseEventFilterEPS_P6QEvent")) {
      taken[10] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[11] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN10QQuickItem14geometryChangeERK6QRectFS2_")) {
      taken[12] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem10itemChangeENS_10ItemChangeERKNS_14ItemChangeDataE")) {
      taken[13] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem15updatePaintNodeEP7QSGNodePNS_19UpdatePaintNodeDataE")) {
      taken[14] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK10QQuickItem12boundingRectEv")) {
      taken[15] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK10QQuickItem8clipRectEv")) {
      taken[16] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK10QQuickItem8containsERK7QPointF")) {
      taken[17] = call;
      return true;
    }
#if QT_CONFIG(im)
    if (!std::strcmp(key, "_ZNK10QQuickItem16inputMethodQueryEN2Qt16InputMethodQueryE")) {
      taken[18] = call;
      return true;
    }
#endif  // QT_CONFIG(im)
    if (!std::strcmp(key, "_ZNK10QQuickItem17isTextureProviderEv")) {
      taken[19] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK10QQuickItem15textureProviderEv")) {
      taken[20] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[21] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN16QQmlParserStatus10classBeginEv")) {
      taken[22] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQmlParserStatus17componentCompleteEv")) {
      taken[23] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem13keyPressEventEP9QKeyEvent")) {
      taken[24] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem15keyReleaseEventEP9QKeyEvent")) {
      taken[25] = call;
      return true;
    }
#if QT_CONFIG(im)
    if (!std::strcmp(key, "_ZN10QQuickItem16inputMethodEventEP17QInputMethodEvent")) {
      taken[26] = call;
      return true;
    }
#endif  // QT_CONFIG(im)
    if (!std::strcmp(key, "_ZN10QQuickItem12focusInEventEP11QFocusEvent")) {
      taken[27] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem13focusOutEventEP11QFocusEvent")) {
      taken[28] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem10touchEventEP11QTouchEvent")) {
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
    if (!std::strcmp(key, "_ZN10QQuickItem16releaseResourcesEv")) {
      taken[34] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem12updatePolishEv")) {
      taken[35] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
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

  //  void QQuickMouseArea::mousePressEvent(QMouseEvent *event)
  void mousePressEvent(QMouseEvent *event) override {
    if (taken[0]) {
      int handled = 0;
      CuteQQuickMouseAreaCall0 call = reinterpret_cast<CuteQQuickMouseAreaCall0>(taken[0]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickMouseArea::mousePressEvent(event);
  }

  //  void QQuickMouseArea::mouseReleaseEvent(QMouseEvent *event)
  void mouseReleaseEvent(QMouseEvent *event) override {
    if (taken[1]) {
      int handled = 0;
      CuteQQuickMouseAreaCall1 call = reinterpret_cast<CuteQQuickMouseAreaCall1>(taken[1]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickMouseArea::mouseReleaseEvent(event);
  }

  //  void QQuickMouseArea::mouseDoubleClickEvent(QMouseEvent *event)
  void mouseDoubleClickEvent(QMouseEvent *event) override {
    if (taken[2]) {
      int handled = 0;
      CuteQQuickMouseAreaCall2 call = reinterpret_cast<CuteQQuickMouseAreaCall2>(taken[2]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickMouseArea::mouseDoubleClickEvent(event);
  }

  //  void QQuickMouseArea::mouseMoveEvent(QMouseEvent *event)
  void mouseMoveEvent(QMouseEvent *event) override {
    if (taken[3]) {
      int handled = 0;
      CuteQQuickMouseAreaCall3 call = reinterpret_cast<CuteQQuickMouseAreaCall3>(taken[3]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickMouseArea::mouseMoveEvent(event);
  }

  //  void QQuickMouseArea::mouseUngrabEvent()
  void mouseUngrabEvent() override {
    if (taken[4]) {
      int handled = 0;
      CuteQQuickMouseAreaCall4 call = reinterpret_cast<CuteQQuickMouseAreaCall4>(taken[4]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickMouseArea::mouseUngrabEvent();
  }

  //  void QQuickMouseArea::touchUngrabEvent()
  void touchUngrabEvent() override {
    if (taken[5]) {
      int handled = 0;
      CuteQQuickMouseAreaCall5 call = reinterpret_cast<CuteQQuickMouseAreaCall5>(taken[5]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickMouseArea::touchUngrabEvent();
  }

  //  void QQuickMouseArea::hoverEnterEvent(QHoverEvent *event)
  void hoverEnterEvent(QHoverEvent *event) override {
    if (taken[6]) {
      int handled = 0;
      CuteQQuickMouseAreaCall6 call = reinterpret_cast<CuteQQuickMouseAreaCall6>(taken[6]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickMouseArea::hoverEnterEvent(event);
  }

  //  void QQuickMouseArea::hoverMoveEvent(QHoverEvent *event)
  void hoverMoveEvent(QHoverEvent *event) override {
    if (taken[7]) {
      int handled = 0;
      CuteQQuickMouseAreaCall7 call = reinterpret_cast<CuteQQuickMouseAreaCall7>(taken[7]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickMouseArea::hoverMoveEvent(event);
  }

  //  void QQuickMouseArea::hoverLeaveEvent(QHoverEvent *event)
  void hoverLeaveEvent(QHoverEvent *event) override {
    if (taken[8]) {
      int handled = 0;
      CuteQQuickMouseAreaCall8 call = reinterpret_cast<CuteQQuickMouseAreaCall8>(taken[8]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickMouseArea::hoverLeaveEvent(event);
  }

#if QT_CONFIG(wheelevent)
  //  void QQuickMouseArea::wheelEvent(QWheelEvent *event)
  void wheelEvent(QWheelEvent *event) override {
    if (taken[9]) {
      int handled = 0;
      CuteQQuickMouseAreaCall9 call = reinterpret_cast<CuteQQuickMouseAreaCall9>(taken[9]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickMouseArea::wheelEvent(event);
  }
#endif  // QT_CONFIG(wheelevent)

  //  bool QQuickMouseArea::childMouseEventFilter(QQuickItem *i, QEvent *e)
  bool childMouseEventFilter(QQuickItem *i, QEvent *e) override {
    if (taken[10]) {
      int handled = 0;
      CuteQQuickMouseAreaCall10 call = reinterpret_cast<CuteQQuickMouseAreaCall10>(taken[10]);
      bool given = call(this, i, e, &handled);
      if (handled) return given;
    }
    return QQuickMouseArea::childMouseEventFilter(i, e);
  }

#if !defined(QT_NO_QOBJECT)
  //  void QQuickMouseArea::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[11]) {
      int handled = 0;
      CuteQQuickMouseAreaCall11 call = reinterpret_cast<CuteQQuickMouseAreaCall11>(taken[11]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickMouseArea::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

  //  void QQuickMouseArea::geometryChange(const QRectF &newGeometry, const
  //      QRectF &oldGeometry)
  void geometryChange(
      const QRectF &newGeometry,
      const QRectF &oldGeometry) override {
    if (taken[12]) {
      int handled = 0;
      CuteQQuickMouseAreaCall12 call = reinterpret_cast<CuteQQuickMouseAreaCall12>(taken[12]);
      call(this, &newGeometry, &oldGeometry, &handled);
      if (handled) return;
    }
    QQuickMouseArea::geometryChange(newGeometry, oldGeometry);
  }

  //  void QQuickMouseArea::itemChange(ItemChange change, const
  //      ItemChangeData &value)
  void itemChange(
      QQuickItem::ItemChange change,
      const QQuickItem::ItemChangeData &value) override {
    if (taken[13]) {
      int handled = 0;
      CuteQQuickMouseAreaCall13 call = reinterpret_cast<CuteQQuickMouseAreaCall13>(taken[13]);
      call(this, static_cast<int>(change), &value, &handled);
      if (handled) return;
    }
    QQuickMouseArea::itemChange(change, value);
  }

  //  QSGNode *QQuickMouseArea::updatePaintNode(QSGNode *a0,
  //      UpdatePaintNodeData *a1)
  QSGNode *updatePaintNode(
      QSGNode *a0,
      QQuickItem::UpdatePaintNodeData *a1) override {
    if (taken[14]) {
      int handled = 0;
      CuteQQuickMouseAreaCall14 call = reinterpret_cast<CuteQQuickMouseAreaCall14>(taken[14]);
      void * given = call(this, a0, a1, &handled);
      if (handled) return static_cast<QSGNode *>(given);
    }
    return QQuickMouseArea::updatePaintNode(a0, a1);
  }

  //  QRectF QQuickItem::boundingRect() const
  QRectF boundingRect() const override {
    if (taken[15]) {
      int handled = 0;
      CuteQQuickMouseAreaCall15 call = reinterpret_cast<CuteQQuickMouseAreaCall15>(taken[15]);
      const QRectF * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QQuickItem::boundingRect();
  }

  //  QRectF QQuickItem::clipRect() const
  QRectF clipRect() const override {
    if (taken[16]) {
      int handled = 0;
      CuteQQuickMouseAreaCall16 call = reinterpret_cast<CuteQQuickMouseAreaCall16>(taken[16]);
      const QRectF * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QQuickItem::clipRect();
  }

  //  bool QQuickItem::contains(const QPointF &point) const
  bool contains(const QPointF &point) const override {
    if (taken[17]) {
      int handled = 0;
      CuteQQuickMouseAreaCall17 call = reinterpret_cast<CuteQQuickMouseAreaCall17>(taken[17]);
      bool given = call(this, &point, &handled);
      if (handled) return given;
    }
    return QQuickItem::contains(point);
  }

#if QT_CONFIG(im)
  //  QVariant QQuickItem::inputMethodQuery(Qt::InputMethodQuery query)
  //      const
  QVariant inputMethodQuery(Qt::InputMethodQuery query) const override {
    if (taken[18]) {
      int handled = 0;
      CuteQQuickMouseAreaCall18 call = reinterpret_cast<CuteQQuickMouseAreaCall18>(taken[18]);
      const QVariant * given = call(this, static_cast<int>(query), &handled);
      if (handled && given) return *given;
    }
    return QQuickItem::inputMethodQuery(query);
  }
#endif  // QT_CONFIG(im)

  //  bool QQuickItem::isTextureProvider() const
  bool isTextureProvider() const override {
    if (taken[19]) {
      int handled = 0;
      CuteQQuickMouseAreaCall19 call = reinterpret_cast<CuteQQuickMouseAreaCall19>(taken[19]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QQuickItem::isTextureProvider();
  }

  //  QSGTextureProvider *QQuickItem::textureProvider() const
  QSGTextureProvider *textureProvider() const override {
    if (taken[20]) {
      int handled = 0;
      CuteQQuickMouseAreaCall20 call = reinterpret_cast<CuteQQuickMouseAreaCall20>(taken[20]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QSGTextureProvider *>(given);
    }
    return QQuickItem::textureProvider();
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QQuickItem::event(QEvent *a0)
  bool event(QEvent *a0) override {
    if (taken[21]) {
      int handled = 0;
      CuteQQuickMouseAreaCall21 call = reinterpret_cast<CuteQQuickMouseAreaCall21>(taken[21]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQuickItem::event(a0);
  }
#endif  // !defined(QT_NO_QOBJECT)

  //  void QQuickItem::classBegin()
  void classBegin() override {
    if (taken[22]) {
      int handled = 0;
      CuteQQuickMouseAreaCall22 call = reinterpret_cast<CuteQQuickMouseAreaCall22>(taken[22]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItem::classBegin();
  }

  //  void QQuickItem::componentComplete()
  void componentComplete() override {
    if (taken[23]) {
      int handled = 0;
      CuteQQuickMouseAreaCall23 call = reinterpret_cast<CuteQQuickMouseAreaCall23>(taken[23]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItem::componentComplete();
  }

  //  void QQuickItem::keyPressEvent(QKeyEvent *event)
  void keyPressEvent(QKeyEvent *event) override {
    if (taken[24]) {
      int handled = 0;
      CuteQQuickMouseAreaCall24 call = reinterpret_cast<CuteQQuickMouseAreaCall24>(taken[24]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::keyPressEvent(event);
  }

  //  void QQuickItem::keyReleaseEvent(QKeyEvent *event)
  void keyReleaseEvent(QKeyEvent *event) override {
    if (taken[25]) {
      int handled = 0;
      CuteQQuickMouseAreaCall25 call = reinterpret_cast<CuteQQuickMouseAreaCall25>(taken[25]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::keyReleaseEvent(event);
  }

#if QT_CONFIG(im)
  //  void QQuickItem::inputMethodEvent(QInputMethodEvent *a0)
  void inputMethodEvent(QInputMethodEvent *a0) override {
    if (taken[26]) {
      int handled = 0;
      CuteQQuickMouseAreaCall26 call = reinterpret_cast<CuteQQuickMouseAreaCall26>(taken[26]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItem::inputMethodEvent(a0);
  }
#endif  // QT_CONFIG(im)

  //  void QQuickItem::focusInEvent(QFocusEvent *a0)
  void focusInEvent(QFocusEvent *a0) override {
    if (taken[27]) {
      int handled = 0;
      CuteQQuickMouseAreaCall27 call = reinterpret_cast<CuteQQuickMouseAreaCall27>(taken[27]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItem::focusInEvent(a0);
  }

  //  void QQuickItem::focusOutEvent(QFocusEvent *a0)
  void focusOutEvent(QFocusEvent *a0) override {
    if (taken[28]) {
      int handled = 0;
      CuteQQuickMouseAreaCall28 call = reinterpret_cast<CuteQQuickMouseAreaCall28>(taken[28]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItem::focusOutEvent(a0);
  }

  //  void QQuickItem::touchEvent(QTouchEvent *event)
  void touchEvent(QTouchEvent *event) override {
    if (taken[29]) {
      int handled = 0;
      CuteQQuickMouseAreaCall29 call = reinterpret_cast<CuteQQuickMouseAreaCall29>(taken[29]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::touchEvent(event);
  }

#if QT_CONFIG(quick_draganddrop)
  //  void QQuickItem::dragEnterEvent(QDragEnterEvent *a0)
  void dragEnterEvent(QDragEnterEvent *a0) override {
    if (taken[30]) {
      int handled = 0;
      CuteQQuickMouseAreaCall30 call = reinterpret_cast<CuteQQuickMouseAreaCall30>(taken[30]);
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
      CuteQQuickMouseAreaCall31 call = reinterpret_cast<CuteQQuickMouseAreaCall31>(taken[31]);
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
      CuteQQuickMouseAreaCall32 call = reinterpret_cast<CuteQQuickMouseAreaCall32>(taken[32]);
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
      CuteQQuickMouseAreaCall33 call = reinterpret_cast<CuteQQuickMouseAreaCall33>(taken[33]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItem::dropEvent(a0);
  }
#endif  // QT_CONFIG(quick_draganddrop)

  //  void QQuickItem::releaseResources()
  void releaseResources() override {
    if (taken[34]) {
      int handled = 0;
      CuteQQuickMouseAreaCall34 call = reinterpret_cast<CuteQQuickMouseAreaCall34>(taken[34]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItem::releaseResources();
  }

  //  void QQuickItem::updatePolish()
  void updatePolish() override {
    if (taken[35]) {
      int handled = 0;
      CuteQQuickMouseAreaCall35 call = reinterpret_cast<CuteQQuickMouseAreaCall35>(taken[35]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItem::updatePolish();
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[36]) {
      int handled = 0;
      CuteQQuickMouseAreaCall36 call = reinterpret_cast<CuteQQuickMouseAreaCall36>(taken[36]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[37]) {
      int handled = 0;
      CuteQQuickMouseAreaCall37 call = reinterpret_cast<CuteQQuickMouseAreaCall37>(taken[37]);
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
      CuteQQuickMouseAreaCall38 call = reinterpret_cast<CuteQQuickMouseAreaCall38>(taken[38]);
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
      CuteQQuickMouseAreaCall39 call = reinterpret_cast<CuteQQuickMouseAreaCall39>(taken[39]);
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
      CuteQQuickMouseAreaCall40 call = reinterpret_cast<CuteQQuickMouseAreaCall40>(taken[40]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QQuickMouseArea::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK15QQuickMouseArea10metaObjectEv(
    const QQuickMouseArea *self) {
  return self->metaObject();
}

//  QString QQuickMouseArea::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN15QQuickMouseArea2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuickMouseArea::tr(s, c, n));
}

//  QQuickMouseArea::QQuickMouseArea(QQuickItem *parent)
extern "C" Q_DECL_EXPORT
QQuickMouseArea *ritual_ZN15QQuickMouseAreaC1EP10QQuickItem(
    QQuickItem *parent) {
  return new CuteQQuickMouseArea(parent);
}

//  QQuickMouseArea::~QQuickMouseArea()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickMouseAreaD1Ev(QQuickMouseArea *self) {
  delete self;
}

//  qreal QQuickMouseArea::mouseX() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK15QQuickMouseArea6mouseXEv(const QQuickMouseArea *self) {
  return self->mouseX();
}

//  qreal QQuickMouseArea::mouseY() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK15QQuickMouseArea6mouseYEv(const QQuickMouseArea *self) {
  return self->mouseY();
}

//  bool QQuickMouseArea::isEnabled() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK15QQuickMouseArea9isEnabledEv(const QQuickMouseArea *self) {
  return self->isEnabled();
}

//  void QQuickMouseArea::setEnabled(bool a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickMouseArea10setEnabledEb(
    QQuickMouseArea *self,
    bool a0) {
  self->setEnabled(a0);
}

//  bool QQuickMouseArea::isScrollGestureEnabled() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK15QQuickMouseArea22isScrollGestureEnabledEv(
    const QQuickMouseArea *self) {
  return self->isScrollGestureEnabled();
}

//  void QQuickMouseArea::setScrollGestureEnabled(bool a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickMouseArea23setScrollGestureEnabledEb(
    QQuickMouseArea *self,
    bool a0) {
  self->setScrollGestureEnabled(a0);
}

//  bool QQuickMouseArea::hovered() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK15QQuickMouseArea7hoveredEv(const QQuickMouseArea *self) {
  return self->hovered();
}

//  bool QQuickMouseArea::isPressed() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK15QQuickMouseArea9isPressedEv(const QQuickMouseArea *self) {
  return self->isPressed();
}

//  bool QQuickMouseArea::containsPress() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK15QQuickMouseArea13containsPressEv(
    const QQuickMouseArea *self) {
  return self->containsPress();
}

//  Qt::MouseButtons QQuickMouseArea::pressedButtons() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK15QQuickMouseArea14pressedButtonsEv(
    const QQuickMouseArea *self) {
  return static_cast<int>(self->pressedButtons().toInt());
}

//  Qt::MouseButtons QQuickMouseArea::acceptedButtons() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK15QQuickMouseArea15acceptedButtonsEv(
    const QQuickMouseArea *self) {
  return static_cast<int>(self->acceptedButtons().toInt());
}

//  void QQuickMouseArea::setAcceptedButtons(Qt::MouseButtons buttons)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickMouseArea18setAcceptedButtonsE6QFlagsIN2Qt11MouseButtonEE(
    QQuickMouseArea *self,
    int buttons) {
  self->setAcceptedButtons(QFlags<Qt::MouseButton>::fromInt(buttons));
}

//  bool QQuickMouseArea::hoverEnabled() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK15QQuickMouseArea12hoverEnabledEv(
    const QQuickMouseArea *self) {
  return self->hoverEnabled();
}

//  void QQuickMouseArea::setHoverEnabled(bool h)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickMouseArea15setHoverEnabledEb(
    QQuickMouseArea *self,
    bool h) {
  self->setHoverEnabled(h);
}

#if QT_CONFIG(quick_draganddrop)
//  QQuickDrag *QQuickMouseArea::drag()
extern "C" Q_DECL_EXPORT
QQuickDrag *ritual_ZN15QQuickMouseArea4dragEv(QQuickMouseArea *self) {
  return self->drag();
}
#endif  // QT_CONFIG(quick_draganddrop)

//  bool QQuickMouseArea::preventStealing() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK15QQuickMouseArea15preventStealingEv(
    const QQuickMouseArea *self) {
  return self->preventStealing();
}

//  void QQuickMouseArea::setPreventStealing(bool prevent)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickMouseArea18setPreventStealingEb(
    QQuickMouseArea *self,
    bool prevent) {
  self->setPreventStealing(prevent);
}

//  bool QQuickMouseArea::propagateComposedEvents() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK15QQuickMouseArea23propagateComposedEventsEv(
    const QQuickMouseArea *self) {
  return self->propagateComposedEvents();
}

//  void QQuickMouseArea::setPropagateComposedEvents(bool propagate)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickMouseArea26setPropagateComposedEventsEb(
    QQuickMouseArea *self,
    bool propagate) {
  self->setPropagateComposedEvents(propagate);
}

#if QT_CONFIG(cursor)
//  Qt::CursorShape QQuickMouseArea::cursorShape() const
extern "C" Q_DECL_EXPORT
Qt::CursorShape ritual_ZNK15QQuickMouseArea11cursorShapeEv(
    const QQuickMouseArea *self) {
  return self->cursorShape();
}
#endif  // QT_CONFIG(cursor)

#if QT_CONFIG(cursor)
//  void QQuickMouseArea::setCursorShape(Qt::CursorShape shape)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickMouseArea14setCursorShapeEN2Qt11CursorShapeE(
    QQuickMouseArea *self,
    Qt::CursorShape shape) {
  self->setCursorShape(shape);
}
#endif  // QT_CONFIG(cursor)

//  int QQuickMouseArea::pressAndHoldInterval() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK15QQuickMouseArea20pressAndHoldIntervalEv(
    const QQuickMouseArea *self) {
  return self->pressAndHoldInterval();
}

//  void QQuickMouseArea::setPressAndHoldInterval(int interval)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickMouseArea23setPressAndHoldIntervalEi(
    QQuickMouseArea *self,
    int interval) {
  self->setPressAndHoldInterval(interval);
}

//  void QQuickMouseArea::resetPressAndHoldInterval()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickMouseArea25resetPressAndHoldIntervalEv(
    QQuickMouseArea *self) {
  self->resetPressAndHoldInterval();
}

//  void QQuickMouseArea::setHovered(bool a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickMouseArea10setHoveredEb(
    QQuickMouseArea *self,
    bool a0) {
  self->setHovered(a0);
}

//  bool QQuickMouseArea::setPressed(Qt::MouseButton button, bool p,
//      Qt::MouseEventSource source)
extern "C" Q_DECL_EXPORT
bool ritual_ZN15QQuickMouseArea10setPressedEN2Qt11MouseButtonEbNS0_16MouseEventSourceE(
    QQuickMouseArea *self,
    Qt::MouseButton button,
    bool p,
    Qt::MouseEventSource source) {
  return self->setPressed(button, p, source);
}

//  bool QQuickMouseArea::sendMouseEvent(QMouseEvent *event)
extern "C" Q_DECL_EXPORT
bool ritual_ZN15QQuickMouseArea14sendMouseEventEP11QMouseEvent(
    QQuickMouseArea *self,
    QMouseEvent *event) {
  return self->sendMouseEvent(event);
}

//  void QQuickMouseArea::mousePressEvent(QMouseEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickMouseArea15mousePressEventEP11QMouseEvent(
    QQuickMouseArea *self,
    QMouseEvent *event) {
  self->mousePressEvent(event);
}

//  void QQuickMouseArea::mouseReleaseEvent(QMouseEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickMouseArea17mouseReleaseEventEP11QMouseEvent(
    QQuickMouseArea *self,
    QMouseEvent *event) {
  self->mouseReleaseEvent(event);
}

//  void QQuickMouseArea::mouseDoubleClickEvent(QMouseEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickMouseArea21mouseDoubleClickEventEP11QMouseEvent(
    QQuickMouseArea *self,
    QMouseEvent *event) {
  self->mouseDoubleClickEvent(event);
}

//  void QQuickMouseArea::mouseMoveEvent(QMouseEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickMouseArea14mouseMoveEventEP11QMouseEvent(
    QQuickMouseArea *self,
    QMouseEvent *event) {
  self->mouseMoveEvent(event);
}

//  void QQuickMouseArea::mouseUngrabEvent()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickMouseArea16mouseUngrabEventEv(QQuickMouseArea *self) {
  self->mouseUngrabEvent();
}

//  void QQuickMouseArea::touchUngrabEvent()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickMouseArea16touchUngrabEventEv(QQuickMouseArea *self) {
  self->touchUngrabEvent();
}

//  void QQuickMouseArea::hoverEnterEvent(QHoverEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickMouseArea15hoverEnterEventEP11QHoverEvent(
    QQuickMouseArea *self,
    QHoverEvent *event) {
  self->hoverEnterEvent(event);
}

//  void QQuickMouseArea::hoverMoveEvent(QHoverEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickMouseArea14hoverMoveEventEP11QHoverEvent(
    QQuickMouseArea *self,
    QHoverEvent *event) {
  self->hoverMoveEvent(event);
}

//  void QQuickMouseArea::hoverLeaveEvent(QHoverEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickMouseArea15hoverLeaveEventEP11QHoverEvent(
    QQuickMouseArea *self,
    QHoverEvent *event) {
  self->hoverLeaveEvent(event);
}

#if QT_CONFIG(wheelevent)
//  void QQuickMouseArea::wheelEvent(QWheelEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickMouseArea10wheelEventEP11QWheelEvent(
    QQuickMouseArea *self,
    QWheelEvent *event) {
  self->wheelEvent(event);
}
#endif  // QT_CONFIG(wheelevent)

//  bool QQuickMouseArea::childMouseEventFilter(QQuickItem *i, QEvent *e)
extern "C" Q_DECL_EXPORT
bool ritual_ZN15QQuickMouseArea21childMouseEventFilterEP10QQuickItemP6QEvent(
    QQuickMouseArea *self,
    QQuickItem *i,
    QEvent *e) {
  return self->childMouseEventFilter(i, e);
}

//  void QQuickMouseArea::timerEvent(QTimerEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickMouseArea10timerEventEP11QTimerEvent(
    QQuickMouseArea *self,
    QTimerEvent *event) {
  self->timerEvent(event);
}

//  void QQuickMouseArea::geometryChange(const QRectF &newGeometry, const
//      QRectF &oldGeometry)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickMouseArea14geometryChangeERK6QRectFS2_(
    QQuickMouseArea *self,
    const QRectF *newGeometry,
    const QRectF *oldGeometry) {
  self->geometryChange(*newGeometry, *oldGeometry);
}

//  void QQuickMouseArea::itemChange(ItemChange change, const ItemChangeData
//      &value)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickMouseArea10itemChangeEN10QQuickItem10ItemChangeERKNS0_14ItemChangeDataE(
    QQuickMouseArea *self,
    QQuickItem::ItemChange change,
    const QQuickItem::ItemChangeData *value) {
  self->itemChange(change, *value);
}

//  QSGNode *QQuickMouseArea::updatePaintNode(QSGNode *a0,
//      UpdatePaintNodeData *a1)
extern "C" Q_DECL_EXPORT
QSGNode *ritual_ZN15QQuickMouseArea15updatePaintNodeEP7QSGNodePN10QQuickItem19UpdatePaintNodeDataE(
    QQuickMouseArea *self,
    QSGNode *a0,
    QQuickItem::UpdatePaintNodeData *a1) {
  return self->updatePaintNode(a0, a1);
}

//  void QQuickMouseArea::ungrabMouse()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickMouseArea11ungrabMouseEv(QQuickMouseArea *self) {
  self->ungrabMouse();
}

//  QQuickMouseAreaPrivate *QQuickMouseArea::d_func()
extern "C" Q_DECL_EXPORT
QQuickMouseAreaPrivate *ritual_ZN15QQuickMouseArea6d_funcEv(
    QQuickMouseArea *self) {
  return self->d_func();
}

//  const QQuickMouseAreaPrivate *QQuickMouseArea::d_func() const
extern "C" Q_DECL_EXPORT
const QQuickMouseAreaPrivate *ritual_ZNK15QQuickMouseArea6d_funcEv(
    const QQuickMouseArea *self) {
  return self->d_func();
}

//  a Python function taken by a CuteQQuickMouseArea, for the function named
//      by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQuickMouseArea(
    QQuickMouseArea *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQuickMouseArea *>(self)->take(key, call);
}

//  void QQuickMouseArea::mousePressEvent(QMouseEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN15QQuickMouseArea15mousePressEventEP11QMouseEvent(
    QQuickMouseArea *self,
    QMouseEvent *event) {
  static_cast<OwnQQuickMouseArea *>(self)->OwnQQuickMouseArea::mousePressEvent(
      event);
}

//  void QQuickMouseArea::mouseReleaseEvent(QMouseEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN15QQuickMouseArea17mouseReleaseEventEP11QMouseEvent(
    QQuickMouseArea *self,
    QMouseEvent *event) {
  static_cast<OwnQQuickMouseArea *>(self)->OwnQQuickMouseArea::mouseReleaseEvent(
      event);
}

//  void QQuickMouseArea::mouseDoubleClickEvent(QMouseEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN15QQuickMouseArea21mouseDoubleClickEventEP11QMouseEvent(
    QQuickMouseArea *self,
    QMouseEvent *event) {
  static_cast<OwnQQuickMouseArea *>(self)->OwnQQuickMouseArea::mouseDoubleClickEvent(
      event);
}

//  void QQuickMouseArea::mouseMoveEvent(QMouseEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN15QQuickMouseArea14mouseMoveEventEP11QMouseEvent(
    QQuickMouseArea *self,
    QMouseEvent *event) {
  static_cast<OwnQQuickMouseArea *>(self)->OwnQQuickMouseArea::mouseMoveEvent(
      event);
}

//  void QQuickMouseArea::mouseUngrabEvent()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN15QQuickMouseArea16mouseUngrabEventEv(
    QQuickMouseArea *self) {
  static_cast<OwnQQuickMouseArea *>(self)->OwnQQuickMouseArea::mouseUngrabEvent();
}

//  void QQuickMouseArea::touchUngrabEvent()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN15QQuickMouseArea16touchUngrabEventEv(
    QQuickMouseArea *self) {
  static_cast<OwnQQuickMouseArea *>(self)->OwnQQuickMouseArea::touchUngrabEvent();
}

//  void QQuickMouseArea::hoverEnterEvent(QHoverEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN15QQuickMouseArea15hoverEnterEventEP11QHoverEvent(
    QQuickMouseArea *self,
    QHoverEvent *event) {
  static_cast<OwnQQuickMouseArea *>(self)->OwnQQuickMouseArea::hoverEnterEvent(
      event);
}

//  void QQuickMouseArea::hoverMoveEvent(QHoverEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN15QQuickMouseArea14hoverMoveEventEP11QHoverEvent(
    QQuickMouseArea *self,
    QHoverEvent *event) {
  static_cast<OwnQQuickMouseArea *>(self)->OwnQQuickMouseArea::hoverMoveEvent(
      event);
}

//  void QQuickMouseArea::hoverLeaveEvent(QHoverEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN15QQuickMouseArea15hoverLeaveEventEP11QHoverEvent(
    QQuickMouseArea *self,
    QHoverEvent *event) {
  static_cast<OwnQQuickMouseArea *>(self)->OwnQQuickMouseArea::hoverLeaveEvent(
      event);
}

#if QT_CONFIG(wheelevent)
//  void QQuickMouseArea::wheelEvent(QWheelEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN15QQuickMouseArea10wheelEventEP11QWheelEvent(
    QQuickMouseArea *self,
    QWheelEvent *event) {
  static_cast<OwnQQuickMouseArea *>(self)->OwnQQuickMouseArea::wheelEvent(
      event);
}
#endif  // QT_CONFIG(wheelevent)

//  bool QQuickMouseArea::childMouseEventFilter(QQuickItem *i, QEvent *e)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN15QQuickMouseArea21childMouseEventFilterEP10QQuickItemP6QEvent(
    QQuickMouseArea *self,
    QQuickItem *i,
    QEvent *e) {
  return static_cast<OwnQQuickMouseArea *>(self)->OwnQQuickMouseArea::childMouseEventFilter(
      i,
      e);
}

//  void QQuickMouseArea::timerEvent(QTimerEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN15QQuickMouseArea10timerEventEP11QTimerEvent(
    QQuickMouseArea *self,
    QTimerEvent *event) {
  static_cast<OwnQQuickMouseArea *>(self)->OwnQQuickMouseArea::timerEvent(
      event);
}

//  void QQuickMouseArea::geometryChange(const QRectF &newGeometry, const
//      QRectF &oldGeometry)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN15QQuickMouseArea14geometryChangeERK6QRectFS2_(
    QQuickMouseArea *self,
    const QRectF *newGeometry,
    const QRectF *oldGeometry) {
  static_cast<OwnQQuickMouseArea *>(self)->OwnQQuickMouseArea::geometryChange(
      *newGeometry,
      *oldGeometry);
}

//  void QQuickMouseArea::itemChange(ItemChange change, const ItemChangeData
//      &value)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN15QQuickMouseArea10itemChangeEN10QQuickItem10ItemChangeERKNS0_14ItemChangeDataE(
    QQuickMouseArea *self,
    QQuickItem::ItemChange change,
    const QQuickItem::ItemChangeData *value) {
  static_cast<OwnQQuickMouseArea *>(self)->OwnQQuickMouseArea::itemChange(
      change,
      *value);
}

//  QSGNode *QQuickMouseArea::updatePaintNode(QSGNode *a0,
//      UpdatePaintNodeData *a1)
extern "C" Q_DECL_EXPORT
QSGNode *ritual_own_ZN15QQuickMouseArea15updatePaintNodeEP7QSGNodePN10QQuickItem19UpdatePaintNodeDataE(
    QQuickMouseArea *self,
    QSGNode *a0,
    QQuickItem::UpdatePaintNodeData *a1) {
  return static_cast<OwnQQuickMouseArea *>(self)->OwnQQuickMouseArea::updatePaintNode(
      a0,
      a1);
}
