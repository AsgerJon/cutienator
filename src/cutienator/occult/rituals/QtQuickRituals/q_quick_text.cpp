//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/6.12.0/QtQuick/private/qquicktext_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtGui/qtguiglobal.h>
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qquicktext_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtGui/qfont.h>
#include <QtGui/qcolor.h>
#include <QtCore/qurl.h>
#include <QtCore/qrect.h>
#include <QtQml/QtQml>
#include <QtQml/qjsvalue.h>
#include <QtCore/qsize.h>
#include <QtQuick/qquickitem.h>
#include <QtCore/qvariant.h>
#include <QtCore/qpoint.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  Only a class built on QQuickText may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQQuickText : QQuickText {
  using QQuickText::mousePressEvent;
  using QQuickText::mouseReleaseEvent;
  using QQuickText::itemChange;
  using QQuickText::geometryChange;
  using QQuickText::updatePaintNode;
  using QQuickText::updatePolish;
  using QQuickText::hoverEnterEvent;
  using QQuickText::hoverMoveEvent;
  using QQuickText::hoverLeaveEvent;
};

//  A QQuickText that Python can take functions over in. Every QQuickText
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQQuickTextCall0)(const void *, int *);
typedef const QRectF * (*CuteQQuickTextCall1)(const void *, int *);
typedef const QRectF * (*CuteQQuickTextCall2)(const void *, int *);
typedef void (*CuteQQuickTextCall3)(const void *, int *);
typedef void (*CuteQQuickTextCall4)(const void *, QMouseEvent *, int *);
typedef void (*CuteQQuickTextCall5)(const void *, QMouseEvent *, int *);
typedef void (*CuteQQuickTextCall6)(const void *, int, const QQuickItem::ItemChangeData *, int *);
typedef void (*CuteQQuickTextCall7)(const void *, const QRectF *, const QRectF *, int *);
typedef void * (*CuteQQuickTextCall8)(const void *, QSGNode *, QQuickItem::UpdatePaintNodeData *, int *);
typedef void (*CuteQQuickTextCall9)(const void *, int *);
typedef void (*CuteQQuickTextCall10)(const void *, QHoverEvent *, int *);
typedef void (*CuteQQuickTextCall11)(const void *, QHoverEvent *, int *);
typedef void (*CuteQQuickTextCall12)(const void *, QHoverEvent *, int *);
typedef bool (*CuteQQuickTextCall13)(const void *, const QPointF *, int *);
#if QT_CONFIG(im)
typedef const QVariant * (*CuteQQuickTextCall14)(const void *, int, int *);
#endif  // QT_CONFIG(im)
typedef bool (*CuteQQuickTextCall15)(const void *, int *);
typedef void * (*CuteQQuickTextCall16)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickTextCall17)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickTextCall18)(const void *, int *);
typedef void (*CuteQQuickTextCall19)(const void *, QKeyEvent *, int *);
typedef void (*CuteQQuickTextCall20)(const void *, QKeyEvent *, int *);
#if QT_CONFIG(im)
typedef void (*CuteQQuickTextCall21)(const void *, QInputMethodEvent *, int *);
#endif  // QT_CONFIG(im)
typedef void (*CuteQQuickTextCall22)(const void *, QFocusEvent *, int *);
typedef void (*CuteQQuickTextCall23)(const void *, QFocusEvent *, int *);
typedef void (*CuteQQuickTextCall24)(const void *, QMouseEvent *, int *);
typedef void (*CuteQQuickTextCall25)(const void *, QMouseEvent *, int *);
typedef void (*CuteQQuickTextCall26)(const void *, int *);
typedef void (*CuteQQuickTextCall27)(const void *, int *);
#if QT_CONFIG(wheelevent)
typedef void (*CuteQQuickTextCall28)(const void *, QWheelEvent *, int *);
#endif  // QT_CONFIG(wheelevent)
typedef void (*CuteQQuickTextCall29)(const void *, QTouchEvent *, int *);
#if QT_CONFIG(quick_draganddrop)
typedef void (*CuteQQuickTextCall30)(const void *, QDragEnterEvent *, int *);
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
typedef void (*CuteQQuickTextCall31)(const void *, QDragMoveEvent *, int *);
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
typedef void (*CuteQQuickTextCall32)(const void *, QDragLeaveEvent *, int *);
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
typedef void (*CuteQQuickTextCall33)(const void *, QDropEvent *, int *);
#endif  // QT_CONFIG(quick_draganddrop)
typedef bool (*CuteQQuickTextCall34)(const void *, QQuickItem *, QEvent *, int *);
typedef void (*CuteQQuickTextCall35)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickTextCall36)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickTextCall37)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickTextCall38)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickTextCall39)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickTextCall40)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickTextCall41)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQQuickText : public QQuickText {
public:
  using QQuickText::QQuickText;
  void *taken[42] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN16QQmlParserStatus17componentCompleteEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK10QQuickItem12boundingRectEv")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK10QQuickItem8clipRectEv")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN19QQuickTextInterface10invalidateEv")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem15mousePressEventEP11QMouseEvent")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem17mouseReleaseEventEP11QMouseEvent")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem10itemChangeENS_10ItemChangeERKNS_14ItemChangeDataE")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem14geometryChangeERK6QRectFS2_")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem15updatePaintNodeEP7QSGNodePNS_19UpdatePaintNodeDataE")) {
      taken[8] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem12updatePolishEv")) {
      taken[9] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem15hoverEnterEventEP11QHoverEvent")) {
      taken[10] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem14hoverMoveEventEP11QHoverEvent")) {
      taken[11] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem15hoverLeaveEventEP11QHoverEvent")) {
      taken[12] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK10QQuickItem8containsERK7QPointF")) {
      taken[13] = call;
      return true;
    }
