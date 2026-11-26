//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/6.12.0/QtQuick/private/qquickrepeater_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtGui/qtguiglobal.h>
#include <QtQuick/qtquickglobal.h>
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#if QT_CONFIG(quick_repeater)
#if QT_CONFIG(quick_repeater)
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qquickrepeater_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qvariant.h>
#include <QtQuick/qquickitem.h>
#include <QtQmlModels/QtQmlModels>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQmlModels/6.12.0/QtQmlModels/private/qqmlchangeset_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qrect.h>
#include <QtCore/qpoint.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  Only a class built on QQuickRepeater may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQQuickRepeater : QQuickRepeater {
  using QQuickRepeater::componentComplete;
  using QQuickRepeater::itemChange;
};

//  A QQuickRepeater that Python can take functions over in. Every QQuickRepeater
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if QT_CONFIG(quick_repeater)
typedef void (*CuteQQuickRepeaterCall0)(const void *, int *);
#endif  // QT_CONFIG(quick_repeater)
#if QT_CONFIG(quick_repeater)
typedef void (*CuteQQuickRepeaterCall1)(const void *, int, const QQuickItem::ItemChangeData *, int *);
#endif  // QT_CONFIG(quick_repeater)
typedef const QRectF * (*CuteQQuickRepeaterCall2)(const void *, int *);
typedef const QRectF * (*CuteQQuickRepeaterCall3)(const void *, int *);
typedef bool (*CuteQQuickRepeaterCall4)(const void *, const QPointF *, int *);
#if QT_CONFIG(im)
typedef const QVariant * (*CuteQQuickRepeaterCall5)(const void *, int, int *);
#endif  // QT_CONFIG(im)
typedef bool (*CuteQQuickRepeaterCall6)(const void *, int *);
typedef void * (*CuteQQuickRepeaterCall7)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickRepeaterCall8)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickRepeaterCall9)(const void *, const QRectF *, const QRectF *, int *);
typedef void (*CuteQQuickRepeaterCall10)(const void *, int *);
typedef void (*CuteQQuickRepeaterCall11)(const void *, QKeyEvent *, int *);
typedef void (*CuteQQuickRepeaterCall12)(const void *, QKeyEvent *, int *);
#if QT_CONFIG(im)
typedef void (*CuteQQuickRepeaterCall13)(const void *, QInputMethodEvent *, int *);
#endif  // QT_CONFIG(im)
typedef void (*CuteQQuickRepeaterCall14)(const void *, QFocusEvent *, int *);
typedef void (*CuteQQuickRepeaterCall15)(const void *, QFocusEvent *, int *);
typedef void (*CuteQQuickRepeaterCall16)(const void *, QMouseEvent *, int *);
typedef void (*CuteQQuickRepeaterCall17)(const void *, QMouseEvent *, int *);
typedef void (*CuteQQuickRepeaterCall18)(const void *, QMouseEvent *, int *);
typedef void (*CuteQQuickRepeaterCall19)(const void *, QMouseEvent *, int *);
typedef void (*CuteQQuickRepeaterCall20)(const void *, int *);
typedef void (*CuteQQuickRepeaterCall21)(const void *, int *);
#if QT_CONFIG(wheelevent)
typedef void (*CuteQQuickRepeaterCall22)(const void *, QWheelEvent *, int *);
#endif  // QT_CONFIG(wheelevent)
typedef void (*CuteQQuickRepeaterCall23)(const void *, QTouchEvent *, int *);
typedef void (*CuteQQuickRepeaterCall24)(const void *, QHoverEvent *, int *);
typedef void (*CuteQQuickRepeaterCall25)(const void *, QHoverEvent *, int *);
typedef void (*CuteQQuickRepeaterCall26)(const void *, QHoverEvent *, int *);
#if QT_CONFIG(quick_draganddrop)
typedef void (*CuteQQuickRepeaterCall27)(const void *, QDragEnterEvent *, int *);
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
typedef void (*CuteQQuickRepeaterCall28)(const void *, QDragMoveEvent *, int *);
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
typedef void (*CuteQQuickRepeaterCall29)(const void *, QDragLeaveEvent *, int *);
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
typedef void (*CuteQQuickRepeaterCall30)(const void *, QDropEvent *, int *);
#endif  // QT_CONFIG(quick_draganddrop)
typedef bool (*CuteQQuickRepeaterCall31)(const void *, QQuickItem *, QEvent *, int *);
typedef void * (*CuteQQuickRepeaterCall32)(const void *, QSGNode *, QQuickItem::UpdatePaintNodeData *, int *);
typedef void (*CuteQQuickRepeaterCall33)(const void *, int *);
typedef void (*CuteQQuickRepeaterCall34)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickRepeaterCall35)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickRepeaterCall36)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickRepeaterCall37)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickRepeaterCall38)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickRepeaterCall39)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickRepeaterCall40)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQQuickRepeater : public QQuickRepeater {
public:
  using QQuickRepeater::QQuickRepeater;
  void *taken[41] = {};

  bool take(const char *key, void *call) {
#if QT_CONFIG(quick_repeater)
    if (!std::strcmp(key, "_ZN16QQmlParserStatus17componentCompleteEv")) {
      taken[0] = call;
      return true;
    }
#endif  // QT_CONFIG(quick_repeater)
#if QT_CONFIG(quick_repeater)
    if (!std::strcmp(key, "_ZN10QQuickItem10itemChangeENS_10ItemChangeERKNS_14ItemChangeDataE")) {
      taken[1] = call;
      return true;
    }
#endif  // QT_CONFIG(quick_repeater)
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
    if (!std::strcmp(key, "_ZN10QQuickItem14geometryChangeERK6QRectFS2_")) {
      taken[9] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQmlParserStatus10classBeginEv")) {
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

#if QT_CONFIG(quick_repeater)
  //  void QQuickRepeater::componentComplete()
  void componentComplete() override {
    if (taken[0]) {
      int handled = 0;
      CuteQQuickRepeaterCall0 call = reinterpret_cast<CuteQQuickRepeaterCall0>(taken[0]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickRepeater::componentComplete();
  }
#endif  // QT_CONFIG(quick_repeater)

#if QT_CONFIG(quick_repeater)
  //  void QQuickRepeater::itemChange(ItemChange change, const
  //      ItemChangeData &value)
  void itemChange(
      QQuickItem::ItemChange change,
      const QQuickItem::ItemChangeData &value) override {
    if (taken[1]) {
      int handled = 0;
      CuteQQuickRepeaterCall1 call = reinterpret_cast<CuteQQuickRepeaterCall1>(taken[1]);
      call(this, static_cast<int>(change), &value, &handled);
      if (handled) return;
    }
    QQuickRepeater::itemChange(change, value);
  }
#endif  // QT_CONFIG(quick_repeater)

  //  QRectF QQuickItem::boundingRect() const
  QRectF boundingRect() const override {
    if (taken[2]) {
      int handled = 0;
      CuteQQuickRepeaterCall2 call = reinterpret_cast<CuteQQuickRepeaterCall2>(taken[2]);
      const QRectF * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QQuickItem::boundingRect();
  }

  //  QRectF QQuickItem::clipRect() const
  QRectF clipRect() const override {
    if (taken[3]) {
      int handled = 0;
      CuteQQuickRepeaterCall3 call = reinterpret_cast<CuteQQuickRepeaterCall3>(taken[3]);
      const QRectF * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QQuickItem::clipRect();
  }

  //  bool QQuickItem::contains(const QPointF &point) const
  bool contains(const QPointF &point) const override {
    if (taken[4]) {
      int handled = 0;
      CuteQQuickRepeaterCall4 call = reinterpret_cast<CuteQQuickRepeaterCall4>(taken[4]);
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
      CuteQQuickRepeaterCall5 call = reinterpret_cast<CuteQQuickRepeaterCall5>(taken[5]);
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
      CuteQQuickRepeaterCall6 call = reinterpret_cast<CuteQQuickRepeaterCall6>(taken[6]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QQuickItem::isTextureProvider();
  }

  //  QSGTextureProvider *QQuickItem::textureProvider() const
  QSGTextureProvider *textureProvider() const override {
    if (taken[7]) {
      int handled = 0;
      CuteQQuickRepeaterCall7 call = reinterpret_cast<CuteQQuickRepeaterCall7>(taken[7]);
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
      CuteQQuickRepeaterCall8 call = reinterpret_cast<CuteQQuickRepeaterCall8>(taken[8]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQuickItem::event(a0);
  }
#endif  // !defined(QT_NO_QOBJECT)

  //  void QQuickItem::geometryChange(const QRectF &newGeometry, const
  //      QRectF &oldGeometry)
  void geometryChange(
      const QRectF &newGeometry,
      const QRectF &oldGeometry) override {
    if (taken[9]) {
      int handled = 0;
      CuteQQuickRepeaterCall9 call = reinterpret_cast<CuteQQuickRepeaterCall9>(taken[9]);
      call(this, &newGeometry, &oldGeometry, &handled);
      if (handled) return;
    }
    QQuickItem::geometryChange(newGeometry, oldGeometry);
  }

  //  void QQuickItem::classBegin()
  void classBegin() override {
    if (taken[10]) {
      int handled = 0;
      CuteQQuickRepeaterCall10 call = reinterpret_cast<CuteQQuickRepeaterCall10>(taken[10]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItem::classBegin();
  }

  //  void QQuickItem::keyPressEvent(QKeyEvent *event)
  void keyPressEvent(QKeyEvent *event) override {
    if (taken[11]) {
      int handled = 0;
      CuteQQuickRepeaterCall11 call = reinterpret_cast<CuteQQuickRepeaterCall11>(taken[11]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::keyPressEvent(event);
  }

  //  void QQuickItem::keyReleaseEvent(QKeyEvent *event)
  void keyReleaseEvent(QKeyEvent *event) override {
    if (taken[12]) {
      int handled = 0;
      CuteQQuickRepeaterCall12 call = reinterpret_cast<CuteQQuickRepeaterCall12>(taken[12]);
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
      CuteQQuickRepeaterCall13 call = reinterpret_cast<CuteQQuickRepeaterCall13>(taken[13]);
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
      CuteQQuickRepeaterCall14 call = reinterpret_cast<CuteQQuickRepeaterCall14>(taken[14]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItem::focusInEvent(a0);
  }

  //  void QQuickItem::focusOutEvent(QFocusEvent *a0)
  void focusOutEvent(QFocusEvent *a0) override {
    if (taken[15]) {
      int handled = 0;
      CuteQQuickRepeaterCall15 call = reinterpret_cast<CuteQQuickRepeaterCall15>(taken[15]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItem::focusOutEvent(a0);
  }

  //  void QQuickItem::mousePressEvent(QMouseEvent *event)
  void mousePressEvent(QMouseEvent *event) override {
    if (taken[16]) {
      int handled = 0;
      CuteQQuickRepeaterCall16 call = reinterpret_cast<CuteQQuickRepeaterCall16>(taken[16]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::mousePressEvent(event);
  }

  //  void QQuickItem::mouseMoveEvent(QMouseEvent *event)
  void mouseMoveEvent(QMouseEvent *event) override {
    if (taken[17]) {
      int handled = 0;
      CuteQQuickRepeaterCall17 call = reinterpret_cast<CuteQQuickRepeaterCall17>(taken[17]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::mouseMoveEvent(event);
  }

  //  void QQuickItem::mouseReleaseEvent(QMouseEvent *event)
  void mouseReleaseEvent(QMouseEvent *event) override {
    if (taken[18]) {
      int handled = 0;
      CuteQQuickRepeaterCall18 call = reinterpret_cast<CuteQQuickRepeaterCall18>(taken[18]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::mouseReleaseEvent(event);
  }

  //  void QQuickItem::mouseDoubleClickEvent(QMouseEvent *event)
  void mouseDoubleClickEvent(QMouseEvent *event) override {
    if (taken[19]) {
      int handled = 0;
      CuteQQuickRepeaterCall19 call = reinterpret_cast<CuteQQuickRepeaterCall19>(taken[19]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::mouseDoubleClickEvent(event);
  }

  //  void QQuickItem::mouseUngrabEvent()
  void mouseUngrabEvent() override {
    if (taken[20]) {
      int handled = 0;
      CuteQQuickRepeaterCall20 call = reinterpret_cast<CuteQQuickRepeaterCall20>(taken[20]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItem::mouseUngrabEvent();
  }

  //  void QQuickItem::touchUngrabEvent()
  void touchUngrabEvent() override {
    if (taken[21]) {
      int handled = 0;
      CuteQQuickRepeaterCall21 call = reinterpret_cast<CuteQQuickRepeaterCall21>(taken[21]);
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
      CuteQQuickRepeaterCall22 call = reinterpret_cast<CuteQQuickRepeaterCall22>(taken[22]);
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
      CuteQQuickRepeaterCall23 call = reinterpret_cast<CuteQQuickRepeaterCall23>(taken[23]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::touchEvent(event);
  }

  //  void QQuickItem::hoverEnterEvent(QHoverEvent *event)
  void hoverEnterEvent(QHoverEvent *event) override {
    if (taken[24]) {
      int handled = 0;
      CuteQQuickRepeaterCall24 call = reinterpret_cast<CuteQQuickRepeaterCall24>(taken[24]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::hoverEnterEvent(event);
  }

  //  void QQuickItem::hoverMoveEvent(QHoverEvent *event)
  void hoverMoveEvent(QHoverEvent *event) override {
    if (taken[25]) {
      int handled = 0;
      CuteQQuickRepeaterCall25 call = reinterpret_cast<CuteQQuickRepeaterCall25>(taken[25]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::hoverMoveEvent(event);
  }

  //  void QQuickItem::hoverLeaveEvent(QHoverEvent *event)
  void hoverLeaveEvent(QHoverEvent *event) override {
    if (taken[26]) {
      int handled = 0;
      CuteQQuickRepeaterCall26 call = reinterpret_cast<CuteQQuickRepeaterCall26>(taken[26]);
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
      CuteQQuickRepeaterCall27 call = reinterpret_cast<CuteQQuickRepeaterCall27>(taken[27]);
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
      CuteQQuickRepeaterCall28 call = reinterpret_cast<CuteQQuickRepeaterCall28>(taken[28]);
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
      CuteQQuickRepeaterCall29 call = reinterpret_cast<CuteQQuickRepeaterCall29>(taken[29]);
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
      CuteQQuickRepeaterCall30 call = reinterpret_cast<CuteQQuickRepeaterCall30>(taken[30]);
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
      CuteQQuickRepeaterCall31 call = reinterpret_cast<CuteQQuickRepeaterCall31>(taken[31]);
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
      CuteQQuickRepeaterCall32 call = reinterpret_cast<CuteQQuickRepeaterCall32>(taken[32]);
      void * given = call(this, a0, a1, &handled);
      if (handled) return static_cast<QSGNode *>(given);
    }
    return QQuickItem::updatePaintNode(a0, a1);
  }

  //  void QQuickItem::releaseResources()
  void releaseResources() override {
    if (taken[33]) {
      int handled = 0;
      CuteQQuickRepeaterCall33 call = reinterpret_cast<CuteQQuickRepeaterCall33>(taken[33]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItem::releaseResources();
  }

  //  void QQuickItem::updatePolish()
  void updatePolish() override {
    if (taken[34]) {
      int handled = 0;
      CuteQQuickRepeaterCall34 call = reinterpret_cast<CuteQQuickRepeaterCall34>(taken[34]);
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
      CuteQQuickRepeaterCall35 call = reinterpret_cast<CuteQQuickRepeaterCall35>(taken[35]);
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
      CuteQQuickRepeaterCall36 call = reinterpret_cast<CuteQQuickRepeaterCall36>(taken[36]);
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
      CuteQQuickRepeaterCall37 call = reinterpret_cast<CuteQQuickRepeaterCall37>(taken[37]);
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
      CuteQQuickRepeaterCall38 call = reinterpret_cast<CuteQQuickRepeaterCall38>(taken[38]);
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
      CuteQQuickRepeaterCall39 call = reinterpret_cast<CuteQQuickRepeaterCall39>(taken[39]);
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
      CuteQQuickRepeaterCall40 call = reinterpret_cast<CuteQQuickRepeaterCall40>(taken[40]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QQuickRepeater::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK14QQuickRepeater10metaObjectEv(
    const QQuickRepeater *self) {
  return self->metaObject();
}

//  void *QQuickRepeater::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN14QQuickRepeater11qt_metacastEPKc(
    QQuickRepeater *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QQuickRepeater::qt_metacall(QMetaObject::Call a0, int a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN14QQuickRepeater11qt_metacallEN11QMetaObject4CallEiPPv(
    QQuickRepeater *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QQuickRepeater::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN14QQuickRepeater2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuickRepeater::tr(s, c, n));
}

//  QQuickRepeater::QQuickRepeater(QQuickItem *parent)
extern "C" Q_DECL_EXPORT
QQuickRepeater *ritual_ZN14QQuickRepeaterC1EP10QQuickItem(
    QQuickItem *parent) {
  return new CuteQQuickRepeater(parent);
}

//  QQuickRepeater::~QQuickRepeater()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickRepeaterD1Ev(QQuickRepeater *self) {
  delete self;
}

//  QVariant QQuickRepeater::model() const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK14QQuickRepeater5modelEv(const QQuickRepeater *self) {
  return new QVariant(self->model());
}

//  void QQuickRepeater::setModel(const QVariant &a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickRepeater8setModelERK8QVariant(
    QQuickRepeater *self,
    const QVariant *a0) {
  self->setModel(*a0);
}

//  QQmlComponent *QQuickRepeater::delegate() const
extern "C" Q_DECL_EXPORT
QQmlComponent *ritual_ZNK14QQuickRepeater8delegateEv(
    const QQuickRepeater *self) {
  return self->delegate();
}

//  void QQuickRepeater::setDelegate(QQmlComponent *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickRepeater11setDelegateEP13QQmlComponent(
    QQuickRepeater *self,
    QQmlComponent *a0) {
  self->setDelegate(a0);
}

//  int QQuickRepeater::count() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK14QQuickRepeater5countEv(const QQuickRepeater *self) {
  return self->count();
}

//  QQuickItem *QQuickRepeater::itemAt(int index) const
extern "C" Q_DECL_EXPORT
QQuickItem *ritual_ZNK14QQuickRepeater6itemAtEi(
    const QQuickRepeater *self,
    int index) {
  return self->itemAt(index);
}

//  QQmlDelegateModel::DelegateModelAccess
//      QQuickRepeater::delegateModelAccess() const
extern "C" Q_DECL_EXPORT
QQmlDelegateModel::DelegateModelAccess ritual_ZNK14QQuickRepeater19delegateModelAccessEv(
    const QQuickRepeater *self) {
  return self->delegateModelAccess();
}

//  void QQuickRepeater::setDelegateModelAccess(QQmlDelegateModel::DelegateMo
//      delAccess delegateModelAccess)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickRepeater22setDelegateModelAccessEN17QQmlDelegateModel19DelegateModelAccessE(
    QQuickRepeater *self,
    QQmlDelegateModel::DelegateModelAccess delegateModelAccess) {
  self->setDelegateModelAccess(delegateModelAccess);
}

//  void QQuickRepeater::modelChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickRepeater12modelChangedEv(QQuickRepeater *self) {
  self->modelChanged();
}

//  void QQuickRepeater::delegateChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickRepeater15delegateChangedEv(QQuickRepeater *self) {
  self->delegateChanged();
}

//  void QQuickRepeater::countChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickRepeater12countChangedEv(QQuickRepeater *self) {
  self->countChanged();
}

//  void QQuickRepeater::itemAdded(int index, QQuickItem *item)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickRepeater9itemAddedEiP10QQuickItem(
    QQuickRepeater *self,
    int index,
    QQuickItem *item) {
  self->itemAdded(index, item);
}

//  void QQuickRepeater::itemRemoved(int index, QQuickItem *item)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickRepeater11itemRemovedEiP10QQuickItem(
    QQuickRepeater *self,
    int index,
    QQuickItem *item) {
  self->itemRemoved(index, item);
}

//  void QQuickRepeater::delegateModelAccessChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickRepeater26delegateModelAccessChangedEv(
    QQuickRepeater *self) {
  self->delegateModelAccessChanged();
}

//  void QQuickRepeater::clear()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickRepeater5clearEv(QQuickRepeater *self) {
  self->clear();
}

//  void QQuickRepeater::regenerate()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickRepeater10regenerateEv(QQuickRepeater *self) {
  self->regenerate();
}

//  void QQuickRepeater::componentComplete()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickRepeater17componentCompleteEv(QQuickRepeater *self) {
  self->componentComplete();
}

//  void QQuickRepeater::itemChange(ItemChange change, const ItemChangeData
//      &value)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickRepeater10itemChangeEN10QQuickItem10ItemChangeERKNS0_14ItemChangeDataE(
    QQuickRepeater *self,
    QQuickItem::ItemChange change,
    const QQuickItem::ItemChangeData *value) {
  self->itemChange(change, *value);
}

//  void QQuickRepeater::createdItem(int index, QObject *item)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickRepeater11createdItemEiP7QObject(
    QQuickRepeater *self,
    int index,
    QObject *item) {
  self->createdItem(index, item);
}

//  void QQuickRepeater::initItem(int a0, QObject *item)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickRepeater8initItemEiP7QObject(
    QQuickRepeater *self,
    int a0,
    QObject *item) {
  self->initItem(a0, item);
}

//  void QQuickRepeater::modelUpdated(const QQmlChangeSet &changeSet, bool
//      reset)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickRepeater12modelUpdatedERK13QQmlChangeSetb(
    QQuickRepeater *self,
    const QQmlChangeSet *changeSet,
    bool reset) {
  self->modelUpdated(*changeSet, reset);
}

//  QQuickRepeaterPrivate *QQuickRepeater::d_func()
extern "C" Q_DECL_EXPORT
QQuickRepeaterPrivate *ritual_ZN14QQuickRepeater6d_funcEv(
    QQuickRepeater *self) {
  return self->d_func();
}

//  const QQuickRepeaterPrivate *QQuickRepeater::d_func() const
extern "C" Q_DECL_EXPORT
const QQuickRepeaterPrivate *ritual_ZNK14QQuickRepeater6d_funcEv(
    const QQuickRepeater *self) {
  return self->d_func();
}

//  a Python function taken by a CuteQQuickRepeater, for the function named
//      by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQuickRepeater(
    QQuickRepeater *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQuickRepeater *>(self)->take(key, call);
}

//  void QQuickRepeater::componentComplete()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN14QQuickRepeater17componentCompleteEv(
    QQuickRepeater *self) {
  static_cast<OwnQQuickRepeater *>(self)->OwnQQuickRepeater::componentComplete();
}

//  void QQuickRepeater::itemChange(ItemChange change, const ItemChangeData
//      &value)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN14QQuickRepeater10itemChangeEN10QQuickItem10ItemChangeERKNS0_14ItemChangeDataE(
    QQuickRepeater *self,
    QQuickItem::ItemChange change,
    const QQuickItem::ItemChangeData *value) {
  static_cast<OwnQQuickRepeater *>(self)->OwnQQuickRepeater::itemChange(
      change,
      *value);
}

#endif  // QT_CONFIG(quick_repeater)
#endif  // QT_CONFIG(quick_repeater)
