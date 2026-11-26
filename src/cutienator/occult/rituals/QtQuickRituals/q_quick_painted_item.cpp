//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/qquickpainteditem.h, Qt 6.12.0. Changes made here are lost.
#include <QtGui/qtguiglobal.h>
#include <QtQuick/QtQuick>
#include <QtQuick/qquickpainteditem.h>
#include <QtCore/qstring.h>
#include <QtCore/qrect.h>
#include <QtCore/qsize.h>
#include <QtGui/qcolor.h>
#include <QtQuick/qquickitem.h>
#include <QtCore/qpoint.h>
#include <QtCore/qvariant.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  Only a class built on QQuickPaintedItem may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQQuickPaintedItem : QQuickPaintedItem {
  using QQuickPaintedItem::updatePaintNode;
  using QQuickPaintedItem::releaseResources;
  using QQuickPaintedItem::itemChange;
};

//  A QQuickPaintedItem that Python can take functions over in. Every QQuickPaintedItem
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQQuickPaintedItemCall0)(const void *, QPainter *, int *);
typedef bool (*CuteQQuickPaintedItemCall1)(const void *, int *);
typedef void * (*CuteQQuickPaintedItemCall2)(const void *, int *);
typedef void * (*CuteQQuickPaintedItemCall3)(const void *, QSGNode *, QQuickItem::UpdatePaintNodeData *, int *);
typedef void (*CuteQQuickPaintedItemCall4)(const void *, int *);
typedef void (*CuteQQuickPaintedItemCall5)(const void *, int, const QQuickItem::ItemChangeData *, int *);
typedef const QRectF * (*CuteQQuickPaintedItemCall6)(const void *, int *);
typedef const QRectF * (*CuteQQuickPaintedItemCall7)(const void *, int *);
typedef bool (*CuteQQuickPaintedItemCall8)(const void *, const QPointF *, int *);
#if QT_CONFIG(im)
typedef const QVariant * (*CuteQQuickPaintedItemCall9)(const void *, int, int *);
#endif  // QT_CONFIG(im)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickPaintedItemCall10)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickPaintedItemCall11)(const void *, const QRectF *, const QRectF *, int *);
typedef void (*CuteQQuickPaintedItemCall12)(const void *, int *);
typedef void (*CuteQQuickPaintedItemCall13)(const void *, int *);
typedef void (*CuteQQuickPaintedItemCall14)(const void *, QKeyEvent *, int *);
typedef void (*CuteQQuickPaintedItemCall15)(const void *, QKeyEvent *, int *);
#if QT_CONFIG(im)
typedef void (*CuteQQuickPaintedItemCall16)(const void *, QInputMethodEvent *, int *);
#endif  // QT_CONFIG(im)
typedef void (*CuteQQuickPaintedItemCall17)(const void *, QFocusEvent *, int *);
typedef void (*CuteQQuickPaintedItemCall18)(const void *, QFocusEvent *, int *);
typedef void (*CuteQQuickPaintedItemCall19)(const void *, QMouseEvent *, int *);
typedef void (*CuteQQuickPaintedItemCall20)(const void *, QMouseEvent *, int *);
typedef void (*CuteQQuickPaintedItemCall21)(const void *, QMouseEvent *, int *);
typedef void (*CuteQQuickPaintedItemCall22)(const void *, QMouseEvent *, int *);
typedef void (*CuteQQuickPaintedItemCall23)(const void *, int *);
typedef void (*CuteQQuickPaintedItemCall24)(const void *, int *);
#if QT_CONFIG(wheelevent)
typedef void (*CuteQQuickPaintedItemCall25)(const void *, QWheelEvent *, int *);
#endif  // QT_CONFIG(wheelevent)
typedef void (*CuteQQuickPaintedItemCall26)(const void *, QTouchEvent *, int *);
typedef void (*CuteQQuickPaintedItemCall27)(const void *, QHoverEvent *, int *);
typedef void (*CuteQQuickPaintedItemCall28)(const void *, QHoverEvent *, int *);
typedef void (*CuteQQuickPaintedItemCall29)(const void *, QHoverEvent *, int *);
#if QT_CONFIG(quick_draganddrop)
typedef void (*CuteQQuickPaintedItemCall30)(const void *, QDragEnterEvent *, int *);
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
typedef void (*CuteQQuickPaintedItemCall31)(const void *, QDragMoveEvent *, int *);
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
typedef void (*CuteQQuickPaintedItemCall32)(const void *, QDragLeaveEvent *, int *);
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
typedef void (*CuteQQuickPaintedItemCall33)(const void *, QDropEvent *, int *);
#endif  // QT_CONFIG(quick_draganddrop)
typedef bool (*CuteQQuickPaintedItemCall34)(const void *, QQuickItem *, QEvent *, int *);
typedef void (*CuteQQuickPaintedItemCall35)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickPaintedItemCall36)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickPaintedItemCall37)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickPaintedItemCall38)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickPaintedItemCall39)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickPaintedItemCall40)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickPaintedItemCall41)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQQuickPaintedItem : public QQuickPaintedItem {
public:
  using QQuickPaintedItem::QQuickPaintedItem;
  void *taken[42] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN17QQuickPaintedItem5paintEP8QPainter")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK10QQuickItem17isTextureProviderEv")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK10QQuickItem15textureProviderEv")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem15updatePaintNodeEP7QSGNodePNS_19UpdatePaintNodeDataE")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem16releaseResourcesEv")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem10itemChangeENS_10ItemChangeERKNS_14ItemChangeDataE")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK10QQuickItem12boundingRectEv")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK10QQuickItem8clipRectEv")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK10QQuickItem8containsERK7QPointF")) {
      taken[8] = call;
      return true;
    }
