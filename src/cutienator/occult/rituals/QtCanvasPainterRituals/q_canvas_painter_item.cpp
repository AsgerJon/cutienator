//  Written by dev_tooling.RitualGenerator from the records of
//  QtCanvasPainter/qcanvaspainteritem.h, Qt 6.12.0. Changes made here are
//  lost.
#include <QtGui/qtguiglobal.h>
#include <QtQuick/qtquickglobal.h>
#include <QtCanvasPainter/qtcanvaspainterglobal.h>
#if 1
#include <QtCanvasPainter/QtCanvasPainter>
#include <QtCanvasPainter/qcanvaspainteritem.h>
#include <QtCore/qstring.h>
#include <QtGui/qcolor.h>
#include <QtCore/qvariant.h>
#include <QtCore/qrect.h>
#include <QtCore/qpoint.h>
#include <QtQuick/QtQuick>
#include <QtQuick/qquickitem.h>
#include <QtCore/qmetaobject.h>
#include <QtCore/qmap.h>
#include <QtCore/qhash.h>
#include <iterator>
#include <cstring>

//  Only a class built on QCanvasPainterItem may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQCanvasPainterItem : QCanvasPainterItem {
  using QCanvasPainterItem::event;
};

//  A QCanvasPainterItem that Python can take functions over in. Every QCanvasPainterItem
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void * (*CuteQCanvasPainterItemCall0)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQCanvasPainterItemCall1)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
typedef bool (*CuteQCanvasPainterItemCall2)(const void *, int *);
typedef void * (*CuteQCanvasPainterItemCall3)(const void *, int *);
typedef void * (*CuteQCanvasPainterItemCall4)(const void *, QSGNode *, QQuickItem::UpdatePaintNodeData *, int *);
typedef void (*CuteQCanvasPainterItemCall5)(const void *, const QRectF *, const QRectF *, int *);
typedef void (*CuteQCanvasPainterItemCall6)(const void *, int *);
typedef const QRectF * (*CuteQCanvasPainterItemCall7)(const void *, int *);
typedef const QRectF * (*CuteQCanvasPainterItemCall8)(const void *, int *);
typedef bool (*CuteQCanvasPainterItemCall9)(const void *, const QPointF *, int *);
#if QT_CONFIG(im)
typedef const QVariant * (*CuteQCanvasPainterItemCall10)(const void *, int, int *);
#endif  // QT_CONFIG(im)
typedef void (*CuteQCanvasPainterItemCall11)(const void *, int, const QQuickItem::ItemChangeData *, int *);
typedef void (*CuteQCanvasPainterItemCall12)(const void *, int *);
typedef void (*CuteQCanvasPainterItemCall13)(const void *, int *);
typedef void (*CuteQCanvasPainterItemCall14)(const void *, QKeyEvent *, int *);
typedef void (*CuteQCanvasPainterItemCall15)(const void *, QKeyEvent *, int *);
#if QT_CONFIG(im)
typedef void (*CuteQCanvasPainterItemCall16)(const void *, QInputMethodEvent *, int *);
#endif  // QT_CONFIG(im)
typedef void (*CuteQCanvasPainterItemCall17)(const void *, QFocusEvent *, int *);
typedef void (*CuteQCanvasPainterItemCall18)(const void *, QFocusEvent *, int *);
typedef void (*CuteQCanvasPainterItemCall19)(const void *, QMouseEvent *, int *);
typedef void (*CuteQCanvasPainterItemCall20)(const void *, QMouseEvent *, int *);
typedef void (*CuteQCanvasPainterItemCall21)(const void *, QMouseEvent *, int *);
typedef void (*CuteQCanvasPainterItemCall22)(const void *, QMouseEvent *, int *);
typedef void (*CuteQCanvasPainterItemCall23)(const void *, int *);
typedef void (*CuteQCanvasPainterItemCall24)(const void *, int *);
#if QT_CONFIG(wheelevent)
typedef void (*CuteQCanvasPainterItemCall25)(const void *, QWheelEvent *, int *);
#endif  // QT_CONFIG(wheelevent)
typedef void (*CuteQCanvasPainterItemCall26)(const void *, QTouchEvent *, int *);
typedef void (*CuteQCanvasPainterItemCall27)(const void *, QHoverEvent *, int *);
typedef void (*CuteQCanvasPainterItemCall28)(const void *, QHoverEvent *, int *);
typedef void (*CuteQCanvasPainterItemCall29)(const void *, QHoverEvent *, int *);
#if QT_CONFIG(quick_draganddrop)
typedef void (*CuteQCanvasPainterItemCall30)(const void *, QDragEnterEvent *, int *);
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
typedef void (*CuteQCanvasPainterItemCall31)(const void *, QDragMoveEvent *, int *);
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
typedef void (*CuteQCanvasPainterItemCall32)(const void *, QDragLeaveEvent *, int *);
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
typedef void (*CuteQCanvasPainterItemCall33)(const void *, QDropEvent *, int *);
#endif  // QT_CONFIG(quick_draganddrop)
typedef bool (*CuteQCanvasPainterItemCall34)(const void *, QQuickItem *, QEvent *, int *);
typedef void (*CuteQCanvasPainterItemCall35)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQCanvasPainterItemCall36)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQCanvasPainterItemCall37)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQCanvasPainterItemCall38)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQCanvasPainterItemCall39)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQCanvasPainterItemCall40)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQCanvasPainterItemCall41)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQCanvasPainterItem : public QCanvasPainterItem {
public:
  using QCanvasPainterItem::QCanvasPainterItem;
  void *taken[42] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZNK18QCanvasPainterItem18createItemRendererEv")) {
      taken[0] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[1] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZNK10QQuickItem17isTextureProviderEv")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK10QQuickItem15textureProviderEv")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem15updatePaintNodeEP7QSGNodePNS_19UpdatePaintNodeDataE")) {
      taken[4] = call;
      return true;
    }
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

  //  QCanvasPainterItemRenderer *QCanvasPainterItem::createItemRenderer()
  //      const
  QCanvasPainterItemRenderer *createItemRenderer() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQCanvasPainterItemCall0 call = reinterpret_cast<CuteQCanvasPainterItemCall0>(taken[0]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QCanvasPainterItemRenderer *>(given);
    }
    return {};
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QCanvasPainterItem::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[1]) {
      int handled = 0;
      CuteQCanvasPainterItemCall1 call = reinterpret_cast<CuteQCanvasPainterItemCall1>(taken[1]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QCanvasPainterItem::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

  //  bool QQuickRhiItem::isTextureProvider() const
  bool isTextureProvider() const override {
    if (taken[2]) {
      int handled = 0;
      CuteQCanvasPainterItemCall2 call = reinterpret_cast<CuteQCanvasPainterItemCall2>(taken[2]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QQuickRhiItem::isTextureProvider();
  }

  //  QSGTextureProvider *QQuickRhiItem::textureProvider() const
  QSGTextureProvider *textureProvider() const override {
    if (taken[3]) {
      int handled = 0;
      CuteQCanvasPainterItemCall3 call = reinterpret_cast<CuteQCanvasPainterItemCall3>(taken[3]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QSGTextureProvider *>(given);
    }
    return QQuickRhiItem::textureProvider();
  }

  //  QSGNode *QQuickRhiItem::updatePaintNode(QSGNode *a0,
  //      UpdatePaintNodeData *a1)
  QSGNode *updatePaintNode(
      QSGNode *a0,
      QQuickItem::UpdatePaintNodeData *a1) override {
    if (taken[4]) {
      int handled = 0;
      CuteQCanvasPainterItemCall4 call = reinterpret_cast<CuteQCanvasPainterItemCall4>(taken[4]);
      void * given = call(this, a0, a1, &handled);
      if (handled) return static_cast<QSGNode *>(given);
    }
    return QQuickRhiItem::updatePaintNode(a0, a1);
  }

  //  void QQuickRhiItem::geometryChange(const QRectF &newGeometry, const
  //      QRectF &oldGeometry)
  void geometryChange(
      const QRectF &newGeometry,
      const QRectF &oldGeometry) override {
    if (taken[5]) {
      int handled = 0;
      CuteQCanvasPainterItemCall5 call = reinterpret_cast<CuteQCanvasPainterItemCall5>(taken[5]);
      call(this, &newGeometry, &oldGeometry, &handled);
      if (handled) return;
    }
    QQuickRhiItem::geometryChange(newGeometry, oldGeometry);
  }

  //  void QQuickRhiItem::releaseResources()
  void releaseResources() override {
    if (taken[6]) {
      int handled = 0;
      CuteQCanvasPainterItemCall6 call = reinterpret_cast<CuteQCanvasPainterItemCall6>(taken[6]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickRhiItem::releaseResources();
  }

  //  QRectF QQuickItem::boundingRect() const
  QRectF boundingRect() const override {
    if (taken[7]) {
      int handled = 0;
      CuteQCanvasPainterItemCall7 call = reinterpret_cast<CuteQCanvasPainterItemCall7>(taken[7]);
      const QRectF * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QQuickItem::boundingRect();
  }

  //  QRectF QQuickItem::clipRect() const
  QRectF clipRect() const override {
    if (taken[8]) {
      int handled = 0;
      CuteQCanvasPainterItemCall8 call = reinterpret_cast<CuteQCanvasPainterItemCall8>(taken[8]);
      const QRectF * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QQuickItem::clipRect();
  }

  //  bool QQuickItem::contains(const QPointF &point) const
  bool contains(const QPointF &point) const override {
    if (taken[9]) {
      int handled = 0;
      CuteQCanvasPainterItemCall9 call = reinterpret_cast<CuteQCanvasPainterItemCall9>(taken[9]);
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
      CuteQCanvasPainterItemCall10 call = reinterpret_cast<CuteQCanvasPainterItemCall10>(taken[10]);
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
      CuteQCanvasPainterItemCall11 call = reinterpret_cast<CuteQCanvasPainterItemCall11>(taken[11]);
      call(this, static_cast<int>(a0), &a1, &handled);
      if (handled) return;
    }
    QQuickItem::itemChange(a0, a1);
  }

  //  void QQuickItem::classBegin()
  void classBegin() override {
    if (taken[12]) {
      int handled = 0;
      CuteQCanvasPainterItemCall12 call = reinterpret_cast<CuteQCanvasPainterItemCall12>(taken[12]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItem::classBegin();
  }

  //  void QQuickItem::componentComplete()
  void componentComplete() override {
    if (taken[13]) {
      int handled = 0;
      CuteQCanvasPainterItemCall13 call = reinterpret_cast<CuteQCanvasPainterItemCall13>(taken[13]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItem::componentComplete();
  }

  //  void QQuickItem::keyPressEvent(QKeyEvent *event)
  void keyPressEvent(QKeyEvent *event) override {
    if (taken[14]) {
      int handled = 0;
      CuteQCanvasPainterItemCall14 call = reinterpret_cast<CuteQCanvasPainterItemCall14>(taken[14]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::keyPressEvent(event);
  }

  //  void QQuickItem::keyReleaseEvent(QKeyEvent *event)
  void keyReleaseEvent(QKeyEvent *event) override {
    if (taken[15]) {
      int handled = 0;
      CuteQCanvasPainterItemCall15 call = reinterpret_cast<CuteQCanvasPainterItemCall15>(taken[15]);
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
      CuteQCanvasPainterItemCall16 call = reinterpret_cast<CuteQCanvasPainterItemCall16>(taken[16]);
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
      CuteQCanvasPainterItemCall17 call = reinterpret_cast<CuteQCanvasPainterItemCall17>(taken[17]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItem::focusInEvent(a0);
  }

  //  void QQuickItem::focusOutEvent(QFocusEvent *a0)
  void focusOutEvent(QFocusEvent *a0) override {
    if (taken[18]) {
      int handled = 0;
      CuteQCanvasPainterItemCall18 call = reinterpret_cast<CuteQCanvasPainterItemCall18>(taken[18]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItem::focusOutEvent(a0);
  }

  //  void QQuickItem::mousePressEvent(QMouseEvent *event)
  void mousePressEvent(QMouseEvent *event) override {
    if (taken[19]) {
      int handled = 0;
      CuteQCanvasPainterItemCall19 call = reinterpret_cast<CuteQCanvasPainterItemCall19>(taken[19]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::mousePressEvent(event);
  }

  //  void QQuickItem::mouseMoveEvent(QMouseEvent *event)
  void mouseMoveEvent(QMouseEvent *event) override {
    if (taken[20]) {
      int handled = 0;
      CuteQCanvasPainterItemCall20 call = reinterpret_cast<CuteQCanvasPainterItemCall20>(taken[20]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::mouseMoveEvent(event);
  }

  //  void QQuickItem::mouseReleaseEvent(QMouseEvent *event)
  void mouseReleaseEvent(QMouseEvent *event) override {
    if (taken[21]) {
      int handled = 0;
      CuteQCanvasPainterItemCall21 call = reinterpret_cast<CuteQCanvasPainterItemCall21>(taken[21]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::mouseReleaseEvent(event);
  }

  //  void QQuickItem::mouseDoubleClickEvent(QMouseEvent *event)
  void mouseDoubleClickEvent(QMouseEvent *event) override {
    if (taken[22]) {
      int handled = 0;
      CuteQCanvasPainterItemCall22 call = reinterpret_cast<CuteQCanvasPainterItemCall22>(taken[22]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::mouseDoubleClickEvent(event);
  }

  //  void QQuickItem::mouseUngrabEvent()
  void mouseUngrabEvent() override {
    if (taken[23]) {
      int handled = 0;
      CuteQCanvasPainterItemCall23 call = reinterpret_cast<CuteQCanvasPainterItemCall23>(taken[23]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItem::mouseUngrabEvent();
  }

  //  void QQuickItem::touchUngrabEvent()
  void touchUngrabEvent() override {
    if (taken[24]) {
      int handled = 0;
      CuteQCanvasPainterItemCall24 call = reinterpret_cast<CuteQCanvasPainterItemCall24>(taken[24]);
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
      CuteQCanvasPainterItemCall25 call = reinterpret_cast<CuteQCanvasPainterItemCall25>(taken[25]);
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
      CuteQCanvasPainterItemCall26 call = reinterpret_cast<CuteQCanvasPainterItemCall26>(taken[26]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::touchEvent(event);
  }

  //  void QQuickItem::hoverEnterEvent(QHoverEvent *event)
  void hoverEnterEvent(QHoverEvent *event) override {
    if (taken[27]) {
      int handled = 0;
      CuteQCanvasPainterItemCall27 call = reinterpret_cast<CuteQCanvasPainterItemCall27>(taken[27]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::hoverEnterEvent(event);
  }

  //  void QQuickItem::hoverMoveEvent(QHoverEvent *event)
  void hoverMoveEvent(QHoverEvent *event) override {
    if (taken[28]) {
      int handled = 0;
      CuteQCanvasPainterItemCall28 call = reinterpret_cast<CuteQCanvasPainterItemCall28>(taken[28]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::hoverMoveEvent(event);
  }

  //  void QQuickItem::hoverLeaveEvent(QHoverEvent *event)
  void hoverLeaveEvent(QHoverEvent *event) override {
    if (taken[29]) {
      int handled = 0;
      CuteQCanvasPainterItemCall29 call = reinterpret_cast<CuteQCanvasPainterItemCall29>(taken[29]);
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
      CuteQCanvasPainterItemCall30 call = reinterpret_cast<CuteQCanvasPainterItemCall30>(taken[30]);
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
      CuteQCanvasPainterItemCall31 call = reinterpret_cast<CuteQCanvasPainterItemCall31>(taken[31]);
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
      CuteQCanvasPainterItemCall32 call = reinterpret_cast<CuteQCanvasPainterItemCall32>(taken[32]);
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
      CuteQCanvasPainterItemCall33 call = reinterpret_cast<CuteQCanvasPainterItemCall33>(taken[33]);
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
      CuteQCanvasPainterItemCall34 call = reinterpret_cast<CuteQCanvasPainterItemCall34>(taken[34]);
      bool given = call(this, a0, a1, &handled);
      if (handled) return given;
    }
    return QQuickItem::childMouseEventFilter(a0, a1);
  }

  //  void QQuickItem::updatePolish()
  void updatePolish() override {
    if (taken[35]) {
      int handled = 0;
      CuteQCanvasPainterItemCall35 call = reinterpret_cast<CuteQCanvasPainterItemCall35>(taken[35]);
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
      CuteQCanvasPainterItemCall36 call = reinterpret_cast<CuteQCanvasPainterItemCall36>(taken[36]);
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
      CuteQCanvasPainterItemCall37 call = reinterpret_cast<CuteQCanvasPainterItemCall37>(taken[37]);
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
      CuteQCanvasPainterItemCall38 call = reinterpret_cast<CuteQCanvasPainterItemCall38>(taken[38]);
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
      CuteQCanvasPainterItemCall39 call = reinterpret_cast<CuteQCanvasPainterItemCall39>(taken[39]);
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
      CuteQCanvasPainterItemCall40 call = reinterpret_cast<CuteQCanvasPainterItemCall40>(taken[40]);
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
      CuteQCanvasPainterItemCall41 call = reinterpret_cast<CuteQCanvasPainterItemCall41>(taken[41]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QCanvasPainterItem::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK18QCanvasPainterItem10metaObjectEv(
    const QCanvasPainterItem *self) {
  return self->metaObject();
}

//  QString QCanvasPainterItem::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN18QCanvasPainterItem2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QCanvasPainterItem::tr(s, c, n));
}

//  QCanvasPainterItem::~QCanvasPainterItem()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QCanvasPainterItemD1Ev(QCanvasPainterItem *self) {
  delete self;
}

//  QColor QCanvasPainterItem::fillColor() const
extern "C" Q_DECL_EXPORT
QColor *ritual_ZNK18QCanvasPainterItem9fillColorEv(
    const QCanvasPainterItem *self) {
  return new QColor(self->fillColor());
}

//  void QCanvasPainterItem::setFillColor(QColor color)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QCanvasPainterItem12setFillColorE6QColor(
    QCanvasPainterItem *self,
    const QColor *color) {
  self->setFillColor(*color);
}

//  QVariantMap QCanvasPainterItem::debug()
extern "C" Q_DECL_EXPORT
QMap<QString, QVariant> *ritual_ZN18QCanvasPainterItem5debugEv(
    QCanvasPainterItem *self) {
  return new QMap<QString, QVariant>(self->debug());
}

//  QCanvasPainterItemRenderer *QCanvasPainterItem::createItemRenderer()
//      const
extern "C" Q_DECL_EXPORT
QCanvasPainterItemRenderer *ritual_ZNK18QCanvasPainterItem18createItemRendererEv(
    const QCanvasPainterItem *self) {
  return self->createItemRenderer();
}

//  QQuickRhiItemRenderer *QCanvasPainterItem::createRenderer()
extern "C" Q_DECL_EXPORT
QQuickRhiItemRenderer *ritual_ZN18QCanvasPainterItem14createRendererEv(
    QCanvasPainterItem *self) {
  return self->createRenderer();
}

//  bool QCanvasPainterItem::event(QEvent *event)
extern "C" Q_DECL_EXPORT
bool ritual_ZN18QCanvasPainterItem5eventEP6QEvent(
    QCanvasPainterItem *self,
    QEvent *event) {
  return self->event(event);
}

//  QCanvasPainterItemPrivate *QCanvasPainterItem::d_func()
extern "C" Q_DECL_EXPORT
QCanvasPainterItemPrivate *ritual_ZN18QCanvasPainterItem6d_funcEv(
    QCanvasPainterItem *self) {
  return self->d_func();
}

//  const QCanvasPainterItemPrivate *QCanvasPainterItem::d_func() const
extern "C" Q_DECL_EXPORT
const QCanvasPainterItemPrivate *ritual_ZNK18QCanvasPainterItem6d_funcEv(
    const QCanvasPainterItem *self) {
  return self->d_func();
}

//  a Python function taken by a CuteQCanvasPainterItem, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QCanvasPainterItem(
    QCanvasPainterItem *self,
    const char *key,
    void *call) {
  return static_cast<CuteQCanvasPainterItem *>(self)->take(key, call);
}

//  bool QCanvasPainterItem::event(QEvent *event)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN18QCanvasPainterItem5eventEP6QEvent(
    QCanvasPainterItem *self,
    QEvent *event) {
  return static_cast<OwnQCanvasPainterItem *>(self)->OwnQCanvasPainterItem::event(
      event);
}

#endif  // 1
