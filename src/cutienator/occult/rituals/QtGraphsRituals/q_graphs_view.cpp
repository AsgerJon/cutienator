//  Written by dev_tooling.RitualGenerator from the records of
//  QtGraphs/6.12.0/QtGraphs/private/qgraphsview_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtGui/qtguiglobal.h>
#include <QtQuick/qtquickglobal.h>
#include <QtGraphs/qgraphsglobal.h>
#include <QtGraphs/6.12.0/QtGraphs/private/qgraphsglobal_p.h>
#if !(!QT_CONFIG(graphs_2d_area) && !QT_CONFIG(graphs_2d_bar) && !QT_CONFIG(graphs_2d_donut_pie) && !QT_CONFIG(graphs_2d_line) && !QT_CONFIG(graphs_2d_scatter) && !QT_CONFIG(graphs_2d_spline) && !QT_CONFIG(graphs_2d_custom))
#include <QtGraphs/6.12.0/QtGraphs/private/qgraphsglobal_p.h>
#include <QtGraphs/QtGraphs>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGraphs/6.12.0/QtGraphs/private/qgraphsview_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qobject.h>
#include <QtCore/qpoint.h>
#include <QtCore/qrect.h>
#include <QtGui/qcolor.h>
#include <QtGui/qeventpoint.h>
#include <QtCore/qvariant.h>
#include <QtQuick/QtQuick>
#include <QtQuick/qquickitem.h>
#include <QtCore/qmetaobject.h>
#include <QtCore/qlist.h>
#include <cstring>

//  Only a class built on QGraphsView may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQGraphsView : QGraphsView {
  using QGraphsView::componentComplete;
  using QGraphsView::geometryChange;
  using QGraphsView::hoverMoveEvent;
  using QGraphsView::wheelEvent;
  using QGraphsView::updatePaintNode;
  using QGraphsView::updatePolish;
};

