//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/6.12.0/QtQuick/private/qquickflipable_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtGui/qtguiglobal.h>
#include <QtQuick/qtquickglobal.h>
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#if QT_CONFIG(quick_flipable)
#if QT_CONFIG(quick_flipable)
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qquickflipable_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qrect.h>
#include <QtCore/qpoint.h>
#include <QtCore/qvariant.h>
#include <QtQuick/qquickitem.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  Only a class built on QQuickFlipable may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQQuickFlipable : QQuickFlipable {
  using QQuickFlipable::updatePolish;
};

//  A QQuickFlipable that Python can take functions over in. Every QQuickFlipable
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if QT_CONFIG(quick_flipable)
typedef void (*CuteQQuickFlipableCall0)(const void *, int *);
#endif  // QT_CONFIG(quick_flipable)
typedef const QRectF * (*CuteQQuickFlipableCall1)(const void *, int *);
typedef const QRectF * (*CuteQQuickFlipableCall2)(const void *, int *);
typedef bool (*CuteQQuickFlipableCall3)(const void *, const QPointF *, int *);
#if QT_CONFIG(im)
typedef const QVariant * (*CuteQQuickFlipableCall4)(const void *, int, int *);
#endif  // QT_CONFIG(im)
typedef bool (*CuteQQuickFlipableCall5)(const void *, int *);
typedef void * (*CuteQQuickFlipableCall6)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickFlipableCall7)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickFlipableCall8)(const void *, int, const QQuickItem::ItemChangeData *, int *);
typedef void (*CuteQQuickFlipableCall9)(const void *, const QRectF *, const QRectF *, int *);
typedef void (*CuteQQuickFlipableCall10)(const void *, int *);
typedef void (*CuteQQuickFlipableCall11)(const void *, int *);
typedef void (*CuteQQuickFlipableCall12)(const void *, QKeyEvent *, int *);
typedef void (*CuteQQuickFlipableCall13)(const void *, QKeyEvent *, int *);
#if QT_CONFIG(im)
typedef void (*CuteQQuickFlipableCall14)(const void *, QInputMethodEvent *, int *);
#endif  // QT_CONFIG(im)
typedef void (*CuteQQuickFlipableCall15)(const void *, QFocusEvent *, int *);
typedef void (*CuteQQuickFlipableCall16)(const void *, QFocusEvent *, int *);
typedef void (*CuteQQuickFlipableCall17)(const void *, QMouseEvent *, int *);
typedef void (*CuteQQuickFlipableCall18)(const void *, QMouseEvent *, int *);
typedef void (*CuteQQuickFlipableCall19)(const void *, QMouseEvent *, int *);
typedef void (*CuteQQuickFlipableCall20)(const void *, QMouseEvent *, int *);
typedef void (*CuteQQuickFlipableCall21)(const void *, int *);
typedef void (*CuteQQuickFlipableCall22)(const void *, int *);
#if QT_CONFIG(wheelevent)
typedef void (*CuteQQuickFlipableCall23)(const void *, QWheelEvent *, int *);
#endif  // QT_CONFIG(wheelevent)
typedef void (*CuteQQuickFlipableCall24)(const void *, QTouchEvent *, int *);
typedef void (*CuteQQuickFlipableCall25)(const void *, QHoverEvent *, int *);
typedef void (*CuteQQuickFlipableCall26)(const void *, QHoverEvent *, int *);
typedef void (*CuteQQuickFlipableCall27)(const void *, QHoverEvent *, int *);
#if QT_CONFIG(quick_draganddrop)
typedef void (*CuteQQuickFlipableCall28)(const void *, QDragEnterEvent *, int *);
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
typedef void (*CuteQQuickFlipableCall29)(const void *, QDragMoveEvent *, int *);
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
typedef void (*CuteQQuickFlipableCall30)(const void *, QDragLeaveEvent *, int *);
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
typedef void (*CuteQQuickFlipableCall31)(const void *, QDropEvent *, int *);
#endif  // QT_CONFIG(quick_draganddrop)
typedef bool (*CuteQQuickFlipableCall32)(const void *, QQuickItem *, QEvent *, int *);
typedef void * (*CuteQQuickFlipableCall33)(const void *, QSGNode *, QQuickItem::UpdatePaintNodeData *, int *);
typedef void (*CuteQQuickFlipableCall34)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickFlipableCall35)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickFlipableCall36)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickFlipableCall37)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickFlipableCall38)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickFlipableCall39)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickFlipableCall40)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQQuickFlipable : public QQuickFlipable {
public:
  using QQuickFlipable::QQuickFlipable;
  void *taken[41] = {};

  bool take(const char *key, void *call) {
#if QT_CONFIG(quick_flipable)
    if (!std::strcmp(key, "_ZN10QQuickItem12updatePolishEv")) {
      taken[0] = call;
      return true;
    }
#endif  // QT_CONFIG(quick_flipable)
    if (!std::strcmp(key, "_ZNK10QQuickItem12boundingRectEv")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK10QQuickItem8clipRectEv")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK10QQuickItem8containsERK7QPointF")) {
      taken[3] = call;
      return true;
    }
#if QT_CONFIG(im)
    if (!std::strcmp(key, "_ZNK10QQuickItem16inputMethodQueryEN2Qt16InputMethodQueryE")) {
      taken[4] = call;
      return true;
    }
#endif  // QT_CONFIG(im)
    if (!std::strcmp(key, "_ZNK10QQuickItem17isTextureProviderEv")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK10QQuickItem15textureProviderEv")) {
      taken[6] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[7] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN10QQuickItem10itemChangeENS_10ItemChangeERKNS_14ItemChangeDataE")) {
      taken[8] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem14geometryChangeERK6QRectFS2_")) {
      taken[9] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQmlParserStatus10classBeginEv")) {
      taken[10] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQmlParserStatus17componentCompleteEv")) {
      taken[11] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem13keyPressEventEP9QKeyEvent")) {
      taken[12] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem15keyReleaseEventEP9QKeyEvent")) {
      taken[13] = call;
      return true;
    }
#if QT_CONFIG(im)
    if (!std::strcmp(key, "_ZN10QQuickItem16inputMethodEventEP17QInputMethodEvent")) {
      taken[14] = call;
      return true;
    }
#endif  // QT_CONFIG(im)
    if (!std::strcmp(key, "_ZN10QQuickItem12focusInEventEP11QFocusEvent")) {
      taken[15] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem13focusOutEventEP11QFocusEvent")) {
      taken[16] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem15mousePressEventEP11QMouseEvent")) {
      taken[17] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem14mouseMoveEventEP11QMouseEvent")) {
      taken[18] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem17mouseReleaseEventEP11QMouseEvent")) {
      taken[19] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem21mouseDoubleClickEventEP11QMouseEvent")) {
      taken[20] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem16mouseUngrabEventEv")) {
      taken[21] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem16touchUngrabEventEv")) {
      taken[22] = call;
      return true;
    }
#if QT_CONFIG(wheelevent)
    if (!std::strcmp(key, "_ZN10QQuickItem10wheelEventEP11QWheelEvent")) {
      taken[23] = call;
      return true;
    }
#endif  // QT_CONFIG(wheelevent)
    if (!std::strcmp(key, "_ZN10QQuickItem10touchEventEP11QTouchEvent")) {
      taken[24] = call;
      return true;
    }
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
    if (!std::strcmp(key, "_ZN10QQuickItem21childMouseEventFilterEPS_P6QEvent")) {
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

#if QT_CONFIG(quick_flipable)
  //  void QQuickFlipable::updatePolish()
  void updatePolish() override {
    if (taken[0]) {
      int handled = 0;
      CuteQQuickFlipableCall0 call = reinterpret_cast<CuteQQuickFlipableCall0>(taken[0]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickFlipable::updatePolish();
  }
#endif  // QT_CONFIG(quick_flipable)

  //  QRectF QQuickItem::boundingRect() const
  QRectF boundingRect() const override {
    if (taken[1]) {
      int handled = 0;
      CuteQQuickFlipableCall1 call = reinterpret_cast<CuteQQuickFlipableCall1>(taken[1]);
      const QRectF * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QQuickItem::boundingRect();
  }

  //  QRectF QQuickItem::clipRect() const
  QRectF clipRect() const override {
    if (taken[2]) {
      int handled = 0;
      CuteQQuickFlipableCall2 call = reinterpret_cast<CuteQQuickFlipableCall2>(taken[2]);
      const QRectF * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QQuickItem::clipRect();
  }

  //  bool QQuickItem::contains(const QPointF &point) const
  bool contains(const QPointF &point) const override {
    if (taken[3]) {
      int handled = 0;
      CuteQQuickFlipableCall3 call = reinterpret_cast<CuteQQuickFlipableCall3>(taken[3]);
      bool given = call(this, &point, &handled);
      if (handled) return given;
    }
    return QQuickItem::contains(point);
  }

#if QT_CONFIG(im)
  //  QVariant QQuickItem::inputMethodQuery(Qt::InputMethodQuery query)
  //      const
  QVariant inputMethodQuery(Qt::InputMethodQuery query) const override {
    if (taken[4]) {
      int handled = 0;
      CuteQQuickFlipableCall4 call = reinterpret_cast<CuteQQuickFlipableCall4>(taken[4]);
      const QVariant * given = call(this, static_cast<int>(query), &handled);
      if (handled && given) return *given;
    }
    return QQuickItem::inputMethodQuery(query);
  }
#endif  // QT_CONFIG(im)

  //  bool QQuickItem::isTextureProvider() const
  bool isTextureProvider() const override {
    if (taken[5]) {
      int handled = 0;
      CuteQQuickFlipableCall5 call = reinterpret_cast<CuteQQuickFlipableCall5>(taken[5]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QQuickItem::isTextureProvider();
  }

  //  QSGTextureProvider *QQuickItem::textureProvider() const
  QSGTextureProvider *textureProvider() const override {
    if (taken[6]) {
      int handled = 0;
      CuteQQuickFlipableCall6 call = reinterpret_cast<CuteQQuickFlipableCall6>(taken[6]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QSGTextureProvider *>(given);
    }
    return QQuickItem::textureProvider();
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QQuickItem::event(QEvent *a0)
  bool event(QEvent *a0) override {
    if (taken[7]) {
      int handled = 0;
      CuteQQuickFlipableCall7 call = reinterpret_cast<CuteQQuickFlipableCall7>(taken[7]);
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
    if (taken[8]) {
      int handled = 0;
      CuteQQuickFlipableCall8 call = reinterpret_cast<CuteQQuickFlipableCall8>(taken[8]);
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
    if (taken[9]) {
      int handled = 0;
      CuteQQuickFlipableCall9 call = reinterpret_cast<CuteQQuickFlipableCall9>(taken[9]);
      call(this, &newGeometry, &oldGeometry, &handled);
      if (handled) return;
    }
    QQuickItem::geometryChange(newGeometry, oldGeometry);
  }

  //  void QQuickItem::classBegin()
  void classBegin() override {
    if (taken[10]) {
      int handled = 0;
      CuteQQuickFlipableCall10 call = reinterpret_cast<CuteQQuickFlipableCall10>(taken[10]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItem::classBegin();
  }

  //  void QQuickItem::componentComplete()
  void componentComplete() override {
    if (taken[11]) {
      int handled = 0;
      CuteQQuickFlipableCall11 call = reinterpret_cast<CuteQQuickFlipableCall11>(taken[11]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItem::componentComplete();
  }

  //  void QQuickItem::keyPressEvent(QKeyEvent *event)
  void keyPressEvent(QKeyEvent *event) override {
    if (taken[12]) {
      int handled = 0;
      CuteQQuickFlipableCall12 call = reinterpret_cast<CuteQQuickFlipableCall12>(taken[12]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::keyPressEvent(event);
  }

  //  void QQuickItem::keyReleaseEvent(QKeyEvent *event)
  void keyReleaseEvent(QKeyEvent *event) override {
    if (taken[13]) {
      int handled = 0;
      CuteQQuickFlipableCall13 call = reinterpret_cast<CuteQQuickFlipableCall13>(taken[13]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::keyReleaseEvent(event);
  }

#if QT_CONFIG(im)
  //  void QQuickItem::inputMethodEvent(QInputMethodEvent *a0)
  void inputMethodEvent(QInputMethodEvent *a0) override {
    if (taken[14]) {
      int handled = 0;
      CuteQQuickFlipableCall14 call = reinterpret_cast<CuteQQuickFlipableCall14>(taken[14]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItem::inputMethodEvent(a0);
  }
#endif  // QT_CONFIG(im)

  //  void QQuickItem::focusInEvent(QFocusEvent *a0)
  void focusInEvent(QFocusEvent *a0) override {
    if (taken[15]) {
      int handled = 0;
      CuteQQuickFlipableCall15 call = reinterpret_cast<CuteQQuickFlipableCall15>(taken[15]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItem::focusInEvent(a0);
  }

  //  void QQuickItem::focusOutEvent(QFocusEvent *a0)
  void focusOutEvent(QFocusEvent *a0) override {
    if (taken[16]) {
      int handled = 0;
      CuteQQuickFlipableCall16 call = reinterpret_cast<CuteQQuickFlipableCall16>(taken[16]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItem::focusOutEvent(a0);
  }

  //  void QQuickItem::mousePressEvent(QMouseEvent *event)
  void mousePressEvent(QMouseEvent *event) override {
    if (taken[17]) {
      int handled = 0;
      CuteQQuickFlipableCall17 call = reinterpret_cast<CuteQQuickFlipableCall17>(taken[17]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::mousePressEvent(event);
  }

  //  void QQuickItem::mouseMoveEvent(QMouseEvent *event)
  void mouseMoveEvent(QMouseEvent *event) override {
    if (taken[18]) {
      int handled = 0;
      CuteQQuickFlipableCall18 call = reinterpret_cast<CuteQQuickFlipableCall18>(taken[18]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::mouseMoveEvent(event);
  }

  //  void QQuickItem::mouseReleaseEvent(QMouseEvent *event)
  void mouseReleaseEvent(QMouseEvent *event) override {
    if (taken[19]) {
      int handled = 0;
      CuteQQuickFlipableCall19 call = reinterpret_cast<CuteQQuickFlipableCall19>(taken[19]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::mouseReleaseEvent(event);
  }

  //  void QQuickItem::mouseDoubleClickEvent(QMouseEvent *event)
  void mouseDoubleClickEvent(QMouseEvent *event) override {
    if (taken[20]) {
      int handled = 0;
      CuteQQuickFlipableCall20 call = reinterpret_cast<CuteQQuickFlipableCall20>(taken[20]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::mouseDoubleClickEvent(event);
  }

  //  void QQuickItem::mouseUngrabEvent()
  void mouseUngrabEvent() override {
    if (taken[21]) {
      int handled = 0;
      CuteQQuickFlipableCall21 call = reinterpret_cast<CuteQQuickFlipableCall21>(taken[21]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItem::mouseUngrabEvent();
  }

  //  void QQuickItem::touchUngrabEvent()
  void touchUngrabEvent() override {
    if (taken[22]) {
      int handled = 0;
      CuteQQuickFlipableCall22 call = reinterpret_cast<CuteQQuickFlipableCall22>(taken[22]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItem::touchUngrabEvent();
  }

#if QT_CONFIG(wheelevent)
  //  void QQuickItem::wheelEvent(QWheelEvent *event)
  void wheelEvent(QWheelEvent *event) override {
    if (taken[23]) {
      int handled = 0;
      CuteQQuickFlipableCall23 call = reinterpret_cast<CuteQQuickFlipableCall23>(taken[23]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::wheelEvent(event);
  }
#endif  // QT_CONFIG(wheelevent)

  //  void QQuickItem::touchEvent(QTouchEvent *event)
  void touchEvent(QTouchEvent *event) override {
    if (taken[24]) {
      int handled = 0;
      CuteQQuickFlipableCall24 call = reinterpret_cast<CuteQQuickFlipableCall24>(taken[24]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::touchEvent(event);
  }

  //  void QQuickItem::hoverEnterEvent(QHoverEvent *event)
  void hoverEnterEvent(QHoverEvent *event) override {
    if (taken[25]) {
      int handled = 0;
      CuteQQuickFlipableCall25 call = reinterpret_cast<CuteQQuickFlipableCall25>(taken[25]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::hoverEnterEvent(event);
  }

  //  void QQuickItem::hoverMoveEvent(QHoverEvent *event)
  void hoverMoveEvent(QHoverEvent *event) override {
    if (taken[26]) {
      int handled = 0;
      CuteQQuickFlipableCall26 call = reinterpret_cast<CuteQQuickFlipableCall26>(taken[26]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::hoverMoveEvent(event);
  }

  //  void QQuickItem::hoverLeaveEvent(QHoverEvent *event)
  void hoverLeaveEvent(QHoverEvent *event) override {
    if (taken[27]) {
      int handled = 0;
      CuteQQuickFlipableCall27 call = reinterpret_cast<CuteQQuickFlipableCall27>(taken[27]);
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
      CuteQQuickFlipableCall28 call = reinterpret_cast<CuteQQuickFlipableCall28>(taken[28]);
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
      CuteQQuickFlipableCall29 call = reinterpret_cast<CuteQQuickFlipableCall29>(taken[29]);
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
      CuteQQuickFlipableCall30 call = reinterpret_cast<CuteQQuickFlipableCall30>(taken[30]);
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
      CuteQQuickFlipableCall31 call = reinterpret_cast<CuteQQuickFlipableCall31>(taken[31]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItem::dropEvent(a0);
  }
#endif  // QT_CONFIG(quick_draganddrop)

  //  bool QQuickItem::childMouseEventFilter(QQuickItem *a0, QEvent *a1)
  bool childMouseEventFilter(QQuickItem *a0, QEvent *a1) override {
    if (taken[32]) {
      int handled = 0;
      CuteQQuickFlipableCall32 call = reinterpret_cast<CuteQQuickFlipableCall32>(taken[32]);
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
    if (taken[33]) {
      int handled = 0;
      CuteQQuickFlipableCall33 call = reinterpret_cast<CuteQQuickFlipableCall33>(taken[33]);
      void * given = call(this, a0, a1, &handled);
      if (handled) return static_cast<QSGNode *>(given);
    }
    return QQuickItem::updatePaintNode(a0, a1);
  }

  //  void QQuickItem::releaseResources()
  void releaseResources() override {
    if (taken[34]) {
      int handled = 0;
      CuteQQuickFlipableCall34 call = reinterpret_cast<CuteQQuickFlipableCall34>(taken[34]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItem::releaseResources();
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[35]) {
      int handled = 0;
      CuteQQuickFlipableCall35 call = reinterpret_cast<CuteQQuickFlipableCall35>(taken[35]);
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
      CuteQQuickFlipableCall36 call = reinterpret_cast<CuteQQuickFlipableCall36>(taken[36]);
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
      CuteQQuickFlipableCall37 call = reinterpret_cast<CuteQQuickFlipableCall37>(taken[37]);
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
      CuteQQuickFlipableCall38 call = reinterpret_cast<CuteQQuickFlipableCall38>(taken[38]);
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
      CuteQQuickFlipableCall39 call = reinterpret_cast<CuteQQuickFlipableCall39>(taken[39]);
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
      CuteQQuickFlipableCall40 call = reinterpret_cast<CuteQQuickFlipableCall40>(taken[40]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QQuickFlipable::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK14QQuickFlipable10metaObjectEv(
    const QQuickFlipable *self) {
  return self->metaObject();
}

//  void *QQuickFlipable::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN14QQuickFlipable11qt_metacastEPKc(
    QQuickFlipable *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QQuickFlipable::qt_metacall(QMetaObject::Call a0, int a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN14QQuickFlipable11qt_metacallEN11QMetaObject4CallEiPPv(
    QQuickFlipable *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QQuickFlipable::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN14QQuickFlipable2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuickFlipable::tr(s, c, n));
}

//  QQuickFlipable::QQuickFlipable(QQuickItem *parent)
extern "C" Q_DECL_EXPORT
QQuickFlipable *ritual_ZN14QQuickFlipableC1EP10QQuickItem(
    QQuickItem *parent) {
  return new CuteQQuickFlipable(parent);
}

//  QQuickFlipable::~QQuickFlipable()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickFlipableD1Ev(QQuickFlipable *self) {
  delete self;
}

//  QQuickItem *QQuickFlipable::front() const
extern "C" Q_DECL_EXPORT
QQuickItem *ritual_ZNK14QQuickFlipable5frontEv(const QQuickFlipable *self) {
  return self->front();
}

//  void QQuickFlipable::setFront(QQuickItem *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickFlipable8setFrontEP10QQuickItem(
    QQuickFlipable *self,
    QQuickItem *a0) {
  self->setFront(a0);
}

//  QQuickItem *QQuickFlipable::back()
extern "C" Q_DECL_EXPORT
QQuickItem *ritual_ZN14QQuickFlipable4backEv(QQuickFlipable *self) {
  return self->back();
}

//  void QQuickFlipable::setBack(QQuickItem *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickFlipable7setBackEP10QQuickItem(
    QQuickFlipable *self,
    QQuickItem *a0) {
  self->setBack(a0);
}

//  Side QQuickFlipable::side() const
extern "C" Q_DECL_EXPORT
QQuickFlipable::Side ritual_ZNK14QQuickFlipable4sideEv(
    const QQuickFlipable *self) {
  return self->side();
}

//  void QQuickFlipable::frontChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickFlipable12frontChangedEv(QQuickFlipable *self) {
  self->frontChanged();
}

//  void QQuickFlipable::backChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickFlipable11backChangedEv(QQuickFlipable *self) {
  self->backChanged();
}

//  void QQuickFlipable::sideChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickFlipable11sideChangedEv(QQuickFlipable *self) {
  self->sideChanged();
}

//  void QQuickFlipable::updatePolish()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickFlipable12updatePolishEv(QQuickFlipable *self) {
  self->updatePolish();
}

//  void QQuickFlipable::retransformBack()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickFlipable15retransformBackEv(QQuickFlipable *self) {
  self->retransformBack();
}

//  QQuickFlipablePrivate *QQuickFlipable::d_func()
extern "C" Q_DECL_EXPORT
QQuickFlipablePrivate *ritual_ZN14QQuickFlipable6d_funcEv(
    QQuickFlipable *self) {
  return self->d_func();
}

//  const QQuickFlipablePrivate *QQuickFlipable::d_func() const
extern "C" Q_DECL_EXPORT
const QQuickFlipablePrivate *ritual_ZNK14QQuickFlipable6d_funcEv(
    const QQuickFlipable *self) {
  return self->d_func();
}

//  a Python function taken by a CuteQQuickFlipable, for the function named
//      by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQuickFlipable(
    QQuickFlipable *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQuickFlipable *>(self)->take(key, call);
}

//  void QQuickFlipable::updatePolish()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN14QQuickFlipable12updatePolishEv(QQuickFlipable *self) {
  static_cast<OwnQQuickFlipable *>(self)->OwnQQuickFlipable::updatePolish();
}

#endif  // QT_CONFIG(quick_flipable)
#endif  // QT_CONFIG(quick_flipable)
