//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/6.12.0/QtQuick/private/qquickpathview_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtGui/qtguiglobal.h>
#include <QtQuick/qtquickglobal.h>
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#if QT_CONFIG(quick_pathview)
#if QT_CONFIG(quick_pathview)
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qquickpathview_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qvariant.h>
#include <QtQmlModels/QtQmlModels>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQmlModels/6.12.0/QtQmlModels/private/qqmlchangeset_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qrect.h>
#include <QtCore/qpoint.h>
#include <QtQuick/qquickitem.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  Only a class built on QQuickPathView may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQQuickPathView : QQuickPathView {
  using QQuickPathView::updatePolish;
  using QQuickPathView::mousePressEvent;
  using QQuickPathView::mouseMoveEvent;
  using QQuickPathView::mouseReleaseEvent;
  using QQuickPathView::childMouseEventFilter;
  using QQuickPathView::mouseUngrabEvent;
  using QQuickPathView::componentComplete;
};

//  A QQuickPathView that Python can take functions over in. Every QQuickPathView
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if QT_CONFIG(quick_pathview)
typedef void (*CuteQQuickPathViewCall0)(const void *, int *);
#endif  // QT_CONFIG(quick_pathview)
#if QT_CONFIG(quick_pathview)
typedef void (*CuteQQuickPathViewCall1)(const void *, QMouseEvent *, int *);
#endif  // QT_CONFIG(quick_pathview)
#if QT_CONFIG(quick_pathview)
typedef void (*CuteQQuickPathViewCall2)(const void *, QMouseEvent *, int *);
#endif  // QT_CONFIG(quick_pathview)
#if QT_CONFIG(quick_pathview)
typedef void (*CuteQQuickPathViewCall3)(const void *, QMouseEvent *, int *);
#endif  // QT_CONFIG(quick_pathview)
#if QT_CONFIG(quick_pathview)
typedef bool (*CuteQQuickPathViewCall4)(const void *, QQuickItem *, QEvent *, int *);
#endif  // QT_CONFIG(quick_pathview)
#if QT_CONFIG(quick_pathview)
typedef void (*CuteQQuickPathViewCall5)(const void *, int *);
#endif  // QT_CONFIG(quick_pathview)
#if QT_CONFIG(quick_pathview)
typedef void (*CuteQQuickPathViewCall6)(const void *, int *);
#endif  // QT_CONFIG(quick_pathview)
typedef const QRectF * (*CuteQQuickPathViewCall7)(const void *, int *);
typedef const QRectF * (*CuteQQuickPathViewCall8)(const void *, int *);
typedef bool (*CuteQQuickPathViewCall9)(const void *, const QPointF *, int *);
#if QT_CONFIG(im)
typedef const QVariant * (*CuteQQuickPathViewCall10)(const void *, int, int *);
#endif  // QT_CONFIG(im)
typedef bool (*CuteQQuickPathViewCall11)(const void *, int *);
typedef void * (*CuteQQuickPathViewCall12)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickPathViewCall13)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickPathViewCall14)(const void *, int, const QQuickItem::ItemChangeData *, int *);
typedef void (*CuteQQuickPathViewCall15)(const void *, const QRectF *, const QRectF *, int *);
typedef void (*CuteQQuickPathViewCall16)(const void *, int *);
typedef void (*CuteQQuickPathViewCall17)(const void *, QKeyEvent *, int *);
typedef void (*CuteQQuickPathViewCall18)(const void *, QKeyEvent *, int *);
#if QT_CONFIG(im)
typedef void (*CuteQQuickPathViewCall19)(const void *, QInputMethodEvent *, int *);
#endif  // QT_CONFIG(im)
typedef void (*CuteQQuickPathViewCall20)(const void *, QFocusEvent *, int *);
typedef void (*CuteQQuickPathViewCall21)(const void *, QFocusEvent *, int *);
typedef void (*CuteQQuickPathViewCall22)(const void *, QMouseEvent *, int *);
typedef void (*CuteQQuickPathViewCall23)(const void *, int *);
#if QT_CONFIG(wheelevent)
typedef void (*CuteQQuickPathViewCall24)(const void *, QWheelEvent *, int *);
#endif  // QT_CONFIG(wheelevent)
typedef void (*CuteQQuickPathViewCall25)(const void *, QTouchEvent *, int *);
typedef void (*CuteQQuickPathViewCall26)(const void *, QHoverEvent *, int *);
typedef void (*CuteQQuickPathViewCall27)(const void *, QHoverEvent *, int *);
typedef void (*CuteQQuickPathViewCall28)(const void *, QHoverEvent *, int *);
#if QT_CONFIG(quick_draganddrop)
typedef void (*CuteQQuickPathViewCall29)(const void *, QDragEnterEvent *, int *);
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
typedef void (*CuteQQuickPathViewCall30)(const void *, QDragMoveEvent *, int *);
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
typedef void (*CuteQQuickPathViewCall31)(const void *, QDragLeaveEvent *, int *);
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
typedef void (*CuteQQuickPathViewCall32)(const void *, QDropEvent *, int *);
#endif  // QT_CONFIG(quick_draganddrop)
typedef void * (*CuteQQuickPathViewCall33)(const void *, QSGNode *, QQuickItem::UpdatePaintNodeData *, int *);
typedef void (*CuteQQuickPathViewCall34)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickPathViewCall35)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickPathViewCall36)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickPathViewCall37)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickPathViewCall38)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickPathViewCall39)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickPathViewCall40)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQQuickPathView : public QQuickPathView {
public:
  using QQuickPathView::QQuickPathView;
  void *taken[41] = {};

  bool take(const char *key, void *call) {
#if QT_CONFIG(quick_pathview)
    if (!std::strcmp(key, "_ZN10QQuickItem12updatePolishEv")) {
      taken[0] = call;
      return true;
    }
#endif  // QT_CONFIG(quick_pathview)
#if QT_CONFIG(quick_pathview)
    if (!std::strcmp(key, "_ZN10QQuickItem15mousePressEventEP11QMouseEvent")) {
      taken[1] = call;
      return true;
    }
#endif  // QT_CONFIG(quick_pathview)
#if QT_CONFIG(quick_pathview)
    if (!std::strcmp(key, "_ZN10QQuickItem14mouseMoveEventEP11QMouseEvent")) {
      taken[2] = call;
      return true;
    }
#endif  // QT_CONFIG(quick_pathview)
#if QT_CONFIG(quick_pathview)
    if (!std::strcmp(key, "_ZN10QQuickItem17mouseReleaseEventEP11QMouseEvent")) {
      taken[3] = call;
      return true;
    }
#endif  // QT_CONFIG(quick_pathview)
#if QT_CONFIG(quick_pathview)
    if (!std::strcmp(key, "_ZN10QQuickItem21childMouseEventFilterEPS_P6QEvent")) {
      taken[4] = call;
      return true;
    }
#endif  // QT_CONFIG(quick_pathview)
#if QT_CONFIG(quick_pathview)
    if (!std::strcmp(key, "_ZN10QQuickItem16mouseUngrabEventEv")) {
      taken[5] = call;
      return true;
    }
#endif  // QT_CONFIG(quick_pathview)
#if QT_CONFIG(quick_pathview)
    if (!std::strcmp(key, "_ZN16QQmlParserStatus17componentCompleteEv")) {
      taken[6] = call;
      return true;
    }
#endif  // QT_CONFIG(quick_pathview)
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
    if (!std::strcmp(key, "_ZN10QQuickItem14geometryChangeERK6QRectFS2_")) {
      taken[15] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQmlParserStatus10classBeginEv")) {
      taken[16] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem13keyPressEventEP9QKeyEvent")) {
      taken[17] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem15keyReleaseEventEP9QKeyEvent")) {
      taken[18] = call;
      return true;
    }
#if QT_CONFIG(im)
    if (!std::strcmp(key, "_ZN10QQuickItem16inputMethodEventEP17QInputMethodEvent")) {
      taken[19] = call;
      return true;
    }
#endif  // QT_CONFIG(im)
    if (!std::strcmp(key, "_ZN10QQuickItem12focusInEventEP11QFocusEvent")) {
      taken[20] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem13focusOutEventEP11QFocusEvent")) {
      taken[21] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem21mouseDoubleClickEventEP11QMouseEvent")) {
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

#if QT_CONFIG(quick_pathview)
  //  void QQuickPathView::updatePolish()
  void updatePolish() override {
    if (taken[0]) {
      int handled = 0;
      CuteQQuickPathViewCall0 call = reinterpret_cast<CuteQQuickPathViewCall0>(taken[0]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickPathView::updatePolish();
  }
#endif  // QT_CONFIG(quick_pathview)

#if QT_CONFIG(quick_pathview)
  //  void QQuickPathView::mousePressEvent(QMouseEvent *event)
  void mousePressEvent(QMouseEvent *event) override {
    if (taken[1]) {
      int handled = 0;
      CuteQQuickPathViewCall1 call = reinterpret_cast<CuteQQuickPathViewCall1>(taken[1]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickPathView::mousePressEvent(event);
  }
#endif  // QT_CONFIG(quick_pathview)

#if QT_CONFIG(quick_pathview)
  //  void QQuickPathView::mouseMoveEvent(QMouseEvent *event)
  void mouseMoveEvent(QMouseEvent *event) override {
    if (taken[2]) {
      int handled = 0;
      CuteQQuickPathViewCall2 call = reinterpret_cast<CuteQQuickPathViewCall2>(taken[2]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickPathView::mouseMoveEvent(event);
  }
#endif  // QT_CONFIG(quick_pathview)

#if QT_CONFIG(quick_pathview)
  //  void QQuickPathView::mouseReleaseEvent(QMouseEvent *a0)
  void mouseReleaseEvent(QMouseEvent *a0) override {
    if (taken[3]) {
      int handled = 0;
      CuteQQuickPathViewCall3 call = reinterpret_cast<CuteQQuickPathViewCall3>(taken[3]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickPathView::mouseReleaseEvent(a0);
  }
#endif  // QT_CONFIG(quick_pathview)

#if QT_CONFIG(quick_pathview)
  //  bool QQuickPathView::childMouseEventFilter(QQuickItem *a0, QEvent
  //      *a1)
  bool childMouseEventFilter(QQuickItem *a0, QEvent *a1) override {
    if (taken[4]) {
      int handled = 0;
      CuteQQuickPathViewCall4 call = reinterpret_cast<CuteQQuickPathViewCall4>(taken[4]);
      bool given = call(this, a0, a1, &handled);
      if (handled) return given;
    }
    return QQuickPathView::childMouseEventFilter(a0, a1);
  }
#endif  // QT_CONFIG(quick_pathview)

#if QT_CONFIG(quick_pathview)
  //  void QQuickPathView::mouseUngrabEvent()
  void mouseUngrabEvent() override {
    if (taken[5]) {
      int handled = 0;
      CuteQQuickPathViewCall5 call = reinterpret_cast<CuteQQuickPathViewCall5>(taken[5]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickPathView::mouseUngrabEvent();
  }
#endif  // QT_CONFIG(quick_pathview)

#if QT_CONFIG(quick_pathview)
  //  void QQuickPathView::componentComplete()
  void componentComplete() override {
    if (taken[6]) {
      int handled = 0;
      CuteQQuickPathViewCall6 call = reinterpret_cast<CuteQQuickPathViewCall6>(taken[6]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickPathView::componentComplete();
  }
#endif  // QT_CONFIG(quick_pathview)

  //  QRectF QQuickItem::boundingRect() const
  QRectF boundingRect() const override {
    if (taken[7]) {
      int handled = 0;
      CuteQQuickPathViewCall7 call = reinterpret_cast<CuteQQuickPathViewCall7>(taken[7]);
      const QRectF * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QQuickItem::boundingRect();
  }

  //  QRectF QQuickItem::clipRect() const
  QRectF clipRect() const override {
    if (taken[8]) {
      int handled = 0;
      CuteQQuickPathViewCall8 call = reinterpret_cast<CuteQQuickPathViewCall8>(taken[8]);
      const QRectF * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QQuickItem::clipRect();
  }

  //  bool QQuickItem::contains(const QPointF &point) const
  bool contains(const QPointF &point) const override {
    if (taken[9]) {
      int handled = 0;
      CuteQQuickPathViewCall9 call = reinterpret_cast<CuteQQuickPathViewCall9>(taken[9]);
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
      CuteQQuickPathViewCall10 call = reinterpret_cast<CuteQQuickPathViewCall10>(taken[10]);
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
      CuteQQuickPathViewCall11 call = reinterpret_cast<CuteQQuickPathViewCall11>(taken[11]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QQuickItem::isTextureProvider();
  }

  //  QSGTextureProvider *QQuickItem::textureProvider() const
  QSGTextureProvider *textureProvider() const override {
    if (taken[12]) {
      int handled = 0;
      CuteQQuickPathViewCall12 call = reinterpret_cast<CuteQQuickPathViewCall12>(taken[12]);
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
      CuteQQuickPathViewCall13 call = reinterpret_cast<CuteQQuickPathViewCall13>(taken[13]);
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
      CuteQQuickPathViewCall14 call = reinterpret_cast<CuteQQuickPathViewCall14>(taken[14]);
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
    if (taken[15]) {
      int handled = 0;
      CuteQQuickPathViewCall15 call = reinterpret_cast<CuteQQuickPathViewCall15>(taken[15]);
      call(this, &newGeometry, &oldGeometry, &handled);
      if (handled) return;
    }
    QQuickItem::geometryChange(newGeometry, oldGeometry);
  }

  //  void QQuickItem::classBegin()
  void classBegin() override {
    if (taken[16]) {
      int handled = 0;
      CuteQQuickPathViewCall16 call = reinterpret_cast<CuteQQuickPathViewCall16>(taken[16]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItem::classBegin();
  }

  //  void QQuickItem::keyPressEvent(QKeyEvent *event)
  void keyPressEvent(QKeyEvent *event) override {
    if (taken[17]) {
      int handled = 0;
      CuteQQuickPathViewCall17 call = reinterpret_cast<CuteQQuickPathViewCall17>(taken[17]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::keyPressEvent(event);
  }

  //  void QQuickItem::keyReleaseEvent(QKeyEvent *event)
  void keyReleaseEvent(QKeyEvent *event) override {
    if (taken[18]) {
      int handled = 0;
      CuteQQuickPathViewCall18 call = reinterpret_cast<CuteQQuickPathViewCall18>(taken[18]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::keyReleaseEvent(event);
  }

#if QT_CONFIG(im)
  //  void QQuickItem::inputMethodEvent(QInputMethodEvent *a0)
  void inputMethodEvent(QInputMethodEvent *a0) override {
    if (taken[19]) {
      int handled = 0;
      CuteQQuickPathViewCall19 call = reinterpret_cast<CuteQQuickPathViewCall19>(taken[19]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItem::inputMethodEvent(a0);
  }
#endif  // QT_CONFIG(im)

  //  void QQuickItem::focusInEvent(QFocusEvent *a0)
  void focusInEvent(QFocusEvent *a0) override {
    if (taken[20]) {
      int handled = 0;
      CuteQQuickPathViewCall20 call = reinterpret_cast<CuteQQuickPathViewCall20>(taken[20]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItem::focusInEvent(a0);
  }

  //  void QQuickItem::focusOutEvent(QFocusEvent *a0)
  void focusOutEvent(QFocusEvent *a0) override {
    if (taken[21]) {
      int handled = 0;
      CuteQQuickPathViewCall21 call = reinterpret_cast<CuteQQuickPathViewCall21>(taken[21]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItem::focusOutEvent(a0);
  }

  //  void QQuickItem::mouseDoubleClickEvent(QMouseEvent *event)
  void mouseDoubleClickEvent(QMouseEvent *event) override {
    if (taken[22]) {
      int handled = 0;
      CuteQQuickPathViewCall22 call = reinterpret_cast<CuteQQuickPathViewCall22>(taken[22]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::mouseDoubleClickEvent(event);
  }

  //  void QQuickItem::touchUngrabEvent()
  void touchUngrabEvent() override {
    if (taken[23]) {
      int handled = 0;
      CuteQQuickPathViewCall23 call = reinterpret_cast<CuteQQuickPathViewCall23>(taken[23]);
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
      CuteQQuickPathViewCall24 call = reinterpret_cast<CuteQQuickPathViewCall24>(taken[24]);
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
      CuteQQuickPathViewCall25 call = reinterpret_cast<CuteQQuickPathViewCall25>(taken[25]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::touchEvent(event);
  }

  //  void QQuickItem::hoverEnterEvent(QHoverEvent *event)
  void hoverEnterEvent(QHoverEvent *event) override {
    if (taken[26]) {
      int handled = 0;
      CuteQQuickPathViewCall26 call = reinterpret_cast<CuteQQuickPathViewCall26>(taken[26]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::hoverEnterEvent(event);
  }

  //  void QQuickItem::hoverMoveEvent(QHoverEvent *event)
  void hoverMoveEvent(QHoverEvent *event) override {
    if (taken[27]) {
      int handled = 0;
      CuteQQuickPathViewCall27 call = reinterpret_cast<CuteQQuickPathViewCall27>(taken[27]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::hoverMoveEvent(event);
  }

  //  void QQuickItem::hoverLeaveEvent(QHoverEvent *event)
  void hoverLeaveEvent(QHoverEvent *event) override {
    if (taken[28]) {
      int handled = 0;
      CuteQQuickPathViewCall28 call = reinterpret_cast<CuteQQuickPathViewCall28>(taken[28]);
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
      CuteQQuickPathViewCall29 call = reinterpret_cast<CuteQQuickPathViewCall29>(taken[29]);
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
      CuteQQuickPathViewCall30 call = reinterpret_cast<CuteQQuickPathViewCall30>(taken[30]);
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
      CuteQQuickPathViewCall31 call = reinterpret_cast<CuteQQuickPathViewCall31>(taken[31]);
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
      CuteQQuickPathViewCall32 call = reinterpret_cast<CuteQQuickPathViewCall32>(taken[32]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItem::dropEvent(a0);
  }
#endif  // QT_CONFIG(quick_draganddrop)

  //  QSGNode *QQuickItem::updatePaintNode(QSGNode *a0, UpdatePaintNodeData
  //      *a1)
  QSGNode *updatePaintNode(
      QSGNode *a0,
      QQuickItem::UpdatePaintNodeData *a1) override {
    if (taken[33]) {
      int handled = 0;
      CuteQQuickPathViewCall33 call = reinterpret_cast<CuteQQuickPathViewCall33>(taken[33]);
      void * given = call(this, a0, a1, &handled);
      if (handled) return static_cast<QSGNode *>(given);
    }
    return QQuickItem::updatePaintNode(a0, a1);
  }

  //  void QQuickItem::releaseResources()
  void releaseResources() override {
    if (taken[34]) {
      int handled = 0;
      CuteQQuickPathViewCall34 call = reinterpret_cast<CuteQQuickPathViewCall34>(taken[34]);
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
      CuteQQuickPathViewCall35 call = reinterpret_cast<CuteQQuickPathViewCall35>(taken[35]);
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
      CuteQQuickPathViewCall36 call = reinterpret_cast<CuteQQuickPathViewCall36>(taken[36]);
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
      CuteQQuickPathViewCall37 call = reinterpret_cast<CuteQQuickPathViewCall37>(taken[37]);
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
      CuteQQuickPathViewCall38 call = reinterpret_cast<CuteQQuickPathViewCall38>(taken[38]);
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
      CuteQQuickPathViewCall39 call = reinterpret_cast<CuteQQuickPathViewCall39>(taken[39]);
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
      CuteQQuickPathViewCall40 call = reinterpret_cast<CuteQQuickPathViewCall40>(taken[40]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QQuickPathView::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK14QQuickPathView10metaObjectEv(
    const QQuickPathView *self) {
  return self->metaObject();
}

//  QString QQuickPathView::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN14QQuickPathView2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuickPathView::tr(s, c, n));
}

//  void QQuickPathView::qt_qmlMarker_attached()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickPathView21qt_qmlMarker_attachedEv(
    QQuickPathView *self) {
  self->qt_qmlMarker_attached();
}

//  QQuickPathView::QQuickPathView(QQuickItem *parent)
extern "C" Q_DECL_EXPORT
QQuickPathView *ritual_ZN14QQuickPathViewC1EP10QQuickItem(
    QQuickItem *parent) {
  return new CuteQQuickPathView(parent);
}

//  QQuickPathView::~QQuickPathView()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickPathViewD1Ev(QQuickPathView *self) {
  delete self;
}

//  QVariant QQuickPathView::model() const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK14QQuickPathView5modelEv(const QQuickPathView *self) {
  return new QVariant(self->model());
}

//  void QQuickPathView::setModel(const QVariant &a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickPathView8setModelERK8QVariant(
    QQuickPathView *self,
    const QVariant *a0) {
  self->setModel(*a0);
}

//  QQuickPath *QQuickPathView::path() const
extern "C" Q_DECL_EXPORT
QQuickPath *ritual_ZNK14QQuickPathView4pathEv(const QQuickPathView *self) {
  return self->path();
}

//  void QQuickPathView::setPath(QQuickPath *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickPathView7setPathEP10QQuickPath(
    QQuickPathView *self,
    QQuickPath *a0) {
  self->setPath(a0);
}

//  int QQuickPathView::currentIndex() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK14QQuickPathView12currentIndexEv(const QQuickPathView *self) {
  return self->currentIndex();
}

//  void QQuickPathView::setCurrentIndex(int idx)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickPathView15setCurrentIndexEi(
    QQuickPathView *self,
    int idx) {
  self->setCurrentIndex(idx);
}

//  QQuickItem *QQuickPathView::currentItem() const
extern "C" Q_DECL_EXPORT
QQuickItem *ritual_ZNK14QQuickPathView11currentItemEv(
    const QQuickPathView *self) {
  return self->currentItem();
}

//  qreal QQuickPathView::offset() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK14QQuickPathView6offsetEv(const QQuickPathView *self) {
  return self->offset();
}

//  void QQuickPathView::setOffset(qreal offset)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickPathView9setOffsetEd(
    QQuickPathView *self,
    qreal offset) {
  self->setOffset(offset);
}

//  QQmlComponent *QQuickPathView::highlight() const
extern "C" Q_DECL_EXPORT
QQmlComponent *ritual_ZNK14QQuickPathView9highlightEv(
    const QQuickPathView *self) {
  return self->highlight();
}

//  void QQuickPathView::setHighlight(QQmlComponent *highlight)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickPathView12setHighlightEP13QQmlComponent(
    QQuickPathView *self,
    QQmlComponent *highlight) {
  self->setHighlight(highlight);
}

//  QQuickItem *QQuickPathView::highlightItem() const
extern "C" Q_DECL_EXPORT
QQuickItem *ritual_ZNK14QQuickPathView13highlightItemEv(
    const QQuickPathView *self) {
  return self->highlightItem();
}

//  HighlightRangeMode QQuickPathView::highlightRangeMode() const
extern "C" Q_DECL_EXPORT
QQuickPathView::HighlightRangeMode ritual_ZNK14QQuickPathView18highlightRangeModeEv(
    const QQuickPathView *self) {
  return self->highlightRangeMode();
}

//  void QQuickPathView::setHighlightRangeMode(HighlightRangeMode mode)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickPathView21setHighlightRangeModeENS_18HighlightRangeModeE(
    QQuickPathView *self,
    QQuickPathView::HighlightRangeMode mode) {
  self->setHighlightRangeMode(mode);
}

//  qreal QQuickPathView::preferredHighlightBegin() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK14QQuickPathView23preferredHighlightBeginEv(
    const QQuickPathView *self) {
  return self->preferredHighlightBegin();
}

//  void QQuickPathView::setPreferredHighlightBegin(qreal a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickPathView26setPreferredHighlightBeginEd(
    QQuickPathView *self,
    qreal a0) {
  self->setPreferredHighlightBegin(a0);
}

//  qreal QQuickPathView::preferredHighlightEnd() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK14QQuickPathView21preferredHighlightEndEv(
    const QQuickPathView *self) {
  return self->preferredHighlightEnd();
}

//  void QQuickPathView::setPreferredHighlightEnd(qreal a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickPathView24setPreferredHighlightEndEd(
    QQuickPathView *self,
    qreal a0) {
  self->setPreferredHighlightEnd(a0);
}

//  int QQuickPathView::highlightMoveDuration() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK14QQuickPathView21highlightMoveDurationEv(
    const QQuickPathView *self) {
  return self->highlightMoveDuration();
}

//  void QQuickPathView::setHighlightMoveDuration(int a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickPathView24setHighlightMoveDurationEi(
    QQuickPathView *self,
    int a0) {
  self->setHighlightMoveDuration(a0);
}

//  qreal QQuickPathView::dragMargin() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK14QQuickPathView10dragMarginEv(const QQuickPathView *self) {
  return self->dragMargin();
}

//  void QQuickPathView::setDragMargin(qreal margin)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickPathView13setDragMarginEd(
    QQuickPathView *self,
    qreal margin) {
  self->setDragMargin(margin);
}

//  qreal QQuickPathView::flickDeceleration() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK14QQuickPathView17flickDecelerationEv(
    const QQuickPathView *self) {
  return self->flickDeceleration();
}

//  void QQuickPathView::setFlickDeceleration(qreal dec)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickPathView20setFlickDecelerationEd(
    QQuickPathView *self,
    qreal dec) {
  self->setFlickDeceleration(dec);
}

//  qreal QQuickPathView::maximumFlickVelocity() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK14QQuickPathView20maximumFlickVelocityEv(
    const QQuickPathView *self) {
  return self->maximumFlickVelocity();
}

//  void QQuickPathView::setMaximumFlickVelocity(qreal a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickPathView23setMaximumFlickVelocityEd(
    QQuickPathView *self,
    qreal a0) {
  self->setMaximumFlickVelocity(a0);
}

//  bool QQuickPathView::isInteractive() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK14QQuickPathView13isInteractiveEv(
    const QQuickPathView *self) {
  return self->isInteractive();
}

//  void QQuickPathView::setInteractive(bool a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickPathView14setInteractiveEb(
    QQuickPathView *self,
    bool a0) {
  self->setInteractive(a0);
}

//  bool QQuickPathView::isMoving() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK14QQuickPathView8isMovingEv(const QQuickPathView *self) {
  return self->isMoving();
}

//  bool QQuickPathView::isFlicking() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK14QQuickPathView10isFlickingEv(const QQuickPathView *self) {
  return self->isFlicking();
}

//  bool QQuickPathView::isDragging() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK14QQuickPathView10isDraggingEv(const QQuickPathView *self) {
  return self->isDragging();
}

//  int QQuickPathView::count() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK14QQuickPathView5countEv(const QQuickPathView *self) {
  return self->count();
}

//  QQmlComponent *QQuickPathView::delegate() const
extern "C" Q_DECL_EXPORT
QQmlComponent *ritual_ZNK14QQuickPathView8delegateEv(
    const QQuickPathView *self) {
  return self->delegate();
}

//  void QQuickPathView::setDelegate(QQmlComponent *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickPathView11setDelegateEP13QQmlComponent(
    QQuickPathView *self,
    QQmlComponent *a0) {
  self->setDelegate(a0);
}

//  int QQuickPathView::pathItemCount() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK14QQuickPathView13pathItemCountEv(const QQuickPathView *self) {
  return self->pathItemCount();
}

//  void QQuickPathView::setPathItemCount(int a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickPathView16setPathItemCountEi(
    QQuickPathView *self,
    int a0) {
  self->setPathItemCount(a0);
}

//  void QQuickPathView::resetPathItemCount()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickPathView18resetPathItemCountEv(QQuickPathView *self) {
  self->resetPathItemCount();
}

//  int QQuickPathView::cacheItemCount() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK14QQuickPathView14cacheItemCountEv(
    const QQuickPathView *self) {
  return self->cacheItemCount();
}

//  void QQuickPathView::setCacheItemCount(int a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickPathView17setCacheItemCountEi(
    QQuickPathView *self,
    int a0) {
  self->setCacheItemCount(a0);
}

//  SnapMode QQuickPathView::snapMode() const
extern "C" Q_DECL_EXPORT
QQuickPathView::SnapMode ritual_ZNK14QQuickPathView8snapModeEv(
    const QQuickPathView *self) {
  return self->snapMode();
}

//  void QQuickPathView::setSnapMode(SnapMode mode)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickPathView11setSnapModeENS_8SnapModeE(
    QQuickPathView *self,
    QQuickPathView::SnapMode mode) {
  self->setSnapMode(mode);
}

//  MovementDirection QQuickPathView::movementDirection() const
extern "C" Q_DECL_EXPORT
QQuickPathView::MovementDirection ritual_ZNK14QQuickPathView17movementDirectionEv(
    const QQuickPathView *self) {
  return self->movementDirection();
}

//  void QQuickPathView::setMovementDirection(MovementDirection dir)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickPathView20setMovementDirectionENS_17MovementDirectionE(
    QQuickPathView *self,
    QQuickPathView::MovementDirection dir) {
  self->setMovementDirection(dir);
}

//  void QQuickPathView::positionViewAtIndex(int index, int mode)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickPathView19positionViewAtIndexEii(
    QQuickPathView *self,
    int index,
    int mode) {
  self->positionViewAtIndex(index, mode);
}

//  int QQuickPathView::indexAt(qreal x, qreal y) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK14QQuickPathView7indexAtEdd(
    const QQuickPathView *self,
    qreal x,
    qreal y) {
  return self->indexAt(x, y);
}

//  QQuickItem *QQuickPathView::itemAt(qreal x, qreal y) const
extern "C" Q_DECL_EXPORT
QQuickItem *ritual_ZNK14QQuickPathView6itemAtEdd(
    const QQuickPathView *self,
    qreal x,
    qreal y) {
  return self->itemAt(x, y);
}

//  QQuickItem *QQuickPathView::itemAtIndex(int index) const
extern "C" Q_DECL_EXPORT
QQuickItem *ritual_ZNK14QQuickPathView11itemAtIndexEi(
    const QQuickPathView *self,
    int index) {
  return self->itemAtIndex(index);
}

//  QQuickPathViewAttached *QQuickPathView::qmlAttachedProperties(QObject
//      *a0)
extern "C" Q_DECL_EXPORT
QQuickPathViewAttached *ritual_ZN14QQuickPathView21qmlAttachedPropertiesEP7QObject(
    QObject *a0) {
  return QQuickPathView::qmlAttachedProperties(a0);
}

//  void QQuickPathView::incrementCurrentIndex()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickPathView21incrementCurrentIndexEv(
    QQuickPathView *self) {
  self->incrementCurrentIndex();
}

//  void QQuickPathView::decrementCurrentIndex()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickPathView21decrementCurrentIndexEv(
    QQuickPathView *self) {
  self->decrementCurrentIndex();
}

//  void QQuickPathView::updatePolish()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickPathView12updatePolishEv(QQuickPathView *self) {
  self->updatePolish();
}

//  void QQuickPathView::mousePressEvent(QMouseEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickPathView15mousePressEventEP11QMouseEvent(
    QQuickPathView *self,
    QMouseEvent *event) {
  self->mousePressEvent(event);
}

//  void QQuickPathView::mouseMoveEvent(QMouseEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickPathView14mouseMoveEventEP11QMouseEvent(
    QQuickPathView *self,
    QMouseEvent *event) {
  self->mouseMoveEvent(event);
}