//  A QGraphsView that Python can take functions over in. Every QGraphsView
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQGraphsViewCall0)(const void *, int *);
typedef void (*CuteQGraphsViewCall1)(const void *, const QRectF *, const QRectF *, int *);
typedef void (*CuteQGraphsViewCall2)(const void *, QHoverEvent *, int *);
#if QT_CONFIG(wheelevent)
typedef void (*CuteQGraphsViewCall3)(const void *, QWheelEvent *, int *);
#endif  // QT_CONFIG(wheelevent)
typedef void * (*CuteQGraphsViewCall4)(const void *, QSGNode *, QQuickItem::UpdatePaintNodeData *, int *);
typedef void (*CuteQGraphsViewCall5)(const void *, int *);
typedef const QRectF * (*CuteQGraphsViewCall6)(const void *, int *);
typedef const QRectF * (*CuteQGraphsViewCall7)(const void *, int *);
typedef bool (*CuteQGraphsViewCall8)(const void *, const QPointF *, int *);
#if QT_CONFIG(im)
typedef const QVariant * (*CuteQGraphsViewCall9)(const void *, int, int *);
#endif  // QT_CONFIG(im)
typedef bool (*CuteQGraphsViewCall10)(const void *, int *);
typedef void * (*CuteQGraphsViewCall11)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQGraphsViewCall12)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
typedef void (*CuteQGraphsViewCall13)(const void *, int, const QQuickItem::ItemChangeData *, int *);
typedef void (*CuteQGraphsViewCall14)(const void *, int *);
typedef void (*CuteQGraphsViewCall15)(const void *, QKeyEvent *, int *);
typedef void (*CuteQGraphsViewCall16)(const void *, QKeyEvent *, int *);
#if QT_CONFIG(im)
typedef void (*CuteQGraphsViewCall17)(const void *, QInputMethodEvent *, int *);
#endif  // QT_CONFIG(im)
typedef void (*CuteQGraphsViewCall18)(const void *, QFocusEvent *, int *);
typedef void (*CuteQGraphsViewCall19)(const void *, QFocusEvent *, int *);
typedef void (*CuteQGraphsViewCall20)(const void *, QMouseEvent *, int *);
typedef void (*CuteQGraphsViewCall21)(const void *, QMouseEvent *, int *);
typedef void (*CuteQGraphsViewCall22)(const void *, QMouseEvent *, int *);
typedef void (*CuteQGraphsViewCall23)(const void *, QMouseEvent *, int *);
typedef void (*CuteQGraphsViewCall24)(const void *, int *);
typedef void (*CuteQGraphsViewCall25)(const void *, int *);
typedef void (*CuteQGraphsViewCall26)(const void *, QTouchEvent *, int *);
typedef void (*CuteQGraphsViewCall27)(const void *, QHoverEvent *, int *);
typedef void (*CuteQGraphsViewCall28)(const void *, QHoverEvent *, int *);
#if QT_CONFIG(quick_draganddrop)
typedef void (*CuteQGraphsViewCall29)(const void *, QDragEnterEvent *, int *);
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
typedef void (*CuteQGraphsViewCall30)(const void *, QDragMoveEvent *, int *);
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
typedef void (*CuteQGraphsViewCall31)(const void *, QDragLeaveEvent *, int *);
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
typedef void (*CuteQGraphsViewCall32)(const void *, QDropEvent *, int *);
#endif  // QT_CONFIG(quick_draganddrop)
typedef bool (*CuteQGraphsViewCall33)(const void *, QQuickItem *, QEvent *, int *);
typedef void (*CuteQGraphsViewCall34)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQGraphsViewCall35)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQGraphsViewCall36)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQGraphsViewCall37)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQGraphsViewCall38)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQGraphsViewCall39)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQGraphsViewCall40)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQGraphsView : public QGraphsView {
public:
  using QGraphsView::QGraphsView;
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
    if (!std::strcmp(key, "_ZN10QQuickItem14hoverMoveEventEP11QHoverEvent")) {
      taken[2] = call;
      return true;
    }
#if QT_CONFIG(wheelevent)
    if (!std::strcmp(key, "_ZN10QQuickItem10wheelEventEP11QWheelEvent")) {
      taken[3] = call;
      return true;
    }
#endif  // QT_CONFIG(wheelevent)
    if (!std::strcmp(key, "_ZN10QQuickItem15updatePaintNodeEP7QSGNodePNS_19UpdatePaintNodeDataE")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem12updatePolishEv")) {
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
    if (!std::strcmp(key, "_ZNK10QQuickItem17isTextureProviderEv")) {
      taken[10] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK10QQuickItem15textureProviderEv")) {
      taken[11] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[12] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN10QQuickItem10itemChangeENS_10ItemChangeERKNS_14ItemChangeDataE")) {
      taken[13] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQmlParserStatus10classBeginEv")) {
      taken[14] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem13keyPressEventEP9QKeyEvent")) {
      taken[15] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem15keyReleaseEventEP9QKeyEvent")) {
      taken[16] = call;
      return true;
    }
#if QT_CONFIG(im)
    if (!std::strcmp(key, "_ZN10QQuickItem16inputMethodEventEP17QInputMethodEvent")) {
      taken[17] = call;
      return true;
    }
#endif  // QT_CONFIG(im)
    if (!std::strcmp(key, "_ZN10QQuickItem12focusInEventEP11QFocusEvent")) {
      taken[18] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem13focusOutEventEP11QFocusEvent")) {
      taken[19] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem15mousePressEventEP11QMouseEvent")) {
      taken[20] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem14mouseMoveEventEP11QMouseEvent")) {
      taken[21] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem17mouseReleaseEventEP11QMouseEvent")) {
      taken[22] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem21mouseDoubleClickEventEP11QMouseEvent")) {
      taken[23] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem16mouseUngrabEventEv")) {
      taken[24] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem16touchUngrabEventEv")) {
      taken[25] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem10touchEventEP11QTouchEvent")) {
      taken[26] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem15hoverEnterEventEP11QHoverEvent")) {
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
    if (!std::strcmp(key, "_ZN10QQuickItem21childMouseEventFilterEPS_P6QEvent")) {
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

  //  void QGraphsView::componentComplete()
  void componentComplete() override {
    if (taken[0]) {
      int handled = 0;
      CuteQGraphsViewCall0 call = reinterpret_cast<CuteQGraphsViewCall0>(taken[0]);
      call(this, &handled);
      if (handled) return;
    }
    QGraphsView::componentComplete();
  }

  //  void QGraphsView::geometryChange(const QRectF &newGeometry, const
  //      QRectF &oldGeometry)
  void geometryChange(
      const QRectF &newGeometry,
      const QRectF &oldGeometry) override {
    if (taken[1]) {
      int handled = 0;
      CuteQGraphsViewCall1 call = reinterpret_cast<CuteQGraphsViewCall1>(taken[1]);
      call(this, &newGeometry, &oldGeometry, &handled);
      if (handled) return;
    }
    QGraphsView::geometryChange(newGeometry, oldGeometry);
  }

  //  void QGraphsView::hoverMoveEvent(QHoverEvent *event)
  void hoverMoveEvent(QHoverEvent *event) override {
    if (taken[2]) {
      int handled = 0;
      CuteQGraphsViewCall2 call = reinterpret_cast<CuteQGraphsViewCall2>(taken[2]);
      call(this, event, &handled);
      if (handled) return;
    }
    QGraphsView::hoverMoveEvent(event);
  }

#if QT_CONFIG(wheelevent)
  //  void QGraphsView::wheelEvent(QWheelEvent *event)
  void wheelEvent(QWheelEvent *event) override {
    if (taken[3]) {
      int handled = 0;
      CuteQGraphsViewCall3 call = reinterpret_cast<CuteQGraphsViewCall3>(taken[3]);
      call(this, event, &handled);
      if (handled) return;
    }
    QGraphsView::wheelEvent(event);
  }
#endif  // QT_CONFIG(wheelevent)

  //  QSGNode *QGraphsView::updatePaintNode(QSGNode *oldNode,
  //      QQuickItem::UpdatePaintNodeData *updatePaintNodeData)
  QSGNode *updatePaintNode(
      QSGNode *oldNode,
      QQuickItem::UpdatePaintNodeData *updatePaintNodeData) override {
    if (taken[4]) {
      int handled = 0;
      CuteQGraphsViewCall4 call = reinterpret_cast<CuteQGraphsViewCall4>(taken[4]);
      void * given = call(this, oldNode, updatePaintNodeData, &handled);
      if (handled) return static_cast<QSGNode *>(given);
    }
    return QGraphsView::updatePaintNode(oldNode, updatePaintNodeData);
  }

  //  void QGraphsView::updatePolish()
  void updatePolish() override {
    if (taken[5]) {
      int handled = 0;
      CuteQGraphsViewCall5 call = reinterpret_cast<CuteQGraphsViewCall5>(taken[5]);
      call(this, &handled);
      if (handled) return;
    }
    QGraphsView::updatePolish();
  }

  //  QRectF QQuickItem::boundingRect() const
  QRectF boundingRect() const override {
    if (taken[6]) {
      int handled = 0;
      CuteQGraphsViewCall6 call = reinterpret_cast<CuteQGraphsViewCall6>(taken[6]);
      const QRectF * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QQuickItem::boundingRect();
  }

  //  QRectF QQuickItem::clipRect() const
  QRectF clipRect() const override {
    if (taken[7]) {
      int handled = 0;
      CuteQGraphsViewCall7 call = reinterpret_cast<CuteQGraphsViewCall7>(taken[7]);
      const QRectF * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QQuickItem::clipRect();
  }

  //  bool QQuickItem::contains(const QPointF &point) const
  bool contains(const QPointF &point) const override {
    if (taken[8]) {
      int handled = 0;
      CuteQGraphsViewCall8 call = reinterpret_cast<CuteQGraphsViewCall8>(taken[8]);
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
      CuteQGraphsViewCall9 call = reinterpret_cast<CuteQGraphsViewCall9>(taken[9]);
      const QVariant * given = call(this, static_cast<int>(query), &handled);
      if (handled && given) return *given;
    }
    return QQuickItem::inputMethodQuery(query);
  }
#endif  // QT_CONFIG(im)

  //  bool QQuickItem::isTextureProvider() const
  bool isTextureProvider() const override {
    if (taken[10]) {
      int handled = 0;
      CuteQGraphsViewCall10 call = reinterpret_cast<CuteQGraphsViewCall10>(taken[10]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QQuickItem::isTextureProvider();
  }

  //  QSGTextureProvider *QQuickItem::textureProvider() const
  QSGTextureProvider *textureProvider() const override {
    if (taken[11]) {
      int handled = 0;
      CuteQGraphsViewCall11 call = reinterpret_cast<CuteQGraphsViewCall11>(taken[11]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QSGTextureProvider *>(given);
    }
    return QQuickItem::textureProvider();
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QQuickItem::event(QEvent *a0)
  bool event(QEvent *a0) override {
    if (taken[12]) {
      int handled = 0;
      CuteQGraphsViewCall12 call = reinterpret_cast<CuteQGraphsViewCall12>(taken[12]);
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
    if (taken[13]) {
      int handled = 0;
      CuteQGraphsViewCall13 call = reinterpret_cast<CuteQGraphsViewCall13>(taken[13]);
      call(this, static_cast<int>(a0), &a1, &handled);
      if (handled) return;
    }
    QQuickItem::itemChange(a0, a1);
  }

  //  void QQuickItem::classBegin()
  void classBegin() override {
    if (taken[14]) {
      int handled = 0;
      CuteQGraphsViewCall14 call = reinterpret_cast<CuteQGraphsViewCall14>(taken[14]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItem::classBegin();
  }

  //  void QQuickItem::keyPressEvent(QKeyEvent *event)
  void keyPressEvent(QKeyEvent *event) override {
    if (taken[15]) {
      int handled = 0;
      CuteQGraphsViewCall15 call = reinterpret_cast<CuteQGraphsViewCall15>(taken[15]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::keyPressEvent(event);
  }

  //  void QQuickItem::keyReleaseEvent(QKeyEvent *event)
  void keyReleaseEvent(QKeyEvent *event) override {
    if (taken[16]) {
      int handled = 0;
      CuteQGraphsViewCall16 call = reinterpret_cast<CuteQGraphsViewCall16>(taken[16]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::keyReleaseEvent(event);
  }

#if QT_CONFIG(im)
  //  void QQuickItem::inputMethodEvent(QInputMethodEvent *a0)
  void inputMethodEvent(QInputMethodEvent *a0) override {
    if (taken[17]) {
      int handled = 0;
      CuteQGraphsViewCall17 call = reinterpret_cast<CuteQGraphsViewCall17>(taken[17]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItem::inputMethodEvent(a0);
  }
#endif  // QT_CONFIG(im)

  //  void QQuickItem::focusInEvent(QFocusEvent *a0)
  void focusInEvent(QFocusEvent *a0) override {
    if (taken[18]) {
      int handled = 0;
      CuteQGraphsViewCall18 call = reinterpret_cast<CuteQGraphsViewCall18>(taken[18]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItem::focusInEvent(a0);
  }

  //  void QQuickItem::focusOutEvent(QFocusEvent *a0)
  void focusOutEvent(QFocusEvent *a0) override {
    if (taken[19]) {
      int handled = 0;
      CuteQGraphsViewCall19 call = reinterpret_cast<CuteQGraphsViewCall19>(taken[19]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItem::focusOutEvent(a0);
  }

  //  void QQuickItem::mousePressEvent(QMouseEvent *event)
  void mousePressEvent(QMouseEvent *event) override {
    if (taken[20]) {
      int handled = 0;
      CuteQGraphsViewCall20 call = reinterpret_cast<CuteQGraphsViewCall20>(taken[20]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::mousePressEvent(event);
  }

  //  void QQuickItem::mouseMoveEvent(QMouseEvent *event)
  void mouseMoveEvent(QMouseEvent *event) override {
    if (taken[21]) {
      int handled = 0;
      CuteQGraphsViewCall21 call = reinterpret_cast<CuteQGraphsViewCall21>(taken[21]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::mouseMoveEvent(event);
  }

  //  void QQuickItem::mouseReleaseEvent(QMouseEvent *event)
  void mouseReleaseEvent(QMouseEvent *event) override {
    if (taken[22]) {
      int handled = 0;
      CuteQGraphsViewCall22 call = reinterpret_cast<CuteQGraphsViewCall22>(taken[22]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::mouseReleaseEvent(event);
  }

  //  void QQuickItem::mouseDoubleClickEvent(QMouseEvent *event)
  void mouseDoubleClickEvent(QMouseEvent *event) override {
    if (taken[23]) {
      int handled = 0;
      CuteQGraphsViewCall23 call = reinterpret_cast<CuteQGraphsViewCall23>(taken[23]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::mouseDoubleClickEvent(event);
  }

  //  void QQuickItem::mouseUngrabEvent()
  void mouseUngrabEvent() override {
    if (taken[24]) {
      int handled = 0;
      CuteQGraphsViewCall24 call = reinterpret_cast<CuteQGraphsViewCall24>(taken[24]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItem::mouseUngrabEvent();
  }

  //  void QQuickItem::touchUngrabEvent()
  void touchUngrabEvent() override {
    if (taken[25]) {
      int handled = 0;
      CuteQGraphsViewCall25 call = reinterpret_cast<CuteQGraphsViewCall25>(taken[25]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItem::touchUngrabEvent();
  }

  //  void QQuickItem::touchEvent(QTouchEvent *event)
  void touchEvent(QTouchEvent *event) override {
    if (taken[26]) {
      int handled = 0;
      CuteQGraphsViewCall26 call = reinterpret_cast<CuteQGraphsViewCall26>(taken[26]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::touchEvent(event);
  }

  //  void QQuickItem::hoverEnterEvent(QHoverEvent *event)
  void hoverEnterEvent(QHoverEvent *event) override {
    if (taken[27]) {
      int handled = 0;
      CuteQGraphsViewCall27 call = reinterpret_cast<CuteQGraphsViewCall27>(taken[27]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::hoverEnterEvent(event);
  }

  //  void QQuickItem::hoverLeaveEvent(QHoverEvent *event)
  void hoverLeaveEvent(QHoverEvent *event) override {
    if (taken[28]) {
      int handled = 0;
      CuteQGraphsViewCall28 call = reinterpret_cast<CuteQGraphsViewCall28>(taken[28]);
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
      CuteQGraphsViewCall29 call = reinterpret_cast<CuteQGraphsViewCall29>(taken[29]);
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
      CuteQGraphsViewCall30 call = reinterpret_cast<CuteQGraphsViewCall30>(taken[30]);
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
      CuteQGraphsViewCall31 call = reinterpret_cast<CuteQGraphsViewCall31>(taken[31]);
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
      CuteQGraphsViewCall32 call = reinterpret_cast<CuteQGraphsViewCall32>(taken[32]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItem::dropEvent(a0);
  }
#endif  // QT_CONFIG(quick_draganddrop)

  //  bool QQuickItem::childMouseEventFilter(QQuickItem *a0, QEvent *a1)
  bool childMouseEventFilter(QQuickItem *a0, QEvent *a1) override {
    if (taken[33]) {
      int handled = 0;
      CuteQGraphsViewCall33 call = reinterpret_cast<CuteQGraphsViewCall33>(taken[33]);
      bool given = call(this, a0, a1, &handled);
      if (handled) return given;
    }
    return QQuickItem::childMouseEventFilter(a0, a1);
  }

  //  void QQuickItem::releaseResources()
  void releaseResources() override {
    if (taken[34]) {
      int handled = 0;
      CuteQGraphsViewCall34 call = reinterpret_cast<CuteQGraphsViewCall34>(taken[34]);
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
      CuteQGraphsViewCall35 call = reinterpret_cast<CuteQGraphsViewCall35>(taken[35]);
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
      CuteQGraphsViewCall36 call = reinterpret_cast<CuteQGraphsViewCall36>(taken[36]);
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
      CuteQGraphsViewCall37 call = reinterpret_cast<CuteQGraphsViewCall37>(taken[37]);
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
      CuteQGraphsViewCall38 call = reinterpret_cast<CuteQGraphsViewCall38>(taken[38]);
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
      CuteQGraphsViewCall39 call = reinterpret_cast<CuteQGraphsViewCall39>(taken[39]);
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
      CuteQGraphsViewCall40 call = reinterpret_cast<CuteQGraphsViewCall40>(taken[40]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QGraphsView::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK11QGraphsView10metaObjectEv(
    const QGraphsView *self) {
  return self->metaObject();
}

//  QString QGraphsView::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN11QGraphsView2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QGraphsView::tr(s, c, n));
}

//  QGraphsView::QGraphsView(QQuickItem *parent)
extern "C" Q_DECL_EXPORT
QGraphsView *ritual_ZN11QGraphsViewC1EP10QQuickItem(QQuickItem *parent) {
  return new CuteQGraphsView(parent);
}

//  QGraphsView::~QGraphsView()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QGraphsViewD1Ev(QGraphsView *self) {
  delete self;
}

//  void QGraphsView::addSeries(QObject *series)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QGraphsView9addSeriesEP7QObject(
    QGraphsView *self,
    QObject *series) {
  self->addSeries(series);
}

//  void QGraphsView::insertSeries(qsizetype index, QObject *series)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QGraphsView12insertSeriesExP7QObject(
    QGraphsView *self,
    qsizetype index,
    QObject *series) {
  self->insertSeries(index, series);
}

//  void QGraphsView::removeSeries(QObject *series)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QGraphsView12removeSeriesEP7QObject(
    QGraphsView *self,
    QObject *series) {
  self->removeSeries(series);
}

//  void QGraphsView::removeSeries(qsizetype index)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QGraphsView12removeSeriesEx(
    QGraphsView *self,
    qsizetype index) {
  self->removeSeries(index);
}

//  bool QGraphsView::hasSeries(QObject *series)
extern "C" Q_DECL_EXPORT
bool ritual_ZN11QGraphsView9hasSeriesEP7QObject(
    QGraphsView *self,
    QObject *series) {
  return self->hasSeries(series);
}

//  QList<QObject *> QGraphsView::getSeriesList() const
extern "C" Q_DECL_EXPORT
QList<QObject *> *ritual_ZNK11QGraphsView13getSeriesListEv(
    const QGraphsView *self) {
  return new QList<QObject *>(self->getSeriesList());
}

//  QPointF QGraphsView::getDataPointCoordinates(QAbstractSeries *series,
//      qreal x, qreal y)
extern "C" Q_DECL_EXPORT
QPointF *ritual_ZN11QGraphsView23getDataPointCoordinatesEP15QAbstractSeriesdd(
    QGraphsView *self,
    QAbstractSeries *series,
    qreal x,
    qreal y) {
  return new QPointF(self->getDataPointCoordinates(series, x, y));
}

//  QGraphsTheme *QGraphsView::theme() const
extern "C" Q_DECL_EXPORT
QGraphsTheme *ritual_ZNK11QGraphsView5themeEv(const QGraphsView *self) {
  return self->theme();
}

//  void QGraphsView::setTheme(QGraphsTheme *newTheme)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QGraphsView8setThemeEP12QGraphsTheme(
    QGraphsView *self,
    QGraphsTheme *newTheme) {
  self->setTheme(newTheme);
}

//  qreal QGraphsView::marginTop() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK11QGraphsView9marginTopEv(const QGraphsView *self) {
  return self->marginTop();
}

//  void QGraphsView::setMarginTop(qreal newMarginTop)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QGraphsView12setMarginTopEd(
    QGraphsView *self,
    qreal newMarginTop) {
  self->setMarginTop(newMarginTop);
}

//  qreal QGraphsView::marginBottom() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK11QGraphsView12marginBottomEv(const QGraphsView *self) {
  return self->marginBottom();
}

//  void QGraphsView::setMarginBottom(qreal newMarginBottom)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QGraphsView15setMarginBottomEd(
    QGraphsView *self,
    qreal newMarginBottom) {
  self->setMarginBottom(newMarginBottom);
}

//  qreal QGraphsView::marginLeft() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK11QGraphsView10marginLeftEv(const QGraphsView *self) {
  return self->marginLeft();
}

//  void QGraphsView::setMarginLeft(qreal newMarginLeft)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QGraphsView13setMarginLeftEd(
    QGraphsView *self,
    qreal newMarginLeft) {
  self->setMarginLeft(newMarginLeft);
}

//  qreal QGraphsView::marginRight() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK11QGraphsView11marginRightEv(const QGraphsView *self) {
  return self->marginRight();
}

//  void QGraphsView::setMarginRight(qreal newMarginRight)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QGraphsView14setMarginRightEd(
    QGraphsView *self,
    qreal newMarginRight) {
  self->setMarginRight(newMarginRight);
}

//  bool QGraphsView::clipPlotArea() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QGraphsView12clipPlotAreaEv(const QGraphsView *self) {
  return self->clipPlotArea();
}

//  void QGraphsView::setClipPlotArea(bool enabled)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QGraphsView15setClipPlotAreaEb(
    QGraphsView *self,
    bool enabled) {
  self->setClipPlotArea(enabled);
}

//  QRectF QGraphsView::plotArea() const
extern "C" Q_DECL_EXPORT
QRectF *ritual_ZNK11QGraphsView8plotAreaEv(const QGraphsView *self) {
  return new QRectF(self->plotArea());
}

//  void QGraphsView::updatePlotArea()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QGraphsView14updatePlotAreaEv(QGraphsView *self) {
  self->updatePlotArea();
}

//  void QGraphsView::updateAxisAreas()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QGraphsView15updateAxisAreasEv(QGraphsView *self) {
  self->updateAxisAreas();
}

//  void QGraphsView::addAxis(QAbstractAxis *axis)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QGraphsView7addAxisEP13QAbstractAxis(
    QGraphsView *self,
    QAbstractAxis *axis) {
  self->addAxis(axis);
}

//  void QGraphsView::removeAxis(QAbstractAxis *axis, bool
//      removeAllReferences)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QGraphsView10removeAxisEP13QAbstractAxisb(
    QGraphsView *self,
    QAbstractAxis *axis,
    bool removeAllReferences) {
  self->removeAxis(axis, removeAllReferences);
}

//  qsizetype QGraphsView::graphSeriesCount() const
extern "C" Q_DECL_EXPORT
qsizetype ritual_ZNK11QGraphsView16graphSeriesCountEv(
    const QGraphsView *self) {
  return self->graphSeriesCount();
}

//  void QGraphsView::setGraphSeriesCount(qsizetype count)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QGraphsView19setGraphSeriesCountEx(
    QGraphsView *self,
    qsizetype count) {
  self->setGraphSeriesCount(count);
}

#if QT_CONFIG(graphs_2d_bar)
//  void QGraphsView::createBarsRenderer()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QGraphsView18createBarsRendererEv(QGraphsView *self) {
  self->createBarsRenderer();
}
#endif  // QT_CONFIG(graphs_2d_bar)

//  void QGraphsView::createAxisRenderer()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QGraphsView18createAxisRendererEv(QGraphsView *self) {
  self->createAxisRenderer();
}

#if QT_CONFIG(graphs_2d_area) || QT_CONFIG(graphs_2d_line) || \
    QT_CONFIG(graphs_2d_scatter) || QT_CONFIG(graphs_2d_spline)
//  void QGraphsView::createPointRenderer()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QGraphsView19createPointRendererEv(QGraphsView *self) {
  self->createPointRenderer();
}
#endif

#if QT_CONFIG(graphs_2d_donut_pie)
//  void QGraphsView::createPieRenderer()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QGraphsView17createPieRendererEv(QGraphsView *self) {
  self->createPieRenderer();
}
#endif  // QT_CONFIG(graphs_2d_donut_pie)

#if QT_CONFIG(graphs_2d_area)
//  void QGraphsView::createAreaRenderer()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QGraphsView18createAreaRendererEv(QGraphsView *self) {
  self->createAreaRenderer();
}
#endif  // QT_CONFIG(graphs_2d_area)

#if QT_CONFIG(graphs_2d_custom)
//  void QGraphsView::createCustomRenderer()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QGraphsView20createCustomRendererEv(QGraphsView *self) {
  self->createCustomRenderer();
}
#endif  // QT_CONFIG(graphs_2d_custom)

#if QT_CONFIG(graphs_2d_high_performance_backend)
//  void QGraphsView::createCanvasPainter()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QGraphsView19createCanvasPainterEv(QGraphsView *self) {
  self->createCanvasPainter();
}
#endif  // QT_CONFIG(graphs_2d_high_performance_backend)

#if QT_CONFIG(graphs_2d_high_performance_backend)
//  void QGraphsView::removeCanvasPainter()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QGraphsView19removeCanvasPainterEv(QGraphsView *self) {
  self->removeCanvasPainter();
}
#endif  // QT_CONFIG(graphs_2d_high_performance_backend)

//  qreal QGraphsView::axisXSmoothing() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK11QGraphsView14axisXSmoothingEv(const QGraphsView *self) {
  return self->axisXSmoothing();
}

//  void QGraphsView::setAxisXSmoothing(qreal smoothing)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QGraphsView17setAxisXSmoothingEd(
    QGraphsView *self,
    qreal smoothing) {
  self->setAxisXSmoothing(smoothing);
}

//  qreal QGraphsView::axisYSmoothing() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK11QGraphsView14axisYSmoothingEv(const QGraphsView *self) {
  return self->axisYSmoothing();
}

//  void QGraphsView::setAxisYSmoothing(qreal smoothing)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QGraphsView17setAxisYSmoothingEd(
    QGraphsView *self,
    qreal smoothing) {
  self->setAxisYSmoothing(smoothing);
}

//  qreal QGraphsView::gridSmoothing() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK11QGraphsView13gridSmoothingEv(const QGraphsView *self) {
  return self->gridSmoothing();
}

//  void QGraphsView::setGridSmoothing(qreal smoothing)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QGraphsView16setGridSmoothingEd(
    QGraphsView *self,
    qreal smoothing) {
  self->setGridSmoothing(smoothing);
}

//  bool QGraphsView::isShadowVisible() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QGraphsView15isShadowVisibleEv(const QGraphsView *self) {
  return self->isShadowVisible();
}

//  void QGraphsView::setShadowVisible(bool newShadowVisibility)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QGraphsView16setShadowVisibleEb(
    QGraphsView *self,
    bool newShadowVisibility) {
  self->setShadowVisible(newShadowVisibility);
}

//  QColor QGraphsView::shadowColor() const
extern "C" Q_DECL_EXPORT
QColor *ritual_ZNK11QGraphsView11shadowColorEv(const QGraphsView *self) {
  return new QColor(self->shadowColor());
}

//  void QGraphsView::setShadowColor(QColor newShadowColor)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QGraphsView14setShadowColorE6QColor(
    QGraphsView *self,
    const QColor *newShadowColor) {
  self->setShadowColor(*newShadowColor);
}

//  qreal QGraphsView::shadowBarWidth() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK11QGraphsView14shadowBarWidthEv(const QGraphsView *self) {
  return self->shadowBarWidth();
}

//  void QGraphsView::setShadowBarWidth(qreal newShadowBarWidth)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QGraphsView17setShadowBarWidthEd(
    QGraphsView *self,
    qreal newShadowBarWidth) {
  self->setShadowBarWidth(newShadowBarWidth);
}

//  qreal QGraphsView::shadowXOffset() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK11QGraphsView13shadowXOffsetEv(const QGraphsView *self) {
  return self->shadowXOffset();
}

//  void QGraphsView::setShadowXOffset(qreal newShadowXOffset)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QGraphsView16setShadowXOffsetEd(
    QGraphsView *self,
    qreal newShadowXOffset) {
  self->setShadowXOffset(newShadowXOffset);
}

//  qreal QGraphsView::shadowYOffset() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK11QGraphsView13shadowYOffsetEv(const QGraphsView *self) {
  return self->shadowYOffset();
}

