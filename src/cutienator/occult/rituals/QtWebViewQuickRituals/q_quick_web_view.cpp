//  Written by dev_tooling.RitualGenerator from the records of
//  QtWebViewQuick/6.12.0/QtWebViewQuick/private/qquickwebview_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtGui/qtguiglobal.h>
#include <QtQuick/qtquickglobal.h>
#include <QtWebViewQuick/6.12.0/QtWebViewQuick/private/qtwebviewquickglobal_p.h>
#include <QtWebViewQuick/QtWebViewQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtWebViewQuick/6.12.0/QtWebViewQuick/private/qquickwebview_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qurl.h>
#include <QtQml/QtQml>
#include <QtQml/qjsvalue.h>
#include <QtWebView/qwebviewloadinginfo.h>
#include <QtCore/qrect.h>
#include <QtQuick/QtQuick>
#include <QtQuick/qquickitem.h>
#include <QtCore/qpoint.h>
#include <QtCore/qvariant.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  Only a class built on QQuickWebView may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQQuickWebView : QQuickWebView {
  using QQuickWebView::classBegin;
};

//  A QQuickWebView that Python can take functions over in. Every QQuickWebView
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQQuickWebViewCall0)(const void *, int *);
typedef void (*CuteQQuickWebViewCall1)(const void *, int *);
typedef void (*CuteQQuickWebViewCall2)(const void *, const QRectF *, const QRectF *, int *);
typedef void (*CuteQQuickWebViewCall3)(const void *, int, const QQuickItem::ItemChangeData *, int *);
typedef void (*CuteQQuickWebViewCall4)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickWebViewCall5)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickWebViewCall6)(const void *, QFocusEvent *, int *);
typedef const QRectF * (*CuteQQuickWebViewCall7)(const void *, int *);
typedef void (*CuteQQuickWebViewCall8)(const void *, int *);
typedef const QRectF * (*CuteQQuickWebViewCall9)(const void *, int *);
typedef bool (*CuteQQuickWebViewCall10)(const void *, const QPointF *, int *);
#if QT_CONFIG(im)
typedef const QVariant * (*CuteQQuickWebViewCall11)(const void *, int, int *);
#endif  // QT_CONFIG(im)
typedef bool (*CuteQQuickWebViewCall12)(const void *, int *);
typedef void * (*CuteQQuickWebViewCall13)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickWebViewCall14)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickWebViewCall15)(const void *, QKeyEvent *, int *);
typedef void (*CuteQQuickWebViewCall16)(const void *, QKeyEvent *, int *);
#if QT_CONFIG(im)
typedef void (*CuteQQuickWebViewCall17)(const void *, QInputMethodEvent *, int *);
#endif  // QT_CONFIG(im)
typedef void (*CuteQQuickWebViewCall18)(const void *, QFocusEvent *, int *);
typedef void (*CuteQQuickWebViewCall19)(const void *, QMouseEvent *, int *);
typedef void (*CuteQQuickWebViewCall20)(const void *, QMouseEvent *, int *);
typedef void (*CuteQQuickWebViewCall21)(const void *, QMouseEvent *, int *);
typedef void (*CuteQQuickWebViewCall22)(const void *, QMouseEvent *, int *);
typedef void (*CuteQQuickWebViewCall23)(const void *, int *);
typedef void (*CuteQQuickWebViewCall24)(const void *, int *);
#if QT_CONFIG(wheelevent)
typedef void (*CuteQQuickWebViewCall25)(const void *, QWheelEvent *, int *);
#endif  // QT_CONFIG(wheelevent)
typedef void (*CuteQQuickWebViewCall26)(const void *, QTouchEvent *, int *);
typedef void (*CuteQQuickWebViewCall27)(const void *, QHoverEvent *, int *);
typedef void (*CuteQQuickWebViewCall28)(const void *, QHoverEvent *, int *);
typedef void (*CuteQQuickWebViewCall29)(const void *, QHoverEvent *, int *);
#if QT_CONFIG(quick_draganddrop)
typedef void (*CuteQQuickWebViewCall30)(const void *, QDragEnterEvent *, int *);
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
typedef void (*CuteQQuickWebViewCall31)(const void *, QDragMoveEvent *, int *);
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
typedef void (*CuteQQuickWebViewCall32)(const void *, QDragLeaveEvent *, int *);
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
typedef void (*CuteQQuickWebViewCall33)(const void *, QDropEvent *, int *);
#endif  // QT_CONFIG(quick_draganddrop)
typedef bool (*CuteQQuickWebViewCall34)(const void *, QQuickItem *, QEvent *, int *);
typedef void * (*CuteQQuickWebViewCall35)(const void *, QSGNode *, QQuickItem::UpdatePaintNodeData *, int *);
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickWebViewCall36)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickWebViewCall37)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickWebViewCall38)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickWebViewCall39)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickWebViewCall40)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQQuickWebView : public QQuickWebView {
public:
  using QQuickWebView::QQuickWebView;
  void *taken[41] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN16QQmlParserStatus10classBeginEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQmlParserStatus17componentCompleteEv")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem14geometryChangeERK6QRectFS2_")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem10itemChangeENS_10ItemChangeERKNS_14ItemChangeDataE")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem12updatePolishEv")) {
      taken[4] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[5] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN10QQuickItem12focusInEventEP11QFocusEvent")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK10QQuickItem8clipRectEv")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem16releaseResourcesEv")) {
      taken[8] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK10QQuickItem12boundingRectEv")) {
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
    if (!std::strcmp(key, "_ZN10QQuickItem15updatePaintNodeEP7QSGNodePNS_19UpdatePaintNodeDataE")) {
      taken[35] = call;
      return true;
    }
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

  //  void QQuickWebView::classBegin()
  void classBegin() override {
    if (taken[0]) {
      int handled = 0;
      CuteQQuickWebViewCall0 call = reinterpret_cast<CuteQQuickWebViewCall0>(taken[0]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickWebView::classBegin();
  }

  //  void QQuickWindowContainer::componentComplete()
  void componentComplete() override {
    if (taken[1]) {
      int handled = 0;
      CuteQQuickWebViewCall1 call = reinterpret_cast<CuteQQuickWebViewCall1>(taken[1]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickWindowContainer::componentComplete();
  }

  //  void QQuickWindowContainer::geometryChange(const QRectF &newGeometry,
  //      const QRectF &oldGeometry)
  void geometryChange(
      const QRectF &newGeometry,
      const QRectF &oldGeometry) override {
    if (taken[2]) {
      int handled = 0;
      CuteQQuickWebViewCall2 call = reinterpret_cast<CuteQQuickWebViewCall2>(taken[2]);
      call(this, &newGeometry, &oldGeometry, &handled);
      if (handled) return;
    }
    QQuickWindowContainer::geometryChange(newGeometry, oldGeometry);
  }

  //  void QQuickWindowContainer::itemChange(QQuickItem::ItemChange a0,
  //      const QQuickItem::ItemChangeData &a1)
  void itemChange(
      QQuickItem::ItemChange a0,
      const QQuickItem::ItemChangeData &a1) override {
    if (taken[3]) {
      int handled = 0;
      CuteQQuickWebViewCall3 call = reinterpret_cast<CuteQQuickWebViewCall3>(taken[3]);
      call(this, static_cast<int>(a0), &a1, &handled);
      if (handled) return;
    }
    QQuickWindowContainer::itemChange(a0, a1);
  }

  //  void QQuickWindowContainer::updatePolish()
  void updatePolish() override {
    if (taken[4]) {
      int handled = 0;
      CuteQQuickWebViewCall4 call = reinterpret_cast<CuteQQuickWebViewCall4>(taken[4]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickWindowContainer::updatePolish();
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QQuickWindowContainer::eventFilter(QObject *object, QEvent
  //      *event)
  bool eventFilter(QObject *object, QEvent *event) override {
    if (taken[5]) {
      int handled = 0;
      CuteQQuickWebViewCall5 call = reinterpret_cast<CuteQQuickWebViewCall5>(taken[5]);
      bool given = call(this, object, event, &handled);
      if (handled) return given;
    }
    return QQuickWindowContainer::eventFilter(object, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

  //  void QQuickWindowContainer::focusInEvent(QFocusEvent *a0)
  void focusInEvent(QFocusEvent *a0) override {
    if (taken[6]) {
      int handled = 0;
      CuteQQuickWebViewCall6 call = reinterpret_cast<CuteQQuickWebViewCall6>(taken[6]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickWindowContainer::focusInEvent(a0);
  }

  //  QRectF QQuickWindowContainer::clipRect() const
  QRectF clipRect() const override {
    if (taken[7]) {
      int handled = 0;
      CuteQQuickWebViewCall7 call = reinterpret_cast<CuteQQuickWebViewCall7>(taken[7]);
      const QRectF * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QQuickWindowContainer::clipRect();
  }

  //  void QQuickWindowContainer::releaseResources()
  void releaseResources() override {
    if (taken[8]) {
      int handled = 0;
      CuteQQuickWebViewCall8 call = reinterpret_cast<CuteQQuickWebViewCall8>(taken[8]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickWindowContainer::releaseResources();
  }

  //  QRectF QQuickItem::boundingRect() const
  QRectF boundingRect() const override {
    if (taken[9]) {
      int handled = 0;
      CuteQQuickWebViewCall9 call = reinterpret_cast<CuteQQuickWebViewCall9>(taken[9]);
      const QRectF * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QQuickItem::boundingRect();
  }

  //  bool QQuickItem::contains(const QPointF &point) const
  bool contains(const QPointF &point) const override {
    if (taken[10]) {
      int handled = 0;
      CuteQQuickWebViewCall10 call = reinterpret_cast<CuteQQuickWebViewCall10>(taken[10]);
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
      CuteQQuickWebViewCall11 call = reinterpret_cast<CuteQQuickWebViewCall11>(taken[11]);
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
      CuteQQuickWebViewCall12 call = reinterpret_cast<CuteQQuickWebViewCall12>(taken[12]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QQuickItem::isTextureProvider();
  }

  //  QSGTextureProvider *QQuickItem::textureProvider() const
  QSGTextureProvider *textureProvider() const override {
    if (taken[13]) {
      int handled = 0;
      CuteQQuickWebViewCall13 call = reinterpret_cast<CuteQQuickWebViewCall13>(taken[13]);
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
      CuteQQuickWebViewCall14 call = reinterpret_cast<CuteQQuickWebViewCall14>(taken[14]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQuickItem::event(a0);
  }
#endif  // !defined(QT_NO_QOBJECT)

  //  void QQuickItem::keyPressEvent(QKeyEvent *event)
  void keyPressEvent(QKeyEvent *event) override {
    if (taken[15]) {
      int handled = 0;
      CuteQQuickWebViewCall15 call = reinterpret_cast<CuteQQuickWebViewCall15>(taken[15]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::keyPressEvent(event);
  }

  //  void QQuickItem::keyReleaseEvent(QKeyEvent *event)
  void keyReleaseEvent(QKeyEvent *event) override {
    if (taken[16]) {
      int handled = 0;
      CuteQQuickWebViewCall16 call = reinterpret_cast<CuteQQuickWebViewCall16>(taken[16]);
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
      CuteQQuickWebViewCall17 call = reinterpret_cast<CuteQQuickWebViewCall17>(taken[17]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItem::inputMethodEvent(a0);
  }
#endif  // QT_CONFIG(im)

  //  void QQuickItem::focusOutEvent(QFocusEvent *a0)
  void focusOutEvent(QFocusEvent *a0) override {
    if (taken[18]) {
      int handled = 0;
      CuteQQuickWebViewCall18 call = reinterpret_cast<CuteQQuickWebViewCall18>(taken[18]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItem::focusOutEvent(a0);
  }

  //  void QQuickItem::mousePressEvent(QMouseEvent *event)
  void mousePressEvent(QMouseEvent *event) override {
    if (taken[19]) {
      int handled = 0;
      CuteQQuickWebViewCall19 call = reinterpret_cast<CuteQQuickWebViewCall19>(taken[19]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::mousePressEvent(event);
  }

  //  void QQuickItem::mouseMoveEvent(QMouseEvent *event)
  void mouseMoveEvent(QMouseEvent *event) override {
    if (taken[20]) {
      int handled = 0;
      CuteQQuickWebViewCall20 call = reinterpret_cast<CuteQQuickWebViewCall20>(taken[20]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::mouseMoveEvent(event);
  }

  //  void QQuickItem::mouseReleaseEvent(QMouseEvent *event)
  void mouseReleaseEvent(QMouseEvent *event) override {
    if (taken[21]) {
      int handled = 0;
      CuteQQuickWebViewCall21 call = reinterpret_cast<CuteQQuickWebViewCall21>(taken[21]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::mouseReleaseEvent(event);
  }

  //  void QQuickItem::mouseDoubleClickEvent(QMouseEvent *event)
  void mouseDoubleClickEvent(QMouseEvent *event) override {
    if (taken[22]) {
      int handled = 0;
      CuteQQuickWebViewCall22 call = reinterpret_cast<CuteQQuickWebViewCall22>(taken[22]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::mouseDoubleClickEvent(event);
  }

  //  void QQuickItem::mouseUngrabEvent()
  void mouseUngrabEvent() override {
    if (taken[23]) {
      int handled = 0;
      CuteQQuickWebViewCall23 call = reinterpret_cast<CuteQQuickWebViewCall23>(taken[23]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItem::mouseUngrabEvent();
  }

  //  void QQuickItem::touchUngrabEvent()
  void touchUngrabEvent() override {
    if (taken[24]) {
      int handled = 0;
      CuteQQuickWebViewCall24 call = reinterpret_cast<CuteQQuickWebViewCall24>(taken[24]);
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
      CuteQQuickWebViewCall25 call = reinterpret_cast<CuteQQuickWebViewCall25>(taken[25]);
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
      CuteQQuickWebViewCall26 call = reinterpret_cast<CuteQQuickWebViewCall26>(taken[26]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::touchEvent(event);
  }

  //  void QQuickItem::hoverEnterEvent(QHoverEvent *event)
  void hoverEnterEvent(QHoverEvent *event) override {
    if (taken[27]) {
      int handled = 0;
      CuteQQuickWebViewCall27 call = reinterpret_cast<CuteQQuickWebViewCall27>(taken[27]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::hoverEnterEvent(event);
  }

  //  void QQuickItem::hoverMoveEvent(QHoverEvent *event)
  void hoverMoveEvent(QHoverEvent *event) override {
    if (taken[28]) {
      int handled = 0;
      CuteQQuickWebViewCall28 call = reinterpret_cast<CuteQQuickWebViewCall28>(taken[28]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::hoverMoveEvent(event);
  }

  //  void QQuickItem::hoverLeaveEvent(QHoverEvent *event)
  void hoverLeaveEvent(QHoverEvent *event) override {
    if (taken[29]) {
      int handled = 0;
      CuteQQuickWebViewCall29 call = reinterpret_cast<CuteQQuickWebViewCall29>(taken[29]);
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
      CuteQQuickWebViewCall30 call = reinterpret_cast<CuteQQuickWebViewCall30>(taken[30]);
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
      CuteQQuickWebViewCall31 call = reinterpret_cast<CuteQQuickWebViewCall31>(taken[31]);
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
      CuteQQuickWebViewCall32 call = reinterpret_cast<CuteQQuickWebViewCall32>(taken[32]);
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
      CuteQQuickWebViewCall33 call = reinterpret_cast<CuteQQuickWebViewCall33>(taken[33]);
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
      CuteQQuickWebViewCall34 call = reinterpret_cast<CuteQQuickWebViewCall34>(taken[34]);
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
    if (taken[35]) {
      int handled = 0;
      CuteQQuickWebViewCall35 call = reinterpret_cast<CuteQQuickWebViewCall35>(taken[35]);
      void * given = call(this, a0, a1, &handled);
      if (handled) return static_cast<QSGNode *>(given);
    }
    return QQuickItem::updatePaintNode(a0, a1);
  }

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[36]) {
      int handled = 0;
      CuteQQuickWebViewCall36 call = reinterpret_cast<CuteQQuickWebViewCall36>(taken[36]);
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
      CuteQQuickWebViewCall37 call = reinterpret_cast<CuteQQuickWebViewCall37>(taken[37]);
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
      CuteQQuickWebViewCall38 call = reinterpret_cast<CuteQQuickWebViewCall38>(taken[38]);
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
      CuteQQuickWebViewCall39 call = reinterpret_cast<CuteQQuickWebViewCall39>(taken[39]);
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
      CuteQQuickWebViewCall40 call = reinterpret_cast<CuteQQuickWebViewCall40>(taken[40]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QQuickWebView::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK13QQuickWebView10metaObjectEv(
    const QQuickWebView *self) {
  return self->metaObject();
}

//  QString QQuickWebView::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN13QQuickWebView2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuickWebView::tr(s, c, n));
}

//  QQuickWebView::QQuickWebView(QQuickItem *parent)
extern "C" Q_DECL_EXPORT
QQuickWebView *ritual_ZN13QQuickWebViewC1EP10QQuickItem(QQuickItem *parent) {
  return new CuteQQuickWebView(parent);
}

//  QQuickWebView::~QQuickWebView()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QQuickWebViewD1Ev(QQuickWebView *self) {
  delete self;
}

//  QString QQuickWebView::httpUserAgent() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK13QQuickWebView13httpUserAgentEv(
    const QQuickWebView *self) {
  return new QString(self->httpUserAgent());
}

//  void QQuickWebView::setHttpUserAgent(const QString &userAgent)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QQuickWebView16setHttpUserAgentERK7QString(
    QQuickWebView *self,
    const QString *userAgent) {
  self->setHttpUserAgent(*userAgent);
}

//  QUrl QQuickWebView::url() const
extern "C" Q_DECL_EXPORT
QUrl *ritual_ZNK13QQuickWebView3urlEv(const QQuickWebView *self) {
  return new QUrl(self->url());
}

//  void QQuickWebView::setUrl(const QUrl &url)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QQuickWebView6setUrlERK4QUrl(
    QQuickWebView *self,
    const QUrl *url) {
  self->setUrl(*url);
}

//  int QQuickWebView::loadProgress() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK13QQuickWebView12loadProgressEv(const QQuickWebView *self) {
  return self->loadProgress();
}

//  QString QQuickWebView::title() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK13QQuickWebView5titleEv(const QQuickWebView *self) {
  return new QString(self->title());
}

//  bool QQuickWebView::canGoBack() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK13QQuickWebView9canGoBackEv(const QQuickWebView *self) {
  return self->canGoBack();
}

//  bool QQuickWebView::isLoading() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK13QQuickWebView9isLoadingEv(const QQuickWebView *self) {
  return self->isLoading();
}

//  bool QQuickWebView::canGoForward() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK13QQuickWebView12canGoForwardEv(const QQuickWebView *self) {
  return self->canGoForward();
}

//  QQuickWebViewSettings *QQuickWebView::settings() const
extern "C" Q_DECL_EXPORT
QQuickWebViewSettings *ritual_ZNK13QQuickWebView8settingsEv(
    const QQuickWebView *self) {
  return self->settings();
}

//  void QQuickWebView::classBegin()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QQuickWebView10classBeginEv(QQuickWebView *self) {
  self->classBegin();
}

//  void QQuickWebView::goBack()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QQuickWebView6goBackEv(QQuickWebView *self) {
  self->goBack();
}

//  void QQuickWebView::goForward()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QQuickWebView9goForwardEv(QQuickWebView *self) {
  self->goForward();
}

//  void QQuickWebView::reload()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QQuickWebView6reloadEv(QQuickWebView *self) {
  self->reload();
}

//  void QQuickWebView::stop()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QQuickWebView4stopEv(QQuickWebView *self) {
  self->stop();
}

//  void QQuickWebView::loadHtml(const QString &html, const QUrl &baseUrl)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QQuickWebView8loadHtmlERK7QStringRK4QUrl(
    QQuickWebView *self,
    const QString *html,
    const QUrl *baseUrl) {
  self->loadHtml(*html, *baseUrl);
}

//  void QQuickWebView::runJavaScript(const QString &script, const QJSValue
//      &callback)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QQuickWebView13runJavaScriptERK7QStringRK8QJSValue(
    QQuickWebView *self,
    const QString *script,
    const QJSValue *callback) {
  self->runJavaScript(*script, *callback);
}

//  void QQuickWebView::setCookie(const QString &domain, const QString &name,
//      const QString &value)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QQuickWebView9setCookieERK7QStringS2_S2_(
    QQuickWebView *self,
    const QString *domain,
    const QString *name,
    const QString *value) {
  self->setCookie(*domain, *name, *value);
}

//  void QQuickWebView::deleteCookie(const QString &domain, const QString
//      &name)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QQuickWebView12deleteCookieERK7QStringS2_(
    QQuickWebView *self,
    const QString *domain,
    const QString *name) {
  self->deleteCookie(*domain, *name);
}

//  void QQuickWebView::deleteAllCookies()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QQuickWebView16deleteAllCookiesEv(QQuickWebView *self) {
  self->deleteAllCookies();
}

//  void QQuickWebView::onLoadingChanged(const QWebViewLoadingInfo
//      &loadRequest)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QQuickWebView16onLoadingChangedERK19QWebViewLoadingInfo(
    QQuickWebView *self,
    const QWebViewLoadingInfo *loadRequest) {
  self->onLoadingChanged(*loadRequest);
}

//  a Python function taken by a CuteQQuickWebView, for the function named by
//      the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQuickWebView(
    QQuickWebView *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQuickWebView *>(self)->take(key, call);
}

//  void QQuickWebView::classBegin()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN13QQuickWebView10classBeginEv(QQuickWebView *self) {
  static_cast<OwnQQuickWebView *>(self)->OwnQQuickWebView::classBegin();
}