#if QT_CONFIG(im)
    if (!std::strcmp(key, "_ZNK10QQuickItem16inputMethodQueryEN2Qt16InputMethodQueryE")) {
      taken[14] = call;
      return true;
    }
#endif  // QT_CONFIG(im)
    if (!std::strcmp(key, "_ZNK10QQuickItem17isTextureProviderEv")) {
      taken[15] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK10QQuickItem15textureProviderEv")) {
      taken[16] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[17] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN16QQmlParserStatus10classBeginEv")) {
      taken[18] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem13keyPressEventEP9QKeyEvent")) {
      taken[19] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem15keyReleaseEventEP9QKeyEvent")) {
      taken[20] = call;
      return true;
    }
#if QT_CONFIG(im)
    if (!std::strcmp(key, "_ZN10QQuickItem16inputMethodEventEP17QInputMethodEvent")) {
      taken[21] = call;
      return true;
    }
#endif  // QT_CONFIG(im)
    if (!std::strcmp(key, "_ZN10QQuickItem12focusInEventEP11QFocusEvent")) {
      taken[22] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem13focusOutEventEP11QFocusEvent")) {
      taken[23] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem14mouseMoveEventEP11QMouseEvent")) {
      taken[24] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem21mouseDoubleClickEventEP11QMouseEvent")) {
      taken[25] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem16mouseUngrabEventEv")) {
      taken[26] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem16touchUngrabEventEv")) {
      taken[27] = call;
      return true;
    }
#if QT_CONFIG(wheelevent)
    if (!std::strcmp(key, "_ZN10QQuickItem10wheelEventEP11QWheelEvent")) {
      taken[28] = call;
      return true;
    }