//  void QQuickPathView::mouseReleaseEvent(QMouseEvent *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickPathView17mouseReleaseEventEP11QMouseEvent(
    QQuickPathView *self,
    QMouseEvent *a0) {
  self->mouseReleaseEvent(a0);
}

//  bool QQuickPathView::childMouseEventFilter(QQuickItem *a0, QEvent *a1)
extern "C" Q_DECL_EXPORT
bool ritual_ZN14QQuickPathView21childMouseEventFilterEP10QQuickItemP6QEvent(
    QQuickPathView *self,
    QQuickItem *a0,
    QEvent *a1) {
  return self->childMouseEventFilter(a0, a1);
}

//  void QQuickPathView::mouseUngrabEvent()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickPathView16mouseUngrabEventEv(QQuickPathView *self) {
  self->mouseUngrabEvent();
}

//  void QQuickPathView::componentComplete()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickPathView17componentCompleteEv(QQuickPathView *self) {
  self->componentComplete();
}

//  void QQuickPathView::refill()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickPathView6refillEv(QQuickPathView *self) {
  self->refill();
}

//  void QQuickPathView::ticked()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickPathView6tickedEv(QQuickPathView *self) {
  self->ticked();
}

//  void QQuickPathView::movementEnding()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickPathView14movementEndingEv(QQuickPathView *self) {
  self->movementEnding();
}

