//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/6.12.0/QtQuick/private/qquickmultipointtoucharea_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtGui/qtguiglobal.h>
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qquickmultipointtoucharea_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qobject.h>
#include <QtCore/qrect.h>
#include <QtCore/qpoint.h>
#include <QtCore/qvariant.h>
#include <QtQuick/qquickitem.h>
#include <QtCore/qmetaobject.h>
#include <QtCore/qlist.h>
#include <cstring>
#include <QtQml/QQmlListProperty>

//  Only a class built on QQuickMultiPointTouchArea may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQQuickMultiPointTouchArea : QQuickMultiPointTouchArea {
  using QQuickMultiPointTouchArea::touchEvent;
  using QQuickMultiPointTouchArea::childMouseEventFilter;
  using QQuickMultiPointTouchArea::mousePressEvent;
  using QQuickMultiPointTouchArea::mouseReleaseEvent;
  using QQuickMultiPointTouchArea::mouseMoveEvent;
  using QQuickMultiPointTouchArea::mouseUngrabEvent;
  using QQuickMultiPointTouchArea::touchUngrabEvent;
  using QQuickMultiPointTouchArea::updatePaintNode;
};

//  A QQuickMultiPointTouchArea that Python can take functions over in. Every QQuickMultiPointTouchArea
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQQuickMultiPointTouchAreaCall0)(const void *, QTouchEvent *, int *);
typedef bool (*CuteQQuickMultiPointTouchAreaCall1)(const void *, QQuickItem *, QEvent *, int *);
typedef void (*CuteQQuickMultiPointTouchAreaCall2)(const void *, QMouseEvent *, int *);
typedef void (*CuteQQuickMultiPointTouchAreaCall3)(const void *, QMouseEvent *, int *);
typedef void (*CuteQQuickMultiPointTouchAreaCall4)(const void *, QMouseEvent *, int *);
typedef void (*CuteQQuickMultiPointTouchAreaCall5)(const void *, int *);
typedef void (*CuteQQuickMultiPointTouchAreaCall6)(const void *, int *);
typedef void * (*CuteQQuickMultiPointTouchAreaCall7)(const void *, QSGNode *, QQuickItem::UpdatePaintNodeData *, int *);
typedef const QRectF * (*CuteQQuickMultiPointTouchAreaCall8)(const void *, int *);
typedef const QRectF * (*CuteQQuickMultiPointTouchAreaCall9)(const void *, int *);
typedef bool (*CuteQQuickMultiPointTouchAreaCall10)(const void *, const QPointF *, int *);
#if QT_CONFIG(im)
typedef const QVariant * (*CuteQQuickMultiPointTouchAreaCall11)(const void *, int, int *);
#endif  // QT_CONFIG(im)
typedef bool (*CuteQQuickMultiPointTouchAreaCall12)(const void *, int *);
typedef void * (*CuteQQuickMultiPointTouchAreaCall13)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickMultiPointTouchAreaCall14)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickMultiPointTouchAreaCall15)(const void *, int, const QQuickItem::ItemChangeData *, int *);
typedef void (*CuteQQuickMultiPointTouchAreaCall16)(const void *, const QRectF *, const QRectF *, int *);
typedef void (*CuteQQuickMultiPointTouchAreaCall17)(const void *, int *);
typedef void (*CuteQQuickMultiPointTouchAreaCall18)(const void *, int *);
typedef void (*CuteQQuickMultiPointTouchAreaCall19)(const void *, QKeyEvent *, int *);
typedef void (*CuteQQuickMultiPointTouchAreaCall20)(const void *, QKeyEvent *, int *);
#if QT_CONFIG(im)
typedef void (*CuteQQuickMultiPointTouchAreaCall21)(const void *, QInputMethodEvent *, int *);
#endif  // QT_CONFIG(im)
typedef void (*CuteQQuickMultiPointTouchAreaCall22)(const void *, QFocusEvent *, int *);
typedef void (*CuteQQuickMultiPointTouchAreaCall23)(const void *, QFocusEvent *, int *);
typedef void (*CuteQQuickMultiPointTouchAreaCall24)(const void *, QMouseEvent *, int *);
#if QT_CONFIG(wheelevent)
typedef void (*CuteQQuickMultiPointTouchAreaCall25)(const void *, QWheelEvent *, int *);
#endif  // QT_CONFIG(wheelevent)
typedef void (*CuteQQuickMultiPointTouchAreaCall26)(const void *, QHoverEvent *, int *);
typedef void (*CuteQQuickMultiPointTouchAreaCall27)(const void *, QHoverEvent *, int *);
typedef void (*CuteQQuickMultiPointTouchAreaCall28)(const void *, QHoverEvent *, int *);
#if QT_CONFIG(quick_draganddrop)
typedef void (*CuteQQuickMultiPointTouchAreaCall29)(const void *, QDragEnterEvent *, int *);
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
typedef void (*CuteQQuickMultiPointTouchAreaCall30)(const void *, QDragMoveEvent *, int *);
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
typedef void (*CuteQQuickMultiPointTouchAreaCall31)(const void *, QDragLeaveEvent *, int *);
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
typedef void (*CuteQQuickMultiPointTouchAreaCall32)(const void *, QDropEvent *, int *);
#endif  // QT_CONFIG(quick_draganddrop)
typedef void (*CuteQQuickMultiPointTouchAreaCall33)(const void *, int *);
typedef void (*CuteQQuickMultiPointTouchAreaCall34)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickMultiPointTouchAreaCall35)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickMultiPointTouchAreaCall36)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickMultiPointTouchAreaCall37)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickMultiPointTouchAreaCall38)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickMultiPointTouchAreaCall39)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickMultiPointTouchAreaCall40)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQQuickMultiPointTouchArea : public QQuickMultiPointTouchArea {
public:
  using QQuickMultiPointTouchArea::QQuickMultiPointTouchArea;
  void *taken[41] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN10QQuickItem10touchEventEP11QTouchEvent")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem21childMouseEventFilterEPS_P6QEvent")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem15mousePressEventEP11QMouseEvent")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem17mouseReleaseEventEP11QMouseEvent")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem14mouseMoveEventEP11QMouseEvent")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem16mouseUngrabEventEv")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem16touchUngrabEventEv")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem15updatePaintNodeEP7QSGNodePNS_19UpdatePaintNodeDataE")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK10QQuickItem12boundingRectEv")) {
      taken[8] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK10QQuickItem8clipRectEv")) {
      taken[9] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK10QQuickItem8containsERK7QPointF")) {
      taken[10] = call;
      return true;
    }