//  void QGraphsView::setShadowYOffset(qreal newShadowYOffset)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QGraphsView16setShadowYOffsetEd(
    QGraphsView *self,
    qreal newShadowYOffset) {
  self->setShadowYOffset(newShadowYOffset);
}

//  qreal QGraphsView::shadowSmoothing() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK11QGraphsView15shadowSmoothingEv(const QGraphsView *self) {
  return self->shadowSmoothing();
}

//  void QGraphsView::setShadowSmoothing(qreal smoothing)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QGraphsView18setShadowSmoothingEd(
    QGraphsView *self,
    qreal smoothing) {
  self->setShadowSmoothing(smoothing);
}

//  QAbstractAxis *QGraphsView::axisX() const
extern "C" Q_DECL_EXPORT
QAbstractAxis *ritual_ZNK11QGraphsView5axisXEv(const QGraphsView *self) {
  return self->axisX();
}

//  void QGraphsView::setAxisX(QAbstractAxis *axis)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QGraphsView8setAxisXEP13QAbstractAxis(
    QGraphsView *self,
    QAbstractAxis *axis) {
  self->setAxisX(axis);
}

//  QAbstractAxis *QGraphsView::axisY() const
extern "C" Q_DECL_EXPORT
QAbstractAxis *ritual_ZNK11QGraphsView5axisYEv(const QGraphsView *self) {
  return self->axisY();
}