//  void QQuickPathView::modelUpdated(const QQmlChangeSet &changeSet, bool
//      reset)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickPathView12modelUpdatedERK13QQmlChangeSetb(
    QQuickPathView *self,
    const QQmlChangeSet *changeSet,
    bool reset) {
  self->modelUpdated(*changeSet, reset);
}

//  void QQuickPathView::createdItem(int index, QObject *item)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickPathView11createdItemEiP7QObject(
    QQuickPathView *self,
    int index,
    QObject *item) {
  self->createdItem(index, item);
}

//  void QQuickPathView::initItem(int index, QObject *item)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickPathView8initItemEiP7QObject(
    QQuickPathView *self,
    int index,
    QObject *item) {
  self->initItem(index, item);
}

//  void QQuickPathView::destroyingItem(QObject *item)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickPathView14destroyingItemEP7QObject(
    QQuickPathView *self,
    QObject *item) {
  self->destroyingItem(item);
}

//  void QQuickPathView::pathUpdated()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickPathView11pathUpdatedEv(QQuickPathView *self) {
  self->pathUpdated();
}

//  QQuickPathViewPrivate *QQuickPathView::d_func()
extern "C" Q_DECL_EXPORT
QQuickPathViewPrivate *ritual_ZN14QQuickPathView6d_funcEv(
    QQuickPathView *self) {
  return self->d_func();
}