#endif  // QT_CONFIG(wheelevent)
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
    if (!std::strcmp(key, "_ZN10QQuickItem21childMouseEventFilterEPS_P6QEvent")) {
      taken[34] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem16releaseResourcesEv")) {
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
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[37] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[38] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[39] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[40] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[41] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

  //  void QQuickText::componentComplete()
  void componentComplete() override {
    if (taken[0]) {
      int handled = 0;
      CuteQQuickTextCall0 call = reinterpret_cast<CuteQQuickTextCall0>(taken[0]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickText::componentComplete();
  }

  //  QRectF QQuickText::boundingRect() const
  QRectF boundingRect() const override {
    if (taken[1]) {
      int handled = 0;
      CuteQQuickTextCall1 call = reinterpret_cast<CuteQQuickTextCall1>(taken[1]);
      const QRectF * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QQuickText::boundingRect();
  }

  //  QRectF QQuickText::clipRect() const
  QRectF clipRect() const override {
    if (taken[2]) {
      int handled = 0;
      CuteQQuickTextCall2 call = reinterpret_cast<CuteQQuickTextCall2>(taken[2]);
      const QRectF * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QQuickText::clipRect();
  }

  //  void QQuickText::invalidate()
  void invalidate() override {
    if (taken[3]) {
      int handled = 0;
      CuteQQuickTextCall3 call = reinterpret_cast<CuteQQuickTextCall3>(taken[3]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickText::invalidate();
  }

  //  void QQuickText::mousePressEvent(QMouseEvent *event)
  void mousePressEvent(QMouseEvent *event) override {
    if (taken[4]) {
      int handled = 0;
      CuteQQuickTextCall4 call = reinterpret_cast<CuteQQuickTextCall4>(taken[4]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickText::mousePressEvent(event);
  }

  //  void QQuickText::mouseReleaseEvent(QMouseEvent *event)
  void mouseReleaseEvent(QMouseEvent *event) override {
    if (taken[5]) {
      int handled = 0;
      CuteQQuickTextCall5 call = reinterpret_cast<CuteQQuickTextCall5>(taken[5]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickText::mouseReleaseEvent(event);
  }

  //  void QQuickText::itemChange(ItemChange change, const ItemChangeData
  //      &value)
  void itemChange(
      QQuickItem::ItemChange change,
      const QQuickItem::ItemChangeData &value) override {
    if (taken[6]) {
      int handled = 0;
      CuteQQuickTextCall6 call = reinterpret_cast<CuteQQuickTextCall6>(taken[6]);
      call(this, static_cast<int>(change), &value, &handled);
      if (handled) return;
    }
    QQuickText::itemChange(change, value);
  }

  //  void QQuickText::geometryChange(const QRectF &newGeometry, const
  //      QRectF &oldGeometry)
  void geometryChange(
      const QRectF &newGeometry,
      const QRectF &oldGeometry) override {
    if (taken[7]) {
      int handled = 0;
      CuteQQuickTextCall7 call = reinterpret_cast<CuteQQuickTextCall7>(taken[7]);
      call(this, &newGeometry, &oldGeometry, &handled);
      if (handled) return;
    }
    QQuickText::geometryChange(newGeometry, oldGeometry);
  }

  //  QSGNode *QQuickText::updatePaintNode(QSGNode *a0, UpdatePaintNodeData
  //      *a1)
  QSGNode *updatePaintNode(
      QSGNode *a0,
      QQuickItem::UpdatePaintNodeData *a1) override {
    if (taken[8]) {
      int handled = 0;
      CuteQQuickTextCall8 call = reinterpret_cast<CuteQQuickTextCall8>(taken[8]);
      void * given = call(this, a0, a1, &handled);
      if (handled) return static_cast<QSGNode *>(given);
    }
    return QQuickText::updatePaintNode(a0, a1);
  }

  //  void QQuickText::updatePolish()
  void updatePolish() override {
    if (taken[9]) {
      int handled = 0;
      CuteQQuickTextCall9 call = reinterpret_cast<CuteQQuickTextCall9>(taken[9]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickText::updatePolish();
  }

  //  void QQuickText::hoverEnterEvent(QHoverEvent *event)
  void hoverEnterEvent(QHoverEvent *event) override {
    if (taken[10]) {
      int handled = 0;
      CuteQQuickTextCall10 call = reinterpret_cast<CuteQQuickTextCall10>(taken[10]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickText::hoverEnterEvent(event);
  }

  //  void QQuickText::hoverMoveEvent(QHoverEvent *event)
  void hoverMoveEvent(QHoverEvent *event) override {
    if (taken[11]) {
      int handled = 0;
      CuteQQuickTextCall11 call = reinterpret_cast<CuteQQuickTextCall11>(taken[11]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickText::hoverMoveEvent(event);
  }

  //  void QQuickText::hoverLeaveEvent(QHoverEvent *event)
  void hoverLeaveEvent(QHoverEvent *event) override {
    if (taken[12]) {
      int handled = 0;
      CuteQQuickTextCall12 call = reinterpret_cast<CuteQQuickTextCall12>(taken[12]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickText::hoverLeaveEvent(event);
  }

  //  bool QQuickItem::contains(const QPointF &point) const
  bool contains(const QPointF &point) const override {
    if (taken[13]) {
      int handled = 0;
      CuteQQuickTextCall13 call = reinterpret_cast<CuteQQuickTextCall13>(taken[13]);
      bool given = call(this, &point, &handled);
      if (handled) return given;
    }
    return QQuickItem::contains(point);
  }

#if QT_CONFIG(im)
  //  QVariant QQuickItem::inputMethodQuery(Qt::InputMethodQuery query)
  //      const
  QVariant inputMethodQuery(Qt::InputMethodQuery query) const override {
    if (taken[14]) {
      int handled = 0;
      CuteQQuickTextCall14 call = reinterpret_cast<CuteQQuickTextCall14>(taken[14]);
      const QVariant * given = call(this, static_cast<int>(query), &handled);
      if (handled && given) return *given;
    }
    return QQuickItem::inputMethodQuery(query);
  }
#endif  // QT_CONFIG(im)

  //  bool QQuickItem::isTextureProvider() const
  bool isTextureProvider() const override {
    if (taken[15]) {
      int handled = 0;
      CuteQQuickTextCall15 call = reinterpret_cast<CuteQQuickTextCall15>(taken[15]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QQuickItem::isTextureProvider();
  }

  //  QSGTextureProvider *QQuickItem::textureProvider() const
  QSGTextureProvider *textureProvider() const override {
    if (taken[16]) {
      int handled = 0;
      CuteQQuickTextCall16 call = reinterpret_cast<CuteQQuickTextCall16>(taken[16]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QSGTextureProvider *>(given);
    }
    return QQuickItem::textureProvider();
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QQuickItem::event(QEvent *a0)
  bool event(QEvent *a0) override {
    if (taken[17]) {
      int handled = 0;
      CuteQQuickTextCall17 call = reinterpret_cast<CuteQQuickTextCall17>(taken[17]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQuickItem::event(a0);
  }
#endif  // !defined(QT_NO_QOBJECT)

  //  void QQuickItem::classBegin()
  void classBegin() override {
    if (taken[18]) {
      int handled = 0;
      CuteQQuickTextCall18 call = reinterpret_cast<CuteQQuickTextCall18>(taken[18]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItem::classBegin();
  }

  //  void QQuickItem::keyPressEvent(QKeyEvent *event)
  void keyPressEvent(QKeyEvent *event) override {
    if (taken[19]) {
      int handled = 0;
      CuteQQuickTextCall19 call = reinterpret_cast<CuteQQuickTextCall19>(taken[19]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::keyPressEvent(event);
  }

  //  void QQuickItem::keyReleaseEvent(QKeyEvent *event)
  void keyReleaseEvent(QKeyEvent *event) override {
    if (taken[20]) {
      int handled = 0;
      CuteQQuickTextCall20 call = reinterpret_cast<CuteQQuickTextCall20>(taken[20]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::keyReleaseEvent(event);
  }

#if QT_CONFIG(im)
  //  void QQuickItem::inputMethodEvent(QInputMethodEvent *a0)
  void inputMethodEvent(QInputMethodEvent *a0) override {
    if (taken[21]) {
      int handled = 0;
      CuteQQuickTextCall21 call = reinterpret_cast<CuteQQuickTextCall21>(taken[21]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItem::inputMethodEvent(a0);
  }
#endif  // QT_CONFIG(im)

  //  void QQuickItem::focusInEvent(QFocusEvent *a0)
  void focusInEvent(QFocusEvent *a0) override {
    if (taken[22]) {
      int handled = 0;
      CuteQQuickTextCall22 call = reinterpret_cast<CuteQQuickTextCall22>(taken[22]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItem::focusInEvent(a0);
  }

  //  void QQuickItem::focusOutEvent(QFocusEvent *a0)
  void focusOutEvent(QFocusEvent *a0) override {
    if (taken[23]) {
      int handled = 0;
      CuteQQuickTextCall23 call = reinterpret_cast<CuteQQuickTextCall23>(taken[23]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItem::focusOutEvent(a0);
  }

  //  void QQuickItem::mouseMoveEvent(QMouseEvent *event)
  void mouseMoveEvent(QMouseEvent *event) override {
    if (taken[24]) {
      int handled = 0;
      CuteQQuickTextCall24 call = reinterpret_cast<CuteQQuickTextCall24>(taken[24]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::mouseMoveEvent(event);
  }

  //  void QQuickItem::mouseDoubleClickEvent(QMouseEvent *event)
  void mouseDoubleClickEvent(QMouseEvent *event) override {
    if (taken[25]) {
      int handled = 0;
      CuteQQuickTextCall25 call = reinterpret_cast<CuteQQuickTextCall25>(taken[25]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::mouseDoubleClickEvent(event);
  }

  //  void QQuickItem::mouseUngrabEvent()
  void mouseUngrabEvent() override {
    if (taken[26]) {
      int handled = 0;
      CuteQQuickTextCall26 call = reinterpret_cast<CuteQQuickTextCall26>(taken[26]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItem::mouseUngrabEvent();
  }

  //  void QQuickItem::touchUngrabEvent()
  void touchUngrabEvent() override {
    if (taken[27]) {
      int handled = 0;
      CuteQQuickTextCall27 call = reinterpret_cast<CuteQQuickTextCall27>(taken[27]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItem::touchUngrabEvent();
  }

#if QT_CONFIG(wheelevent)
  //  void QQuickItem::wheelEvent(QWheelEvent *event)
  void wheelEvent(QWheelEvent *event) override {
    if (taken[28]) {
      int handled = 0;
      CuteQQuickTextCall28 call = reinterpret_cast<CuteQQuickTextCall28>(taken[28]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::wheelEvent(event);
  }
#endif  // QT_CONFIG(wheelevent)

  //  void QQuickItem::touchEvent(QTouchEvent *event)
  void touchEvent(QTouchEvent *event) override {
    if (taken[29]) {
      int handled = 0;
      CuteQQuickTextCall29 call = reinterpret_cast<CuteQQuickTextCall29>(taken[29]);
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
      CuteQQuickTextCall30 call = reinterpret_cast<CuteQQuickTextCall30>(taken[30]);
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
      CuteQQuickTextCall31 call = reinterpret_cast<CuteQQuickTextCall31>(taken[31]);
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
      CuteQQuickTextCall32 call = reinterpret_cast<CuteQQuickTextCall32>(taken[32]);
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
      CuteQQuickTextCall33 call = reinterpret_cast<CuteQQuickTextCall33>(taken[33]);
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
      CuteQQuickTextCall34 call = reinterpret_cast<CuteQQuickTextCall34>(taken[34]);
      bool given = call(this, a0, a1, &handled);
      if (handled) return given;
    }
    return QQuickItem::childMouseEventFilter(a0, a1);
  }

  //  void QQuickItem::releaseResources()
  void releaseResources() override {
    if (taken[35]) {
      int handled = 0;
      CuteQQuickTextCall35 call = reinterpret_cast<CuteQQuickTextCall35>(taken[35]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItem::releaseResources();
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[36]) {
      int handled = 0;
      CuteQQuickTextCall36 call = reinterpret_cast<CuteQQuickTextCall36>(taken[36]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[37]) {
      int handled = 0;
      CuteQQuickTextCall37 call = reinterpret_cast<CuteQQuickTextCall37>(taken[37]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[38]) {
      int handled = 0;
      CuteQQuickTextCall38 call = reinterpret_cast<CuteQQuickTextCall38>(taken[38]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[39]) {
      int handled = 0;
      CuteQQuickTextCall39 call = reinterpret_cast<CuteQQuickTextCall39>(taken[39]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[40]) {
      int handled = 0;
      CuteQQuickTextCall40 call = reinterpret_cast<CuteQQuickTextCall40>(taken[40]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[41]) {
      int handled = 0;
      CuteQQuickTextCall41 call = reinterpret_cast<CuteQQuickTextCall41>(taken[41]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QQuickText::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK10QQuickText10metaObjectEv(
    const QQuickText *self) {
  return self->metaObject();
}

//  QString QQuickText::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN10QQuickText2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuickText::tr(s, c, n));
}

//  QQuickText::QQuickText(QQuickItem *parent)
extern "C" Q_DECL_EXPORT
QQuickText *ritual_ZN10QQuickTextC1EP10QQuickItem(QQuickItem *parent) {
  return new CuteQQuickText(parent);
}

//  QQuickText::~QQuickText()
extern "C" Q_DECL_EXPORT
void ritual_ZN10QQuickTextD1Ev(QQuickText *self) {
  delete self;
}

//  QString QQuickText::text() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK10QQuickText4textEv(const QQuickText *self) {
  return new QString(self->text());
}

//  void QQuickText::setText(const QString &a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QQuickText7setTextERK7QString(
    QQuickText *self,
    const QString *a0) {
  self->setText(*a0);
}

//  QFont QQuickText::font() const
extern "C" Q_DECL_EXPORT
QFont *ritual_ZNK10QQuickText4fontEv(const QQuickText *self) {
  return new QFont(self->font());
}

//  void QQuickText::setFont(const QFont &font)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QQuickText7setFontERK5QFont(
    QQuickText *self,
    const QFont *font) {
  self->setFont(*font);
}

//  QColor QQuickText::color() const
extern "C" Q_DECL_EXPORT
QColor *ritual_ZNK10QQuickText5colorEv(const QQuickText *self) {
  return new QColor(self->color());
}

//  void QQuickText::setColor(const QColor &c)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QQuickText8setColorERK6QColor(
    QQuickText *self,
    const QColor *c) {
  self->setColor(*c);
}

//  QColor QQuickText::linkColor() const
extern "C" Q_DECL_EXPORT
QColor *ritual_ZNK10QQuickText9linkColorEv(const QQuickText *self) {
  return new QColor(self->linkColor());
}

//  void QQuickText::setLinkColor(const QColor &color)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QQuickText12setLinkColorERK6QColor(
    QQuickText *self,
    const QColor *color) {
  self->setLinkColor(*color);
}

//  TextStyle QQuickText::style() const
extern "C" Q_DECL_EXPORT
QQuickText::TextStyle ritual_ZNK10QQuickText5styleEv(
    const QQuickText *self) {
  return self->style();
}

//  void QQuickText::setStyle(TextStyle style)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QQuickText8setStyleENS_9TextStyleE(
    QQuickText *self,
    QQuickText::TextStyle style) {
  self->setStyle(style);
}

//  QColor QQuickText::styleColor() const
extern "C" Q_DECL_EXPORT
QColor *ritual_ZNK10QQuickText10styleColorEv(const QQuickText *self) {
  return new QColor(self->styleColor());
}

//  void QQuickText::setStyleColor(const QColor &c)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QQuickText13setStyleColorERK6QColor(
    QQuickText *self,
    const QColor *c) {
  self->setStyleColor(*c);
}

//  HAlignment QQuickText::hAlign() const
extern "C" Q_DECL_EXPORT
QQuickText::HAlignment ritual_ZNK10QQuickText6hAlignEv(
    const QQuickText *self) {
  return self->hAlign();
}

//  void QQuickText::setHAlign(HAlignment align)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QQuickText9setHAlignENS_10HAlignmentE(
    QQuickText *self,
    QQuickText::HAlignment align) {
  self->setHAlign(align);
}

//  void QQuickText::resetHAlign()
extern "C" Q_DECL_EXPORT
void ritual_ZN10QQuickText11resetHAlignEv(QQuickText *self) {
  self->resetHAlign();
}

//  HAlignment QQuickText::effectiveHAlign() const
extern "C" Q_DECL_EXPORT
QQuickText::HAlignment ritual_ZNK10QQuickText15effectiveHAlignEv(
    const QQuickText *self) {
  return self->effectiveHAlign();
}

//  VAlignment QQuickText::vAlign() const
extern "C" Q_DECL_EXPORT
QQuickText::VAlignment ritual_ZNK10QQuickText6vAlignEv(
    const QQuickText *self) {
  return self->vAlign();
}

//  void QQuickText::setVAlign(VAlignment align)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QQuickText9setVAlignENS_10VAlignmentE(
    QQuickText *self,
    QQuickText::VAlignment align) {
  self->setVAlign(align);
}

//  WrapMode QQuickText::wrapMode() const
extern "C" Q_DECL_EXPORT
QQuickText::WrapMode ritual_ZNK10QQuickText8wrapModeEv(
    const QQuickText *self) {
  return self->wrapMode();
}

//  void QQuickText::setWrapMode(WrapMode w)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QQuickText11setWrapModeENS_8WrapModeE(
    QQuickText *self,
    QQuickText::WrapMode w) {
  self->setWrapMode(w);
}

//  int QQuickText::lineCount() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK10QQuickText9lineCountEv(const QQuickText *self) {
  return self->lineCount();
}

//  bool QQuickText::truncated() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK10QQuickText9truncatedEv(const QQuickText *self) {
  return self->truncated();
}

//  int QQuickText::maximumLineCount() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK10QQuickText16maximumLineCountEv(const QQuickText *self) {
  return self->maximumLineCount();
}

//  void QQuickText::setMaximumLineCount(int lines)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QQuickText19setMaximumLineCountEi(
    QQuickText *self,
    int lines) {
  self->setMaximumLineCount(lines);
}

//  void QQuickText::resetMaximumLineCount()
extern "C" Q_DECL_EXPORT
void ritual_ZN10QQuickText21resetMaximumLineCountEv(QQuickText *self) {
  self->resetMaximumLineCount();
}

//  TextFormat QQuickText::textFormat() const
extern "C" Q_DECL_EXPORT
QQuickText::TextFormat ritual_ZNK10QQuickText10textFormatEv(
    const QQuickText *self) {
  return self->textFormat();
}

//  void QQuickText::setTextFormat(TextFormat format)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QQuickText13setTextFormatENS_10TextFormatE(
    QQuickText *self,
    QQuickText::TextFormat format) {
  self->setTextFormat(format);
}

//  TextElideMode QQuickText::elideMode() const
extern "C" Q_DECL_EXPORT
QQuickText::TextElideMode ritual_ZNK10QQuickText9elideModeEv(
    const QQuickText *self) {
  return self->elideMode();
}

//  void QQuickText::setElideMode(TextElideMode a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QQuickText12setElideModeENS_13TextElideModeE(
    QQuickText *self,
    QQuickText::TextElideMode a0) {
  self->setElideMode(a0);
}

//  qreal QQuickText::lineHeight() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK10QQuickText10lineHeightEv(const QQuickText *self) {
  return self->lineHeight();
}

//  void QQuickText::setLineHeight(qreal lineHeight)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QQuickText13setLineHeightEd(
    QQuickText *self,
    qreal lineHeight) {
  self->setLineHeight(lineHeight);
}

//  LineHeightMode QQuickText::lineHeightMode() const
extern "C" Q_DECL_EXPORT
QQuickText::LineHeightMode ritual_ZNK10QQuickText14lineHeightModeEv(
    const QQuickText *self) {
  return self->lineHeightMode();
}

//  void QQuickText::setLineHeightMode(LineHeightMode a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QQuickText17setLineHeightModeENS_14LineHeightModeE(
    QQuickText *self,
    QQuickText::LineHeightMode a0) {
  self->setLineHeightMode(a0);
}

//  QUrl QQuickText::baseUrl() const
extern "C" Q_DECL_EXPORT
QUrl *ritual_ZNK10QQuickText7baseUrlEv(const QQuickText *self) {
  return new QUrl(self->baseUrl());
}

//  void QQuickText::setBaseUrl(const QUrl &url)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QQuickText10setBaseUrlERK4QUrl(
    QQuickText *self,
    const QUrl *url) {
  self->setBaseUrl(*url);
}

//  void QQuickText::resetBaseUrl()
extern "C" Q_DECL_EXPORT
void ritual_ZN10QQuickText12resetBaseUrlEv(QQuickText *self) {
  self->resetBaseUrl();
}

//  int QQuickText::minimumPixelSize() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK10QQuickText16minimumPixelSizeEv(const QQuickText *self) {
  return self->minimumPixelSize();
}

//  void QQuickText::setMinimumPixelSize(int size)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QQuickText19setMinimumPixelSizeEi(
    QQuickText *self,
    int size) {
  self->setMinimumPixelSize(size);
}

//  int QQuickText::minimumPointSize() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK10QQuickText16minimumPointSizeEv(const QQuickText *self) {
  return self->minimumPointSize();
}

//  void QQuickText::setMinimumPointSize(int size)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QQuickText19setMinimumPointSizeEi(
    QQuickText *self,
    int size) {
  self->setMinimumPointSize(size);
}

//  FontSizeMode QQuickText::fontSizeMode() const
extern "C" Q_DECL_EXPORT
QQuickText::FontSizeMode ritual_ZNK10QQuickText12fontSizeModeEv(
    const QQuickText *self) {
  return self->fontSizeMode();
}

//  void QQuickText::setFontSizeMode(FontSizeMode mode)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QQuickText15setFontSizeModeENS_12FontSizeModeE(
    QQuickText *self,
    QQuickText::FontSizeMode mode) {
  self->setFontSizeMode(mode);
}

//  void QQuickText::componentComplete()
extern "C" Q_DECL_EXPORT
void ritual_ZN10QQuickText17componentCompleteEv(QQuickText *self) {
  self->componentComplete();
}

//  int QQuickText::resourcesLoading() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK10QQuickText16resourcesLoadingEv(const QQuickText *self) {
  return self->resourcesLoading();
}

//  qreal QQuickText::contentWidth() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK10QQuickText12contentWidthEv(const QQuickText *self) {
  return self->contentWidth();
}

//  qreal QQuickText::contentHeight() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK10QQuickText13contentHeightEv(const QQuickText *self) {
  return self->contentHeight();
}

//  QRectF QQuickText::boundingRect() const
extern "C" Q_DECL_EXPORT
QRectF *ritual_ZNK10QQuickText12boundingRectEv(const QQuickText *self) {
  return new QRectF(self->boundingRect());
}

//  QRectF QQuickText::clipRect() const
extern "C" Q_DECL_EXPORT
QRectF *ritual_ZNK10QQuickText8clipRectEv(const QQuickText *self) {
  return new QRectF(self->clipRect());
}

//  void QQuickText::forceLayout()
extern "C" Q_DECL_EXPORT
void ritual_ZN10QQuickText11forceLayoutEv(QQuickText *self) {
  self->forceLayout();
}

//  RenderType QQuickText::renderType() const
extern "C" Q_DECL_EXPORT
QQuickText::RenderType ritual_ZNK10QQuickText10renderTypeEv(
    const QQuickText *self) {
  return self->renderType();
}

//  void QQuickText::setRenderType(RenderType renderType)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QQuickText13setRenderTypeENS_10RenderTypeE(
    QQuickText *self,
    QQuickText::RenderType renderType) {
  self->setRenderType(renderType);
}

//  int QQuickText::renderTypeQuality() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK10QQuickText17renderTypeQualityEv(const QQuickText *self) {
  return self->renderTypeQuality();
}

//  void QQuickText::setRenderTypeQuality(int renderTypeQuality)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QQuickText20setRenderTypeQualityEi(
    QQuickText *self,
    int renderTypeQuality) {
  self->setRenderTypeQuality(renderTypeQuality);
}

//  QString QQuickText::hoveredLink() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK10QQuickText11hoveredLinkEv(const QQuickText *self) {
  return new QString(self->hoveredLink());
}

//  QString QQuickText::linkAt(qreal x, qreal y) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK10QQuickText6linkAtEdd(
    const QQuickText *self,
    qreal x,
    qreal y) {
  return new QString(self->linkAt(x, y));
}

//  qreal QQuickText::padding() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK10QQuickText7paddingEv(const QQuickText *self) {
  return self->padding();
}

//  void QQuickText::setPadding(qreal padding)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QQuickText10setPaddingEd(QQuickText *self, qreal padding) {
  self->setPadding(padding);
}

//  void QQuickText::resetPadding()
extern "C" Q_DECL_EXPORT
void ritual_ZN10QQuickText12resetPaddingEv(QQuickText *self) {
  self->resetPadding();
}

//  qreal QQuickText::topPadding() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK10QQuickText10topPaddingEv(const QQuickText *self) {
  return self->topPadding();
}

//  void QQuickText::setTopPadding(qreal padding)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QQuickText13setTopPaddingEd(
    QQuickText *self,
    qreal padding) {
  self->setTopPadding(padding);
}

//  void QQuickText::resetTopPadding()
extern "C" Q_DECL_EXPORT
void ritual_ZN10QQuickText15resetTopPaddingEv(QQuickText *self) {
  self->resetTopPadding();
}

//  qreal QQuickText::leftPadding() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK10QQuickText11leftPaddingEv(const QQuickText *self) {
  return self->leftPadding();
}

//  void QQuickText::setLeftPadding(qreal padding)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QQuickText14setLeftPaddingEd(
    QQuickText *self,
    qreal padding) {
  self->setLeftPadding(padding);
}

//  void QQuickText::resetLeftPadding()
extern "C" Q_DECL_EXPORT
void ritual_ZN10QQuickText16resetLeftPaddingEv(QQuickText *self) {
  self->resetLeftPadding();
}

//  qreal QQuickText::rightPadding() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK10QQuickText12rightPaddingEv(const QQuickText *self) {
  return self->rightPadding();
}

//  void QQuickText::setRightPadding(qreal padding)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QQuickText15setRightPaddingEd(
    QQuickText *self,
    qreal padding) {
  self->setRightPadding(padding);
}

//  void QQuickText::resetRightPadding()
extern "C" Q_DECL_EXPORT
void ritual_ZN10QQuickText17resetRightPaddingEv(QQuickText *self) {
  self->resetRightPadding();
}

//  qreal QQuickText::bottomPadding() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK10QQuickText13bottomPaddingEv(const QQuickText *self) {
  return self->bottomPadding();
}

//  void QQuickText::setBottomPadding(qreal padding)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QQuickText16setBottomPaddingEd(
    QQuickText *self,
    qreal padding) {
  self->setBottomPadding(padding);
}

//  void QQuickText::resetBottomPadding()
extern "C" Q_DECL_EXPORT
void ritual_ZN10QQuickText18resetBottomPaddingEv(QQuickText *self) {
  self->resetBottomPadding();
}

//  QJSValue QQuickText::fontInfo() const
extern "C" Q_DECL_EXPORT
QJSValue *ritual_ZNK10QQuickText8fontInfoEv(const QQuickText *self) {
  return new QJSValue(self->fontInfo());
}

//  QSizeF QQuickText::advance() const
extern "C" Q_DECL_EXPORT
QSizeF *ritual_ZNK10QQuickText7advanceEv(const QQuickText *self) {
  return new QSizeF(self->advance());
}

//  void QQuickText::invalidate()
extern "C" Q_DECL_EXPORT
void ritual_ZN10QQuickText10invalidateEv(QQuickText *self) {
  self->invalidate();
}

//  void QQuickText::mousePressEvent(QMouseEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QQuickText15mousePressEventEP11QMouseEvent(
    QQuickText *self,
    QMouseEvent *event) {
  self->mousePressEvent(event);
}

//  void QQuickText::mouseReleaseEvent(QMouseEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QQuickText17mouseReleaseEventEP11QMouseEvent(
    QQuickText *self,
    QMouseEvent *event) {
  self->mouseReleaseEvent(event);
}

//  void QQuickText::itemChange(ItemChange change, const ItemChangeData
//      &value)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QQuickText10itemChangeEN10QQuickItem10ItemChangeERKNS0_14ItemChangeDataE(
    QQuickText *self,
    QQuickItem::ItemChange change,
    const QQuickItem::ItemChangeData *value) {
  self->itemChange(change, *value);
}

//  void QQuickText::geometryChange(const QRectF &newGeometry, const QRectF
//      &oldGeometry)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QQuickText14geometryChangeERK6QRectFS2_(
    QQuickText *self,
    const QRectF *newGeometry,
    const QRectF *oldGeometry) {
  self->geometryChange(*newGeometry, *oldGeometry);
}

//  QSGNode *QQuickText::updatePaintNode(QSGNode *a0, UpdatePaintNodeData
//      *a1)
extern "C" Q_DECL_EXPORT
QSGNode *ritual_ZN10QQuickText15updatePaintNodeEP7QSGNodePN10QQuickItem19UpdatePaintNodeDataE(
    QQuickText *self,
    QSGNode *a0,
    QQuickItem::UpdatePaintNodeData *a1) {
  return self->updatePaintNode(a0, a1);
}

//  void QQuickText::updatePolish()
extern "C" Q_DECL_EXPORT
void ritual_ZN10QQuickText12updatePolishEv(QQuickText *self) {
  self->updatePolish();
}

//  void QQuickText::hoverEnterEvent(QHoverEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QQuickText15hoverEnterEventEP11QHoverEvent(
    QQuickText *self,
    QHoverEvent *event) {
  self->hoverEnterEvent(event);
}

//  void QQuickText::hoverMoveEvent(QHoverEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QQuickText14hoverMoveEventEP11QHoverEvent(
    QQuickText *self,
    QHoverEvent *event) {
  self->hoverMoveEvent(event);
}

//  void QQuickText::hoverLeaveEvent(QHoverEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QQuickText15hoverLeaveEventEP11QHoverEvent(
    QQuickText *self,
    QHoverEvent *event) {
  self->hoverLeaveEvent(event);
}

//  void QQuickText::invalidateFontCaches()
extern "C" Q_DECL_EXPORT
void ritual_ZN10QQuickText20invalidateFontCachesEv(QQuickText *self) {
  self->invalidateFontCaches();
}

//  void QQuickText::q_updateLayout()
extern "C" Q_DECL_EXPORT
void ritual_ZN10QQuickText14q_updateLayoutEv(QQuickText *self) {
  self->q_updateLayout();
}

//  void QQuickText::triggerPreprocess()
extern "C" Q_DECL_EXPORT
void ritual_ZN10QQuickText17triggerPreprocessEv(QQuickText *self) {
  self->triggerPreprocess();
}

//  QVariant QQuickText::loadResource(int type, const QUrl &source)
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZN10QQuickText12loadResourceEiRK4QUrl(
    QQuickText *self,
    int type,
    const QUrl *source) {
  return new QVariant(self->loadResource(type, *source));
}

//  void QQuickText::resourceRequestFinished()
extern "C" Q_DECL_EXPORT
void ritual_ZN10QQuickText23resourceRequestFinishedEv(QQuickText *self) {
  self->resourceRequestFinished();
}

//  void QQuickText::imageDownloadFinished()
extern "C" Q_DECL_EXPORT
void ritual_ZN10QQuickText21imageDownloadFinishedEv(QQuickText *self) {
  self->imageDownloadFinished();
}

//  QQuickTextPrivate *QQuickText::d_func()
extern "C" Q_DECL_EXPORT
QQuickTextPrivate *ritual_ZN10QQuickText6d_funcEv(QQuickText *self) {
  return self->d_func();
}

//  const QQuickTextPrivate *QQuickText::d_func() const
extern "C" Q_DECL_EXPORT
const QQuickTextPrivate *ritual_ZNK10QQuickText6d_funcEv(
    const QQuickText *self) {
  return self->d_func();
}

//  QQuickText as the QQuickTextInterface it is built on
extern "C" Q_DECL_EXPORT
QQuickTextInterface *ritual_cast_QQuickText_QQuickTextInterface(
    QQuickText *self) {
  return static_cast<QQuickTextInterface *>(self);
}

//  a Python function taken by a CuteQQuickText, for the function named by
//      the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQuickText(QQuickText *self, const char *key, void *call) {
  return static_cast<CuteQQuickText *>(self)->take(key, call);
}

//  void QQuickText::componentComplete()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN10QQuickText17componentCompleteEv(QQuickText *self) {
  self->QQuickText::componentComplete();
}

//  QRectF QQuickText::boundingRect() const
extern "C" Q_DECL_EXPORT
QRectF *ritual_own_ZNK10QQuickText12boundingRectEv(const QQuickText *self) {
  return new QRectF(self->QQuickText::boundingRect());
}

//  QRectF QQuickText::clipRect() const
extern "C" Q_DECL_EXPORT
QRectF *ritual_own_ZNK10QQuickText8clipRectEv(const QQuickText *self) {
  return new QRectF(self->QQuickText::clipRect());
}

//  void QQuickText::invalidate()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN10QQuickText10invalidateEv(QQuickText *self) {
  self->QQuickText::invalidate();
}

//  void QQuickText::mousePressEvent(QMouseEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN10QQuickText15mousePressEventEP11QMouseEvent(
    QQuickText *self,
    QMouseEvent *event) {
  static_cast<OwnQQuickText *>(self)->OwnQQuickText::mousePressEvent(event);
}

//  void QQuickText::mouseReleaseEvent(QMouseEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN10QQuickText17mouseReleaseEventEP11QMouseEvent(
    QQuickText *self,
    QMouseEvent *event) {
  static_cast<OwnQQuickText *>(self)->OwnQQuickText::mouseReleaseEvent(
      event);
}

