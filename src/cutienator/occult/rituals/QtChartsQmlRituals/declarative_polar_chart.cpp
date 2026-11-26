//  Written by dev_tooling.RitualGenerator from the records of
//  QtChartsQml/6.12.0/QtChartsQml/private/declarativepolarchart_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtGui/qtguiglobal.h>
#include <QtQuick/qtquickglobal.h>
#include <QtChartsQml/6.12.0/QtChartsQml/private/declarativechartglobal_p.h>
#include <QtChartsQml/QtChartsQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtChartsQml/6.12.0/QtChartsQml/private/declarativepolarchart_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qrect.h>
#include <QtCore/qpoint.h>
#include <QtCore/qvariant.h>
#include <QtQuick/QtQuick>
#include <QtQuick/qquickitem.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A DeclarativePolarChart that Python can take functions over in. Every DeclarativePolarChart
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteDeclarativePolarChartCall0)(const void *, int *);
typedef void (*CuteDeclarativePolarChartCall1)(const void *, const QRectF *, const QRectF *, int *);
typedef void * (*CuteDeclarativePolarChartCall2)(const void *, QSGNode *, QQuickItem::UpdatePaintNodeData *, int *);
typedef void (*CuteDeclarativePolarChartCall3)(const void *, QMouseEvent *, int *);
typedef void (*CuteDeclarativePolarChartCall4)(const void *, QMouseEvent *, int *);
typedef void (*CuteDeclarativePolarChartCall5)(const void *, QHoverEvent *, int *);
typedef void (*CuteDeclarativePolarChartCall6)(const void *, QMouseEvent *, int *);
typedef const QRectF * (*CuteDeclarativePolarChartCall7)(const void *, int *);
typedef const QRectF * (*CuteDeclarativePolarChartCall8)(const void *, int *);
typedef bool (*CuteDeclarativePolarChartCall9)(const void *, const QPointF *, int *);
#if QT_CONFIG(im)
typedef const QVariant * (*CuteDeclarativePolarChartCall10)(const void *, int, int *);
#endif  // QT_CONFIG(im)
typedef bool (*CuteDeclarativePolarChartCall11)(const void *, int *);
typedef void * (*CuteDeclarativePolarChartCall12)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteDeclarativePolarChartCall13)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
typedef void (*CuteDeclarativePolarChartCall14)(const void *, int, const QQuickItem::ItemChangeData *, int *);
typedef void (*CuteDeclarativePolarChartCall15)(const void *, int *);
typedef void (*CuteDeclarativePolarChartCall16)(const void *, QKeyEvent *, int *);
typedef void (*CuteDeclarativePolarChartCall17)(const void *, QKeyEvent *, int *);
#if QT_CONFIG(im)
typedef void (*CuteDeclarativePolarChartCall18)(const void *, QInputMethodEvent *, int *);
#endif  // QT_CONFIG(im)
typedef void (*CuteDeclarativePolarChartCall19)(const void *, QFocusEvent *, int *);
typedef void (*CuteDeclarativePolarChartCall20)(const void *, QFocusEvent *, int *);
typedef void (*CuteDeclarativePolarChartCall21)(const void *, QMouseEvent *, int *);
typedef void (*CuteDeclarativePolarChartCall22)(const void *, int *);
typedef void (*CuteDeclarativePolarChartCall23)(const void *, int *);
#if QT_CONFIG(wheelevent)
typedef void (*CuteDeclarativePolarChartCall24)(const void *, QWheelEvent *, int *);
#endif  // QT_CONFIG(wheelevent)
typedef void (*CuteDeclarativePolarChartCall25)(const void *, QTouchEvent *, int *);
typedef void (*CuteDeclarativePolarChartCall26)(const void *, QHoverEvent *, int *);
typedef void (*CuteDeclarativePolarChartCall27)(const void *, QHoverEvent *, int *);
#if QT_CONFIG(quick_draganddrop)
typedef void (*CuteDeclarativePolarChartCall28)(const void *, QDragEnterEvent *, int *);
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
typedef void (*CuteDeclarativePolarChartCall29)(const void *, QDragMoveEvent *, int *);
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
typedef void (*CuteDeclarativePolarChartCall30)(const void *, QDragLeaveEvent *, int *);
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
typedef void (*CuteDeclarativePolarChartCall31)(const void *, QDropEvent *, int *);
#endif  // QT_CONFIG(quick_draganddrop)
typedef bool (*CuteDeclarativePolarChartCall32)(const void *, QQuickItem *, QEvent *, int *);
typedef void (*CuteDeclarativePolarChartCall33)(const void *, int *);
typedef void (*CuteDeclarativePolarChartCall34)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteDeclarativePolarChartCall35)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteDeclarativePolarChartCall36)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteDeclarativePolarChartCall37)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteDeclarativePolarChartCall38)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteDeclarativePolarChartCall39)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteDeclarativePolarChartCall40)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteDeclarativePolarChart : public DeclarativePolarChart {
public:
  using DeclarativePolarChart::DeclarativePolarChart;
  void *taken[41] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN16QQmlParserStatus17componentCompleteEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem14geometryChangeERK6QRectFS2_")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem15updatePaintNodeEP7QSGNodePNS_19UpdatePaintNodeDataE")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem15mousePressEventEP11QMouseEvent")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem17mouseReleaseEventEP11QMouseEvent")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem14hoverMoveEventEP11QHoverEvent")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem21mouseDoubleClickEventEP11QMouseEvent")) {
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
    if (!std::strcmp(key, "_ZNK10QQuickItem17isTextureProviderEv")) {
      taken[11] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK10QQuickItem15textureProviderEv")) {
      taken[12] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[13] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN10QQuickItem10itemChangeENS_10ItemChangeERKNS_14ItemChangeDataE")) {
      taken[14] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQmlParserStatus10classBeginEv")) {
      taken[15] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem13keyPressEventEP9QKeyEvent")) {
      taken[16] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem15keyReleaseEventEP9QKeyEvent")) {
      taken[17] = call;
      return true;
    }
#if QT_CONFIG(im)
    if (!std::strcmp(key, "_ZN10QQuickItem16inputMethodEventEP17QInputMethodEvent")) {
      taken[18] = call;
      return true;
    }
#endif  // QT_CONFIG(im)
    if (!std::strcmp(key, "_ZN10QQuickItem12focusInEventEP11QFocusEvent")) {
      taken[19] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem13focusOutEventEP11QFocusEvent")) {
      taken[20] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem14mouseMoveEventEP11QMouseEvent")) {
      taken[21] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem16mouseUngrabEventEv")) {
      taken[22] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem16touchUngrabEventEv")) {
      taken[23] = call;
      return true;
    }
#if QT_CONFIG(wheelevent)
    if (!std::strcmp(key, "_ZN10QQuickItem10wheelEventEP11QWheelEvent")) {
      taken[24] = call;
      return true;
    }
#endif  // QT_CONFIG(wheelevent)
    if (!std::strcmp(key, "_ZN10QQuickItem10touchEventEP11QTouchEvent")) {
      taken[25] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem15hoverEnterEventEP11QHoverEvent")) {
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

  //  void DeclarativeChart::componentComplete()
  void componentComplete() override {
    if (taken[0]) {
      int handled = 0;
      CuteDeclarativePolarChartCall0 call = reinterpret_cast<CuteDeclarativePolarChartCall0>(taken[0]);
      call(this, &handled);
      if (handled) return;
    }
    DeclarativeChart::componentComplete();
  }

  //  void DeclarativeChart::geometryChange(const QRectF &newGeometry,
  //      const QRectF &oldGeometry)
  void geometryChange(
      const QRectF &newGeometry,
      const QRectF &oldGeometry) override {
    if (taken[1]) {
      int handled = 0;
      CuteDeclarativePolarChartCall1 call = reinterpret_cast<CuteDeclarativePolarChartCall1>(taken[1]);
      call(this, &newGeometry, &oldGeometry, &handled);
      if (handled) return;
    }
    DeclarativeChart::geometryChange(newGeometry, oldGeometry);
  }

  //  QSGNode *DeclarativeChart::updatePaintNode(QSGNode *oldNode,
  //      UpdatePaintNodeData *a1)
  QSGNode *updatePaintNode(
      QSGNode *oldNode,
      QQuickItem::UpdatePaintNodeData *a1) override {
    if (taken[2]) {
      int handled = 0;
      CuteDeclarativePolarChartCall2 call = reinterpret_cast<CuteDeclarativePolarChartCall2>(taken[2]);
      void * given = call(this, oldNode, a1, &handled);
      if (handled) return static_cast<QSGNode *>(given);
    }
    return DeclarativeChart::updatePaintNode(oldNode, a1);
  }

  //  void DeclarativeChart::mousePressEvent(QMouseEvent *event)
  void mousePressEvent(QMouseEvent *event) override {
    if (taken[3]) {
      int handled = 0;
      CuteDeclarativePolarChartCall3 call = reinterpret_cast<CuteDeclarativePolarChartCall3>(taken[3]);
      call(this, event, &handled);
      if (handled) return;
    }
    DeclarativeChart::mousePressEvent(event);
  }

  //  void DeclarativeChart::mouseReleaseEvent(QMouseEvent *event)
  void mouseReleaseEvent(QMouseEvent *event) override {
    if (taken[4]) {
      int handled = 0;
      CuteDeclarativePolarChartCall4 call = reinterpret_cast<CuteDeclarativePolarChartCall4>(taken[4]);
      call(this, event, &handled);
      if (handled) return;
    }
    DeclarativeChart::mouseReleaseEvent(event);
  }

  //  void DeclarativeChart::hoverMoveEvent(QHoverEvent *event)
  void hoverMoveEvent(QHoverEvent *event) override {
    if (taken[5]) {
      int handled = 0;
      CuteDeclarativePolarChartCall5 call = reinterpret_cast<CuteDeclarativePolarChartCall5>(taken[5]);
      call(this, event, &handled);
      if (handled) return;
    }
    DeclarativeChart::hoverMoveEvent(event);
  }

  //  void DeclarativeChart::mouseDoubleClickEvent(QMouseEvent *event)
  void mouseDoubleClickEvent(QMouseEvent *event) override {
    if (taken[6]) {
      int handled = 0;
      CuteDeclarativePolarChartCall6 call = reinterpret_cast<CuteDeclarativePolarChartCall6>(taken[6]);
      call(this, event, &handled);
      if (handled) return;
    }
    DeclarativeChart::mouseDoubleClickEvent(event);
  }

  //  QRectF QQuickItem::boundingRect() const
  QRectF boundingRect() const override {
    if (taken[7]) {
      int handled = 0;
      CuteDeclarativePolarChartCall7 call = reinterpret_cast<CuteDeclarativePolarChartCall7>(taken[7]);
      const QRectF * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QQuickItem::boundingRect();
  }

  //  QRectF QQuickItem::clipRect() const
  QRectF clipRect() const override {
    if (taken[8]) {
      int handled = 0;
      CuteDeclarativePolarChartCall8 call = reinterpret_cast<CuteDeclarativePolarChartCall8>(taken[8]);
      const QRectF * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QQuickItem::clipRect();
  }

  //  bool QQuickItem::contains(const QPointF &point) const
  bool contains(const QPointF &point) const override {
    if (taken[9]) {
      int handled = 0;
      CuteDeclarativePolarChartCall9 call = reinterpret_cast<CuteDeclarativePolarChartCall9>(taken[9]);
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
      CuteDeclarativePolarChartCall10 call = reinterpret_cast<CuteDeclarativePolarChartCall10>(taken[10]);
      const QVariant * given = call(this, static_cast<int>(query), &handled);
      if (handled && given) return *given;
    }
    return QQuickItem::inputMethodQuery(query);
  }
#endif  // QT_CONFIG(im)

  //  bool QQuickItem::isTextureProvider() const
  bool isTextureProvider() const override {
    if (taken[11]) {
      int handled = 0;
      CuteDeclarativePolarChartCall11 call = reinterpret_cast<CuteDeclarativePolarChartCall11>(taken[11]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QQuickItem::isTextureProvider();
  }

  //  QSGTextureProvider *QQuickItem::textureProvider() const
  QSGTextureProvider *textureProvider() const override {
    if (taken[12]) {
      int handled = 0;
      CuteDeclarativePolarChartCall12 call = reinterpret_cast<CuteDeclarativePolarChartCall12>(taken[12]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QSGTextureProvider *>(given);
    }
    return QQuickItem::textureProvider();
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QQuickItem::event(QEvent *a0)
  bool event(QEvent *a0) override {
    if (taken[13]) {
      int handled = 0;
      CuteDeclarativePolarChartCall13 call = reinterpret_cast<CuteDeclarativePolarChartCall13>(taken[13]);
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
    if (taken[14]) {
      int handled = 0;
      CuteDeclarativePolarChartCall14 call = reinterpret_cast<CuteDeclarativePolarChartCall14>(taken[14]);
      call(this, static_cast<int>(a0), &a1, &handled);
      if (handled) return;
    }
    QQuickItem::itemChange(a0, a1);
  }

  //  void QQuickItem::classBegin()
  void classBegin() override {
    if (taken[15]) {
      int handled = 0;
      CuteDeclarativePolarChartCall15 call = reinterpret_cast<CuteDeclarativePolarChartCall15>(taken[15]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItem::classBegin();
  }

  //  void QQuickItem::keyPressEvent(QKeyEvent *event)
  void keyPressEvent(QKeyEvent *event) override {
    if (taken[16]) {
      int handled = 0;
      CuteDeclarativePolarChartCall16 call = reinterpret_cast<CuteDeclarativePolarChartCall16>(taken[16]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::keyPressEvent(event);
  }

  //  void QQuickItem::keyReleaseEvent(QKeyEvent *event)
  void keyReleaseEvent(QKeyEvent *event) override {
    if (taken[17]) {
      int handled = 0;
      CuteDeclarativePolarChartCall17 call = reinterpret_cast<CuteDeclarativePolarChartCall17>(taken[17]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::keyReleaseEvent(event);
  }

#if QT_CONFIG(im)
  //  void QQuickItem::inputMethodEvent(QInputMethodEvent *a0)
  void inputMethodEvent(QInputMethodEvent *a0) override {
    if (taken[18]) {
      int handled = 0;
      CuteDeclarativePolarChartCall18 call = reinterpret_cast<CuteDeclarativePolarChartCall18>(taken[18]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItem::inputMethodEvent(a0);
  }
#endif  // QT_CONFIG(im)

  //  void QQuickItem::focusInEvent(QFocusEvent *a0)
  void focusInEvent(QFocusEvent *a0) override {
    if (taken[19]) {
      int handled = 0;
      CuteDeclarativePolarChartCall19 call = reinterpret_cast<CuteDeclarativePolarChartCall19>(taken[19]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItem::focusInEvent(a0);
  }

  //  void QQuickItem::focusOutEvent(QFocusEvent *a0)
  void focusOutEvent(QFocusEvent *a0) override {
    if (taken[20]) {
      int handled = 0;
      CuteDeclarativePolarChartCall20 call = reinterpret_cast<CuteDeclarativePolarChartCall20>(taken[20]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItem::focusOutEvent(a0);
  }

  //  void QQuickItem::mouseMoveEvent(QMouseEvent *event)
  void mouseMoveEvent(QMouseEvent *event) override {
    if (taken[21]) {
      int handled = 0;
      CuteDeclarativePolarChartCall21 call = reinterpret_cast<CuteDeclarativePolarChartCall21>(taken[21]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::mouseMoveEvent(event);
  }

  //  void QQuickItem::mouseUngrabEvent()
  void mouseUngrabEvent() override {
    if (taken[22]) {
      int handled = 0;
      CuteDeclarativePolarChartCall22 call = reinterpret_cast<CuteDeclarativePolarChartCall22>(taken[22]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItem::mouseUngrabEvent();
  }

  //  void QQuickItem::touchUngrabEvent()
  void touchUngrabEvent() override {
    if (taken[23]) {
      int handled = 0;
      CuteDeclarativePolarChartCall23 call = reinterpret_cast<CuteDeclarativePolarChartCall23>(taken[23]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItem::touchUngrabEvent();
  }

#if QT_CONFIG(wheelevent)
  //  void QQuickItem::wheelEvent(QWheelEvent *event)
  void wheelEvent(QWheelEvent *event) override {
    if (taken[24]) {
      int handled = 0;
      CuteDeclarativePolarChartCall24 call = reinterpret_cast<CuteDeclarativePolarChartCall24>(taken[24]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::wheelEvent(event);
  }
#endif  // QT_CONFIG(wheelevent)

  //  void QQuickItem::touchEvent(QTouchEvent *event)
  void touchEvent(QTouchEvent *event) override {
    if (taken[25]) {
      int handled = 0;
      CuteDeclarativePolarChartCall25 call = reinterpret_cast<CuteDeclarativePolarChartCall25>(taken[25]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::touchEvent(event);
  }

  //  void QQuickItem::hoverEnterEvent(QHoverEvent *event)
  void hoverEnterEvent(QHoverEvent *event) override {
    if (taken[26]) {
      int handled = 0;
      CuteDeclarativePolarChartCall26 call = reinterpret_cast<CuteDeclarativePolarChartCall26>(taken[26]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::hoverEnterEvent(event);
  }

  //  void QQuickItem::hoverLeaveEvent(QHoverEvent *event)
  void hoverLeaveEvent(QHoverEvent *event) override {
    if (taken[27]) {
      int handled = 0;
      CuteDeclarativePolarChartCall27 call = reinterpret_cast<CuteDeclarativePolarChartCall27>(taken[27]);
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
      CuteDeclarativePolarChartCall28 call = reinterpret_cast<CuteDeclarativePolarChartCall28>(taken[28]);
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
      CuteDeclarativePolarChartCall29 call = reinterpret_cast<CuteDeclarativePolarChartCall29>(taken[29]);
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
      CuteDeclarativePolarChartCall30 call = reinterpret_cast<CuteDeclarativePolarChartCall30>(taken[30]);
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
      CuteDeclarativePolarChartCall31 call = reinterpret_cast<CuteDeclarativePolarChartCall31>(taken[31]);
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
      CuteDeclarativePolarChartCall32 call = reinterpret_cast<CuteDeclarativePolarChartCall32>(taken[32]);
      bool given = call(this, a0, a1, &handled);
      if (handled) return given;
    }
    return QQuickItem::childMouseEventFilter(a0, a1);
  }

  //  void QQuickItem::releaseResources()
  void releaseResources() override {
    if (taken[33]) {
      int handled = 0;
      CuteDeclarativePolarChartCall33 call = reinterpret_cast<CuteDeclarativePolarChartCall33>(taken[33]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItem::releaseResources();
  }

  //  void QQuickItem::updatePolish()
  void updatePolish() override {
    if (taken[34]) {
      int handled = 0;
      CuteDeclarativePolarChartCall34 call = reinterpret_cast<CuteDeclarativePolarChartCall34>(taken[34]);
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
      CuteDeclarativePolarChartCall35 call = reinterpret_cast<CuteDeclarativePolarChartCall35>(taken[35]);
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
      CuteDeclarativePolarChartCall36 call = reinterpret_cast<CuteDeclarativePolarChartCall36>(taken[36]);
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
      CuteDeclarativePolarChartCall37 call = reinterpret_cast<CuteDeclarativePolarChartCall37>(taken[37]);
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
      CuteDeclarativePolarChartCall38 call = reinterpret_cast<CuteDeclarativePolarChartCall38>(taken[38]);
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
      CuteDeclarativePolarChartCall39 call = reinterpret_cast<CuteDeclarativePolarChartCall39>(taken[39]);
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
      CuteDeclarativePolarChartCall40 call = reinterpret_cast<CuteDeclarativePolarChartCall40>(taken[40]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *DeclarativePolarChart::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK21DeclarativePolarChart10metaObjectEv(
    const DeclarativePolarChart *self) {
  return self->metaObject();
}

//  void *DeclarativePolarChart::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN21DeclarativePolarChart11qt_metacastEPKc(
    DeclarativePolarChart *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int DeclarativePolarChart::qt_metacall(QMetaObject::Call a0, int a1, void
//      **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN21DeclarativePolarChart11qt_metacallEN11QMetaObject4CallEiPPv(
    DeclarativePolarChart *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString DeclarativePolarChart::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN21DeclarativePolarChart2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(DeclarativePolarChart::tr(s, c, n));
}

//  DeclarativePolarChart::DeclarativePolarChart(QQuickItem *parent)
extern "C" Q_DECL_EXPORT
DeclarativePolarChart *ritual_ZN21DeclarativePolarChartC1EP10QQuickItem(
    QQuickItem *parent) {
  return new CuteDeclarativePolarChart(parent);
}

//  DeclarativePolarChart::~DeclarativePolarChart()
extern "C" Q_DECL_EXPORT
void ritual_ZN21DeclarativePolarChartD1Ev(DeclarativePolarChart *self) {
  delete self;
}

//  a Python function taken by a CuteDeclarativePolarChart, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_DeclarativePolarChart(
    DeclarativePolarChart *self,
    const char *key,
    void *call) {
  return static_cast<CuteDeclarativePolarChart *>(self)->take(key, call);
}
