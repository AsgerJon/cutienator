//  Written by dev_tooling.RitualGenerator from the records of
//  QtLocation/6.12.0/QtLocation/private/qdeclarativegeomapitemview_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtGui/qtguiglobal.h>
#include <QtQuick/qtquickglobal.h>
#include <QtLocation/6.12.0/QtLocation/private/qlocationglobal_p.h>
#include <QtLocation/QtLocation>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtLocation/6.12.0/QtLocation/private/qdeclarativegeomapitemview_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qvariant.h>
#include <QtQuick/QtQuick>
#include <QtQuick/qquickitem.h>
#include <QtQmlModels/QtQmlModels>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQmlModels/6.12.0/QtQmlModels/private/qqmlchangeset_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qrect.h>
#include <QtCore/qpoint.h>
#include <QtCore/qmetaobject.h>
#include <QtCore/qlist.h>
#include <cstring>

//  A QDeclarativeGeoMapItemView that Python can take functions over in. Every QDeclarativeGeoMapItemView
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQDeclarativeGeoMapItemViewCall0)(const void *, int *);
typedef void (*CuteQDeclarativeGeoMapItemViewCall1)(const void *, int *);
typedef const QRectF * (*CuteQDeclarativeGeoMapItemViewCall2)(const void *, int *);
typedef const QRectF * (*CuteQDeclarativeGeoMapItemViewCall3)(const void *, int *);
typedef bool (*CuteQDeclarativeGeoMapItemViewCall4)(const void *, const QPointF *, int *);
#if QT_CONFIG(im)
typedef const QVariant * (*CuteQDeclarativeGeoMapItemViewCall5)(const void *, int, int *);
#endif  // QT_CONFIG(im)
typedef bool (*CuteQDeclarativeGeoMapItemViewCall6)(const void *, int *);
typedef void * (*CuteQDeclarativeGeoMapItemViewCall7)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQDeclarativeGeoMapItemViewCall8)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
typedef void (*CuteQDeclarativeGeoMapItemViewCall9)(const void *, int, const QQuickItem::ItemChangeData *, int *);
typedef void (*CuteQDeclarativeGeoMapItemViewCall10)(const void *, const QRectF *, const QRectF *, int *);
typedef void (*CuteQDeclarativeGeoMapItemViewCall11)(const void *, QKeyEvent *, int *);
typedef void (*CuteQDeclarativeGeoMapItemViewCall12)(const void *, QKeyEvent *, int *);
#if QT_CONFIG(im)
typedef void (*CuteQDeclarativeGeoMapItemViewCall13)(const void *, QInputMethodEvent *, int *);
#endif  // QT_CONFIG(im)
typedef void (*CuteQDeclarativeGeoMapItemViewCall14)(const void *, QFocusEvent *, int *);
typedef void (*CuteQDeclarativeGeoMapItemViewCall15)(const void *, QFocusEvent *, int *);
typedef void (*CuteQDeclarativeGeoMapItemViewCall16)(const void *, QMouseEvent *, int *);
typedef void (*CuteQDeclarativeGeoMapItemViewCall17)(const void *, QMouseEvent *, int *);
typedef void (*CuteQDeclarativeGeoMapItemViewCall18)(const void *, QMouseEvent *, int *);
typedef void (*CuteQDeclarativeGeoMapItemViewCall19)(const void *, QMouseEvent *, int *);
typedef void (*CuteQDeclarativeGeoMapItemViewCall20)(const void *, int *);
typedef void (*CuteQDeclarativeGeoMapItemViewCall21)(const void *, int *);
#if QT_CONFIG(wheelevent)
typedef void (*CuteQDeclarativeGeoMapItemViewCall22)(const void *, QWheelEvent *, int *);
#endif  // QT_CONFIG(wheelevent)
typedef void (*CuteQDeclarativeGeoMapItemViewCall23)(const void *, QTouchEvent *, int *);
typedef void (*CuteQDeclarativeGeoMapItemViewCall24)(const void *, QHoverEvent *, int *);
typedef void (*CuteQDeclarativeGeoMapItemViewCall25)(const void *, QHoverEvent *, int *);
typedef void (*CuteQDeclarativeGeoMapItemViewCall26)(const void *, QHoverEvent *, int *);
#if QT_CONFIG(quick_draganddrop)
typedef void (*CuteQDeclarativeGeoMapItemViewCall27)(const void *, QDragEnterEvent *, int *);
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
typedef void (*CuteQDeclarativeGeoMapItemViewCall28)(const void *, QDragMoveEvent *, int *);
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
typedef void (*CuteQDeclarativeGeoMapItemViewCall29)(const void *, QDragLeaveEvent *, int *);
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
typedef void (*CuteQDeclarativeGeoMapItemViewCall30)(const void *, QDropEvent *, int *);
#endif  // QT_CONFIG(quick_draganddrop)
typedef bool (*CuteQDeclarativeGeoMapItemViewCall31)(const void *, QQuickItem *, QEvent *, int *);
typedef void * (*CuteQDeclarativeGeoMapItemViewCall32)(const void *, QSGNode *, QQuickItem::UpdatePaintNodeData *, int *);
typedef void (*CuteQDeclarativeGeoMapItemViewCall33)(const void *, int *);
typedef void (*CuteQDeclarativeGeoMapItemViewCall34)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQDeclarativeGeoMapItemViewCall35)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQDeclarativeGeoMapItemViewCall36)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQDeclarativeGeoMapItemViewCall37)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQDeclarativeGeoMapItemViewCall38)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQDeclarativeGeoMapItemViewCall39)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQDeclarativeGeoMapItemViewCall40)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQDeclarativeGeoMapItemView : public QDeclarativeGeoMapItemView {
public:
  using QDeclarativeGeoMapItemView::QDeclarativeGeoMapItemView;
  void *taken[41] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN16QQmlParserStatus17componentCompleteEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQmlParserStatus10classBeginEv")) {
      taken[1] = call;
      return true;
    }
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
    if (!std::strcmp(key, "_ZN10QQuickItem10itemChangeENS_10ItemChangeERKNS_14ItemChangeDataE")) {
      taken[9] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem14geometryChangeERK6QRectFS2_")) {
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

  //  void QDeclarativeGeoMapItemView::componentComplete()
  void componentComplete() override {
    if (taken[0]) {
      int handled = 0;
      CuteQDeclarativeGeoMapItemViewCall0 call = reinterpret_cast<CuteQDeclarativeGeoMapItemViewCall0>(taken[0]);
      call(this, &handled);
      if (handled) return;
    }
    QDeclarativeGeoMapItemView::componentComplete();
  }

  //  void QDeclarativeGeoMapItemView::classBegin()
  void classBegin() override {
    if (taken[1]) {
      int handled = 0;
      CuteQDeclarativeGeoMapItemViewCall1 call = reinterpret_cast<CuteQDeclarativeGeoMapItemViewCall1>(taken[1]);
      call(this, &handled);
      if (handled) return;
    }
    QDeclarativeGeoMapItemView::classBegin();
  }

  //  QRectF QQuickItem::boundingRect() const
  QRectF boundingRect() const override {
    if (taken[2]) {
      int handled = 0;
      CuteQDeclarativeGeoMapItemViewCall2 call = reinterpret_cast<CuteQDeclarativeGeoMapItemViewCall2>(taken[2]);
      const QRectF * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QQuickItem::boundingRect();
  }

  //  QRectF QQuickItem::clipRect() const
  QRectF clipRect() const override {
    if (taken[3]) {
      int handled = 0;
      CuteQDeclarativeGeoMapItemViewCall3 call = reinterpret_cast<CuteQDeclarativeGeoMapItemViewCall3>(taken[3]);
      const QRectF * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QQuickItem::clipRect();
  }

  //  bool QQuickItem::contains(const QPointF &point) const
  bool contains(const QPointF &point) const override {
    if (taken[4]) {
      int handled = 0;
      CuteQDeclarativeGeoMapItemViewCall4 call = reinterpret_cast<CuteQDeclarativeGeoMapItemViewCall4>(taken[4]);
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
      CuteQDeclarativeGeoMapItemViewCall5 call = reinterpret_cast<CuteQDeclarativeGeoMapItemViewCall5>(taken[5]);
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
      CuteQDeclarativeGeoMapItemViewCall6 call = reinterpret_cast<CuteQDeclarativeGeoMapItemViewCall6>(taken[6]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QQuickItem::isTextureProvider();
  }

  //  QSGTextureProvider *QQuickItem::textureProvider() const
  QSGTextureProvider *textureProvider() const override {
    if (taken[7]) {
      int handled = 0;
      CuteQDeclarativeGeoMapItemViewCall7 call = reinterpret_cast<CuteQDeclarativeGeoMapItemViewCall7>(taken[7]);
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
      CuteQDeclarativeGeoMapItemViewCall8 call = reinterpret_cast<CuteQDeclarativeGeoMapItemViewCall8>(taken[8]);
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
    if (taken[9]) {
      int handled = 0;
      CuteQDeclarativeGeoMapItemViewCall9 call = reinterpret_cast<CuteQDeclarativeGeoMapItemViewCall9>(taken[9]);
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
    if (taken[10]) {
      int handled = 0;
      CuteQDeclarativeGeoMapItemViewCall10 call = reinterpret_cast<CuteQDeclarativeGeoMapItemViewCall10>(taken[10]);
      call(this, &newGeometry, &oldGeometry, &handled);
      if (handled) return;
    }
    QQuickItem::geometryChange(newGeometry, oldGeometry);
  }

  //  void QQuickItem::keyPressEvent(QKeyEvent *event)
  void keyPressEvent(QKeyEvent *event) override {
    if (taken[11]) {
      int handled = 0;
      CuteQDeclarativeGeoMapItemViewCall11 call = reinterpret_cast<CuteQDeclarativeGeoMapItemViewCall11>(taken[11]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::keyPressEvent(event);
  }

  //  void QQuickItem::keyReleaseEvent(QKeyEvent *event)
  void keyReleaseEvent(QKeyEvent *event) override {
    if (taken[12]) {
      int handled = 0;
      CuteQDeclarativeGeoMapItemViewCall12 call = reinterpret_cast<CuteQDeclarativeGeoMapItemViewCall12>(taken[12]);
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
      CuteQDeclarativeGeoMapItemViewCall13 call = reinterpret_cast<CuteQDeclarativeGeoMapItemViewCall13>(taken[13]);
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
      CuteQDeclarativeGeoMapItemViewCall14 call = reinterpret_cast<CuteQDeclarativeGeoMapItemViewCall14>(taken[14]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItem::focusInEvent(a0);
  }

  //  void QQuickItem::focusOutEvent(QFocusEvent *a0)
  void focusOutEvent(QFocusEvent *a0) override {
    if (taken[15]) {
      int handled = 0;
      CuteQDeclarativeGeoMapItemViewCall15 call = reinterpret_cast<CuteQDeclarativeGeoMapItemViewCall15>(taken[15]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItem::focusOutEvent(a0);
  }

  //  void QQuickItem::mousePressEvent(QMouseEvent *event)
  void mousePressEvent(QMouseEvent *event) override {
    if (taken[16]) {
      int handled = 0;
      CuteQDeclarativeGeoMapItemViewCall16 call = reinterpret_cast<CuteQDeclarativeGeoMapItemViewCall16>(taken[16]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::mousePressEvent(event);
  }

  //  void QQuickItem::mouseMoveEvent(QMouseEvent *event)
  void mouseMoveEvent(QMouseEvent *event) override {
    if (taken[17]) {
      int handled = 0;
      CuteQDeclarativeGeoMapItemViewCall17 call = reinterpret_cast<CuteQDeclarativeGeoMapItemViewCall17>(taken[17]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::mouseMoveEvent(event);
  }

  //  void QQuickItem::mouseReleaseEvent(QMouseEvent *event)
  void mouseReleaseEvent(QMouseEvent *event) override {
    if (taken[18]) {
      int handled = 0;
      CuteQDeclarativeGeoMapItemViewCall18 call = reinterpret_cast<CuteQDeclarativeGeoMapItemViewCall18>(taken[18]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::mouseReleaseEvent(event);
  }

  //  void QQuickItem::mouseDoubleClickEvent(QMouseEvent *event)
  void mouseDoubleClickEvent(QMouseEvent *event) override {
    if (taken[19]) {
      int handled = 0;
      CuteQDeclarativeGeoMapItemViewCall19 call = reinterpret_cast<CuteQDeclarativeGeoMapItemViewCall19>(taken[19]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::mouseDoubleClickEvent(event);
  }

  //  void QQuickItem::mouseUngrabEvent()
  void mouseUngrabEvent() override {
    if (taken[20]) {
      int handled = 0;
      CuteQDeclarativeGeoMapItemViewCall20 call = reinterpret_cast<CuteQDeclarativeGeoMapItemViewCall20>(taken[20]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItem::mouseUngrabEvent();
  }

  //  void QQuickItem::touchUngrabEvent()
  void touchUngrabEvent() override {
    if (taken[21]) {
      int handled = 0;
      CuteQDeclarativeGeoMapItemViewCall21 call = reinterpret_cast<CuteQDeclarativeGeoMapItemViewCall21>(taken[21]);
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
      CuteQDeclarativeGeoMapItemViewCall22 call = reinterpret_cast<CuteQDeclarativeGeoMapItemViewCall22>(taken[22]);
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
      CuteQDeclarativeGeoMapItemViewCall23 call = reinterpret_cast<CuteQDeclarativeGeoMapItemViewCall23>(taken[23]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::touchEvent(event);
  }

  //  void QQuickItem::hoverEnterEvent(QHoverEvent *event)
  void hoverEnterEvent(QHoverEvent *event) override {
    if (taken[24]) {
      int handled = 0;
      CuteQDeclarativeGeoMapItemViewCall24 call = reinterpret_cast<CuteQDeclarativeGeoMapItemViewCall24>(taken[24]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::hoverEnterEvent(event);
  }

  //  void QQuickItem::hoverMoveEvent(QHoverEvent *event)
  void hoverMoveEvent(QHoverEvent *event) override {
    if (taken[25]) {
      int handled = 0;
      CuteQDeclarativeGeoMapItemViewCall25 call = reinterpret_cast<CuteQDeclarativeGeoMapItemViewCall25>(taken[25]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::hoverMoveEvent(event);
  }

  //  void QQuickItem::hoverLeaveEvent(QHoverEvent *event)
  void hoverLeaveEvent(QHoverEvent *event) override {
    if (taken[26]) {
      int handled = 0;
      CuteQDeclarativeGeoMapItemViewCall26 call = reinterpret_cast<CuteQDeclarativeGeoMapItemViewCall26>(taken[26]);
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
      CuteQDeclarativeGeoMapItemViewCall27 call = reinterpret_cast<CuteQDeclarativeGeoMapItemViewCall27>(taken[27]);
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
      CuteQDeclarativeGeoMapItemViewCall28 call = reinterpret_cast<CuteQDeclarativeGeoMapItemViewCall28>(taken[28]);
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
      CuteQDeclarativeGeoMapItemViewCall29 call = reinterpret_cast<CuteQDeclarativeGeoMapItemViewCall29>(taken[29]);
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
      CuteQDeclarativeGeoMapItemViewCall30 call = reinterpret_cast<CuteQDeclarativeGeoMapItemViewCall30>(taken[30]);
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
      CuteQDeclarativeGeoMapItemViewCall31 call = reinterpret_cast<CuteQDeclarativeGeoMapItemViewCall31>(taken[31]);
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
      CuteQDeclarativeGeoMapItemViewCall32 call = reinterpret_cast<CuteQDeclarativeGeoMapItemViewCall32>(taken[32]);
      void * given = call(this, a0, a1, &handled);
      if (handled) return static_cast<QSGNode *>(given);
    }
    return QQuickItem::updatePaintNode(a0, a1);
  }

  //  void QQuickItem::releaseResources()
  void releaseResources() override {
    if (taken[33]) {
      int handled = 0;
      CuteQDeclarativeGeoMapItemViewCall33 call = reinterpret_cast<CuteQDeclarativeGeoMapItemViewCall33>(taken[33]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItem::releaseResources();
  }

  //  void QQuickItem::updatePolish()
  void updatePolish() override {
    if (taken[34]) {
      int handled = 0;
      CuteQDeclarativeGeoMapItemViewCall34 call = reinterpret_cast<CuteQDeclarativeGeoMapItemViewCall34>(taken[34]);
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
      CuteQDeclarativeGeoMapItemViewCall35 call = reinterpret_cast<CuteQDeclarativeGeoMapItemViewCall35>(taken[35]);
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
      CuteQDeclarativeGeoMapItemViewCall36 call = reinterpret_cast<CuteQDeclarativeGeoMapItemViewCall36>(taken[36]);
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
      CuteQDeclarativeGeoMapItemViewCall37 call = reinterpret_cast<CuteQDeclarativeGeoMapItemViewCall37>(taken[37]);
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
      CuteQDeclarativeGeoMapItemViewCall38 call = reinterpret_cast<CuteQDeclarativeGeoMapItemViewCall38>(taken[38]);
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
      CuteQDeclarativeGeoMapItemViewCall39 call = reinterpret_cast<CuteQDeclarativeGeoMapItemViewCall39>(taken[39]);
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
      CuteQDeclarativeGeoMapItemViewCall40 call = reinterpret_cast<CuteQDeclarativeGeoMapItemViewCall40>(taken[40]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QDeclarativeGeoMapItemView::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK26QDeclarativeGeoMapItemView10metaObjectEv(
    const QDeclarativeGeoMapItemView *self) {
  return self->metaObject();
}

//  void *QDeclarativeGeoMapItemView::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN26QDeclarativeGeoMapItemView11qt_metacastEPKc(
    QDeclarativeGeoMapItemView *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QDeclarativeGeoMapItemView::qt_metacall(QMetaObject::Call a0, int a1,
//      void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN26QDeclarativeGeoMapItemView11qt_metacallEN11QMetaObject4CallEiPPv(
    QDeclarativeGeoMapItemView *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QDeclarativeGeoMapItemView::tr(const char *s, const char *c, int
//      n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN26QDeclarativeGeoMapItemView2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QDeclarativeGeoMapItemView::tr(s, c, n));
}

//  QDeclarativeGeoMapItemView::QDeclarativeGeoMapItemView(QQuickItem
//      *parent)
extern "C" Q_DECL_EXPORT
QDeclarativeGeoMapItemView *ritual_ZN26QDeclarativeGeoMapItemViewC1EP10QQuickItem(
    QQuickItem *parent) {
  return new CuteQDeclarativeGeoMapItemView(parent);
}

//  QDeclarativeGeoMapItemView::~QDeclarativeGeoMapItemView()
extern "C" Q_DECL_EXPORT
void ritual_ZN26QDeclarativeGeoMapItemViewD1Ev(
    QDeclarativeGeoMapItemView *self) {
  delete self;
}

//  QVariant QDeclarativeGeoMapItemView::model() const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK26QDeclarativeGeoMapItemView5modelEv(
    const QDeclarativeGeoMapItemView *self) {
  return new QVariant(self->model());
}

//  void QDeclarativeGeoMapItemView::setModel(const QVariant &a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QDeclarativeGeoMapItemView8setModelERK8QVariant(
    QDeclarativeGeoMapItemView *self,
    const QVariant *a0) {
  self->setModel(*a0);
}

//  QQmlComponent *QDeclarativeGeoMapItemView::delegate() const
extern "C" Q_DECL_EXPORT
QQmlComponent *ritual_ZNK26QDeclarativeGeoMapItemView8delegateEv(
    const QDeclarativeGeoMapItemView *self) {
  return self->delegate();
}

//  void QDeclarativeGeoMapItemView::setDelegate(QQmlComponent *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QDeclarativeGeoMapItemView11setDelegateEP13QQmlComponent(
    QDeclarativeGeoMapItemView *self,
    QQmlComponent *a0) {
  self->setDelegate(a0);
}

//  bool QDeclarativeGeoMapItemView::autoFitViewport() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK26QDeclarativeGeoMapItemView15autoFitViewportEv(
    const QDeclarativeGeoMapItemView *self) {
  return self->autoFitViewport();
}

//  void QDeclarativeGeoMapItemView::setAutoFitViewport(const bool &fit)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QDeclarativeGeoMapItemView18setAutoFitViewportERKb(
    QDeclarativeGeoMapItemView *self,
    bool fit) {
  self->setAutoFitViewport(fit);
}

//  void QDeclarativeGeoMapItemView::setMap(QDeclarativeGeoMap *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QDeclarativeGeoMapItemView6setMapEP18QDeclarativeGeoMap(
    QDeclarativeGeoMapItemView *self,
    QDeclarativeGeoMap *a0) {
  self->setMap(a0);
}

//  void QDeclarativeGeoMapItemView::removeInstantiatedItems(bool transition)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QDeclarativeGeoMapItemView23removeInstantiatedItemsEb(
    QDeclarativeGeoMapItemView *self,
    bool transition) {
  self->removeInstantiatedItems(transition);
}

//  void QDeclarativeGeoMapItemView::instantiateAllItems()
extern "C" Q_DECL_EXPORT
void ritual_ZN26QDeclarativeGeoMapItemView19instantiateAllItemsEv(
    QDeclarativeGeoMapItemView *self) {
  self->instantiateAllItems();
}

//  void QDeclarativeGeoMapItemView::setIncubateDelegates(bool useIncubators)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QDeclarativeGeoMapItemView20setIncubateDelegatesEb(
    QDeclarativeGeoMapItemView *self,
    bool useIncubators) {
  self->setIncubateDelegates(useIncubators);
}

//  bool QDeclarativeGeoMapItemView::incubateDelegates() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK26QDeclarativeGeoMapItemView17incubateDelegatesEv(
    const QDeclarativeGeoMapItemView *self) {
  return self->incubateDelegates();
}

//  QQmlDelegateModel::DelegateModelAccess
//      QDeclarativeGeoMapItemView::delegateModelAccess() const
extern "C" Q_DECL_EXPORT
QQmlDelegateModel::DelegateModelAccess ritual_ZNK26QDeclarativeGeoMapItemView19delegateModelAccessEv(
    const QDeclarativeGeoMapItemView *self) {
  return self->delegateModelAccess();
}

//  void QDeclarativeGeoMapItemView::setDelegateModelAccess(QQmlDelegateModel
//      ::DelegateModelAccess delegateModelAccess)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QDeclarativeGeoMapItemView22setDelegateModelAccessEN17QQmlDelegateModel19DelegateModelAccessE(
    QDeclarativeGeoMapItemView *self,
    QQmlDelegateModel::DelegateModelAccess delegateModelAccess) {
  self->setDelegateModelAccess(delegateModelAccess);
}

//  QList<QQuickItem *> QDeclarativeGeoMapItemView::mapItems()
extern "C" Q_DECL_EXPORT
QList<QQuickItem *> *ritual_ZN26QDeclarativeGeoMapItemView8mapItemsEv(
    QDeclarativeGeoMapItemView *self) {
  return new QList<QQuickItem *>(self->mapItems());
}

//  void QDeclarativeGeoMapItemView::componentComplete()
extern "C" Q_DECL_EXPORT
void ritual_ZN26QDeclarativeGeoMapItemView17componentCompleteEv(
    QDeclarativeGeoMapItemView *self) {
  self->componentComplete();
}

//  void QDeclarativeGeoMapItemView::classBegin()
extern "C" Q_DECL_EXPORT
void ritual_ZN26QDeclarativeGeoMapItemView10classBeginEv(
    QDeclarativeGeoMapItemView *self) {
  self->classBegin();
}

//  void QDeclarativeGeoMapItemView::modelChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN26QDeclarativeGeoMapItemView12modelChangedEv(
    QDeclarativeGeoMapItemView *self) {
  self->modelChanged();
}

//  void QDeclarativeGeoMapItemView::delegateChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN26QDeclarativeGeoMapItemView15delegateChangedEv(
    QDeclarativeGeoMapItemView *self) {
  self->delegateChanged();
}

//  void QDeclarativeGeoMapItemView::autoFitViewportChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN26QDeclarativeGeoMapItemView22autoFitViewportChangedEv(
    QDeclarativeGeoMapItemView *self) {
  self->autoFitViewportChanged();
}

//  void QDeclarativeGeoMapItemView::incubateDelegatesChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN26QDeclarativeGeoMapItemView24incubateDelegatesChangedEv(
    QDeclarativeGeoMapItemView *self) {
  self->incubateDelegatesChanged();
}

//  void QDeclarativeGeoMapItemView::delegateModelAccessChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN26QDeclarativeGeoMapItemView26delegateModelAccessChangedEv(
    QDeclarativeGeoMapItemView *self) {
  self->delegateModelAccessChanged();
}

//  void QDeclarativeGeoMapItemView::destroyingItem(QObject *object)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QDeclarativeGeoMapItemView14destroyingItemEP7QObject(
    QDeclarativeGeoMapItemView *self,
    QObject *object) {
  self->destroyingItem(object);
}

//  void QDeclarativeGeoMapItemView::initItem(int index, QObject *object)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QDeclarativeGeoMapItemView8initItemEiP7QObject(
    QDeclarativeGeoMapItemView *self,
    int index,
    QObject *object) {
  self->initItem(index, object);
}

//  void QDeclarativeGeoMapItemView::createdItem(int index, QObject *object)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QDeclarativeGeoMapItemView11createdItemEiP7QObject(
    QDeclarativeGeoMapItemView *self,
    int index,
    QObject *object) {
  self->createdItem(index, object);
}

//  void QDeclarativeGeoMapItemView::modelUpdated(const QQmlChangeSet
//      &changeSet, bool reset)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QDeclarativeGeoMapItemView12modelUpdatedERK13QQmlChangeSetb(
    QDeclarativeGeoMapItemView *self,
    const QQmlChangeSet *changeSet,
    bool reset) {
  self->modelUpdated(*changeSet, reset);
}

//  void QDeclarativeGeoMapItemView::exitTransitionFinished()
extern "C" Q_DECL_EXPORT
void ritual_ZN26QDeclarativeGeoMapItemView22exitTransitionFinishedEv(
    QDeclarativeGeoMapItemView *self) {
  self->exitTransitionFinished();
}

//  void QDeclarativeGeoMapItemView::fitViewport()
extern "C" Q_DECL_EXPORT
void ritual_ZN26QDeclarativeGeoMapItemView11fitViewportEv(
    QDeclarativeGeoMapItemView *self) {
  self->fitViewport();
}

//  void QDeclarativeGeoMapItemView::removeDelegateFromMap(int index, bool
//      transition)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QDeclarativeGeoMapItemView21removeDelegateFromMapEib(
    QDeclarativeGeoMapItemView *self,
    int index,
    bool transition) {
  self->removeDelegateFromMap(index, transition);
}

//  void QDeclarativeGeoMapItemView::removeDelegateFromMap(QQuickItem *o)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QDeclarativeGeoMapItemView21removeDelegateFromMapEP10QQuickItem(
    QDeclarativeGeoMapItemView *self,
    QQuickItem *o) {
  self->removeDelegateFromMap(o);
}

//  void QDeclarativeGeoMapItemView::transitionItemOut(QQuickItem *o)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QDeclarativeGeoMapItemView17transitionItemOutEP10QQuickItem(
    QDeclarativeGeoMapItemView *self,
    QQuickItem *o) {
  self->transitionItemOut(o);
}

//  void QDeclarativeGeoMapItemView::terminateExitTransition(QQuickItem *o)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QDeclarativeGeoMapItemView23terminateExitTransitionEP10QQuickItem(
    QDeclarativeGeoMapItemView *self,
    QQuickItem *o) {
  self->terminateExitTransition(o);
}

//  QQmlInstanceModel::ReleaseFlags
//      QDeclarativeGeoMapItemView::disposeDelegate(QQuickItem *item)
extern "C" Q_DECL_EXPORT
int ritual_ZN26QDeclarativeGeoMapItemView15disposeDelegateEP10QQuickItem(
    QDeclarativeGeoMapItemView *self,
    QQuickItem *item) {
  return static_cast<int>(self->disposeDelegate(item).toInt());
}

//  void QDeclarativeGeoMapItemView::insertInstantiatedItem(int index,
//      QQuickItem *o, bool createdItem)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QDeclarativeGeoMapItemView22insertInstantiatedItemEiP10QQuickItemb(
    QDeclarativeGeoMapItemView *self,
    int index,
    QQuickItem *o,
    bool createdItem) {
  self->insertInstantiatedItem(index, o, createdItem);
}

//  void QDeclarativeGeoMapItemView::addItemToMap(QDeclarativeGeoMapItemBase
//      *item, int index, bool createdItem)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QDeclarativeGeoMapItemView12addItemToMapEP26QDeclarativeGeoMapItemBaseib(
    QDeclarativeGeoMapItemView *self,
    QDeclarativeGeoMapItemBase *item,
    int index,
    bool createdItem) {
  self->addItemToMap(item, index, createdItem);
}

//  void
//      QDeclarativeGeoMapItemView::addItemViewToMap(QDeclarativeGeoMapItemVi
//      ew *item, int index, bool createdItem)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QDeclarativeGeoMapItemView16addItemViewToMapEPS_ib(
    QDeclarativeGeoMapItemView *self,
    QDeclarativeGeoMapItemView *item,
    int index,
    bool createdItem) {
  self->addItemViewToMap(item, index, createdItem);
}

//  void
//      QDeclarativeGeoMapItemView::addItemGroupToMap(QDeclarativeGeoMapItemG
//      roup *item, int index, bool createdItem)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QDeclarativeGeoMapItemView17addItemGroupToMapEP27QDeclarativeGeoMapItemGroupib(
    QDeclarativeGeoMapItemView *self,
    QDeclarativeGeoMapItemGroup *item,
    int index,
    bool createdItem) {
  self->addItemGroupToMap(item, index, createdItem);
}

//  void QDeclarativeGeoMapItemView::addDelegateToMap(QQuickItem *object, int
//      index, bool createdItem)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QDeclarativeGeoMapItemView16addDelegateToMapEP10QQuickItemib(
    QDeclarativeGeoMapItemView *self,
    QQuickItem *object,
    int index,
    bool createdItem) {
  self->addDelegateToMap(object, index, createdItem);
}

//  a Python function taken by a CuteQDeclarativeGeoMapItemView, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QDeclarativeGeoMapItemView(
    QDeclarativeGeoMapItemView *self,
    const char *key,
    void *call) {
  return static_cast<CuteQDeclarativeGeoMapItemView *>(self)->take(key, call);
}

//  void QDeclarativeGeoMapItemView::componentComplete()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN26QDeclarativeGeoMapItemView17componentCompleteEv(
    QDeclarativeGeoMapItemView *self) {
  self->QDeclarativeGeoMapItemView::componentComplete();
}

//  void QDeclarativeGeoMapItemView::classBegin()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN26QDeclarativeGeoMapItemView10classBeginEv(
    QDeclarativeGeoMapItemView *self) {
  self->QDeclarativeGeoMapItemView::classBegin();
}