//  void QQuickText::itemChange(ItemChange change, const ItemChangeData
//      &value)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN10QQuickText10itemChangeEN10QQuickItem10ItemChangeERKNS0_14ItemChangeDataE(
    QQuickText *self,
    QQuickItem::ItemChange change,
    const QQuickItem::ItemChangeData *value) {
  static_cast<OwnQQuickText *>(self)->OwnQQuickText::itemChange(
      change,
      *value);
}

//  void QQuickText::geometryChange(const QRectF &newGeometry, const QRectF
//      &oldGeometry)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN10QQuickText14geometryChangeERK6QRectFS2_(
    QQuickText *self,
    const QRectF *newGeometry,
    const QRectF *oldGeometry) {
  static_cast<OwnQQuickText *>(self)->OwnQQuickText::geometryChange(
      *newGeometry,
      *oldGeometry);
}

//  QSGNode *QQuickText::updatePaintNode(QSGNode *a0, UpdatePaintNodeData
//      *a1)
extern "C" Q_DECL_EXPORT
QSGNode *ritual_own_ZN10QQuickText15updatePaintNodeEP7QSGNodePN10QQuickItem19UpdatePaintNodeDataE(
    QQuickText *self,
    QSGNode *a0,
    QQuickItem::UpdatePaintNodeData *a1) {
  return static_cast<OwnQQuickText *>(self)->OwnQQuickText::updatePaintNode(
      a0,
      a1);
}

//  void QQuickText::updatePolish()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN10QQuickText12updatePolishEv(QQuickText *self) {
  static_cast<OwnQQuickText *>(self)->OwnQQuickText::updatePolish();
}

//  void QQuickText::hoverEnterEvent(QHoverEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN10QQuickText15hoverEnterEventEP11QHoverEvent(
    QQuickText *self,
    QHoverEvent *event) {
  static_cast<OwnQQuickText *>(self)->OwnQQuickText::hoverEnterEvent(event);
}

//  void QQuickText::hoverMoveEvent(QHoverEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN10QQuickText14hoverMoveEventEP11QHoverEvent(
    QQuickText *self,
    QHoverEvent *event) {
  static_cast<OwnQQuickText *>(self)->OwnQQuickText::hoverMoveEvent(event);
}

//  void QQuickText::hoverLeaveEvent(QHoverEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN10QQuickText15hoverLeaveEventEP11QHoverEvent(
    QQuickText *self,
    QHoverEvent *event) {
  static_cast<OwnQQuickText *>(self)->OwnQQuickText::hoverLeaveEvent(event);
}