//  void QGraphsView::setAxisY(QAbstractAxis *axis)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QGraphsView8setAxisYEP13QAbstractAxis(
    QGraphsView *self,
    QAbstractAxis *axis) {
  self->setAxisY(axis);
}

//  Qt::Orientation QGraphsView::orientation() const
extern "C" Q_DECL_EXPORT
Qt::Orientation ritual_ZNK11QGraphsView11orientationEv(
    const QGraphsView *self) {
  return self->orientation();
}

//  void QGraphsView::setOrientation(Qt::Orientation newOrientation)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QGraphsView14setOrientationEN2Qt11OrientationE(
    QGraphsView *self,
    Qt::Orientation newOrientation) {
  self->setOrientation(newOrientation);
}

//  ZoomStyle QGraphsView::zoomStyle() const
extern "C" Q_DECL_EXPORT
QGraphsView::ZoomStyle ritual_ZNK11QGraphsView9zoomStyleEv(
    const QGraphsView *self) {
  return self->zoomStyle();
}

//  void QGraphsView::setZoomStyle(ZoomStyle newZoomStyle)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QGraphsView12setZoomStyleENS_9ZoomStyleE(
    QGraphsView *self,
    QGraphsView::ZoomStyle newZoomStyle) {
  self->setZoomStyle(newZoomStyle);
}