#if QT_CONFIG(im)
    if (!std::strcmp(key, "_ZNK10QQuickItem16inputMethodQueryEN2Qt16InputMethodQueryE")) {
      taken[11] = call;
      return true;
    }
#endif  // QT_CONFIG(im)
    if (!std::strcmp(key, "_ZNK10QQuickItem17isTextureProviderEv")) {
      taken[12] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK10QQuickItem15textureProviderEv")) {
      taken[13] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[14] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN10QQuickItem10itemChangeENS_10ItemChangeERKNS_14ItemChangeDataE")) {
      taken[15] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem14geometryChangeERK6QRectFS2_")) {
      taken[16] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQmlParserStatus10classBeginEv")) {
      taken[17] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQmlParserStatus17componentCompleteEv")) {
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
    if (!std::strcmp(key, "_ZN10QQuickItem21mouseDoubleClickEventEP11QMouseEvent")) {
      taken[24] = call;
      return true;
    }
#if QT_CONFIG(wheelevent)
    if (!std::strcmp(key, "_ZN10QQuickItem10wheelEventEP11QWheelEvent")) {
      taken[25] = call;
      return true;
    }
#endif  // QT_CONFIG(wheelevent)
    if (!std::strcmp(key, "_ZN10QQuickItem15hoverEnterEventEP11QHoverEvent")) {
      taken[26] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem14hoverMoveEventEP11QHoverEvent")) {
      taken[27] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem15hoverLeaveEventEP11QHoverEvent")) {
      taken[28] = call;
      return true;
    }
#if QT_CONFIG(quick_draganddrop)
    if (!std::strcmp(key, "_ZN10QQuickItem14dragEnterEventEP15QDragEnterEvent")) {
      taken[29] = call;
      return true;
    }
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
    if (!std::strcmp(key, "_ZN10QQuickItem13dragMoveEventEP14QDragMoveEvent")) {
      taken[30] = call;
      return true;
    }
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
    if (!std::strcmp(key, "_ZN10QQuickItem14dragLeaveEventEP15QDragLeaveEvent")) {
      taken[31] = call;
      return true;
    }
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
    if (!std::strcmp(key, "_ZN10QQuickItem9dropEventEP10QDropEvent")) {
      taken[32] = call;
      return true;
    }
#endif  // QT_CONFIG(quick_draganddrop)
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

  //  void QQuickMultiPointTouchArea::touchEvent(QTouchEvent *a0)
  void touchEvent(QTouchEvent *a0) override {
    if (taken[0]) {
      int handled = 0;
      CuteQQuickMultiPointTouchAreaCall0 call = reinterpret_cast<CuteQQuickMultiPointTouchAreaCall0>(taken[0]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickMultiPointTouchArea::touchEvent(a0);
  }

  //  bool QQuickMultiPointTouchArea::childMouseEventFilter(QQuickItem
  //      *receiver, QEvent *event)
  bool childMouseEventFilter(QQuickItem *receiver, QEvent *event) override {
    if (taken[1]) {
      int handled = 0;
      CuteQQuickMultiPointTouchAreaCall1 call = reinterpret_cast<CuteQQuickMultiPointTouchAreaCall1>(taken[1]);
      bool given = call(this, receiver, event, &handled);
      if (handled) return given;
    }
    return QQuickMultiPointTouchArea::childMouseEventFilter(receiver, event);
  }

  //  void QQuickMultiPointTouchArea::mousePressEvent(QMouseEvent *event)
  void mousePressEvent(QMouseEvent *event) override {
    if (taken[2]) {
      int handled = 0;
      CuteQQuickMultiPointTouchAreaCall2 call = reinterpret_cast<CuteQQuickMultiPointTouchAreaCall2>(taken[2]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickMultiPointTouchArea::mousePressEvent(event);
  }

  //  void QQuickMultiPointTouchArea::mouseReleaseEvent(QMouseEvent *event)
  void mouseReleaseEvent(QMouseEvent *event) override {
    if (taken[3]) {
      int handled = 0;
      CuteQQuickMultiPointTouchAreaCall3 call = reinterpret_cast<CuteQQuickMultiPointTouchAreaCall3>(taken[3]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickMultiPointTouchArea::mouseReleaseEvent(event);
  }

  //  void QQuickMultiPointTouchArea::mouseMoveEvent(QMouseEvent *event)
  void mouseMoveEvent(QMouseEvent *event) override {
    if (taken[4]) {
      int handled = 0;
      CuteQQuickMultiPointTouchAreaCall4 call = reinterpret_cast<CuteQQuickMultiPointTouchAreaCall4>(taken[4]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickMultiPointTouchArea::mouseMoveEvent(event);
  }

  //  void QQuickMultiPointTouchArea::mouseUngrabEvent()
  void mouseUngrabEvent() override {
    if (taken[5]) {
      int handled = 0;
      CuteQQuickMultiPointTouchAreaCall5 call = reinterpret_cast<CuteQQuickMultiPointTouchAreaCall5>(taken[5]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickMultiPointTouchArea::mouseUngrabEvent();
  }

  //  void QQuickMultiPointTouchArea::touchUngrabEvent()
  void touchUngrabEvent() override {
    if (taken[6]) {
      int handled = 0;
      CuteQQuickMultiPointTouchAreaCall6 call = reinterpret_cast<CuteQQuickMultiPointTouchAreaCall6>(taken[6]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickMultiPointTouchArea::touchUngrabEvent();
  }

  //  QSGNode *QQuickMultiPointTouchArea::updatePaintNode(QSGNode *a0,
  //      UpdatePaintNodeData *a1)
  QSGNode *updatePaintNode(
      QSGNode *a0,
      QQuickItem::UpdatePaintNodeData *a1) override {
    if (taken[7]) {
      int handled = 0;
      CuteQQuickMultiPointTouchAreaCall7 call = reinterpret_cast<CuteQQuickMultiPointTouchAreaCall7>(taken[7]);
      void * given = call(this, a0, a1, &handled);
      if (handled) return static_cast<QSGNode *>(given);
    }
    return QQuickMultiPointTouchArea::updatePaintNode(a0, a1);
  }

  //  QRectF QQuickItem::boundingRect() const
  QRectF boundingRect() const override {
    if (taken[8]) {
      int handled = 0;
      CuteQQuickMultiPointTouchAreaCall8 call = reinterpret_cast<CuteQQuickMultiPointTouchAreaCall8>(taken[8]);
      const QRectF * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QQuickItem::boundingRect();
  }

  //  QRectF QQuickItem::clipRect() const
  QRectF clipRect() const override {
    if (taken[9]) {
      int handled = 0;
      CuteQQuickMultiPointTouchAreaCall9 call = reinterpret_cast<CuteQQuickMultiPointTouchAreaCall9>(taken[9]);
      const QRectF * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QQuickItem::clipRect();
  }

  //  bool QQuickItem::contains(const QPointF &point) const
  bool contains(const QPointF &point) const override {
    if (taken[10]) {
      int handled = 0;
      CuteQQuickMultiPointTouchAreaCall10 call = reinterpret_cast<CuteQQuickMultiPointTouchAreaCall10>(taken[10]);
      bool given = call(this, &point, &handled);
      if (handled) return given;
    }
    return QQuickItem::contains(point);
  }

#if QT_CONFIG(im)
  //  QVariant QQuickItem::inputMethodQuery(Qt::InputMethodQuery query)
  //      const
  QVariant inputMethodQuery(Qt::InputMethodQuery query) const override {
    if (taken[11]) {
      int handled = 0;
      CuteQQuickMultiPointTouchAreaCall11 call = reinterpret_cast<CuteQQuickMultiPointTouchAreaCall11>(taken[11]);
      const QVariant * given = call(this, static_cast<int>(query), &handled);
      if (handled && given) return *given;
    }
    return QQuickItem::inputMethodQuery(query);
  }
#endif  // QT_CONFIG(im)

  //  bool QQuickItem::isTextureProvider() const
  bool isTextureProvider() const override {
    if (taken[12]) {
      int handled = 0;
      CuteQQuickMultiPointTouchAreaCall12 call = reinterpret_cast<CuteQQuickMultiPointTouchAreaCall12>(taken[12]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QQuickItem::isTextureProvider();
  }

  //  QSGTextureProvider *QQuickItem::textureProvider() const
  QSGTextureProvider *textureProvider() const override {
    if (taken[13]) {
      int handled = 0;
      CuteQQuickMultiPointTouchAreaCall13 call = reinterpret_cast<CuteQQuickMultiPointTouchAreaCall13>(taken[13]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QSGTextureProvider *>(given);
    }
    return QQuickItem::textureProvider();
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QQuickItem::event(QEvent *a0)
  bool event(QEvent *a0) override {
    if (taken[14]) {
      int handled = 0;
      CuteQQuickMultiPointTouchAreaCall14 call = reinterpret_cast<CuteQQuickMultiPointTouchAreaCall14>(taken[14]);
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
    if (taken[15]) {
      int handled = 0;
      CuteQQuickMultiPointTouchAreaCall15 call = reinterpret_cast<CuteQQuickMultiPointTouchAreaCall15>(taken[15]);
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
    if (taken[16]) {
      int handled = 0;
      CuteQQuickMultiPointTouchAreaCall16 call = reinterpret_cast<CuteQQuickMultiPointTouchAreaCall16>(taken[16]);
      call(this, &newGeometry, &oldGeometry, &handled);
      if (handled) return;
    }
    QQuickItem::geometryChange(newGeometry, oldGeometry);
  }

  //  void QQuickItem::classBegin()
  void classBegin() override {
    if (taken[17]) {
      int handled = 0;
      CuteQQuickMultiPointTouchAreaCall17 call = reinterpret_cast<CuteQQuickMultiPointTouchAreaCall17>(taken[17]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItem::classBegin();
  }

  //  void QQuickItem::componentComplete()
  void componentComplete() override {
    if (taken[18]) {
      int handled = 0;
      CuteQQuickMultiPointTouchAreaCall18 call = reinterpret_cast<CuteQQuickMultiPointTouchAreaCall18>(taken[18]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItem::componentComplete();
  }

  //  void QQuickItem::keyPressEvent(QKeyEvent *event)
  void keyPressEvent(QKeyEvent *event) override {
    if (taken[19]) {
      int handled = 0;
      CuteQQuickMultiPointTouchAreaCall19 call = reinterpret_cast<CuteQQuickMultiPointTouchAreaCall19>(taken[19]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::keyPressEvent(event);
  }

  //  void QQuickItem::keyReleaseEvent(QKeyEvent *event)
  void keyReleaseEvent(QKeyEvent *event) override {
    if (taken[20]) {
      int handled = 0;
      CuteQQuickMultiPointTouchAreaCall20 call = reinterpret_cast<CuteQQuickMultiPointTouchAreaCall20>(taken[20]);
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
      CuteQQuickMultiPointTouchAreaCall21 call = reinterpret_cast<CuteQQuickMultiPointTouchAreaCall21>(taken[21]);
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
      CuteQQuickMultiPointTouchAreaCall22 call = reinterpret_cast<CuteQQuickMultiPointTouchAreaCall22>(taken[22]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItem::focusInEvent(a0);
  }

  //  void QQuickItem::focusOutEvent(QFocusEvent *a0)
  void focusOutEvent(QFocusEvent *a0) override {
    if (taken[23]) {
      int handled = 0;
      CuteQQuickMultiPointTouchAreaCall23 call = reinterpret_cast<CuteQQuickMultiPointTouchAreaCall23>(taken[23]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItem::focusOutEvent(a0);
  }

  //  void QQuickItem::mouseDoubleClickEvent(QMouseEvent *event)
  void mouseDoubleClickEvent(QMouseEvent *event) override {
    if (taken[24]) {
      int handled = 0;
      CuteQQuickMultiPointTouchAreaCall24 call = reinterpret_cast<CuteQQuickMultiPointTouchAreaCall24>(taken[24]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::mouseDoubleClickEvent(event);
  }

#if QT_CONFIG(wheelevent)
  //  void QQuickItem::wheelEvent(QWheelEvent *event)
  void wheelEvent(QWheelEvent *event) override {
    if (taken[25]) {
      int handled = 0;
      CuteQQuickMultiPointTouchAreaCall25 call = reinterpret_cast<CuteQQuickMultiPointTouchAreaCall25>(taken[25]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::wheelEvent(event);
  }
#endif  // QT_CONFIG(wheelevent)

  //  void QQuickItem::hoverEnterEvent(QHoverEvent *event)
  void hoverEnterEvent(QHoverEvent *event) override {
    if (taken[26]) {
      int handled = 0;
      CuteQQuickMultiPointTouchAreaCall26 call = reinterpret_cast<CuteQQuickMultiPointTouchAreaCall26>(taken[26]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::hoverEnterEvent(event);
  }

  //  void QQuickItem::hoverMoveEvent(QHoverEvent *event)
  void hoverMoveEvent(QHoverEvent *event) override {
    if (taken[27]) {
      int handled = 0;
      CuteQQuickMultiPointTouchAreaCall27 call = reinterpret_cast<CuteQQuickMultiPointTouchAreaCall27>(taken[27]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::hoverMoveEvent(event);
  }

  //  void QQuickItem::hoverLeaveEvent(QHoverEvent *event)
  void hoverLeaveEvent(QHoverEvent *event) override {
    if (taken[28]) {
      int handled = 0;
      CuteQQuickMultiPointTouchAreaCall28 call = reinterpret_cast<CuteQQuickMultiPointTouchAreaCall28>(taken[28]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::hoverLeaveEvent(event);
  }

#if QT_CONFIG(quick_draganddrop)
  //  void QQuickItem::dragEnterEvent(QDragEnterEvent *a0)
  void dragEnterEvent(QDragEnterEvent *a0) override {
    if (taken[29]) {
      int handled = 0;
      CuteQQuickMultiPointTouchAreaCall29 call = reinterpret_cast<CuteQQuickMultiPointTouchAreaCall29>(taken[29]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItem::dragEnterEvent(a0);
  }
#endif  // QT_CONFIG(quick_draganddrop)

#if QT_CONFIG(quick_draganddrop)
  //  void QQuickItem::dragMoveEvent(QDragMoveEvent *a0)
  void dragMoveEvent(QDragMoveEvent *a0) override {
    if (taken[30]) {
      int handled = 0;
      CuteQQuickMultiPointTouchAreaCall30 call = reinterpret_cast<CuteQQuickMultiPointTouchAreaCall30>(taken[30]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItem::dragMoveEvent(a0);
  }
#endif  // QT_CONFIG(quick_draganddrop)

#if QT_CONFIG(quick_draganddrop)
  //  void QQuickItem::dragLeaveEvent(QDragLeaveEvent *a0)
  void dragLeaveEvent(QDragLeaveEvent *a0) override {
    if (taken[31]) {
      int handled = 0;
      CuteQQuickMultiPointTouchAreaCall31 call = reinterpret_cast<CuteQQuickMultiPointTouchAreaCall31>(taken[31]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItem::dragLeaveEvent(a0);
  }
#endif  // QT_CONFIG(quick_draganddrop)

#if QT_CONFIG(quick_draganddrop)
  //  void QQuickItem::dropEvent(QDropEvent *a0)
  void dropEvent(QDropEvent *a0) override {
    if (taken[32]) {
      int handled = 0;
      CuteQQuickMultiPointTouchAreaCall32 call = reinterpret_cast<CuteQQuickMultiPointTouchAreaCall32>(taken[32]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItem::dropEvent(a0);
  }
#endif  // QT_CONFIG(quick_draganddrop)

  //  void QQuickItem::releaseResources()
  void releaseResources() override {
    if (taken[33]) {
      int handled = 0;
      CuteQQuickMultiPointTouchAreaCall33 call = reinterpret_cast<CuteQQuickMultiPointTouchAreaCall33>(taken[33]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItem::releaseResources();
  }

  //  void QQuickItem::updatePolish()
  void updatePolish() override {
    if (taken[34]) {
      int handled = 0;
      CuteQQuickMultiPointTouchAreaCall34 call = reinterpret_cast<CuteQQuickMultiPointTouchAreaCall34>(taken[34]);
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
      CuteQQuickMultiPointTouchAreaCall35 call = reinterpret_cast<CuteQQuickMultiPointTouchAreaCall35>(taken[35]);
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
      CuteQQuickMultiPointTouchAreaCall36 call = reinterpret_cast<CuteQQuickMultiPointTouchAreaCall36>(taken[36]);
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
      CuteQQuickMultiPointTouchAreaCall37 call = reinterpret_cast<CuteQQuickMultiPointTouchAreaCall37>(taken[37]);
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
      CuteQQuickMultiPointTouchAreaCall38 call = reinterpret_cast<CuteQQuickMultiPointTouchAreaCall38>(taken[38]);
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
      CuteQQuickMultiPointTouchAreaCall39 call = reinterpret_cast<CuteQQuickMultiPointTouchAreaCall39>(taken[39]);
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
      CuteQQuickMultiPointTouchAreaCall40 call = reinterpret_cast<CuteQQuickMultiPointTouchAreaCall40>(taken[40]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QQuickMultiPointTouchArea::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK25QQuickMultiPointTouchArea10metaObjectEv(
    const QQuickMultiPointTouchArea *self) {
  return self->metaObject();
}

//  void *QQuickMultiPointTouchArea::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN25QQuickMultiPointTouchArea11qt_metacastEPKc(
    QQuickMultiPointTouchArea *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QQuickMultiPointTouchArea::qt_metacall(QMetaObject::Call a0, int a1,
//      void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN25QQuickMultiPointTouchArea11qt_metacallEN11QMetaObject4CallEiPPv(
    QQuickMultiPointTouchArea *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QQuickMultiPointTouchArea::tr(const char *s, const char *c, int
//      n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN25QQuickMultiPointTouchArea2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuickMultiPointTouchArea::tr(s, c, n));
}

//  QQuickMultiPointTouchArea::QQuickMultiPointTouchArea(QQuickItem *parent)
extern "C" Q_DECL_EXPORT
QQuickMultiPointTouchArea *ritual_ZN25QQuickMultiPointTouchAreaC1EP10QQuickItem(
    QQuickItem *parent) {
  return new CuteQQuickMultiPointTouchArea(parent);
}

//  QQuickMultiPointTouchArea::~QQuickMultiPointTouchArea()
extern "C" Q_DECL_EXPORT
void ritual_ZN25QQuickMultiPointTouchAreaD1Ev(
    QQuickMultiPointTouchArea *self) {
  delete self;
}

//  int QQuickMultiPointTouchArea::minimumTouchPoints() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK25QQuickMultiPointTouchArea18minimumTouchPointsEv(
    const QQuickMultiPointTouchArea *self) {
  return self->minimumTouchPoints();
}

//  void QQuickMultiPointTouchArea::setMinimumTouchPoints(int num)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QQuickMultiPointTouchArea21setMinimumTouchPointsEi(
    QQuickMultiPointTouchArea *self,
    int num) {
  self->setMinimumTouchPoints(num);
}

//  int QQuickMultiPointTouchArea::maximumTouchPoints() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK25QQuickMultiPointTouchArea18maximumTouchPointsEv(
    const QQuickMultiPointTouchArea *self) {
  return self->maximumTouchPoints();
}

//  void QQuickMultiPointTouchArea::setMaximumTouchPoints(int num)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QQuickMultiPointTouchArea21setMaximumTouchPointsEi(
    QQuickMultiPointTouchArea *self,
    int num) {
  self->setMaximumTouchPoints(num);
}

//  bool QQuickMultiPointTouchArea::mouseEnabled() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK25QQuickMultiPointTouchArea12mouseEnabledEv(
    const QQuickMultiPointTouchArea *self) {
  return self->mouseEnabled();
}

//  void QQuickMultiPointTouchArea::setMouseEnabled(bool arg)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QQuickMultiPointTouchArea15setMouseEnabledEb(
    QQuickMultiPointTouchArea *self,
    bool arg) {
  self->setMouseEnabled(arg);
}

//  QQmlListProperty<QQuickTouchPoint>
//      QQuickMultiPointTouchArea::touchPoints()
extern "C" Q_DECL_EXPORT
QQmlListProperty<QQuickTouchPoint> *ritual_ZN25QQuickMultiPointTouchArea11touchPointsEv(
    QQuickMultiPointTouchArea *self) {
  return new QQmlListProperty<QQuickTouchPoint>(self->touchPoints());
}

//  void QQuickMultiPointTouchArea::touchPoint_append(QQmlListProperty<QQuick
//      TouchPoint> *list, QQuickTouchPoint *touch)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QQuickMultiPointTouchArea17touchPoint_appendEP16QQmlListPropertyI16QQuickTouchPointEPS1_(
    QQmlListProperty<QQuickTouchPoint> *list,
    QQuickTouchPoint *touch) {
  QQuickMultiPointTouchArea::touchPoint_append(list, touch);
}

//  qsizetype QQuickMultiPointTouchArea::touchPoint_count(QQmlListProperty<QQ
//      uickTouchPoint> *list)
extern "C" Q_DECL_EXPORT
qsizetype ritual_ZN25QQuickMultiPointTouchArea16touchPoint_countEP16QQmlListPropertyI16QQuickTouchPointE(
    QQmlListProperty<QQuickTouchPoint> *list) {
  return QQuickMultiPointTouchArea::touchPoint_count(list);
}

//  QQuickTouchPoint *QQuickMultiPointTouchArea::touchPoint_at(QQmlListProper
//      ty<QQuickTouchPoint> *list, qsizetype index)
extern "C" Q_DECL_EXPORT
QQuickTouchPoint *ritual_ZN25QQuickMultiPointTouchArea13touchPoint_atEP16QQmlListPropertyI16QQuickTouchPointEx(
    QQmlListProperty<QQuickTouchPoint> *list,
    qsizetype index) {
  return QQuickMultiPointTouchArea::touchPoint_at(list, index);
}

#if QT_VERSION < QT_VERSION_CHECK(7, 0, 0)
//  void QQuickMultiPointTouchArea::pressed(const QList<QObject *>
//      &touchPoints)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QQuickMultiPointTouchArea7pressedERK5QListIP7QObjectE(
    QQuickMultiPointTouchArea *self,
    const QList<QObject *> *touchPoints) {
  self->pressed(*touchPoints);
}
#endif  // QT_VERSION < QT_VERSION_CHECK(7, 0, 0)

#if QT_VERSION < QT_VERSION_CHECK(7, 0, 0)
//  void QQuickMultiPointTouchArea::updated(const QList<QObject *>
//      &touchPoints)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QQuickMultiPointTouchArea7updatedERK5QListIP7QObjectE(
    QQuickMultiPointTouchArea *self,
    const QList<QObject *> *touchPoints) {
  self->updated(*touchPoints);
}
#endif  // QT_VERSION < QT_VERSION_CHECK(7, 0, 0)

#if QT_VERSION < QT_VERSION_CHECK(7, 0, 0)
//  void QQuickMultiPointTouchArea::released(const QList<QObject *>
//      &touchPoints)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QQuickMultiPointTouchArea8releasedERK5QListIP7QObjectE(
    QQuickMultiPointTouchArea *self,
    const QList<QObject *> *touchPoints) {
  self->released(*touchPoints);
}
#endif  // QT_VERSION < QT_VERSION_CHECK(7, 0, 0)

#if QT_VERSION < QT_VERSION_CHECK(7, 0, 0)
//  void QQuickMultiPointTouchArea::canceled(const QList<QObject *>
//      &touchPoints)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QQuickMultiPointTouchArea8canceledERK5QListIP7QObjectE(
    QQuickMultiPointTouchArea *self,
    const QList<QObject *> *touchPoints) {
  self->canceled(*touchPoints);
}
#endif  // QT_VERSION < QT_VERSION_CHECK(7, 0, 0)

//  void QQuickMultiPointTouchArea::gestureStarted(QQuickGrabGestureEvent
//      *gesture)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QQuickMultiPointTouchArea14gestureStartedEP22QQuickGrabGestureEvent(
    QQuickMultiPointTouchArea *self,
    QQuickGrabGestureEvent *gesture) {
  self->gestureStarted(gesture);
}

#if QT_VERSION < QT_VERSION_CHECK(7, 0, 0)
//  void QQuickMultiPointTouchArea::touchUpdated(const QList<QObject *>
//      &touchPoints)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QQuickMultiPointTouchArea12touchUpdatedERK5QListIP7QObjectE(
    QQuickMultiPointTouchArea *self,
    const QList<QObject *> *touchPoints) {
  self->touchUpdated(*touchPoints);
}
#endif  // QT_VERSION < QT_VERSION_CHECK(7, 0, 0)

//  void QQuickMultiPointTouchArea::minimumTouchPointsChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN25QQuickMultiPointTouchArea25minimumTouchPointsChangedEv(
    QQuickMultiPointTouchArea *self) {
  self->minimumTouchPointsChanged();
}

//  void QQuickMultiPointTouchArea::maximumTouchPointsChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN25QQuickMultiPointTouchArea25maximumTouchPointsChangedEv(
    QQuickMultiPointTouchArea *self) {
  self->maximumTouchPointsChanged();
}

//  void QQuickMultiPointTouchArea::mouseEnabledChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN25QQuickMultiPointTouchArea19mouseEnabledChangedEv(
    QQuickMultiPointTouchArea *self) {
  self->mouseEnabledChanged();
}

//  void QQuickMultiPointTouchArea::touchEvent(QTouchEvent *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QQuickMultiPointTouchArea10touchEventEP11QTouchEvent(
    QQuickMultiPointTouchArea *self,
    QTouchEvent *a0) {
  self->touchEvent(a0);
}

//  bool QQuickMultiPointTouchArea::childMouseEventFilter(QQuickItem
//      *receiver, QEvent *event)
extern "C" Q_DECL_EXPORT
bool ritual_ZN25QQuickMultiPointTouchArea21childMouseEventFilterEP10QQuickItemP6QEvent(
    QQuickMultiPointTouchArea *self,
    QQuickItem *receiver,
    QEvent *event) {
  return self->childMouseEventFilter(receiver, event);
}

//  void QQuickMultiPointTouchArea::mousePressEvent(QMouseEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QQuickMultiPointTouchArea15mousePressEventEP11QMouseEvent(
    QQuickMultiPointTouchArea *self,
    QMouseEvent *event) {
  self->mousePressEvent(event);
}

//  void QQuickMultiPointTouchArea::mouseReleaseEvent(QMouseEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QQuickMultiPointTouchArea17mouseReleaseEventEP11QMouseEvent(
    QQuickMultiPointTouchArea *self,
    QMouseEvent *event) {
  self->mouseReleaseEvent(event);
}

//  void QQuickMultiPointTouchArea::mouseMoveEvent(QMouseEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QQuickMultiPointTouchArea14mouseMoveEventEP11QMouseEvent(
    QQuickMultiPointTouchArea *self,
    QMouseEvent *event) {
  self->mouseMoveEvent(event);
}

//  void QQuickMultiPointTouchArea::mouseUngrabEvent()
extern "C" Q_DECL_EXPORT
void ritual_ZN25QQuickMultiPointTouchArea16mouseUngrabEventEv(
    QQuickMultiPointTouchArea *self) {
  self->mouseUngrabEvent();
}

//  void QQuickMultiPointTouchArea::touchUngrabEvent()
extern "C" Q_DECL_EXPORT
void ritual_ZN25QQuickMultiPointTouchArea16touchUngrabEventEv(
    QQuickMultiPointTouchArea *self) {
  self->touchUngrabEvent();
}

//  void QQuickMultiPointTouchArea::addTouchPrototype(QQuickTouchPoint
//      *prototype)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QQuickMultiPointTouchArea17addTouchPrototypeEP16QQuickTouchPoint(
    QQuickMultiPointTouchArea *self,
    QQuickTouchPoint *prototype) {
  self->addTouchPrototype(prototype);
}

//  void QQuickMultiPointTouchArea::addTouchPoint(const QEventPoint *p)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QQuickMultiPointTouchArea13addTouchPointEPK11QEventPoint(
    QQuickMultiPointTouchArea *self,
    const QEventPoint *p) {
  self->addTouchPoint(p);
}

//  void QQuickMultiPointTouchArea::addTouchPoint(const QMouseEvent *e)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QQuickMultiPointTouchArea13addTouchPointEPK11QMouseEvent(
    QQuickMultiPointTouchArea *self,
    const QMouseEvent *e) {
  self->addTouchPoint(e);
}

//  void QQuickMultiPointTouchArea::clearTouchLists()
extern "C" Q_DECL_EXPORT
void ritual_ZN25QQuickMultiPointTouchArea15clearTouchListsEv(
    QQuickMultiPointTouchArea *self) {
  self->clearTouchLists();
}

//  void QQuickMultiPointTouchArea::updateTouchPoint(QQuickTouchPoint *a0,
//      const QEventPoint *a1)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QQuickMultiPointTouchArea16updateTouchPointEP16QQuickTouchPointPK11QEventPoint(
    QQuickMultiPointTouchArea *self,
    QQuickTouchPoint *a0,
    const QEventPoint *a1) {
  self->updateTouchPoint(a0, a1);
}

//  void QQuickMultiPointTouchArea::updateTouchPoint(QQuickTouchPoint *dtp,
//      const QMouseEvent *e)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QQuickMultiPointTouchArea16updateTouchPointEP16QQuickTouchPointPK11QMouseEvent(
    QQuickMultiPointTouchArea *self,
    QQuickTouchPoint *dtp,
    const QMouseEvent *e) {
  self->updateTouchPoint(dtp, e);
}

//  void QQuickMultiPointTouchArea::updateTouchData(QEvent *a0,
//      RemapEventPoints remap)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QQuickMultiPointTouchArea15updateTouchDataEP6QEventNS_16RemapEventPointsE(
    QQuickMultiPointTouchArea *self,
    QEvent *a0,
    QQuickMultiPointTouchArea::RemapEventPoints remap) {
  self->updateTouchData(a0, remap);
}

//  bool QQuickMultiPointTouchArea::sendMouseEvent(QMouseEvent *event)
extern "C" Q_DECL_EXPORT
bool ritual_ZN25QQuickMultiPointTouchArea14sendMouseEventEP11QMouseEvent(
    QQuickMultiPointTouchArea *self,
    QMouseEvent *event) {
  return self->sendMouseEvent(event);
}

//  bool QQuickMultiPointTouchArea::shouldFilter(QEvent *event)
extern "C" Q_DECL_EXPORT
bool ritual_ZN25QQuickMultiPointTouchArea12shouldFilterEP6QEvent(
    QQuickMultiPointTouchArea *self,
    QEvent *event) {
  return self->shouldFilter(event);
}

//  void QQuickMultiPointTouchArea::grabGesture(QPointingDevice *dev)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QQuickMultiPointTouchArea11grabGestureEP15QPointingDevice(
    QQuickMultiPointTouchArea *self,
    QPointingDevice *dev) {
  self->grabGesture(dev);
}

//  QSGNode *QQuickMultiPointTouchArea::updatePaintNode(QSGNode *a0,
//      UpdatePaintNodeData *a1)
extern "C" Q_DECL_EXPORT
QSGNode *ritual_ZN25QQuickMultiPointTouchArea15updatePaintNodeEP7QSGNodePN10QQuickItem19UpdatePaintNodeDataE(
    QQuickMultiPointTouchArea *self,
    QSGNode *a0,
    QQuickItem::UpdatePaintNodeData *a1) {
  return self->updatePaintNode(a0, a1);
}

//  void QQuickMultiPointTouchArea::ungrab(bool normalRelease)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QQuickMultiPointTouchArea6ungrabEb(
    QQuickMultiPointTouchArea *self,
    bool normalRelease) {
  self->ungrab(normalRelease);
}

//  a Python function taken by a CuteQQuickMultiPointTouchArea, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQuickMultiPointTouchArea(
    QQuickMultiPointTouchArea *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQuickMultiPointTouchArea *>(self)->take(key, call);
}

//  void QQuickMultiPointTouchArea::touchEvent(QTouchEvent *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN25QQuickMultiPointTouchArea10touchEventEP11QTouchEvent(
    QQuickMultiPointTouchArea *self,
    QTouchEvent *a0) {
  static_cast<OwnQQuickMultiPointTouchArea *>(self)->OwnQQuickMultiPointTouchArea::touchEvent(
      a0);
}

//  bool QQuickMultiPointTouchArea::childMouseEventFilter(QQuickItem
//      *receiver, QEvent *event)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN25QQuickMultiPointTouchArea21childMouseEventFilterEP10QQuickItemP6QEvent(
    QQuickMultiPointTouchArea *self,
    QQuickItem *receiver,
    QEvent *event) {
  return static_cast<OwnQQuickMultiPointTouchArea *>(self)->OwnQQuickMultiPointTouchArea::childMouseEventFilter(
      receiver,
      event);
}

//  void QQuickMultiPointTouchArea::mousePressEvent(QMouseEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN25QQuickMultiPointTouchArea15mousePressEventEP11QMouseEvent(
    QQuickMultiPointTouchArea *self,
    QMouseEvent *event) {
  static_cast<OwnQQuickMultiPointTouchArea *>(self)->OwnQQuickMultiPointTouchArea::mousePressEvent(
      event);
}

//  void QQuickMultiPointTouchArea::mouseReleaseEvent(QMouseEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN25QQuickMultiPointTouchArea17mouseReleaseEventEP11QMouseEvent(
    QQuickMultiPointTouchArea *self,
    QMouseEvent *event) {
  static_cast<OwnQQuickMultiPointTouchArea *>(self)->OwnQQuickMultiPointTouchArea::mouseReleaseEvent(
      event);
}

//  void QQuickMultiPointTouchArea::mouseMoveEvent(QMouseEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN25QQuickMultiPointTouchArea14mouseMoveEventEP11QMouseEvent(
    QQuickMultiPointTouchArea *self,
    QMouseEvent *event) {
  static_cast<OwnQQuickMultiPointTouchArea *>(self)->OwnQQuickMultiPointTouchArea::mouseMoveEvent(
      event);
}

//  void QQuickMultiPointTouchArea::mouseUngrabEvent()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN25QQuickMultiPointTouchArea16mouseUngrabEventEv(
    QQuickMultiPointTouchArea *self) {
  static_cast<OwnQQuickMultiPointTouchArea *>(self)->OwnQQuickMultiPointTouchArea::mouseUngrabEvent();
}

//  void QQuickMultiPointTouchArea::touchUngrabEvent()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN25QQuickMultiPointTouchArea16touchUngrabEventEv(
    QQuickMultiPointTouchArea *self) {
  static_cast<OwnQQuickMultiPointTouchArea *>(self)->OwnQQuickMultiPointTouchArea::touchUngrabEvent();
}

//  QSGNode *QQuickMultiPointTouchArea::updatePaintNode(QSGNode *a0,
//      UpdatePaintNodeData *a1)
extern "C" Q_DECL_EXPORT
QSGNode *ritual_own_ZN25QQuickMultiPointTouchArea15updatePaintNodeEP7QSGNodePN10QQuickItem19UpdatePaintNodeDataE(
    QQuickMultiPointTouchArea *self,
    QSGNode *a0,
    QQuickItem::UpdatePaintNodeData *a1) {
  return static_cast<OwnQQuickMultiPointTouchArea *>(self)->OwnQQuickMultiPointTouchArea::updatePaintNode(
      a0,
      a1);
}

//  a QQmlListProperty<QQuickTouchPoint> a ritual of
//      QQuickMultiPointTouchArea gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QQuickMultiPointTouchArea__QQmlListProperty_QQuickTouchPoint(
    QQmlListProperty<QQuickTouchPoint> *self) {
  delete self;
}