//  const QQuickPathViewPrivate *QQuickPathView::d_func() const
extern "C" Q_DECL_EXPORT
const QQuickPathViewPrivate *ritual_ZNK14QQuickPathView6d_funcEv(
    const QQuickPathView *self) {
  return self->d_func();
}

//  a Python function taken by a CuteQQuickPathView, for the function named
//      by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQuickPathView(
    QQuickPathView *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQuickPathView *>(self)->take(key, call);
}

//  void QQuickPathView::updatePolish()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN14QQuickPathView12updatePolishEv(QQuickPathView *self) {
  static_cast<OwnQQuickPathView *>(self)->OwnQQuickPathView::updatePolish();
}

//  void QQuickPathView::mousePressEvent(QMouseEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN14QQuickPathView15mousePressEventEP11QMouseEvent(
    QQuickPathView *self,
    QMouseEvent *event) {
  static_cast<OwnQQuickPathView *>(self)->OwnQQuickPathView::mousePressEvent(
      event);
}

//  void QQuickPathView::mouseMoveEvent(QMouseEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN14QQuickPathView14mouseMoveEventEP11QMouseEvent(
    QQuickPathView *self,
    QMouseEvent *event) {
  static_cast<OwnQQuickPathView *>(self)->OwnQQuickPathView::mouseMoveEvent(
      event);
}

