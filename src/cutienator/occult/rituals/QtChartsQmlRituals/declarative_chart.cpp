//  Written by dev_tooling.RitualGenerator from the records of
//  QtChartsQml/6.12.0/QtChartsQml/private/declarativechart_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtGui/qtguiglobal.h>
#include <QtQuick/qtquickglobal.h>
#include <QtChartsQml/6.12.0/QtChartsQml/private/declarativechartglobal_p.h>
#include <QtChartsQml/QtChartsQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtChartsQml/6.12.0/QtChartsQml/private/declarativechart_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qrect.h>
#include <QtCore/qeasingcurve.h>
#include <QtGui/qfont.h>
#include <QtGui/qcolor.h>
#include <QtCore/qlocale.h>
#include <QtCore/qpoint.h>
#include <QtCore/qvariant.h>
#include <QtQuick/QtQuick>
#include <QtQuick/qquickitem.h>
#include <QtCore/qmetaobject.h>
#include <QtCore/qlist.h>
#include <cstring>

//  Only a class built on DeclarativeChart may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnDeclarativeChart : DeclarativeChart {
  using DeclarativeChart::mousePressEvent;
  using DeclarativeChart::mouseReleaseEvent;
  using DeclarativeChart::hoverMoveEvent;
  using DeclarativeChart::mouseDoubleClickEvent;
};

