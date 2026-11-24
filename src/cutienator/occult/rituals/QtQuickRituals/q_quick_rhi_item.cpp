//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/qquickrhiitem.h, Qt 6.12.0. Changes made here are lost.
#include <QtGui/qtguiglobal.h>
#include <QtQuick/QtQuick>
#include <QtQuick/qquickrhiitem.h>
#include <QtCore/qstring.h>
#include <QtCore/qsize.h>
#include <QtCore/qrect.h>
#include <QtCore/qpoint.h>
#include <QtCore/qvariant.h>
#include <QtQuick/qquickitem.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  Only a class built on QQuickRhiItem may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQQuickRhiItem : QQuickRhiItem {
  using QQuickRhiItem::updatePaintNode;
  using QQuickRhiItem::event;
  using QQuickRhiItem::geometryChange;
  using QQuickRhiItem::releaseResources;
};

//  A QQuickRhiItem that Python can take functions over in. Every QQuickRhiItem
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef bool (*CuteQQuickRhiItemCall0)(const void *, int *);
typedef void * (*CuteQQuickRhiItemCall1)(const void *, int *);
typedef void * (*CuteQQuickRhiItemCall2)(const void *, int *);
typedef void * (*CuteQQuickRhiItemCall3)(const void *, QSGNode *, QQuickItem::UpdatePaintNodeData *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickRhiItemCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickRhiItemCall5)(const void *, const QRectF *, const QRectF *, int *);
typedef void (*CuteQQuickRhiItemCall6)(const void *, int *);
typedef const QRectF * (*CuteQQuickRhiItemCall7)(const void *, int *);
typedef const QRectF * (*CuteQQuickRhiItemCall8)(const void *, int *);
typedef bool (*CuteQQuickRhiItemCall9)(const void *, const QPointF *, int *);
#if QT_CONFIG(im)
typedef const QVariant * (*CuteQQuickRhiItemCall10)(const void *, int, int *);
#endif  // QT_CONFIG(im)
typedef void (*CuteQQuickRhiItemCall11)(const void *, int, const QQuickItem::ItemChangeData *, int *);
typedef void (*CuteQQuickRhiItemCall12)(const void *, int *);
typedef void (*CuteQQuickRhiItemCall13)(const void *, int *);
typedef void (*CuteQQuickRhiItemCall14)(const void *, QKeyEvent *, int *);
typedef void (*CuteQQuickRhiItemCall15)(const void *, QKeyEvent *, int *);
#if QT_CONFIG(im)
typedef void (*CuteQQuickRhiItemCall16)(const void *, QInputMethodEvent *, int *);
#endif  // QT_CONFIG(im)
typedef void (*CuteQQuickRhiItemCall17)(const void *, QFocusEvent *, int *);
typedef void (*CuteQQuickRhiItemCall18)(const void *, QFocusEvent *, int *);
typedef void (*CuteQQuickRhiItemCall19)(const void *, QMouseEvent *, int *);
typedef void (*CuteQQuickRhiItemCall20)(const void *, QMouseEvent *, int *);
typedef void (*CuteQQuickRhiItemCall21)(const void *, QMouseEvent *, int *);
typedef void (*CuteQQuickRhiItemCall22)(const void *, QMouseEvent *, int *);
typedef void (*CuteQQuickRhiItemCall23)(const void *, int *);
typedef void (*CuteQQuickRhiItemCall24)(const void *, int *);
#if QT_CONFIG(wheelevent)
typedef void (*CuteQQuickRhiItemCall25)(const void *, QWheelEvent *, int *);
#endif  // QT_CONFIG(wheelevent)
typedef void (*CuteQQuickRhiItemCall26)(const void *, QTouchEvent *, int *);
typedef void (*CuteQQuickRhiItemCall27)(const void *, QHoverEvent *, int *);
typedef void (*CuteQQuickRhiItemCall28)(const void *, QHoverEvent *, int *);
typedef void (*CuteQQuickRhiItemCall29)(const void *, QHoverEvent *, int *);
#if QT_CONFIG(quick_draganddrop)
typedef void (*CuteQQuickRhiItemCall30)(const void *, QDragEnterEvent *, int *);
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
typedef void (*CuteQQuickRhiItemCall31)(const void *, QDragMoveEvent *, int *);
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
typedef void (*CuteQQuickRhiItemCall32)(const void *, QDragLeaveEvent *, int *);
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
typedef void (*CuteQQuickRhiItemCall33)(const void *, QDropEvent *, int *);
#endif  // QT_CONFIG(quick_draganddrop)
typedef bool (*CuteQQuickRhiItemCall34)(const void *, QQuickItem *, QEvent *, int *);
typedef void (*CuteQQuickRhiItemCall35)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickRhiItemCall36)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickRhiItemCall37)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickRhiItemCall38)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickRhiItemCall39)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickRhiItemCall40)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickRhiItemCall41)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQQuickRhiItem : public QQuickRhiItem {
public:
  using QQuickRhiItem::QQuickRhiItem;
  void *taken[42] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZNK10QQuickItem17isTextureProviderEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK10QQuickItem15textureProviderEv")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN13QQuickRhiItem14createRendererEv")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem15updatePaintNodeEP7QSGNodePNS_19UpdatePaintNodeDataE")) {
      taken[3] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[4] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN10QQuickItem14geometryChangeERK6QRectFS2_")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem16releaseResourcesEv")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK10QQuickItem12boundingRectEv")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK10QQuickItem8clipRectEv")) {
      taken[8] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK10QQuickItem8containsERK7QPointF")) {
      taken[9] = call;
      return true;
    }