#if QT_CONFIG(im)
    if (!std::strcmp(key, "_ZNK10QQuickItem16inputMethodQueryEN2Qt16InputMethodQueryE")) {
      taken[9] = call;
      return true;
    }
#endif  // QT_CONFIG(im)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[10] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN10QQuickItem14geometryChangeERK6QRectFS2_")) {
      taken[11] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQmlParserStatus10classBeginEv")) {
      taken[12] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQmlParserStatus17componentCompleteEv")) {
      taken[13] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem13keyPressEventEP9QKeyEvent")) {
      taken[14] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem15keyReleaseEventEP9QKeyEvent")) {
      taken[15] = call;
      return true;
    }
#if QT_CONFIG(im)
    if (!std::strcmp(key, "_ZN10QQuickItem16inputMethodEventEP17QInputMethodEvent")) {
      taken[16] = call;
      return true;
    }
#endif  // QT_CONFIG(im)
    if (!std::strcmp(key, "_ZN10QQuickItem12focusInEventEP11QFocusEvent")) {
      taken[17] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem13focusOutEventEP11QFocusEvent")) {
      taken[18] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem15mousePressEventEP11QMouseEvent")) {
      taken[19] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem14mouseMoveEventEP11QMouseEvent")) {
      taken[20] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem17mouseReleaseEventEP11QMouseEvent")) {
      taken[21] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem21mouseDoubleClickEventEP11QMouseEvent")) {
      taken[22] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem16mouseUngrabEventEv")) {
      taken[23] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem16touchUngrabEventEv")) {
      taken[24] = call;
      return true;
    }
#if QT_CONFIG(wheelevent)
    if (!std::strcmp(key, "_ZN10QQuickItem10wheelEventEP11QWheelEvent")) {
      taken[25] = call;
      return true;
    }