//  PanStyle QGraphsView::panStyle() const
extern "C" Q_DECL_EXPORT
QGraphsView::PanStyle ritual_ZNK11QGraphsView8panStyleEv(
    const QGraphsView *self) {
  return self->panStyle();
}

//  void QGraphsView::setPanStyle(PanStyle newPanStyle)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QGraphsView11setPanStyleENS_8PanStyleE(
    QGraphsView *self,
    QGraphsView::PanStyle newPanStyle) {
  self->setPanStyle(newPanStyle);
}

//  bool QGraphsView::zoomAreaEnabled() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QGraphsView15zoomAreaEnabledEv(const QGraphsView *self) {
  return self->zoomAreaEnabled();
}

//  void QGraphsView::setZoomAreaEnabled(bool newZoomAreaEnabled)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QGraphsView18setZoomAreaEnabledEb(
    QGraphsView *self,
    bool newZoomAreaEnabled) {
  self->setZoomAreaEnabled(newZoomAreaEnabled);
}

//  QQmlComponent *QGraphsView::zoomAreaDelegate() const
extern "C" Q_DECL_EXPORT
QQmlComponent *ritual_ZNK11QGraphsView16zoomAreaDelegateEv(
    const QGraphsView *self) {
  return self->zoomAreaDelegate();
}