//  A DeclarativeChart that Python can take functions over in. Every DeclarativeChart
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteDeclarativeChartCall0)(const void *, int *);
typedef void (*CuteDeclarativeChartCall1)(const void *, const QRectF *, const QRectF *, int *);
typedef void * (*CuteDeclarativeChartCall2)(const void *, QSGNode *, QQuickItem::UpdatePaintNodeData *, int *);
typedef void (*CuteDeclarativeChartCall3)(const void *, QMouseEvent *, int *);
typedef void (*CuteDeclarativeChartCall4)(const void *, QMouseEvent *, int *);
typedef void (*CuteDeclarativeChartCall5)(const void *, QHoverEvent *, int *);
typedef void (*CuteDeclarativeChartCall6)(const void *, QMouseEvent *, int *);
typedef const QRectF * (*CuteDeclarativeChartCall7)(const void *, int *);
typedef const QRectF * (*CuteDeclarativeChartCall8)(const void *, int *);
typedef bool (*CuteDeclarativeChartCall9)(const void *, const QPointF *, int *);
#if QT_CONFIG(im)
typedef const QVariant * (*CuteDeclarativeChartCall10)(const void *, int, int *);
#endif  // QT_CONFIG(im)
typedef bool (*CuteDeclarativeChartCall11)(const void *, int *);
typedef void * (*CuteDeclarativeChartCall12)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteDeclarativeChartCall13)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
typedef void (*CuteDeclarativeChartCall14)(const void *, int, const QQuickItem::ItemChangeData *, int *);
typedef void (*CuteDeclarativeChartCall15)(const void *, int *);
typedef void (*CuteDeclarativeChartCall16)(const void *, QKeyEvent *, int *);
typedef void (*CuteDeclarativeChartCall17)(const void *, QKeyEvent *, int *);
#if QT_CONFIG(im)
typedef void (*CuteDeclarativeChartCall18)(const void *, QInputMethodEvent *, int *);
#endif  // QT_CONFIG(im)
typedef void (*CuteDeclarativeChartCall19)(const void *, QFocusEvent *, int *);
typedef void (*CuteDeclarativeChartCall20)(const void *, QFocusEvent *, int *);
typedef void (*CuteDeclarativeChartCall21)(const void *, QMouseEvent *, int *);
typedef void (*CuteDeclarativeChartCall22)(const void *, int *);
typedef void (*CuteDeclarativeChartCall23)(const void *, int *);
#if QT_CONFIG(wheelevent)
typedef void (*CuteDeclarativeChartCall24)(const void *, QWheelEvent *, int *);
#endif  // QT_CONFIG(wheelevent)
typedef void (*CuteDeclarativeChartCall25)(const void *, QTouchEvent *, int *);
typedef void (*CuteDeclarativeChartCall26)(const void *, QHoverEvent *, int *);
typedef void (*CuteDeclarativeChartCall27)(const void *, QHoverEvent *, int *);
#if QT_CONFIG(quick_draganddrop)
typedef void (*CuteDeclarativeChartCall28)(const void *, QDragEnterEvent *, int *);
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
typedef void (*CuteDeclarativeChartCall29)(const void *, QDragMoveEvent *, int *);
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
typedef void (*CuteDeclarativeChartCall30)(const void *, QDragLeaveEvent *, int *);
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
typedef void (*CuteDeclarativeChartCall31)(const void *, QDropEvent *, int *);
#endif  // QT_CONFIG(quick_draganddrop)
typedef bool (*CuteDeclarativeChartCall32)(const void *, QQuickItem *, QEvent *, int *);
typedef void (*CuteDeclarativeChartCall33)(const void *, int *);
typedef void (*CuteDeclarativeChartCall34)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteDeclarativeChartCall35)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteDeclarativeChartCall36)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteDeclarativeChartCall37)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteDeclarativeChartCall38)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteDeclarativeChartCall39)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteDeclarativeChartCall40)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteDeclarativeChart : public DeclarativeChart {
public:
  using DeclarativeChart::DeclarativeChart;
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
      CuteDeclarativeChartCall0 call = reinterpret_cast<CuteDeclarativeChartCall0>(taken[0]);
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
      CuteDeclarativeChartCall1 call = reinterpret_cast<CuteDeclarativeChartCall1>(taken[1]);
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
      CuteDeclarativeChartCall2 call = reinterpret_cast<CuteDeclarativeChartCall2>(taken[2]);
      void * given = call(this, oldNode, a1, &handled);
      if (handled) return static_cast<QSGNode *>(given);
    }
    return DeclarativeChart::updatePaintNode(oldNode, a1);
  }

  //  void DeclarativeChart::mousePressEvent(QMouseEvent *event)
  void mousePressEvent(QMouseEvent *event) override {
    if (taken[3]) {
      int handled = 0;
      CuteDeclarativeChartCall3 call = reinterpret_cast<CuteDeclarativeChartCall3>(taken[3]);
      call(this, event, &handled);
      if (handled) return;
    }
    DeclarativeChart::mousePressEvent(event);
  }

  //  void DeclarativeChart::mouseReleaseEvent(QMouseEvent *event)
  void mouseReleaseEvent(QMouseEvent *event) override {
    if (taken[4]) {
      int handled = 0;
      CuteDeclarativeChartCall4 call = reinterpret_cast<CuteDeclarativeChartCall4>(taken[4]);
      call(this, event, &handled);
      if (handled) return;
    }
    DeclarativeChart::mouseReleaseEvent(event);
  }

  //  void DeclarativeChart::hoverMoveEvent(QHoverEvent *event)
  void hoverMoveEvent(QHoverEvent *event) override {
    if (taken[5]) {
      int handled = 0;
      CuteDeclarativeChartCall5 call = reinterpret_cast<CuteDeclarativeChartCall5>(taken[5]);
      call(this, event, &handled);
      if (handled) return;
    }
    DeclarativeChart::hoverMoveEvent(event);
  }

  //  void DeclarativeChart::mouseDoubleClickEvent(QMouseEvent *event)
  void mouseDoubleClickEvent(QMouseEvent *event) override {
    if (taken[6]) {
      int handled = 0;
      CuteDeclarativeChartCall6 call = reinterpret_cast<CuteDeclarativeChartCall6>(taken[6]);
      call(this, event, &handled);
      if (handled) return;
    }
    DeclarativeChart::mouseDoubleClickEvent(event);
  }

  //  QRectF QQuickItem::boundingRect() const
  QRectF boundingRect() const override {
    if (taken[7]) {
      int handled = 0;
      CuteDeclarativeChartCall7 call = reinterpret_cast<CuteDeclarativeChartCall7>(taken[7]);
      const QRectF * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QQuickItem::boundingRect();
  }

  //  QRectF QQuickItem::clipRect() const
  QRectF clipRect() const override {
    if (taken[8]) {
      int handled = 0;
      CuteDeclarativeChartCall8 call = reinterpret_cast<CuteDeclarativeChartCall8>(taken[8]);
      const QRectF * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QQuickItem::clipRect();
  }

  //  bool QQuickItem::contains(const QPointF &point) const
  bool contains(const QPointF &point) const override {
    if (taken[9]) {
      int handled = 0;
      CuteDeclarativeChartCall9 call = reinterpret_cast<CuteDeclarativeChartCall9>(taken[9]);
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
      CuteDeclarativeChartCall10 call = reinterpret_cast<CuteDeclarativeChartCall10>(taken[10]);
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
      CuteDeclarativeChartCall11 call = reinterpret_cast<CuteDeclarativeChartCall11>(taken[11]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QQuickItem::isTextureProvider();
  }

  //  QSGTextureProvider *QQuickItem::textureProvider() const
  QSGTextureProvider *textureProvider() const override {
    if (taken[12]) {
      int handled = 0;
      CuteDeclarativeChartCall12 call = reinterpret_cast<CuteDeclarativeChartCall12>(taken[12]);
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
      CuteDeclarativeChartCall13 call = reinterpret_cast<CuteDeclarativeChartCall13>(taken[13]);
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
      CuteDeclarativeChartCall14 call = reinterpret_cast<CuteDeclarativeChartCall14>(taken[14]);
      call(this, static_cast<int>(a0), &a1, &handled);
      if (handled) return;
    }
    QQuickItem::itemChange(a0, a1);
  }

  //  void QQuickItem::classBegin()
  void classBegin() override {
    if (taken[15]) {
      int handled = 0;
      CuteDeclarativeChartCall15 call = reinterpret_cast<CuteDeclarativeChartCall15>(taken[15]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItem::classBegin();
  }

  //  void QQuickItem::keyPressEvent(QKeyEvent *event)
  void keyPressEvent(QKeyEvent *event) override {
    if (taken[16]) {
      int handled = 0;
      CuteDeclarativeChartCall16 call = reinterpret_cast<CuteDeclarativeChartCall16>(taken[16]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::keyPressEvent(event);
  }

  //  void QQuickItem::keyReleaseEvent(QKeyEvent *event)
  void keyReleaseEvent(QKeyEvent *event) override {
    if (taken[17]) {
      int handled = 0;
      CuteDeclarativeChartCall17 call = reinterpret_cast<CuteDeclarativeChartCall17>(taken[17]);
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
      CuteDeclarativeChartCall18 call = reinterpret_cast<CuteDeclarativeChartCall18>(taken[18]);
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
      CuteDeclarativeChartCall19 call = reinterpret_cast<CuteDeclarativeChartCall19>(taken[19]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItem::focusInEvent(a0);
  }

  //  void QQuickItem::focusOutEvent(QFocusEvent *a0)
  void focusOutEvent(QFocusEvent *a0) override {
    if (taken[20]) {
      int handled = 0;
      CuteDeclarativeChartCall20 call = reinterpret_cast<CuteDeclarativeChartCall20>(taken[20]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItem::focusOutEvent(a0);
  }

  //  void QQuickItem::mouseMoveEvent(QMouseEvent *event)
  void mouseMoveEvent(QMouseEvent *event) override {
    if (taken[21]) {
      int handled = 0;
      CuteDeclarativeChartCall21 call = reinterpret_cast<CuteDeclarativeChartCall21>(taken[21]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::mouseMoveEvent(event);
  }

  //  void QQuickItem::mouseUngrabEvent()
  void mouseUngrabEvent() override {
    if (taken[22]) {
      int handled = 0;
      CuteDeclarativeChartCall22 call = reinterpret_cast<CuteDeclarativeChartCall22>(taken[22]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItem::mouseUngrabEvent();
  }

  //  void QQuickItem::touchUngrabEvent()
  void touchUngrabEvent() override {
    if (taken[23]) {
      int handled = 0;
      CuteDeclarativeChartCall23 call = reinterpret_cast<CuteDeclarativeChartCall23>(taken[23]);
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
      CuteDeclarativeChartCall24 call = reinterpret_cast<CuteDeclarativeChartCall24>(taken[24]);
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
      CuteDeclarativeChartCall25 call = reinterpret_cast<CuteDeclarativeChartCall25>(taken[25]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::touchEvent(event);
  }

  //  void QQuickItem::hoverEnterEvent(QHoverEvent *event)
  void hoverEnterEvent(QHoverEvent *event) override {
    if (taken[26]) {
      int handled = 0;
      CuteDeclarativeChartCall26 call = reinterpret_cast<CuteDeclarativeChartCall26>(taken[26]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::hoverEnterEvent(event);
  }

  //  void QQuickItem::hoverLeaveEvent(QHoverEvent *event)
  void hoverLeaveEvent(QHoverEvent *event) override {
    if (taken[27]) {
      int handled = 0;
      CuteDeclarativeChartCall27 call = reinterpret_cast<CuteDeclarativeChartCall27>(taken[27]);
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
      CuteDeclarativeChartCall28 call = reinterpret_cast<CuteDeclarativeChartCall28>(taken[28]);
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
      CuteDeclarativeChartCall29 call = reinterpret_cast<CuteDeclarativeChartCall29>(taken[29]);
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
      CuteDeclarativeChartCall30 call = reinterpret_cast<CuteDeclarativeChartCall30>(taken[30]);
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
      CuteDeclarativeChartCall31 call = reinterpret_cast<CuteDeclarativeChartCall31>(taken[31]);
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
      CuteDeclarativeChartCall32 call = reinterpret_cast<CuteDeclarativeChartCall32>(taken[32]);
      bool given = call(this, a0, a1, &handled);
      if (handled) return given;
    }
    return QQuickItem::childMouseEventFilter(a0, a1);
  }

  //  void QQuickItem::releaseResources()
  void releaseResources() override {
    if (taken[33]) {
      int handled = 0;
      CuteDeclarativeChartCall33 call = reinterpret_cast<CuteDeclarativeChartCall33>(taken[33]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItem::releaseResources();
  }

  //  void QQuickItem::updatePolish()
  void updatePolish() override {
    if (taken[34]) {
      int handled = 0;
      CuteDeclarativeChartCall34 call = reinterpret_cast<CuteDeclarativeChartCall34>(taken[34]);
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
      CuteDeclarativeChartCall35 call = reinterpret_cast<CuteDeclarativeChartCall35>(taken[35]);
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
      CuteDeclarativeChartCall36 call = reinterpret_cast<CuteDeclarativeChartCall36>(taken[36]);
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
      CuteDeclarativeChartCall37 call = reinterpret_cast<CuteDeclarativeChartCall37>(taken[37]);
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
      CuteDeclarativeChartCall38 call = reinterpret_cast<CuteDeclarativeChartCall38>(taken[38]);
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
      CuteDeclarativeChartCall39 call = reinterpret_cast<CuteDeclarativeChartCall39>(taken[39]);
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
      CuteDeclarativeChartCall40 call = reinterpret_cast<CuteDeclarativeChartCall40>(taken[40]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *DeclarativeChart::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK16DeclarativeChart10metaObjectEv(
    const DeclarativeChart *self) {
  return self->metaObject();
}

//  QString DeclarativeChart::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN16DeclarativeChart2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(DeclarativeChart::tr(s, c, n));
}

//  DeclarativeChart::DeclarativeChart(QQuickItem *parent)
extern "C" Q_DECL_EXPORT
DeclarativeChart *ritual_ZN16DeclarativeChartC1EP10QQuickItem(
    QQuickItem *parent) {
  return new CuteDeclarativeChart(parent);
}

//  DeclarativeChart::~DeclarativeChart()
extern "C" Q_DECL_EXPORT
void ritual_ZN16DeclarativeChartD1Ev(DeclarativeChart *self) {
  delete self;
}

//  void DeclarativeChart::componentComplete()
extern "C" Q_DECL_EXPORT
void ritual_ZN16DeclarativeChart17componentCompleteEv(
    DeclarativeChart *self) {
  self->componentComplete();
}

//  void DeclarativeChart::geometryChange(const QRectF &newGeometry, const
//      QRectF &oldGeometry)
extern "C" Q_DECL_EXPORT
void ritual_ZN16DeclarativeChart14geometryChangeERK6QRectFS2_(
    DeclarativeChart *self,
    const QRectF *newGeometry,
    const QRectF *oldGeometry) {
  self->geometryChange(*newGeometry, *oldGeometry);
}

//  QSGNode *DeclarativeChart::updatePaintNode(QSGNode *oldNode,
//      UpdatePaintNodeData *a1)
extern "C" Q_DECL_EXPORT
QSGNode *ritual_ZN16DeclarativeChart15updatePaintNodeEP7QSGNodePN10QQuickItem19UpdatePaintNodeDataE(
    DeclarativeChart *self,
    QSGNode *oldNode,
    QQuickItem::UpdatePaintNodeData *a1) {
  return self->updatePaintNode(oldNode, a1);
}

//  void DeclarativeChart::mousePressEvent(QMouseEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN16DeclarativeChart15mousePressEventEP11QMouseEvent(
    DeclarativeChart *self,
    QMouseEvent *event) {
  self->mousePressEvent(event);
}

//  void DeclarativeChart::mouseReleaseEvent(QMouseEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN16DeclarativeChart17mouseReleaseEventEP11QMouseEvent(
    DeclarativeChart *self,
    QMouseEvent *event) {
  self->mouseReleaseEvent(event);
}

//  void DeclarativeChart::hoverMoveEvent(QHoverEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN16DeclarativeChart14hoverMoveEventEP11QHoverEvent(
    DeclarativeChart *self,
    QHoverEvent *event) {
  self->hoverMoveEvent(event);
}

//  void DeclarativeChart::mouseDoubleClickEvent(QMouseEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN16DeclarativeChart21mouseDoubleClickEventEP11QMouseEvent(
    DeclarativeChart *self,
    QMouseEvent *event) {
  self->mouseDoubleClickEvent(event);
}

//  void DeclarativeChart::handleAntialiasingChanged(bool enable)
extern "C" Q_DECL_EXPORT
void ritual_ZN16DeclarativeChart25handleAntialiasingChangedEb(
    DeclarativeChart *self,
    bool enable) {
  self->handleAntialiasingChanged(enable);
}

//  void DeclarativeChart::sceneChanged(const QList<QRectF> &region)
extern "C" Q_DECL_EXPORT
void ritual_ZN16DeclarativeChart12sceneChangedERK5QListI6QRectFE(
    DeclarativeChart *self,
    const QList<QRectF> *region) {
  self->sceneChanged(*region);
}

//  void DeclarativeChart::renderScene()
extern "C" Q_DECL_EXPORT
void ritual_ZN16DeclarativeChart11renderSceneEv(DeclarativeChart *self) {
  self->renderScene();
}

//  void DeclarativeChart::setTheme(DeclarativeChart::Theme theme)
extern "C" Q_DECL_EXPORT
void ritual_ZN16DeclarativeChart8setThemeENS_5ThemeE(
    DeclarativeChart *self,
    DeclarativeChart::Theme theme) {
  self->setTheme(theme);
}

//  DeclarativeChart::Theme DeclarativeChart::theme()
extern "C" Q_DECL_EXPORT
DeclarativeChart::Theme ritual_ZN16DeclarativeChart5themeEv(
    DeclarativeChart *self) {
  return self->theme();
}

//  void DeclarativeChart::setAnimationOptions(DeclarativeChart::Animation
//      animations)
extern "C" Q_DECL_EXPORT
void ritual_ZN16DeclarativeChart19setAnimationOptionsENS_9AnimationE(
    DeclarativeChart *self,
    DeclarativeChart::Animation animations) {
  self->setAnimationOptions(animations);
}

//  DeclarativeChart::Animation DeclarativeChart::animationOptions()
extern "C" Q_DECL_EXPORT
DeclarativeChart::Animation ritual_ZN16DeclarativeChart16animationOptionsEv(
    DeclarativeChart *self) {
  return self->animationOptions();
}

//  void DeclarativeChart::setAnimationDuration(int msecs)
extern "C" Q_DECL_EXPORT
void ritual_ZN16DeclarativeChart20setAnimationDurationEi(
    DeclarativeChart *self,
    int msecs) {
  self->setAnimationDuration(msecs);
}

//  int DeclarativeChart::animationDuration() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK16DeclarativeChart17animationDurationEv(
    const DeclarativeChart *self) {
  return self->animationDuration();
}

//  void DeclarativeChart::setAnimationEasingCurve(const QEasingCurve &curve)
extern "C" Q_DECL_EXPORT
void ritual_ZN16DeclarativeChart23setAnimationEasingCurveERK12QEasingCurve(
    DeclarativeChart *self,
    const QEasingCurve *curve) {
  self->setAnimationEasingCurve(*curve);
}

//  QEasingCurve DeclarativeChart::animationEasingCurve() const
extern "C" Q_DECL_EXPORT
QEasingCurve *ritual_ZNK16DeclarativeChart20animationEasingCurveEv(
    const DeclarativeChart *self) {
  return new QEasingCurve(self->animationEasingCurve());
}

//  void DeclarativeChart::setTitle(QString title)
extern "C" Q_DECL_EXPORT
void ritual_ZN16DeclarativeChart8setTitleE7QString(
    DeclarativeChart *self,
    const QString *title) {
  self->setTitle(*title);
}

//  QString DeclarativeChart::title()
extern "C" Q_DECL_EXPORT
QString *ritual_ZN16DeclarativeChart5titleEv(DeclarativeChart *self) {
  return new QString(self->title());
}

//  QLegend *DeclarativeChart::legend()
extern "C" Q_DECL_EXPORT
QLegend *ritual_ZN16DeclarativeChart6legendEv(DeclarativeChart *self) {
  return self->legend();
}

//  QFont DeclarativeChart::titleFont() const
extern "C" Q_DECL_EXPORT
QFont *ritual_ZNK16DeclarativeChart9titleFontEv(
    const DeclarativeChart *self) {
  return new QFont(self->titleFont());
}

//  void DeclarativeChart::setTitleFont(const QFont &font)
extern "C" Q_DECL_EXPORT
void ritual_ZN16DeclarativeChart12setTitleFontERK5QFont(
    DeclarativeChart *self,
    const QFont *font) {
  self->setTitleFont(*font);
}

//  void DeclarativeChart::setTitleColor(QColor color)
extern "C" Q_DECL_EXPORT
void ritual_ZN16DeclarativeChart13setTitleColorE6QColor(
    DeclarativeChart *self,
    const QColor *color) {
  self->setTitleColor(*color);
}

//  QColor DeclarativeChart::titleColor()
extern "C" Q_DECL_EXPORT
QColor *ritual_ZN16DeclarativeChart10titleColorEv(DeclarativeChart *self) {
  return new QColor(self->titleColor());
}

//  void DeclarativeChart::setBackgroundColor(QColor color)
extern "C" Q_DECL_EXPORT
void ritual_ZN16DeclarativeChart18setBackgroundColorE6QColor(
    DeclarativeChart *self,
    const QColor *color) {
  self->setBackgroundColor(*color);
}

//  QColor DeclarativeChart::backgroundColor()
extern "C" Q_DECL_EXPORT
QColor *ritual_ZN16DeclarativeChart15backgroundColorEv(
    DeclarativeChart *self) {
  return new QColor(self->backgroundColor());
}

//  void DeclarativeChart::setPlotAreaColor(QColor color)
extern "C" Q_DECL_EXPORT
void ritual_ZN16DeclarativeChart16setPlotAreaColorE6QColor(
    DeclarativeChart *self,
    const QColor *color) {
  self->setPlotAreaColor(*color);
}

//  QColor DeclarativeChart::plotAreaColor()
extern "C" Q_DECL_EXPORT
QColor *ritual_ZN16DeclarativeChart13plotAreaColorEv(
    DeclarativeChart *self) {
  return new QColor(self->plotAreaColor());
}

//  void DeclarativeChart::setLocalizeNumbers(bool localize)
extern "C" Q_DECL_EXPORT
void ritual_ZN16DeclarativeChart18setLocalizeNumbersEb(
    DeclarativeChart *self,
    bool localize) {
  self->setLocalizeNumbers(localize);
}

//  bool DeclarativeChart::localizeNumbers() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK16DeclarativeChart15localizeNumbersEv(
    const DeclarativeChart *self) {
  return self->localizeNumbers();
}

//  void DeclarativeChart::setLocale(const QLocale &locale)
extern "C" Q_DECL_EXPORT
void ritual_ZN16DeclarativeChart9setLocaleERK7QLocale(
    DeclarativeChart *self,
    const QLocale *locale) {
  self->setLocale(*locale);
}

//  QLocale DeclarativeChart::locale() const
extern "C" Q_DECL_EXPORT
QLocale *ritual_ZNK16DeclarativeChart6localeEv(
    const DeclarativeChart *self) {
  return new QLocale(self->locale());
}

//  int DeclarativeChart::count()
extern "C" Q_DECL_EXPORT
int ritual_ZN16DeclarativeChart5countEv(DeclarativeChart *self) {
  return self->count();
}

//  void DeclarativeChart::setDropShadowEnabled(bool enabled)
extern "C" Q_DECL_EXPORT
void ritual_ZN16DeclarativeChart20setDropShadowEnabledEb(
    DeclarativeChart *self,
    bool enabled) {
  self->setDropShadowEnabled(enabled);
}

//  bool DeclarativeChart::dropShadowEnabled()
extern "C" Q_DECL_EXPORT
bool ritual_ZN16DeclarativeChart17dropShadowEnabledEv(
    DeclarativeChart *self) {
  return self->dropShadowEnabled();
}

//  qreal DeclarativeChart::backgroundRoundness() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK16DeclarativeChart19backgroundRoundnessEv(
    const DeclarativeChart *self) {
  return self->backgroundRoundness();
}

//  void DeclarativeChart::setBackgroundRoundness(qreal diameter)
extern "C" Q_DECL_EXPORT
void ritual_ZN16DeclarativeChart22setBackgroundRoundnessEd(
    DeclarativeChart *self,
    qreal diameter) {
  self->setBackgroundRoundness(diameter);
}

//  DeclarativeMargins *DeclarativeChart::margins()
extern "C" Q_DECL_EXPORT
DeclarativeMargins *ritual_ZN16DeclarativeChart7marginsEv(
    DeclarativeChart *self) {
  return self->margins();
}

//  QRectF DeclarativeChart::plotArea()
extern "C" Q_DECL_EXPORT
QRectF *ritual_ZN16DeclarativeChart8plotAreaEv(DeclarativeChart *self) {
  return new QRectF(self->plotArea());
}

//  void DeclarativeChart::setPlotArea(const QRectF &rect)
extern "C" Q_DECL_EXPORT
void ritual_ZN16DeclarativeChart11setPlotAreaERK6QRectF(
    DeclarativeChart *self,
    const QRectF *rect) {
  self->setPlotArea(*rect);
}

//  QAbstractAxis *DeclarativeChart::defaultAxis(Qt::Orientation orientation,
//      QAbstractSeries *series)
extern "C" Q_DECL_EXPORT
QAbstractAxis *ritual_ZN16DeclarativeChart11defaultAxisEN2Qt11OrientationEP15QAbstractSeries(
    DeclarativeChart *self,
    Qt::Orientation orientation,
    QAbstractSeries *series) {
  return self->defaultAxis(orientation, series);
}

//  void DeclarativeChart::initializeAxes(QAbstractSeries *series)
extern "C" Q_DECL_EXPORT
void ritual_ZN16DeclarativeChart14initializeAxesEP15QAbstractSeries(
    DeclarativeChart *self,
    QAbstractSeries *series) {
  self->initializeAxes(series);
}

//  void DeclarativeChart::doInitializeAxes(QAbstractSeries *series,
//      DeclarativeAxes *axes)
extern "C" Q_DECL_EXPORT
void ritual_ZN16DeclarativeChart16doInitializeAxesEP15QAbstractSeriesP15DeclarativeAxes(
    DeclarativeChart *self,
    QAbstractSeries *series,
    DeclarativeAxes *axes) {
  self->doInitializeAxes(series, axes);
}

//  QAbstractSeries *DeclarativeChart::series(int index)
extern "C" Q_DECL_EXPORT
QAbstractSeries *ritual_ZN16DeclarativeChart6seriesEi(
    DeclarativeChart *self,
    int index) {
  return self->series(index);
}

//  QAbstractSeries *DeclarativeChart::series(QString seriesName)
extern "C" Q_DECL_EXPORT
QAbstractSeries *ritual_ZN16DeclarativeChart6seriesE7QString(
    DeclarativeChart *self,
    const QString *seriesName) {
  return self->series(*seriesName);
}

//  QAbstractSeries *DeclarativeChart::createSeries(int type, QString name,
//      QAbstractAxis *axisX, QAbstractAxis *axisY)
extern "C" Q_DECL_EXPORT
QAbstractSeries *ritual_ZN16DeclarativeChart12createSeriesEi7QStringP13QAbstractAxisS2_(
    DeclarativeChart *self,
    int type,
    const QString *name,
    QAbstractAxis *axisX,
    QAbstractAxis *axisY) {
  return self->createSeries(type, *name, axisX, axisY);
}

//  void DeclarativeChart::removeSeries(QAbstractSeries *series)
extern "C" Q_DECL_EXPORT
void ritual_ZN16DeclarativeChart12removeSeriesEP15QAbstractSeries(
    DeclarativeChart *self,
    QAbstractSeries *series) {
  self->removeSeries(series);
}

//  void DeclarativeChart::removeAllSeries()
extern "C" Q_DECL_EXPORT
void ritual_ZN16DeclarativeChart15removeAllSeriesEv(DeclarativeChart *self) {
  self->removeAllSeries();
}

//  void DeclarativeChart::setAxisX(QAbstractAxis *axis, QAbstractSeries
//      *series)
extern "C" Q_DECL_EXPORT
void ritual_ZN16DeclarativeChart8setAxisXEP13QAbstractAxisP15QAbstractSeries(
    DeclarativeChart *self,
    QAbstractAxis *axis,
    QAbstractSeries *series) {
  self->setAxisX(axis, series);
}

//  void DeclarativeChart::setAxisY(QAbstractAxis *axis, QAbstractSeries
//      *series)
extern "C" Q_DECL_EXPORT
void ritual_ZN16DeclarativeChart8setAxisYEP13QAbstractAxisP15QAbstractSeries(
    DeclarativeChart *self,
    QAbstractAxis *axis,
    QAbstractSeries *series) {
  self->setAxisY(axis, series);
}

//  QAbstractAxis *DeclarativeChart::axisX(QAbstractSeries *series)
extern "C" Q_DECL_EXPORT
QAbstractAxis *ritual_ZN16DeclarativeChart5axisXEP15QAbstractSeries(
    DeclarativeChart *self,
    QAbstractSeries *series) {
  return self->axisX(series);
}

//  QAbstractAxis *DeclarativeChart::axisY(QAbstractSeries *series)
extern "C" Q_DECL_EXPORT
QAbstractAxis *ritual_ZN16DeclarativeChart5axisYEP15QAbstractSeries(
    DeclarativeChart *self,
    QAbstractSeries *series) {
  return self->axisY(series);
}

//  void DeclarativeChart::zoom(qreal factor)
extern "C" Q_DECL_EXPORT
void ritual_ZN16DeclarativeChart4zoomEd(
    DeclarativeChart *self,
    qreal factor) {
  self->zoom(factor);
}

//  void DeclarativeChart::zoomIn()
extern "C" Q_DECL_EXPORT
void ritual_ZN16DeclarativeChart6zoomInEv(DeclarativeChart *self) {
  self->zoomIn();
}

//  void DeclarativeChart::zoomIn(const QRectF &rectangle)
extern "C" Q_DECL_EXPORT
void ritual_ZN16DeclarativeChart6zoomInERK6QRectF(
    DeclarativeChart *self,
    const QRectF *rectangle) {
  self->zoomIn(*rectangle);
}

//  void DeclarativeChart::zoomOut()
extern "C" Q_DECL_EXPORT
void ritual_ZN16DeclarativeChart7zoomOutEv(DeclarativeChart *self) {
  self->zoomOut();
}

//  void DeclarativeChart::zoomReset()
extern "C" Q_DECL_EXPORT
void ritual_ZN16DeclarativeChart9zoomResetEv(DeclarativeChart *self) {
  self->zoomReset();
}

//  bool DeclarativeChart::isZoomed()
extern "C" Q_DECL_EXPORT
bool ritual_ZN16DeclarativeChart8isZoomedEv(DeclarativeChart *self) {
  return self->isZoomed();
}

//  void DeclarativeChart::scrollLeft(qreal pixels)
extern "C" Q_DECL_EXPORT
void ritual_ZN16DeclarativeChart10scrollLeftEd(
    DeclarativeChart *self,
    qreal pixels) {
  self->scrollLeft(pixels);
}

//  void DeclarativeChart::scrollRight(qreal pixels)
extern "C" Q_DECL_EXPORT
void ritual_ZN16DeclarativeChart11scrollRightEd(
    DeclarativeChart *self,
    qreal pixels) {
  self->scrollRight(pixels);
}

//  void DeclarativeChart::scrollUp(qreal pixels)
extern "C" Q_DECL_EXPORT
void ritual_ZN16DeclarativeChart8scrollUpEd(
    DeclarativeChart *self,
    qreal pixels) {
  self->scrollUp(pixels);
}

//  void DeclarativeChart::scrollDown(qreal pixels)
extern "C" Q_DECL_EXPORT
void ritual_ZN16DeclarativeChart10scrollDownEd(
    DeclarativeChart *self,
    qreal pixels) {
  self->scrollDown(pixels);
}

//  QPointF DeclarativeChart::mapToValue(const QPointF &position,
//      QAbstractSeries *series)
extern "C" Q_DECL_EXPORT
QPointF *ritual_ZN16DeclarativeChart10mapToValueERK7QPointFP15QAbstractSeries(
    DeclarativeChart *self,
    const QPointF *position,
    QAbstractSeries *series) {
  return new QPointF(self->mapToValue(*position, series));
}

//  QPointF DeclarativeChart::mapToPosition(const QPointF &value,
//      QAbstractSeries *series)
extern "C" Q_DECL_EXPORT
QPointF *ritual_ZN16DeclarativeChart13mapToPositionERK7QPointFP15QAbstractSeries(
    DeclarativeChart *self,
    const QPointF *value,
    QAbstractSeries *series) {
  return new QPointF(self->mapToPosition(*value, series));
}

//  void DeclarativeChart::changeMargins(int top, int bottom, int left, int
//      right)
extern "C" Q_DECL_EXPORT
void ritual_ZN16DeclarativeChart13changeMarginsEiiii(
    DeclarativeChart *self,
    int top,
    int bottom,
    int left,
    int right) {
  self->changeMargins(top, bottom, left, right);
}

//  void DeclarativeChart::handleAxisXSet(QAbstractAxis *axis)
extern "C" Q_DECL_EXPORT
void ritual_ZN16DeclarativeChart14handleAxisXSetEP13QAbstractAxis(
    DeclarativeChart *self,
    QAbstractAxis *axis) {
  self->handleAxisXSet(axis);
}

//  void DeclarativeChart::handleAxisYSet(QAbstractAxis *axis)
extern "C" Q_DECL_EXPORT
void ritual_ZN16DeclarativeChart14handleAxisYSetEP13QAbstractAxis(
    DeclarativeChart *self,
    QAbstractAxis *axis) {
  self->handleAxisYSet(axis);
}

//  void DeclarativeChart::handleAxisXTopSet(QAbstractAxis *axis)
extern "C" Q_DECL_EXPORT
void ritual_ZN16DeclarativeChart17handleAxisXTopSetEP13QAbstractAxis(
    DeclarativeChart *self,
    QAbstractAxis *axis) {
  self->handleAxisXTopSet(axis);
}

//  void DeclarativeChart::handleAxisYRightSet(QAbstractAxis *axis)
extern "C" Q_DECL_EXPORT
void ritual_ZN16DeclarativeChart19handleAxisYRightSetEP13QAbstractAxis(
    DeclarativeChart *self,
    QAbstractAxis *axis) {
  self->handleAxisYRightSet(axis);
}

//  void DeclarativeChart::handleSeriesAdded(QAbstractSeries *series)
extern "C" Q_DECL_EXPORT
void ritual_ZN16DeclarativeChart17handleSeriesAddedEP15QAbstractSeries(
    DeclarativeChart *self,
    QAbstractSeries *series) {
  self->handleSeriesAdded(series);
}

//  void DeclarativeChart::handlePendingRenderNodeMouseEventResponses()
extern "C" Q_DECL_EXPORT
void ritual_ZN16DeclarativeChart42handlePendingRenderNodeMouseEventResponsesEv(
    DeclarativeChart *self) {
  self->handlePendingRenderNodeMouseEventResponses();
}

//  DeclarativeChart::DeclarativeChart(QChart::ChartType type, QQuickItem
//      *parent)
extern "C" Q_DECL_EXPORT
DeclarativeChart *ritual_ZN16DeclarativeChartC1EN6QChart9ChartTypeEP10QQuickItem(
    QChart::ChartType type,
    QQuickItem *parent) {
  return new CuteDeclarativeChart(type, parent);
}

//  void DeclarativeChart::initChart(QChart::ChartType type)
extern "C" Q_DECL_EXPORT
void ritual_ZN16DeclarativeChart9initChartEN6QChart9ChartTypeE(
    DeclarativeChart *self,
    QChart::ChartType type) {
  self->initChart(type);
}

//  void DeclarativeChart::seriesAxisAttachHelper(QAbstractSeries *series,
//      QAbstractAxis *axis, Qt::Orientations orientation, Qt::Alignment
//      alignment)
extern "C" Q_DECL_EXPORT
void ritual_ZN16DeclarativeChart22seriesAxisAttachHelperEP15QAbstractSeriesP13QAbstractAxis6QFlagsIN2Qt11OrientationEES4_INS5_13AlignmentFlagEE(
    DeclarativeChart *self,
    QAbstractSeries *series,
    QAbstractAxis *axis,
    int orientation,
    int alignment) {
  self->seriesAxisAttachHelper(
      series,
      axis,
      QFlags<Qt::Orientation>::fromInt(orientation),
      QFlags<Qt::AlignmentFlag>::fromInt(alignment));
}

//  void DeclarativeChart::findMinMaxForSeries(QAbstractSeries *series,
//      Qt::Orientations orientation, qreal &min, qreal &max)
extern "C" Q_DECL_EXPORT
void ritual_ZN16DeclarativeChart19findMinMaxForSeriesEP15QAbstractSeries6QFlagsIN2Qt11OrientationEERdS6_(
    DeclarativeChart *self,
    QAbstractSeries *series,
    int orientation,
    qreal *min,
    qreal *max) {
  self->findMinMaxForSeries(
      series,
      QFlags<Qt::Orientation>::fromInt(orientation),
      *min,
      *max);
}

//  void DeclarativeChart::queueRendererMouseEvent(QMouseEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN16DeclarativeChart23queueRendererMouseEventEP11QMouseEvent(
    DeclarativeChart *self,
    QMouseEvent *event) {
  self->queueRendererMouseEvent(event);
}

//  a Python function taken by a CuteDeclarativeChart, for the function named
//      by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_DeclarativeChart(
    DeclarativeChart *self,
    const char *key,
    void *call) {
  return static_cast<CuteDeclarativeChart *>(self)->take(key, call);
}

//  void DeclarativeChart::componentComplete()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN16DeclarativeChart17componentCompleteEv(
    DeclarativeChart *self) {
  self->DeclarativeChart::componentComplete();
}

//  void DeclarativeChart::geometryChange(const QRectF &newGeometry, const
//      QRectF &oldGeometry)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN16DeclarativeChart14geometryChangeERK6QRectFS2_(
    DeclarativeChart *self,
    const QRectF *newGeometry,
    const QRectF *oldGeometry) {
  self->DeclarativeChart::geometryChange(*newGeometry, *oldGeometry);
}

//  QSGNode *DeclarativeChart::updatePaintNode(QSGNode *oldNode,
//      UpdatePaintNodeData *a1)
extern "C" Q_DECL_EXPORT
QSGNode *ritual_own_ZN16DeclarativeChart15updatePaintNodeEP7QSGNodePN10QQuickItem19UpdatePaintNodeDataE(
    DeclarativeChart *self,
    QSGNode *oldNode,
    QQuickItem::UpdatePaintNodeData *a1) {
  return self->DeclarativeChart::updatePaintNode(oldNode, a1);
}

//  void DeclarativeChart::mousePressEvent(QMouseEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN16DeclarativeChart15mousePressEventEP11QMouseEvent(
    DeclarativeChart *self,
    QMouseEvent *event) {
  static_cast<OwnDeclarativeChart *>(self)->OwnDeclarativeChart::mousePressEvent(
      event);
}

//  void DeclarativeChart::mouseReleaseEvent(QMouseEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN16DeclarativeChart17mouseReleaseEventEP11QMouseEvent(
    DeclarativeChart *self,
    QMouseEvent *event) {
  static_cast<OwnDeclarativeChart *>(self)->OwnDeclarativeChart::mouseReleaseEvent(
      event);
}

//  void DeclarativeChart::hoverMoveEvent(QHoverEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN16DeclarativeChart14hoverMoveEventEP11QHoverEvent(
    DeclarativeChart *self,
    QHoverEvent *event) {
  static_cast<OwnDeclarativeChart *>(self)->OwnDeclarativeChart::hoverMoveEvent(
      event);
}

//  void DeclarativeChart::mouseDoubleClickEvent(QMouseEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN16DeclarativeChart21mouseDoubleClickEventEP11QMouseEvent(
    DeclarativeChart *self,
    QMouseEvent *event) {
  static_cast<OwnDeclarativeChart *>(self)->OwnDeclarativeChart::mouseDoubleClickEvent(
      event);
}