//  void QQuickPathView::mouseReleaseEvent(QMouseEvent *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN14QQuickPathView17mouseReleaseEventEP11QMouseEvent(
    QQuickPathView *self,
    QMouseEvent *a0) {
  static_cast<OwnQQuickPathView *>(self)->OwnQQuickPathView::mouseReleaseEvent(
      a0);
}

//  bool QQuickPathView::childMouseEventFilter(QQuickItem *a0, QEvent *a1)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN14QQuickPathView21childMouseEventFilterEP10QQuickItemP6QEvent(
    QQuickPathView *self,
    QQuickItem *a0,
    QEvent *a1) {
  return static_cast<OwnQQuickPathView *>(self)->OwnQQuickPathView::childMouseEventFilter(
      a0,
      a1);
}

//  void QQuickPathView::mouseUngrabEvent()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN14QQuickPathView16mouseUngrabEventEv(
    QQuickPathView *self) {
  static_cast<OwnQQuickPathView *>(self)->OwnQQuickPathView::mouseUngrabEvent();
}

//  void QQuickPathView::componentComplete()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN14QQuickPathView17componentCompleteEv(
    QQuickPathView *self) {
  static_cast<OwnQQuickPathView *>(self)->OwnQQuickPathView::componentComplete();
}

#endif  // QT_CONFIG(quick_pathview)
#endif  // QT_CONFIG(quick_pathview)