//  void QGraphsView::setZoomAreaDelegate(QQmlComponent *newZoomAreaDelegate)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QGraphsView19setZoomAreaDelegateEP13QQmlComponent(
    QGraphsView *self,
    QQmlComponent *newZoomAreaDelegate) {
  self->setZoomAreaDelegate(newZoomAreaDelegate);
}

//  qreal QGraphsView::zoomSensitivity() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK11QGraphsView15zoomSensitivityEv(const QGraphsView *self) {
  return self->zoomSensitivity();
}

//  void QGraphsView::setZoomSensitivity(qreal newZoomSensitivity)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QGraphsView18setZoomSensitivityEd(
    QGraphsView *self,
    qreal newZoomSensitivity) {
  self->setZoomSensitivity(newZoomSensitivity);
}

#if QT_CONFIG(graphs_2d_custom)
//  qreal QGraphsView::mapX(QCustomSeries *series, qreal x)
extern "C" Q_DECL_EXPORT
qreal ritual_ZN11QGraphsView4mapXEP13QCustomSeriesd(
    QGraphsView *self,
    QCustomSeries *series,
    qreal x) {
  return self->mapX(series, x);
}
#endif  // QT_CONFIG(graphs_2d_custom)

#if QT_CONFIG(graphs_2d_custom)
//  qreal QGraphsView::mapY(QCustomSeries *series, qreal y)
extern "C" Q_DECL_EXPORT
qreal ritual_ZN11QGraphsView4mapYEP13QCustomSeriesd(
    QGraphsView *self,
    QCustomSeries *series,
    qreal y) {
  return self->mapY(series, y);
}
#endif  // QT_CONFIG(graphs_2d_custom)