#if QT_CONFIG(im)
    if (!std::strcmp(key, "_ZNK10QQuickItem16inputMethodQueryEN2Qt16InputMethodQueryE")) {
      taken[10] = call;
      return true;
    }
#endif  // QT_CONFIG(im)
    if (!std::strcmp(key, "_ZN10QQuickItem10itemChangeENS_10ItemChangeERKNS_14ItemChangeDataE")) {
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

  //  bool QQuickRhiItem::isTextureProvider() const
  bool isTextureProvider() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQQuickRhiItemCall0 call = reinterpret_cast<CuteQQuickRhiItemCall0>(taken[0]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QQuickRhiItem::isTextureProvider();
  }

  //  QSGTextureProvider *QQuickRhiItem::textureProvider() const
  QSGTextureProvider *textureProvider() const override {
    if (taken[1]) {
      int handled = 0;
      CuteQQuickRhiItemCall1 call = reinterpret_cast<CuteQQuickRhiItemCall1>(taken[1]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QSGTextureProvider *>(given);
    }
    return QQuickRhiItem::textureProvider();
  }

  //  QQuickRhiItemRenderer *QQuickRhiItem::createRenderer()
  QQuickRhiItemRenderer *createRenderer() override {
    if (taken[2]) {
      int handled = 0;
      CuteQQuickRhiItemCall2 call = reinterpret_cast<CuteQQuickRhiItemCall2>(taken[2]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QQuickRhiItemRenderer *>(given);
    }
    return {};
  }

  //  QSGNode *QQuickRhiItem::updatePaintNode(QSGNode *a0,
  //      UpdatePaintNodeData *a1)
  QSGNode *updatePaintNode(
      QSGNode *a0,
      QQuickItem::UpdatePaintNodeData *a1) override {
    if (taken[3]) {
      int handled = 0;
      CuteQQuickRhiItemCall3 call = reinterpret_cast<CuteQQuickRhiItemCall3>(taken[3]);
      void * given = call(this, a0, a1, &handled);
      if (handled) return static_cast<QSGNode *>(given);
    }
    return QQuickRhiItem::updatePaintNode(a0, a1);
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QQuickRhiItem::event(QEvent *a0)
  bool event(QEvent *a0) override {
    if (taken[4]) {
      int handled = 0;
      CuteQQuickRhiItemCall4 call = reinterpret_cast<CuteQQuickRhiItemCall4>(taken[4]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQuickRhiItem::event(a0);
  }
#endif  // !defined(QT_NO_QOBJECT)

  //  void QQuickRhiItem::geometryChange(const QRectF &newGeometry, const
  //      QRectF &oldGeometry)
  void geometryChange(
      const QRectF &newGeometry,
      const QRectF &oldGeometry) override {
    if (taken[5]) {
      int handled = 0;
      CuteQQuickRhiItemCall5 call = reinterpret_cast<CuteQQuickRhiItemCall5>(taken[5]);
      call(this, &newGeometry, &oldGeometry, &handled);
      if (handled) return;
    }
    QQuickRhiItem::geometryChange(newGeometry, oldGeometry);
  }

  //  void QQuickRhiItem::releaseResources()
  void releaseResources() override {
    if (taken[6]) {
      int handled = 0;
      CuteQQuickRhiItemCall6 call = reinterpret_cast<CuteQQuickRhiItemCall6>(taken[6]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickRhiItem::releaseResources();
  }

  //  QRectF QQuickItem::boundingRect() const
  QRectF boundingRect() const override {
    if (taken[7]) {
      int handled = 0;
      CuteQQuickRhiItemCall7 call = reinterpret_cast<CuteQQuickRhiItemCall7>(taken[7]);
      const QRectF * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QQuickItem::boundingRect();
  }

  //  QRectF QQuickItem::clipRect() const
  QRectF clipRect() const override {
    if (taken[8]) {
      int handled = 0;
      CuteQQuickRhiItemCall8 call = reinterpret_cast<CuteQQuickRhiItemCall8>(taken[8]);
      const QRectF * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QQuickItem::clipRect();
  }

  //  bool QQuickItem::contains(const QPointF &point) const
  bool contains(const QPointF &point) const override {
    if (taken[9]) {
      int handled = 0;
      CuteQQuickRhiItemCall9 call = reinterpret_cast<CuteQQuickRhiItemCall9>(taken[9]);
      bool given = call(this, &point, &handled);
      if (handled) return given;
    }
    return QQuickItem::contains(point);
  }

#if QT_CONFIG(im)
  //  QVariant QQuickItem::inputMethodQuery(Qt::InputMethodQuery query)
  //      const
  QVariant inputMethodQuery(Qt::InputMethodQuery query) const override {
    if (taken[10]) {
      int handled = 0;
      CuteQQuickRhiItemCall10 call = reinterpret_cast<CuteQQuickRhiItemCall10>(taken[10]);
      const QVariant * given = call(this, static_cast<int>(query), &handled);
      if (handled && given) return *given;
    }
    return QQuickItem::inputMethodQuery(query);
  }
#endif  // QT_CONFIG(im)

  //  void QQuickItem::itemChange(ItemChange a0, const ItemChangeData &a1)
  void itemChange(
      QQuickItem::ItemChange a0,
      const QQuickItem::ItemChangeData &a1) override {
    if (taken[11]) {
      int handled = 0;
      CuteQQuickRhiItemCall11 call = reinterpret_cast<CuteQQuickRhiItemCall11>(taken[11]);
      call(this, static_cast<int>(a0), &a1, &handled);
      if (handled) return;
    }
    QQuickItem::itemChange(a0, a1);
  }

  //  void QQuickItem::classBegin()
  void classBegin() override {
    if (taken[12]) {
      int handled = 0;
      CuteQQuickRhiItemCall12 call = reinterpret_cast<CuteQQuickRhiItemCall12>(taken[12]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItem::classBegin();
  }

  //  void QQuickItem::componentComplete()
  void componentComplete() override {
    if (taken[13]) {
      int handled = 0;
      CuteQQuickRhiItemCall13 call = reinterpret_cast<CuteQQuickRhiItemCall13>(taken[13]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItem::componentComplete();
  }

  //  void QQuickItem::keyPressEvent(QKeyEvent *event)
  void keyPressEvent(QKeyEvent *event) override {
    if (taken[14]) {
      int handled = 0;
      CuteQQuickRhiItemCall14 call = reinterpret_cast<CuteQQuickRhiItemCall14>(taken[14]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::keyPressEvent(event);
  }

  //  void QQuickItem::keyReleaseEvent(QKeyEvent *event)
  void keyReleaseEvent(QKeyEvent *event) override {
    if (taken[15]) {
      int handled = 0;
      CuteQQuickRhiItemCall15 call = reinterpret_cast<CuteQQuickRhiItemCall15>(taken[15]);
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
      CuteQQuickRhiItemCall16 call = reinterpret_cast<CuteQQuickRhiItemCall16>(taken[16]);
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
      CuteQQuickRhiItemCall17 call = reinterpret_cast<CuteQQuickRhiItemCall17>(taken[17]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItem::focusInEvent(a0);
  }

  //  void QQuickItem::focusOutEvent(QFocusEvent *a0)
  void focusOutEvent(QFocusEvent *a0) override {
    if (taken[18]) {
      int handled = 0;
      CuteQQuickRhiItemCall18 call = reinterpret_cast<CuteQQuickRhiItemCall18>(taken[18]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItem::focusOutEvent(a0);
  }

  //  void QQuickItem::mousePressEvent(QMouseEvent *event)
  void mousePressEvent(QMouseEvent *event) override {
    if (taken[19]) {
      int handled = 0;
      CuteQQuickRhiItemCall19 call = reinterpret_cast<CuteQQuickRhiItemCall19>(taken[19]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::mousePressEvent(event);
  }

  //  void QQuickItem::mouseMoveEvent(QMouseEvent *event)
  void mouseMoveEvent(QMouseEvent *event) override {
    if (taken[20]) {
      int handled = 0;
      CuteQQuickRhiItemCall20 call = reinterpret_cast<CuteQQuickRhiItemCall20>(taken[20]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::mouseMoveEvent(event);
  }

  //  void QQuickItem::mouseReleaseEvent(QMouseEvent *event)
  void mouseReleaseEvent(QMouseEvent *event) override {
    if (taken[21]) {
      int handled = 0;
      CuteQQuickRhiItemCall21 call = reinterpret_cast<CuteQQuickRhiItemCall21>(taken[21]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::mouseReleaseEvent(event);
  }

  //  void QQuickItem::mouseDoubleClickEvent(QMouseEvent *event)
  void mouseDoubleClickEvent(QMouseEvent *event) override {
    if (taken[22]) {
      int handled = 0;
      CuteQQuickRhiItemCall22 call = reinterpret_cast<CuteQQuickRhiItemCall22>(taken[22]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::mouseDoubleClickEvent(event);
  }

  //  void QQuickItem::mouseUngrabEvent()
  void mouseUngrabEvent() override {
    if (taken[23]) {
      int handled = 0;
      CuteQQuickRhiItemCall23 call = reinterpret_cast<CuteQQuickRhiItemCall23>(taken[23]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItem::mouseUngrabEvent();
  }

  //  void QQuickItem::touchUngrabEvent()
  void touchUngrabEvent() override {
    if (taken[24]) {
      int handled = 0;
      CuteQQuickRhiItemCall24 call = reinterpret_cast<CuteQQuickRhiItemCall24>(taken[24]);
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
      CuteQQuickRhiItemCall25 call = reinterpret_cast<CuteQQuickRhiItemCall25>(taken[25]);
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
      CuteQQuickRhiItemCall26 call = reinterpret_cast<CuteQQuickRhiItemCall26>(taken[26]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::touchEvent(event);
  }

  //  void QQuickItem::hoverEnterEvent(QHoverEvent *event)
  void hoverEnterEvent(QHoverEvent *event) override {
    if (taken[27]) {
      int handled = 0;
      CuteQQuickRhiItemCall27 call = reinterpret_cast<CuteQQuickRhiItemCall27>(taken[27]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::hoverEnterEvent(event);
  }

  //  void QQuickItem::hoverMoveEvent(QHoverEvent *event)
  void hoverMoveEvent(QHoverEvent *event) override {
    if (taken[28]) {
      int handled = 0;
      CuteQQuickRhiItemCall28 call = reinterpret_cast<CuteQQuickRhiItemCall28>(taken[28]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::hoverMoveEvent(event);
  }

  //  void QQuickItem::hoverLeaveEvent(QHoverEvent *event)
  void hoverLeaveEvent(QHoverEvent *event) override {
    if (taken[29]) {
      int handled = 0;
      CuteQQuickRhiItemCall29 call = reinterpret_cast<CuteQQuickRhiItemCall29>(taken[29]);
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
      CuteQQuickRhiItemCall30 call = reinterpret_cast<CuteQQuickRhiItemCall30>(taken[30]);
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
      CuteQQuickRhiItemCall31 call = reinterpret_cast<CuteQQuickRhiItemCall31>(taken[31]);
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
      CuteQQuickRhiItemCall32 call = reinterpret_cast<CuteQQuickRhiItemCall32>(taken[32]);
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
      CuteQQuickRhiItemCall33 call = reinterpret_cast<CuteQQuickRhiItemCall33>(taken[33]);
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
      CuteQQuickRhiItemCall34 call = reinterpret_cast<CuteQQuickRhiItemCall34>(taken[34]);
      bool given = call(this, a0, a1, &handled);
      if (handled) return given;
    }
    return QQuickItem::childMouseEventFilter(a0, a1);
  }

  //  void QQuickItem::updatePolish()
  void updatePolish() override {
    if (taken[35]) {
      int handled = 0;
      CuteQQuickRhiItemCall35 call = reinterpret_cast<CuteQQuickRhiItemCall35>(taken[35]);
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
      CuteQQuickRhiItemCall36 call = reinterpret_cast<CuteQQuickRhiItemCall36>(taken[36]);
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
      CuteQQuickRhiItemCall37 call = reinterpret_cast<CuteQQuickRhiItemCall37>(taken[37]);
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
      CuteQQuickRhiItemCall38 call = reinterpret_cast<CuteQQuickRhiItemCall38>(taken[38]);
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
      CuteQQuickRhiItemCall39 call = reinterpret_cast<CuteQQuickRhiItemCall39>(taken[39]);
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
      CuteQQuickRhiItemCall40 call = reinterpret_cast<CuteQQuickRhiItemCall40>(taken[40]);
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
      CuteQQuickRhiItemCall41 call = reinterpret_cast<CuteQQuickRhiItemCall41>(taken[41]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QQuickRhiItem::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK13QQuickRhiItem10metaObjectEv(
    const QQuickRhiItem *self) {
  return self->metaObject();
}

//  QString QQuickRhiItem::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN13QQuickRhiItem2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuickRhiItem::tr(s, c, n));
}

//  QQuickRhiItemPrivate *QQuickRhiItem::d_func()
extern "C" Q_DECL_EXPORT
QQuickRhiItemPrivate *ritual_ZN13QQuickRhiItem6d_funcEv(
    QQuickRhiItem *self) {
  return self->d_func();
}

//  const QQuickRhiItemPrivate *QQuickRhiItem::d_func() const
extern "C" Q_DECL_EXPORT
const QQuickRhiItemPrivate *ritual_ZNK13QQuickRhiItem6d_funcEv(
    const QQuickRhiItem *self) {
  return self->d_func();
}

//  QQuickRhiItem::~QQuickRhiItem()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QQuickRhiItemD1Ev(QQuickRhiItem *self) {
  delete self;
}

//  int QQuickRhiItem::sampleCount() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK13QQuickRhiItem11sampleCountEv(const QQuickRhiItem *self) {
  return self->sampleCount();
}

//  void QQuickRhiItem::setSampleCount(int samples)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QQuickRhiItem14setSampleCountEi(
    QQuickRhiItem *self,
    int samples) {
  self->setSampleCount(samples);
}

//  TextureFormat QQuickRhiItem::colorBufferFormat() const
extern "C" Q_DECL_EXPORT
QQuickRhiItem::TextureFormat ritual_ZNK13QQuickRhiItem17colorBufferFormatEv(
    const QQuickRhiItem *self) {
  return self->colorBufferFormat();
}

//  void QQuickRhiItem::setColorBufferFormat(TextureFormat format)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QQuickRhiItem20setColorBufferFormatENS_13TextureFormatE(
    QQuickRhiItem *self,
    QQuickRhiItem::TextureFormat format) {
  self->setColorBufferFormat(format);
}

//  bool QQuickRhiItem::isMirrorVerticallyEnabled() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK13QQuickRhiItem25isMirrorVerticallyEnabledEv(
    const QQuickRhiItem *self) {
  return self->isMirrorVerticallyEnabled();
}

//  void QQuickRhiItem::setMirrorVertically(bool enable)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QQuickRhiItem19setMirrorVerticallyEb(
    QQuickRhiItem *self,
    bool enable) {
  self->setMirrorVertically(enable);
}

//  bool QQuickRhiItem::alphaBlending() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK13QQuickRhiItem13alphaBlendingEv(const QQuickRhiItem *self) {
  return self->alphaBlending();
}

//  void QQuickRhiItem::setAlphaBlending(bool enable)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QQuickRhiItem16setAlphaBlendingEb(
    QQuickRhiItem *self,
    bool enable) {
  self->setAlphaBlending(enable);
}

//  int QQuickRhiItem::fixedColorBufferWidth() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK13QQuickRhiItem21fixedColorBufferWidthEv(
    const QQuickRhiItem *self) {
  return self->fixedColorBufferWidth();
}

//  void QQuickRhiItem::setFixedColorBufferWidth(int width)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QQuickRhiItem24setFixedColorBufferWidthEi(
    QQuickRhiItem *self,
    int width) {
  self->setFixedColorBufferWidth(width);
}

//  int QQuickRhiItem::fixedColorBufferHeight() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK13QQuickRhiItem22fixedColorBufferHeightEv(
    const QQuickRhiItem *self) {
  return self->fixedColorBufferHeight();
}

//  void QQuickRhiItem::setFixedColorBufferHeight(int height)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QQuickRhiItem25setFixedColorBufferHeightEi(
    QQuickRhiItem *self,
    int height) {
  self->setFixedColorBufferHeight(height);
}

//  QSize QQuickRhiItem::effectiveColorBufferSize() const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK13QQuickRhiItem24effectiveColorBufferSizeEv(
    const QQuickRhiItem *self) {
  return new QSize(self->effectiveColorBufferSize());
}

//  bool QQuickRhiItem::isTextureProvider() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK13QQuickRhiItem17isTextureProviderEv(
    const QQuickRhiItem *self) {
  return self->isTextureProvider();
}

//  QSGTextureProvider *QQuickRhiItem::textureProvider() const
extern "C" Q_DECL_EXPORT
QSGTextureProvider *ritual_ZNK13QQuickRhiItem15textureProviderEv(
    const QQuickRhiItem *self) {
  return self->textureProvider();
}

//  QQuickRhiItemRenderer *QQuickRhiItem::createRenderer()
extern "C" Q_DECL_EXPORT
QQuickRhiItemRenderer *ritual_ZN13QQuickRhiItem14createRendererEv(
    QQuickRhiItem *self) {
  return self->createRenderer();
}

//  bool QQuickRhiItem::isAutoRenderTargetEnabled() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK13QQuickRhiItem25isAutoRenderTargetEnabledEv(
    const QQuickRhiItem *self) {
  return self->isAutoRenderTargetEnabled();
}

//  void QQuickRhiItem::setAutoRenderTarget(bool enabled)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QQuickRhiItem19setAutoRenderTargetEb(
    QQuickRhiItem *self,
    bool enabled) {
  self->setAutoRenderTarget(enabled);
}

//  QSGNode *QQuickRhiItem::updatePaintNode(QSGNode *a0, UpdatePaintNodeData
//      *a1)
extern "C" Q_DECL_EXPORT
QSGNode *ritual_ZN13QQuickRhiItem15updatePaintNodeEP7QSGNodePN10QQuickItem19UpdatePaintNodeDataE(
    QQuickRhiItem *self,
    QSGNode *a0,
    QQuickItem::UpdatePaintNodeData *a1) {
  return self->updatePaintNode(a0, a1);
}

//  bool QQuickRhiItem::event(QEvent *a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN13QQuickRhiItem5eventEP6QEvent(
    QQuickRhiItem *self,
    QEvent *a0) {
  return self->event(a0);
}

//  void QQuickRhiItem::geometryChange(const QRectF &newGeometry, const
//      QRectF &oldGeometry)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QQuickRhiItem14geometryChangeERK6QRectFS2_(
    QQuickRhiItem *self,
    const QRectF *newGeometry,
    const QRectF *oldGeometry) {
  self->geometryChange(*newGeometry, *oldGeometry);
}

//  void QQuickRhiItem::releaseResources()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QQuickRhiItem16releaseResourcesEv(QQuickRhiItem *self) {
  self->releaseResources();
}

//  void QQuickRhiItem::invalidateSceneGraph()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QQuickRhiItem20invalidateSceneGraphEv(QQuickRhiItem *self) {
  self->invalidateSceneGraph();
}

//  a Python function taken by a CuteQQuickRhiItem, for the function named by
//      the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQuickRhiItem(
    QQuickRhiItem *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQuickRhiItem *>(self)->take(key, call);
}

//  bool QQuickRhiItem::isTextureProvider() const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK13QQuickRhiItem17isTextureProviderEv(
    const QQuickRhiItem *self) {
  return self->QQuickRhiItem::isTextureProvider();
}

//  QSGTextureProvider *QQuickRhiItem::textureProvider() const
extern "C" Q_DECL_EXPORT
QSGTextureProvider *ritual_own_ZNK13QQuickRhiItem15textureProviderEv(
    const QQuickRhiItem *self) {
  return self->QQuickRhiItem::textureProvider();
}

//  QSGNode *QQuickRhiItem::updatePaintNode(QSGNode *a0, UpdatePaintNodeData
//      *a1)
extern "C" Q_DECL_EXPORT
QSGNode *ritual_own_ZN13QQuickRhiItem15updatePaintNodeEP7QSGNodePN10QQuickItem19UpdatePaintNodeDataE(
    QQuickRhiItem *self,
    QSGNode *a0,
    QQuickItem::UpdatePaintNodeData *a1) {
  return static_cast<OwnQQuickRhiItem *>(self)->OwnQQuickRhiItem::updatePaintNode(
      a0,
      a1);
}

//  bool QQuickRhiItem::event(QEvent *a0)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN13QQuickRhiItem5eventEP6QEvent(
    QQuickRhiItem *self,
    QEvent *a0) {
  return static_cast<OwnQQuickRhiItem *>(self)->OwnQQuickRhiItem::event(a0);
}

//  void QQuickRhiItem::geometryChange(const QRectF &newGeometry, const
//      QRectF &oldGeometry)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN13QQuickRhiItem14geometryChangeERK6QRectFS2_(
    QQuickRhiItem *self,
    const QRectF *newGeometry,
    const QRectF *oldGeometry) {
  static_cast<OwnQQuickRhiItem *>(self)->OwnQQuickRhiItem::geometryChange(
      *newGeometry,
      *oldGeometry);
}

//  void QQuickRhiItem::releaseResources()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN13QQuickRhiItem16releaseResourcesEv(QQuickRhiItem *self) {
  static_cast<OwnQQuickRhiItem *>(self)->OwnQQuickRhiItem::releaseResources();
}