#endif  // QT_CONFIG(wheelevent)
    if (!std::strcmp(key, "_ZN10QQuickItem10touchEventEP11QTouchEvent")) {
      taken[26] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem15hoverEnterEventEP11QHoverEvent")) {
      taken[27] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem14hoverMoveEventEP11QHoverEvent")) {
      taken[28] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem15hoverLeaveEventEP11QHoverEvent")) {
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

  //  void QQuickPaintedItem::paint(QPainter *painter)
  void paint(QPainter *painter) override {
    if (taken[0]) {
      int handled = 0;
      CuteQQuickPaintedItemCall0 call = reinterpret_cast<CuteQQuickPaintedItemCall0>(taken[0]);
      call(this, painter, &handled);
      if (handled) return;
    }
  }

  //  bool QQuickPaintedItem::isTextureProvider() const
  bool isTextureProvider() const override {
    if (taken[1]) {
      int handled = 0;
      CuteQQuickPaintedItemCall1 call = reinterpret_cast<CuteQQuickPaintedItemCall1>(taken[1]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QQuickPaintedItem::isTextureProvider();
  }

  //  QSGTextureProvider *QQuickPaintedItem::textureProvider() const
  QSGTextureProvider *textureProvider() const override {
    if (taken[2]) {
      int handled = 0;
      CuteQQuickPaintedItemCall2 call = reinterpret_cast<CuteQQuickPaintedItemCall2>(taken[2]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QSGTextureProvider *>(given);
    }
    return QQuickPaintedItem::textureProvider();
  }

  //  QSGNode *QQuickPaintedItem::updatePaintNode(QSGNode *a0,
  //      UpdatePaintNodeData *a1)
  QSGNode *updatePaintNode(
      QSGNode *a0,
      QQuickItem::UpdatePaintNodeData *a1) override {
    if (taken[3]) {
      int handled = 0;
      CuteQQuickPaintedItemCall3 call = reinterpret_cast<CuteQQuickPaintedItemCall3>(taken[3]);
      void * given = call(this, a0, a1, &handled);
      if (handled) return static_cast<QSGNode *>(given);
    }
    return QQuickPaintedItem::updatePaintNode(a0, a1);
  }

  //  void QQuickPaintedItem::releaseResources()
  void releaseResources() override {
    if (taken[4]) {
      int handled = 0;
      CuteQQuickPaintedItemCall4 call = reinterpret_cast<CuteQQuickPaintedItemCall4>(taken[4]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickPaintedItem::releaseResources();
  }

  //  void QQuickPaintedItem::itemChange(ItemChange a0, const
  //      ItemChangeData &a1)
  void itemChange(
      QQuickItem::ItemChange a0,
      const QQuickItem::ItemChangeData &a1) override {
    if (taken[5]) {
      int handled = 0;
      CuteQQuickPaintedItemCall5 call = reinterpret_cast<CuteQQuickPaintedItemCall5>(taken[5]);
      call(this, static_cast<int>(a0), &a1, &handled);
      if (handled) return;
    }
    QQuickPaintedItem::itemChange(a0, a1);
  }

  //  QRectF QQuickItem::boundingRect() const
  QRectF boundingRect() const override {
    if (taken[6]) {
      int handled = 0;
      CuteQQuickPaintedItemCall6 call = reinterpret_cast<CuteQQuickPaintedItemCall6>(taken[6]);
      const QRectF * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QQuickItem::boundingRect();
  }

  //  QRectF QQuickItem::clipRect() const
  QRectF clipRect() const override {
    if (taken[7]) {
      int handled = 0;
      CuteQQuickPaintedItemCall7 call = reinterpret_cast<CuteQQuickPaintedItemCall7>(taken[7]);
      const QRectF * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QQuickItem::clipRect();
  }

  //  bool QQuickItem::contains(const QPointF &point) const
  bool contains(const QPointF &point) const override {
    if (taken[8]) {
      int handled = 0;
      CuteQQuickPaintedItemCall8 call = reinterpret_cast<CuteQQuickPaintedItemCall8>(taken[8]);
      bool given = call(this, &point, &handled);
      if (handled) return given;
    }
    return QQuickItem::contains(point);
  }

#if QT_CONFIG(im)
  //  QVariant QQuickItem::inputMethodQuery(Qt::InputMethodQuery query)
  //      const
  QVariant inputMethodQuery(Qt::InputMethodQuery query) const override {
    if (taken[9]) {
      int handled = 0;
      CuteQQuickPaintedItemCall9 call = reinterpret_cast<CuteQQuickPaintedItemCall9>(taken[9]);
      const QVariant * given = call(this, static_cast<int>(query), &handled);
      if (handled && given) return *given;
    }
    return QQuickItem::inputMethodQuery(query);
  }
#endif  // QT_CONFIG(im)

#if !defined(QT_NO_QOBJECT)
  //  bool QQuickItem::event(QEvent *a0)
  bool event(QEvent *a0) override {
    if (taken[10]) {
      int handled = 0;
      CuteQQuickPaintedItemCall10 call = reinterpret_cast<CuteQQuickPaintedItemCall10>(taken[10]);
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
    if (taken[11]) {
      int handled = 0;
      CuteQQuickPaintedItemCall11 call = reinterpret_cast<CuteQQuickPaintedItemCall11>(taken[11]);
      call(this, &newGeometry, &oldGeometry, &handled);
      if (handled) return;
    }
    QQuickItem::geometryChange(newGeometry, oldGeometry);
  }

  //  void QQuickItem::classBegin()
  void classBegin() override {
    if (taken[12]) {
      int handled = 0;
      CuteQQuickPaintedItemCall12 call = reinterpret_cast<CuteQQuickPaintedItemCall12>(taken[12]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItem::classBegin();
  }

  //  void QQuickItem::componentComplete()
  void componentComplete() override {
    if (taken[13]) {
      int handled = 0;
      CuteQQuickPaintedItemCall13 call = reinterpret_cast<CuteQQuickPaintedItemCall13>(taken[13]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItem::componentComplete();
  }

  //  void QQuickItem::keyPressEvent(QKeyEvent *event)
  void keyPressEvent(QKeyEvent *event) override {
    if (taken[14]) {
      int handled = 0;
      CuteQQuickPaintedItemCall14 call = reinterpret_cast<CuteQQuickPaintedItemCall14>(taken[14]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::keyPressEvent(event);
  }

  //  void QQuickItem::keyReleaseEvent(QKeyEvent *event)
  void keyReleaseEvent(QKeyEvent *event) override {
    if (taken[15]) {
      int handled = 0;
      CuteQQuickPaintedItemCall15 call = reinterpret_cast<CuteQQuickPaintedItemCall15>(taken[15]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::keyReleaseEvent(event);
  }

#if QT_CONFIG(im)
  //  void QQuickItem::inputMethodEvent(QInputMethodEvent *a0)
  void inputMethodEvent(QInputMethodEvent *a0) override {
    if (taken[16]) {
      int handled = 0;
      CuteQQuickPaintedItemCall16 call = reinterpret_cast<CuteQQuickPaintedItemCall16>(taken[16]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItem::inputMethodEvent(a0);
  }
#endif  // QT_CONFIG(im)

  //  void QQuickItem::focusInEvent(QFocusEvent *a0)
  void focusInEvent(QFocusEvent *a0) override {
    if (taken[17]) {
      int handled = 0;
      CuteQQuickPaintedItemCall17 call = reinterpret_cast<CuteQQuickPaintedItemCall17>(taken[17]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItem::focusInEvent(a0);
  }

  //  void QQuickItem::focusOutEvent(QFocusEvent *a0)
  void focusOutEvent(QFocusEvent *a0) override {
    if (taken[18]) {
      int handled = 0;
      CuteQQuickPaintedItemCall18 call = reinterpret_cast<CuteQQuickPaintedItemCall18>(taken[18]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItem::focusOutEvent(a0);
  }

  //  void QQuickItem::mousePressEvent(QMouseEvent *event)
  void mousePressEvent(QMouseEvent *event) override {
    if (taken[19]) {
      int handled = 0;
      CuteQQuickPaintedItemCall19 call = reinterpret_cast<CuteQQuickPaintedItemCall19>(taken[19]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::mousePressEvent(event);
  }

  //  void QQuickItem::mouseMoveEvent(QMouseEvent *event)
  void mouseMoveEvent(QMouseEvent *event) override {
    if (taken[20]) {
      int handled = 0;
      CuteQQuickPaintedItemCall20 call = reinterpret_cast<CuteQQuickPaintedItemCall20>(taken[20]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::mouseMoveEvent(event);
  }

  //  void QQuickItem::mouseReleaseEvent(QMouseEvent *event)
  void mouseReleaseEvent(QMouseEvent *event) override {
    if (taken[21]) {
      int handled = 0;
      CuteQQuickPaintedItemCall21 call = reinterpret_cast<CuteQQuickPaintedItemCall21>(taken[21]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::mouseReleaseEvent(event);
  }

  //  void QQuickItem::mouseDoubleClickEvent(QMouseEvent *event)
  void mouseDoubleClickEvent(QMouseEvent *event) override {
    if (taken[22]) {
      int handled = 0;
      CuteQQuickPaintedItemCall22 call = reinterpret_cast<CuteQQuickPaintedItemCall22>(taken[22]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::mouseDoubleClickEvent(event);
  }

  //  void QQuickItem::mouseUngrabEvent()
  void mouseUngrabEvent() override {
    if (taken[23]) {
      int handled = 0;
      CuteQQuickPaintedItemCall23 call = reinterpret_cast<CuteQQuickPaintedItemCall23>(taken[23]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItem::mouseUngrabEvent();
  }

  //  void QQuickItem::touchUngrabEvent()
  void touchUngrabEvent() override {
    if (taken[24]) {
      int handled = 0;
      CuteQQuickPaintedItemCall24 call = reinterpret_cast<CuteQQuickPaintedItemCall24>(taken[24]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItem::touchUngrabEvent();
  }

#if QT_CONFIG(wheelevent)
  //  void QQuickItem::wheelEvent(QWheelEvent *event)
  void wheelEvent(QWheelEvent *event) override {
    if (taken[25]) {
      int handled = 0;
      CuteQQuickPaintedItemCall25 call = reinterpret_cast<CuteQQuickPaintedItemCall25>(taken[25]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::wheelEvent(event);
  }
#endif  // QT_CONFIG(wheelevent)

  //  void QQuickItem::touchEvent(QTouchEvent *event)
  void touchEvent(QTouchEvent *event) override {
    if (taken[26]) {
      int handled = 0;
      CuteQQuickPaintedItemCall26 call = reinterpret_cast<CuteQQuickPaintedItemCall26>(taken[26]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::touchEvent(event);
  }

  //  void QQuickItem::hoverEnterEvent(QHoverEvent *event)
  void hoverEnterEvent(QHoverEvent *event) override {
    if (taken[27]) {
      int handled = 0;
      CuteQQuickPaintedItemCall27 call = reinterpret_cast<CuteQQuickPaintedItemCall27>(taken[27]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::hoverEnterEvent(event);
  }

  //  void QQuickItem::hoverMoveEvent(QHoverEvent *event)
  void hoverMoveEvent(QHoverEvent *event) override {
    if (taken[28]) {
      int handled = 0;
      CuteQQuickPaintedItemCall28 call = reinterpret_cast<CuteQQuickPaintedItemCall28>(taken[28]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::hoverMoveEvent(event);
  }

  //  void QQuickItem::hoverLeaveEvent(QHoverEvent *event)
  void hoverLeaveEvent(QHoverEvent *event) override {
    if (taken[29]) {
      int handled = 0;
      CuteQQuickPaintedItemCall29 call = reinterpret_cast<CuteQQuickPaintedItemCall29>(taken[29]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::hoverLeaveEvent(event);
  }

#if QT_CONFIG(quick_draganddrop)
  //  void QQuickItem::dragEnterEvent(QDragEnterEvent *a0)
  void dragEnterEvent(QDragEnterEvent *a0) override {
    if (taken[30]) {
      int handled = 0;
      CuteQQuickPaintedItemCall30 call = reinterpret_cast<CuteQQuickPaintedItemCall30>(taken[30]);
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
      CuteQQuickPaintedItemCall31 call = reinterpret_cast<CuteQQuickPaintedItemCall31>(taken[31]);
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
      CuteQQuickPaintedItemCall32 call = reinterpret_cast<CuteQQuickPaintedItemCall32>(taken[32]);
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
      CuteQQuickPaintedItemCall33 call = reinterpret_cast<CuteQQuickPaintedItemCall33>(taken[33]);
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
      CuteQQuickPaintedItemCall34 call = reinterpret_cast<CuteQQuickPaintedItemCall34>(taken[34]);
      bool given = call(this, a0, a1, &handled);
      if (handled) return given;
    }
    return QQuickItem::childMouseEventFilter(a0, a1);
  }

  //  void QQuickItem::updatePolish()
  void updatePolish() override {
    if (taken[35]) {
      int handled = 0;
      CuteQQuickPaintedItemCall35 call = reinterpret_cast<CuteQQuickPaintedItemCall35>(taken[35]);
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
      CuteQQuickPaintedItemCall36 call = reinterpret_cast<CuteQQuickPaintedItemCall36>(taken[36]);
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
      CuteQQuickPaintedItemCall37 call = reinterpret_cast<CuteQQuickPaintedItemCall37>(taken[37]);
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
      CuteQQuickPaintedItemCall38 call = reinterpret_cast<CuteQQuickPaintedItemCall38>(taken[38]);
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
      CuteQQuickPaintedItemCall39 call = reinterpret_cast<CuteQQuickPaintedItemCall39>(taken[39]);
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
      CuteQQuickPaintedItemCall40 call = reinterpret_cast<CuteQQuickPaintedItemCall40>(taken[40]);
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
      CuteQQuickPaintedItemCall41 call = reinterpret_cast<CuteQQuickPaintedItemCall41>(taken[41]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QQuickPaintedItem::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK17QQuickPaintedItem10metaObjectEv(
    const QQuickPaintedItem *self) {
  return self->metaObject();
}

//  void *QQuickPaintedItem::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN17QQuickPaintedItem11qt_metacastEPKc(
    QQuickPaintedItem *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QQuickPaintedItem::qt_metacall(QMetaObject::Call a0, int a1, void
//      **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN17QQuickPaintedItem11qt_metacallEN11QMetaObject4CallEiPPv(
    QQuickPaintedItem *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QQuickPaintedItem::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN17QQuickPaintedItem2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuickPaintedItem::tr(s, c, n));
}

//  void QQuickPaintedItem::qt_qmlMarker_uncreatable()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickPaintedItem24qt_qmlMarker_uncreatableEv(
    QQuickPaintedItem *self) {
  self->qt_qmlMarker_uncreatable();
}

//  QQuickPaintedItem::QQuickPaintedItem(QQuickItem *parent)
extern "C" Q_DECL_EXPORT
QQuickPaintedItem *ritual_ZN17QQuickPaintedItemC1EP10QQuickItem(
    QQuickItem *parent) {
  return new CuteQQuickPaintedItem(parent);
}

//  QQuickPaintedItem::~QQuickPaintedItem()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickPaintedItemD1Ev(QQuickPaintedItem *self) {
  delete self;
}

//  void QQuickPaintedItem::update(const QRect &rect)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickPaintedItem6updateERK5QRect(
    QQuickPaintedItem *self,
    const QRect *rect) {
  self->update(*rect);
}

//  bool QQuickPaintedItem::opaquePainting() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK17QQuickPaintedItem14opaquePaintingEv(
    const QQuickPaintedItem *self) {
  return self->opaquePainting();
}

//  void QQuickPaintedItem::setOpaquePainting(bool opaque)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickPaintedItem17setOpaquePaintingEb(
    QQuickPaintedItem *self,
    bool opaque) {
  self->setOpaquePainting(opaque);
}

//  bool QQuickPaintedItem::antialiasing() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK17QQuickPaintedItem12antialiasingEv(
    const QQuickPaintedItem *self) {
  return self->antialiasing();
}

//  void QQuickPaintedItem::setAntialiasing(bool enable)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickPaintedItem15setAntialiasingEb(
    QQuickPaintedItem *self,
    bool enable) {
  self->setAntialiasing(enable);
}

//  bool QQuickPaintedItem::mipmap() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK17QQuickPaintedItem6mipmapEv(const QQuickPaintedItem *self) {
  return self->mipmap();
}

//  void QQuickPaintedItem::setMipmap(bool enable)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickPaintedItem9setMipmapEb(
    QQuickPaintedItem *self,
    bool enable) {
  self->setMipmap(enable);
}

//  PerformanceHints QQuickPaintedItem::performanceHints() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK17QQuickPaintedItem16performanceHintsEv(
    const QQuickPaintedItem *self) {
  return static_cast<int>(self->performanceHints().toInt());
}

//  void QQuickPaintedItem::setPerformanceHint(PerformanceHint hint, bool
//      enabled)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickPaintedItem18setPerformanceHintENS_15PerformanceHintEb(
    QQuickPaintedItem *self,
    QQuickPaintedItem::PerformanceHint hint,
    bool enabled) {
  self->setPerformanceHint(hint, enabled);
}

//  void QQuickPaintedItem::setPerformanceHints(PerformanceHints hints)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickPaintedItem19setPerformanceHintsE6QFlagsINS_15PerformanceHintEE(
    QQuickPaintedItem *self,
    int hints) {
  self->setPerformanceHints(
      QFlags<QQuickPaintedItem::PerformanceHint>::fromInt(hints));
}

//  QRectF QQuickPaintedItem::contentsBoundingRect() const
extern "C" Q_DECL_EXPORT
QRectF *ritual_ZNK17QQuickPaintedItem20contentsBoundingRectEv(
    const QQuickPaintedItem *self) {
  return new QRectF(self->contentsBoundingRect());
}

//  QSize QQuickPaintedItem::contentsSize() const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK17QQuickPaintedItem12contentsSizeEv(
    const QQuickPaintedItem *self) {
  return new QSize(self->contentsSize());
}

//  void QQuickPaintedItem::setContentsSize(const QSize &a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickPaintedItem15setContentsSizeERK5QSize(
    QQuickPaintedItem *self,
    const QSize *a0) {
  self->setContentsSize(*a0);
}

//  void QQuickPaintedItem::resetContentsSize()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickPaintedItem17resetContentsSizeEv(
    QQuickPaintedItem *self) {
  self->resetContentsSize();
}

//  qreal QQuickPaintedItem::contentsScale() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK17QQuickPaintedItem13contentsScaleEv(
    const QQuickPaintedItem *self) {
  return self->contentsScale();
}

//  void QQuickPaintedItem::setContentsScale(qreal a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickPaintedItem16setContentsScaleEd(
    QQuickPaintedItem *self,
    qreal a0) {
  self->setContentsScale(a0);
}

//  QSize QQuickPaintedItem::textureSize() const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK17QQuickPaintedItem11textureSizeEv(
    const QQuickPaintedItem *self) {
  return new QSize(self->textureSize());
}

//  void QQuickPaintedItem::setTextureSize(const QSize &size)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickPaintedItem14setTextureSizeERK5QSize(
    QQuickPaintedItem *self,
    const QSize *size) {
  self->setTextureSize(*size);
}

//  QColor QQuickPaintedItem::fillColor() const
extern "C" Q_DECL_EXPORT
QColor *ritual_ZNK17QQuickPaintedItem9fillColorEv(
    const QQuickPaintedItem *self) {
  return new QColor(self->fillColor());
}

//  void QQuickPaintedItem::setFillColor(const QColor &a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickPaintedItem12setFillColorERK6QColor(
    QQuickPaintedItem *self,
    const QColor *a0) {
  self->setFillColor(*a0);
}

//  RenderTarget QQuickPaintedItem::renderTarget() const
extern "C" Q_DECL_EXPORT
QQuickPaintedItem::RenderTarget ritual_ZNK17QQuickPaintedItem12renderTargetEv(
    const QQuickPaintedItem *self) {
  return self->renderTarget();
}

//  void QQuickPaintedItem::setRenderTarget(RenderTarget target)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickPaintedItem15setRenderTargetENS_12RenderTargetE(
    QQuickPaintedItem *self,
    QQuickPaintedItem::RenderTarget target) {
  self->setRenderTarget(target);
}

//  void QQuickPaintedItem::paint(QPainter *painter)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickPaintedItem5paintEP8QPainter(
    QQuickPaintedItem *self,
    QPainter *painter) {
  self->paint(painter);
}

//  bool QQuickPaintedItem::isTextureProvider() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK17QQuickPaintedItem17isTextureProviderEv(
    const QQuickPaintedItem *self) {
  return self->isTextureProvider();
}

//  QSGTextureProvider *QQuickPaintedItem::textureProvider() const
extern "C" Q_DECL_EXPORT
QSGTextureProvider *ritual_ZNK17QQuickPaintedItem15textureProviderEv(
    const QQuickPaintedItem *self) {
  return self->textureProvider();
}

//  void QQuickPaintedItem::fillColorChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickPaintedItem16fillColorChangedEv(
    QQuickPaintedItem *self) {
  self->fillColorChanged();
}

//  void QQuickPaintedItem::contentsSizeChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickPaintedItem19contentsSizeChangedEv(
    QQuickPaintedItem *self) {
  self->contentsSizeChanged();
}

//  void QQuickPaintedItem::contentsScaleChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickPaintedItem20contentsScaleChangedEv(
    QQuickPaintedItem *self) {
  self->contentsScaleChanged();
}

//  void QQuickPaintedItem::renderTargetChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickPaintedItem19renderTargetChangedEv(
    QQuickPaintedItem *self) {
  self->renderTargetChanged();
}

//  void QQuickPaintedItem::textureSizeChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickPaintedItem18textureSizeChangedEv(
    QQuickPaintedItem *self) {
  self->textureSizeChanged();
}

//  QQuickPaintedItem::QQuickPaintedItem(QQuickPaintedItemPrivate &dd,
//      QQuickItem *parent)
extern "C" Q_DECL_EXPORT
QQuickPaintedItem *ritual_ZN17QQuickPaintedItemC1ER24QQuickPaintedItemPrivateP10QQuickItem(
    QQuickPaintedItemPrivate *dd,
    QQuickItem *parent) {
  return new CuteQQuickPaintedItem(*dd, parent);
}

//  QSGNode *QQuickPaintedItem::updatePaintNode(QSGNode *a0,
//      UpdatePaintNodeData *a1)
extern "C" Q_DECL_EXPORT
QSGNode *ritual_ZN17QQuickPaintedItem15updatePaintNodeEP7QSGNodePN10QQuickItem19UpdatePaintNodeDataE(
    QQuickPaintedItem *self,
    QSGNode *a0,
    QQuickItem::UpdatePaintNodeData *a1) {
  return self->updatePaintNode(a0, a1);
}

//  void QQuickPaintedItem::releaseResources()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickPaintedItem16releaseResourcesEv(
    QQuickPaintedItem *self) {
  self->releaseResources();
}

//  void QQuickPaintedItem::itemChange(ItemChange a0, const ItemChangeData
//      &a1)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickPaintedItem10itemChangeEN10QQuickItem10ItemChangeERKNS0_14ItemChangeDataE(
    QQuickPaintedItem *self,
    QQuickItem::ItemChange a0,
    const QQuickItem::ItemChangeData *a1) {
  self->itemChange(a0, *a1);
}

//  void QQuickPaintedItem::invalidateSceneGraph()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickPaintedItem20invalidateSceneGraphEv(
    QQuickPaintedItem *self) {
  self->invalidateSceneGraph();
}

//  QQuickPaintedItemPrivate *QQuickPaintedItem::d_func()
extern "C" Q_DECL_EXPORT
QQuickPaintedItemPrivate *ritual_ZN17QQuickPaintedItem6d_funcEv(
    QQuickPaintedItem *self) {
  return self->d_func();
}

//  const QQuickPaintedItemPrivate *QQuickPaintedItem::d_func() const
extern "C" Q_DECL_EXPORT
const QQuickPaintedItemPrivate *ritual_ZNK17QQuickPaintedItem6d_funcEv(
    const QQuickPaintedItem *self) {
  return self->d_func();
}

//  a Python function taken by a CuteQQuickPaintedItem, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQuickPaintedItem(
    QQuickPaintedItem *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQuickPaintedItem *>(self)->take(key, call);
}

//  bool QQuickPaintedItem::isTextureProvider() const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK17QQuickPaintedItem17isTextureProviderEv(
    const QQuickPaintedItem *self) {
  return self->QQuickPaintedItem::isTextureProvider();
}

//  QSGTextureProvider *QQuickPaintedItem::textureProvider() const
extern "C" Q_DECL_EXPORT
QSGTextureProvider *ritual_own_ZNK17QQuickPaintedItem15textureProviderEv(
    const QQuickPaintedItem *self) {
  return self->QQuickPaintedItem::textureProvider();
}

//  QSGNode *QQuickPaintedItem::updatePaintNode(QSGNode *a0,
//      UpdatePaintNodeData *a1)
extern "C" Q_DECL_EXPORT
QSGNode *ritual_own_ZN17QQuickPaintedItem15updatePaintNodeEP7QSGNodePN10QQuickItem19UpdatePaintNodeDataE(
    QQuickPaintedItem *self,
    QSGNode *a0,
    QQuickItem::UpdatePaintNodeData *a1) {
  return static_cast<OwnQQuickPaintedItem *>(self)->OwnQQuickPaintedItem::updatePaintNode(
      a0,
      a1);
}

//  void QQuickPaintedItem::releaseResources()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17QQuickPaintedItem16releaseResourcesEv(
    QQuickPaintedItem *self) {
  static_cast<OwnQQuickPaintedItem *>(self)->OwnQQuickPaintedItem::releaseResources();
}

//  void QQuickPaintedItem::itemChange(ItemChange a0, const ItemChangeData
//      &a1)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17QQuickPaintedItem10itemChangeEN10QQuickItem10ItemChangeERKNS0_14ItemChangeDataE(
    QQuickPaintedItem *self,
    QQuickItem::ItemChange a0,
    const QQuickItem::ItemChangeData *a1) {
  static_cast<OwnQQuickPaintedItem *>(self)->OwnQQuickPaintedItem::itemChange(
      a0,
      *a1);
}