//  CustomRenderer *QGraphsView::customRenderer() const
extern "C" Q_DECL_EXPORT
CustomRenderer *ritual_ZNK11QGraphsView14customRendererEv(
    const QGraphsView *self) {
  return self->customRenderer();
}

//  bool QGraphsView::useCanvasPainter() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QGraphsView16useCanvasPainterEv(const QGraphsView *self) {
  return self->useCanvasPainter();
}

//  void QGraphsView::setUseCanvasPainter(bool newUseCanvasPainter)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QGraphsView19setUseCanvasPainterEb(
    QGraphsView *self,
    bool newUseCanvasPainter) {
  self->setUseCanvasPainter(newUseCanvasPainter);
}

//  bool QGraphsView::dynamicLabelMargins() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QGraphsView19dynamicLabelMarginsEv(
    const QGraphsView *self) {
  return self->dynamicLabelMargins();
}

//  void QGraphsView::setDynamicLabelMargins(bool newDynamicLabelMargins)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QGraphsView22setDynamicLabelMarginsEb(
    QGraphsView *self,
    bool newDynamicLabelMargins) {
  self->setDynamicLabelMargins(newDynamicLabelMargins);
}

//  void QGraphsView::handleHoverEnter(const QString &seriesName, QPointF
//      position, QPointF value)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QGraphsView16handleHoverEnterERK7QString7QPointFS3_(
    QGraphsView *self,
    const QString *seriesName,
    const QPointF *position,
    const QPointF *value) {
  self->handleHoverEnter(*seriesName, *position, *value);
}

//  void QGraphsView::handleHoverExit(const QString &seriesName, QPointF
//      position)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QGraphsView15handleHoverExitERK7QString7QPointF(
    QGraphsView *self,
    const QString *seriesName,
    const QPointF *position) {
  self->handleHoverExit(*seriesName, *position);
}

//  void QGraphsView::handleHover(const QString &seriesName, QPointF
//      position, QPointF value)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QGraphsView11handleHoverERK7QString7QPointFS3_(
    QGraphsView *self,
    const QString *seriesName,
    const QPointF *position,
    const QPointF *value) {
  self->handleHover(*seriesName, *position, *value);
}

//  void QGraphsView::updateComponentSizes()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QGraphsView20updateComponentSizesEv(QGraphsView *self) {
  self->updateComponentSizes();
}

//  void QGraphsView::componentComplete()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QGraphsView17componentCompleteEv(QGraphsView *self) {
  self->componentComplete();
}

//  void QGraphsView::geometryChange(const QRectF &newGeometry, const QRectF
//      &oldGeometry)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QGraphsView14geometryChangeERK6QRectFS2_(
    QGraphsView *self,
    const QRectF *newGeometry,
    const QRectF *oldGeometry) {
  self->geometryChange(*newGeometry, *oldGeometry);
}

//  void QGraphsView::hoverMoveEvent(QHoverEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QGraphsView14hoverMoveEventEP11QHoverEvent(
    QGraphsView *self,
    QHoverEvent *event) {
  self->hoverMoveEvent(event);
}

//  void QGraphsView::wheelEvent(QWheelEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QGraphsView10wheelEventEP11QWheelEvent(
    QGraphsView *self,
    QWheelEvent *event) {
  self->wheelEvent(event);
}

//  QSGNode *QGraphsView::updatePaintNode(QSGNode *oldNode,
//      QQuickItem::UpdatePaintNodeData *updatePaintNodeData)
extern "C" Q_DECL_EXPORT
QSGNode *ritual_ZN11QGraphsView15updatePaintNodeEP7QSGNodePN10QQuickItem19UpdatePaintNodeDataE(
    QGraphsView *self,
    QSGNode *oldNode,
    QQuickItem::UpdatePaintNodeData *updatePaintNodeData) {
  return self->updatePaintNode(oldNode, updatePaintNodeData);
}

//  void QGraphsView::updatePolish()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QGraphsView12updatePolishEv(QGraphsView *self) {
  self->updatePolish();
}

//  void QGraphsView::polishAndUpdate()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QGraphsView15polishAndUpdateEv(QGraphsView *self) {
  self->polishAndUpdate();
}

//  int QGraphsView::getSeriesRendererIndex(QAbstractSeries *series)
extern "C" Q_DECL_EXPORT
int ritual_ZN11QGraphsView22getSeriesRendererIndexEP15QAbstractSeries(
    QGraphsView *self,
    QAbstractSeries *series) {
  return self->getSeriesRendererIndex(series);
}

//  void QGraphsView::onPinchScaleChanged(qreal delta)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QGraphsView19onPinchScaleChangedEd(
    QGraphsView *self,
    qreal delta) {
  self->onPinchScaleChanged(delta);
}

//  void QGraphsView::onPinchGrabChanged(QPointingDevice::GrabTransition
//      transition, QEventPoint point)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QGraphsView18onPinchGrabChangedEN15QPointingDevice14GrabTransitionE11QEventPoint(
    QGraphsView *self,
    QPointingDevice::GrabTransition transition,
    const QEventPoint *point) {
  self->onPinchGrabChanged(transition, *point);
}

//  a Python function taken by a CuteQGraphsView, for the function named by
//      the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QGraphsView(
    QGraphsView *self,
    const char *key,
    void *call) {
  return static_cast<CuteQGraphsView *>(self)->take(key, call);
}

//  void QGraphsView::componentComplete()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN11QGraphsView17componentCompleteEv(QGraphsView *self) {
  static_cast<OwnQGraphsView *>(self)->OwnQGraphsView::componentComplete();
}

//  void QGraphsView::geometryChange(const QRectF &newGeometry, const QRectF
//      &oldGeometry)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN11QGraphsView14geometryChangeERK6QRectFS2_(
    QGraphsView *self,
    const QRectF *newGeometry,
    const QRectF *oldGeometry) {
  static_cast<OwnQGraphsView *>(self)->OwnQGraphsView::geometryChange(
      *newGeometry,
      *oldGeometry);
}

//  void QGraphsView::hoverMoveEvent(QHoverEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN11QGraphsView14hoverMoveEventEP11QHoverEvent(
    QGraphsView *self,
    QHoverEvent *event) {
  static_cast<OwnQGraphsView *>(self)->OwnQGraphsView::hoverMoveEvent(event);
}

//  void QGraphsView::wheelEvent(QWheelEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN11QGraphsView10wheelEventEP11QWheelEvent(
    QGraphsView *self,
    QWheelEvent *event) {
  static_cast<OwnQGraphsView *>(self)->OwnQGraphsView::wheelEvent(event);
}

//  QSGNode *QGraphsView::updatePaintNode(QSGNode *oldNode,
//      QQuickItem::UpdatePaintNodeData *updatePaintNodeData)
extern "C" Q_DECL_EXPORT
QSGNode *ritual_own_ZN11QGraphsView15updatePaintNodeEP7QSGNodePN10QQuickItem19UpdatePaintNodeDataE(
    QGraphsView *self,
    QSGNode *oldNode,
    QQuickItem::UpdatePaintNodeData *updatePaintNodeData) {
  return static_cast<OwnQGraphsView *>(self)->OwnQGraphsView::updatePaintNode(
      oldNode,
      updatePaintNodeData);
}

//  void QGraphsView::updatePolish()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN11QGraphsView12updatePolishEv(QGraphsView *self) {
  static_cast<OwnQGraphsView *>(self)->OwnQGraphsView::updatePolish();
}

#endif  // !(!QT_CONFIG(graphs_2d_area) && !QT_CONFIG(graphs_2d_bar) && !QT_CONFIG(graphs_2d_donut_pie) && !QT_CONFIG(graphs_2d_line) && !QT_CONFIG(graphs_2d_scatter) && !QT_CONFIG(graphs_2d_spline) && !QT_CONFIG(graphs_2d_custom))
