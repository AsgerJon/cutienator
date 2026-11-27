//  Written by dev_tooling.RitualGenerator from the records of
//  QtWebEngineQuick/6.12.0/QtWebEngineQuick/private/qquickwebengineview_p.h,
//  Qt 6.12.0. Changes made here are lost.
#include <QtGui/qtguiglobal.h>
#include <QtQuick/qtquickglobal.h>
#include <QtWebEngineQuick/6.12.0/QtWebEngineQuick/private/qtwebenginequickglobal_p.h>
#include <QtWebEngineQuick/QtWebEngineQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtWebEngineQuick/6.12.0/QtWebEngineQuick/private/qquickwebengineview_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qurl.h>
#include <QtGui/qcolor.h>
#include <QtCore/qsize.h>
#include <QtCore/qpoint.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtWebEngineQuick/6.12.0/QtWebEngineQuick/private/qquickwebengineframe_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/QtQml>
#include <QtQml/qjsvalue.h>
#include <QtWebEngineCore/qwebengineloadinginfo.h>
#include <QtWebEngineCore/qwebenginecertificateerror.h>
#include <QtWebEngineCore/qwebenginefullscreenrequest.h>
#include <QtWebEngineCore/qwebenginequotarequest.h>
#include <QtCore/qrect.h>
#include <QtWebEngineCore/qwebengineregisterprotocolhandlerrequest.h>
#include <QtWebEngineCore/qwebenginefindtextresult.h>
#include <QtWebEngineCore/qwebenginefilesystemaccessrequest.h>
#include <QtWebEngineCore/qwebenginedesktopmediarequest.h>
#include <QtWebEngineCore/qwebenginepermission.h>
#include <QtQuick/QtQuick>
#include <QtQuick/qquickitem.h>
#include <QtCore/qvariant.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  Only a class built on QQuickWebEngineView may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQQuickWebEngineView : QQuickWebEngineView {
  using QQuickWebEngineView::geometryChange;
  using QQuickWebEngineView::itemChange;
  using QQuickWebEngineView::dragEnterEvent;
  using QQuickWebEngineView::dragLeaveEvent;
  using QQuickWebEngineView::dragMoveEvent;
  using QQuickWebEngineView::dropEvent;
};

//  A QQuickWebEngineView that Python can take functions over in. Every QQuickWebEngineView
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQQuickWebEngineViewCall0)(const void *, int *);
typedef void (*CuteQQuickWebEngineViewCall1)(const void *, const QRectF *, const QRectF *, int *);
typedef void (*CuteQQuickWebEngineViewCall2)(const void *, int, const QQuickItem::ItemChangeData *, int *);
#if QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(draganddrop)
typedef void (*CuteQQuickWebEngineViewCall3)(const void *, QDragEnterEvent *, int *);
#endif  // QT_CONFIG(draganddrop)
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(draganddrop)
typedef void (*CuteQQuickWebEngineViewCall4)(const void *, QDragLeaveEvent *, int *);
#endif  // QT_CONFIG(draganddrop)
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(draganddrop)
typedef void (*CuteQQuickWebEngineViewCall5)(const void *, QDragMoveEvent *, int *);
#endif  // QT_CONFIG(draganddrop)
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(draganddrop)
typedef void (*CuteQQuickWebEngineViewCall6)(const void *, QDropEvent *, int *);
#endif  // QT_CONFIG(draganddrop)
#endif  // QT_CONFIG(quick_draganddrop)
typedef const QRectF * (*CuteQQuickWebEngineViewCall7)(const void *, int *);
typedef const QRectF * (*CuteQQuickWebEngineViewCall8)(const void *, int *);
typedef bool (*CuteQQuickWebEngineViewCall9)(const void *, const QPointF *, int *);
#if QT_CONFIG(im)
typedef const QVariant * (*CuteQQuickWebEngineViewCall10)(const void *, int, int *);
#endif  // QT_CONFIG(im)
typedef bool (*CuteQQuickWebEngineViewCall11)(const void *, int *);
typedef void * (*CuteQQuickWebEngineViewCall12)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickWebEngineViewCall13)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickWebEngineViewCall14)(const void *, int *);
typedef void (*CuteQQuickWebEngineViewCall15)(const void *, QKeyEvent *, int *);
typedef void (*CuteQQuickWebEngineViewCall16)(const void *, QKeyEvent *, int *);
#if QT_CONFIG(im)
typedef void (*CuteQQuickWebEngineViewCall17)(const void *, QInputMethodEvent *, int *);
#endif  // QT_CONFIG(im)
typedef void (*CuteQQuickWebEngineViewCall18)(const void *, QFocusEvent *, int *);
typedef void (*CuteQQuickWebEngineViewCall19)(const void *, QFocusEvent *, int *);
typedef void (*CuteQQuickWebEngineViewCall20)(const void *, QMouseEvent *, int *);
typedef void (*CuteQQuickWebEngineViewCall21)(const void *, QMouseEvent *, int *);
typedef void (*CuteQQuickWebEngineViewCall22)(const void *, QMouseEvent *, int *);
typedef void (*CuteQQuickWebEngineViewCall23)(const void *, QMouseEvent *, int *);
typedef void (*CuteQQuickWebEngineViewCall24)(const void *, int *);
typedef void (*CuteQQuickWebEngineViewCall25)(const void *, int *);
#if QT_CONFIG(wheelevent)
typedef void (*CuteQQuickWebEngineViewCall26)(const void *, QWheelEvent *, int *);
#endif  // QT_CONFIG(wheelevent)
typedef void (*CuteQQuickWebEngineViewCall27)(const void *, QTouchEvent *, int *);
typedef void (*CuteQQuickWebEngineViewCall28)(const void *, QHoverEvent *, int *);
typedef void (*CuteQQuickWebEngineViewCall29)(const void *, QHoverEvent *, int *);
typedef void (*CuteQQuickWebEngineViewCall30)(const void *, QHoverEvent *, int *);
typedef bool (*CuteQQuickWebEngineViewCall31)(const void *, QQuickItem *, QEvent *, int *);
typedef void * (*CuteQQuickWebEngineViewCall32)(const void *, QSGNode *, QQuickItem::UpdatePaintNodeData *, int *);
typedef void (*CuteQQuickWebEngineViewCall33)(const void *, int *);
typedef void (*CuteQQuickWebEngineViewCall34)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickWebEngineViewCall35)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickWebEngineViewCall36)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickWebEngineViewCall37)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickWebEngineViewCall38)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickWebEngineViewCall39)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickWebEngineViewCall40)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQQuickWebEngineView : public QQuickWebEngineView {
public:
  using QQuickWebEngineView::QQuickWebEngineView;
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
    if (!std::strcmp(key, "_ZN10QQuickItem10itemChangeENS_10ItemChangeERKNS_14ItemChangeDataE")) {
      taken[2] = call;
      return true;
    }
#if QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(draganddrop)
    if (!std::strcmp(key, "_ZN10QQuickItem14dragEnterEventEP15QDragEnterEvent")) {
      taken[3] = call;
      return true;
    }
#endif  // QT_CONFIG(draganddrop)
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(draganddrop)
    if (!std::strcmp(key, "_ZN10QQuickItem14dragLeaveEventEP15QDragLeaveEvent")) {
      taken[4] = call;
      return true;
    }
#endif  // QT_CONFIG(draganddrop)
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(draganddrop)
    if (!std::strcmp(key, "_ZN10QQuickItem13dragMoveEventEP14QDragMoveEvent")) {
      taken[5] = call;
      return true;
    }
#endif  // QT_CONFIG(draganddrop)
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(draganddrop)
    if (!std::strcmp(key, "_ZN10QQuickItem9dropEventEP10QDropEvent")) {
      taken[6] = call;
      return true;
    }
#endif  // QT_CONFIG(draganddrop)
#endif  // QT_CONFIG(quick_draganddrop)
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
#if QT_CONFIG(wheelevent)
    if (!std::strcmp(key, "_ZN10QQuickItem10wheelEventEP11QWheelEvent")) {
      taken[26] = call;
      return true;
    }
#endif  // QT_CONFIG(wheelevent)
    if (!std::strcmp(key, "_ZN10QQuickItem10touchEventEP11QTouchEvent")) {
      taken[27] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem15hoverEnterEventEP11QHoverEvent")) {
      taken[28] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem14hoverMoveEventEP11QHoverEvent")) {
      taken[29] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem15hoverLeaveEventEP11QHoverEvent")) {
      taken[30] = call;
      return true;
    }
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

  //  void QQuickWebEngineView::componentComplete()
  void componentComplete() override {
    if (taken[0]) {
      int handled = 0;
      CuteQQuickWebEngineViewCall0 call = reinterpret_cast<CuteQQuickWebEngineViewCall0>(taken[0]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickWebEngineView::componentComplete();
  }

  //  void QQuickWebEngineView::geometryChange(const QRectF &newGeometry,
  //      const QRectF &oldGeometry)
  void geometryChange(
      const QRectF &newGeometry,
      const QRectF &oldGeometry) override {
    if (taken[1]) {
      int handled = 0;
      CuteQQuickWebEngineViewCall1 call = reinterpret_cast<CuteQQuickWebEngineViewCall1>(taken[1]);
      call(this, &newGeometry, &oldGeometry, &handled);
      if (handled) return;
    }
    QQuickWebEngineView::geometryChange(newGeometry, oldGeometry);
  }

  //  void QQuickWebEngineView::itemChange(ItemChange a0, const
  //      ItemChangeData &a1)
  void itemChange(
      QQuickItem::ItemChange a0,
      const QQuickItem::ItemChangeData &a1) override {
    if (taken[2]) {
      int handled = 0;
      CuteQQuickWebEngineViewCall2 call = reinterpret_cast<CuteQQuickWebEngineViewCall2>(taken[2]);
      call(this, static_cast<int>(a0), &a1, &handled);
      if (handled) return;
    }
    QQuickWebEngineView::itemChange(a0, a1);
  }

#if QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(draganddrop)
  //  void QQuickWebEngineView::dragEnterEvent(QDragEnterEvent *e)
  void dragEnterEvent(QDragEnterEvent *e) override {
    if (taken[3]) {
      int handled = 0;
      CuteQQuickWebEngineViewCall3 call = reinterpret_cast<CuteQQuickWebEngineViewCall3>(taken[3]);
      call(this, e, &handled);
      if (handled) return;
    }
    QQuickWebEngineView::dragEnterEvent(e);
  }
#endif  // QT_CONFIG(draganddrop)
#endif  // QT_CONFIG(quick_draganddrop)

#if QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(draganddrop)
  //  void QQuickWebEngineView::dragLeaveEvent(QDragLeaveEvent *e)
  void dragLeaveEvent(QDragLeaveEvent *e) override {
    if (taken[4]) {
      int handled = 0;
      CuteQQuickWebEngineViewCall4 call = reinterpret_cast<CuteQQuickWebEngineViewCall4>(taken[4]);
      call(this, e, &handled);
      if (handled) return;
    }
    QQuickWebEngineView::dragLeaveEvent(e);
  }
#endif  // QT_CONFIG(draganddrop)
#endif  // QT_CONFIG(quick_draganddrop)

#if QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(draganddrop)
  //  void QQuickWebEngineView::dragMoveEvent(QDragMoveEvent *e)
  void dragMoveEvent(QDragMoveEvent *e) override {
    if (taken[5]) {
      int handled = 0;
      CuteQQuickWebEngineViewCall5 call = reinterpret_cast<CuteQQuickWebEngineViewCall5>(taken[5]);
      call(this, e, &handled);
      if (handled) return;
    }
    QQuickWebEngineView::dragMoveEvent(e);
  }
#endif  // QT_CONFIG(draganddrop)
#endif  // QT_CONFIG(quick_draganddrop)

#if QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(draganddrop)
  //  void QQuickWebEngineView::dropEvent(QDropEvent *e)
  void dropEvent(QDropEvent *e) override {
    if (taken[6]) {
      int handled = 0;
      CuteQQuickWebEngineViewCall6 call = reinterpret_cast<CuteQQuickWebEngineViewCall6>(taken[6]);
      call(this, e, &handled);
      if (handled) return;
    }
    QQuickWebEngineView::dropEvent(e);
  }
#endif  // QT_CONFIG(draganddrop)
#endif  // QT_CONFIG(quick_draganddrop)

  //  QRectF QQuickItem::boundingRect() const
  QRectF boundingRect() const override {
    if (taken[7]) {
      int handled = 0;
      CuteQQuickWebEngineViewCall7 call = reinterpret_cast<CuteQQuickWebEngineViewCall7>(taken[7]);
      const QRectF * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QQuickItem::boundingRect();
  }

  //  QRectF QQuickItem::clipRect() const
  QRectF clipRect() const override {
    if (taken[8]) {
      int handled = 0;
      CuteQQuickWebEngineViewCall8 call = reinterpret_cast<CuteQQuickWebEngineViewCall8>(taken[8]);
      const QRectF * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QQuickItem::clipRect();
  }

  //  bool QQuickItem::contains(const QPointF &point) const
  bool contains(const QPointF &point) const override {
    if (taken[9]) {
      int handled = 0;
      CuteQQuickWebEngineViewCall9 call = reinterpret_cast<CuteQQuickWebEngineViewCall9>(taken[9]);
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
      CuteQQuickWebEngineViewCall10 call = reinterpret_cast<CuteQQuickWebEngineViewCall10>(taken[10]);
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
      CuteQQuickWebEngineViewCall11 call = reinterpret_cast<CuteQQuickWebEngineViewCall11>(taken[11]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QQuickItem::isTextureProvider();
  }

  //  QSGTextureProvider *QQuickItem::textureProvider() const
  QSGTextureProvider *textureProvider() const override {
    if (taken[12]) {
      int handled = 0;
      CuteQQuickWebEngineViewCall12 call = reinterpret_cast<CuteQQuickWebEngineViewCall12>(taken[12]);
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
      CuteQQuickWebEngineViewCall13 call = reinterpret_cast<CuteQQuickWebEngineViewCall13>(taken[13]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQuickItem::event(a0);
  }
#endif  // !defined(QT_NO_QOBJECT)

  //  void QQuickItem::classBegin()
  void classBegin() override {
    if (taken[14]) {
      int handled = 0;
      CuteQQuickWebEngineViewCall14 call = reinterpret_cast<CuteQQuickWebEngineViewCall14>(taken[14]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItem::classBegin();
  }

  //  void QQuickItem::keyPressEvent(QKeyEvent *event)
  void keyPressEvent(QKeyEvent *event) override {
    if (taken[15]) {
      int handled = 0;
      CuteQQuickWebEngineViewCall15 call = reinterpret_cast<CuteQQuickWebEngineViewCall15>(taken[15]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::keyPressEvent(event);
  }

  //  void QQuickItem::keyReleaseEvent(QKeyEvent *event)
  void keyReleaseEvent(QKeyEvent *event) override {
    if (taken[16]) {
      int handled = 0;
      CuteQQuickWebEngineViewCall16 call = reinterpret_cast<CuteQQuickWebEngineViewCall16>(taken[16]);
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
      CuteQQuickWebEngineViewCall17 call = reinterpret_cast<CuteQQuickWebEngineViewCall17>(taken[17]);
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
      CuteQQuickWebEngineViewCall18 call = reinterpret_cast<CuteQQuickWebEngineViewCall18>(taken[18]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItem::focusInEvent(a0);
  }

  //  void QQuickItem::focusOutEvent(QFocusEvent *a0)
  void focusOutEvent(QFocusEvent *a0) override {
    if (taken[19]) {
      int handled = 0;
      CuteQQuickWebEngineViewCall19 call = reinterpret_cast<CuteQQuickWebEngineViewCall19>(taken[19]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItem::focusOutEvent(a0);
  }

  //  void QQuickItem::mousePressEvent(QMouseEvent *event)
  void mousePressEvent(QMouseEvent *event) override {
    if (taken[20]) {
      int handled = 0;
      CuteQQuickWebEngineViewCall20 call = reinterpret_cast<CuteQQuickWebEngineViewCall20>(taken[20]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::mousePressEvent(event);
  }

  //  void QQuickItem::mouseMoveEvent(QMouseEvent *event)
  void mouseMoveEvent(QMouseEvent *event) override {
    if (taken[21]) {
      int handled = 0;
      CuteQQuickWebEngineViewCall21 call = reinterpret_cast<CuteQQuickWebEngineViewCall21>(taken[21]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::mouseMoveEvent(event);
  }

  //  void QQuickItem::mouseReleaseEvent(QMouseEvent *event)
  void mouseReleaseEvent(QMouseEvent *event) override {
    if (taken[22]) {
      int handled = 0;
      CuteQQuickWebEngineViewCall22 call = reinterpret_cast<CuteQQuickWebEngineViewCall22>(taken[22]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::mouseReleaseEvent(event);
  }

  //  void QQuickItem::mouseDoubleClickEvent(QMouseEvent *event)
  void mouseDoubleClickEvent(QMouseEvent *event) override {
    if (taken[23]) {
      int handled = 0;
      CuteQQuickWebEngineViewCall23 call = reinterpret_cast<CuteQQuickWebEngineViewCall23>(taken[23]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::mouseDoubleClickEvent(event);
  }

  //  void QQuickItem::mouseUngrabEvent()
  void mouseUngrabEvent() override {
    if (taken[24]) {
      int handled = 0;
      CuteQQuickWebEngineViewCall24 call = reinterpret_cast<CuteQQuickWebEngineViewCall24>(taken[24]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItem::mouseUngrabEvent();
  }

  //  void QQuickItem::touchUngrabEvent()
  void touchUngrabEvent() override {
    if (taken[25]) {
      int handled = 0;
      CuteQQuickWebEngineViewCall25 call = reinterpret_cast<CuteQQuickWebEngineViewCall25>(taken[25]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItem::touchUngrabEvent();
  }

#if QT_CONFIG(wheelevent)
  //  void QQuickItem::wheelEvent(QWheelEvent *event)
  void wheelEvent(QWheelEvent *event) override {
    if (taken[26]) {
      int handled = 0;
      CuteQQuickWebEngineViewCall26 call = reinterpret_cast<CuteQQuickWebEngineViewCall26>(taken[26]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::wheelEvent(event);
  }
#endif  // QT_CONFIG(wheelevent)

  //  void QQuickItem::touchEvent(QTouchEvent *event)
  void touchEvent(QTouchEvent *event) override {
    if (taken[27]) {
      int handled = 0;
      CuteQQuickWebEngineViewCall27 call = reinterpret_cast<CuteQQuickWebEngineViewCall27>(taken[27]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::touchEvent(event);
  }

  //  void QQuickItem::hoverEnterEvent(QHoverEvent *event)
  void hoverEnterEvent(QHoverEvent *event) override {
    if (taken[28]) {
      int handled = 0;
      CuteQQuickWebEngineViewCall28 call = reinterpret_cast<CuteQQuickWebEngineViewCall28>(taken[28]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::hoverEnterEvent(event);
  }

  //  void QQuickItem::hoverMoveEvent(QHoverEvent *event)
  void hoverMoveEvent(QHoverEvent *event) override {
    if (taken[29]) {
      int handled = 0;
      CuteQQuickWebEngineViewCall29 call = reinterpret_cast<CuteQQuickWebEngineViewCall29>(taken[29]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::hoverMoveEvent(event);
  }

  //  void QQuickItem::hoverLeaveEvent(QHoverEvent *event)
  void hoverLeaveEvent(QHoverEvent *event) override {
    if (taken[30]) {
      int handled = 0;
      CuteQQuickWebEngineViewCall30 call = reinterpret_cast<CuteQQuickWebEngineViewCall30>(taken[30]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::hoverLeaveEvent(event);
  }

  //  bool QQuickItem::childMouseEventFilter(QQuickItem *a0, QEvent *a1)
  bool childMouseEventFilter(QQuickItem *a0, QEvent *a1) override {
    if (taken[31]) {
      int handled = 0;
      CuteQQuickWebEngineViewCall31 call = reinterpret_cast<CuteQQuickWebEngineViewCall31>(taken[31]);
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
      CuteQQuickWebEngineViewCall32 call = reinterpret_cast<CuteQQuickWebEngineViewCall32>(taken[32]);
      void * given = call(this, a0, a1, &handled);
      if (handled) return static_cast<QSGNode *>(given);
    }
    return QQuickItem::updatePaintNode(a0, a1);
  }

  //  void QQuickItem::releaseResources()
  void releaseResources() override {
    if (taken[33]) {
      int handled = 0;
      CuteQQuickWebEngineViewCall33 call = reinterpret_cast<CuteQQuickWebEngineViewCall33>(taken[33]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItem::releaseResources();
  }

  //  void QQuickItem::updatePolish()
  void updatePolish() override {
    if (taken[34]) {
      int handled = 0;
      CuteQQuickWebEngineViewCall34 call = reinterpret_cast<CuteQQuickWebEngineViewCall34>(taken[34]);
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
      CuteQQuickWebEngineViewCall35 call = reinterpret_cast<CuteQQuickWebEngineViewCall35>(taken[35]);
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
      CuteQQuickWebEngineViewCall36 call = reinterpret_cast<CuteQQuickWebEngineViewCall36>(taken[36]);
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
      CuteQQuickWebEngineViewCall37 call = reinterpret_cast<CuteQQuickWebEngineViewCall37>(taken[37]);
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
      CuteQQuickWebEngineViewCall38 call = reinterpret_cast<CuteQQuickWebEngineViewCall38>(taken[38]);
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
      CuteQQuickWebEngineViewCall39 call = reinterpret_cast<CuteQQuickWebEngineViewCall39>(taken[39]);
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
      CuteQQuickWebEngineViewCall40 call = reinterpret_cast<CuteQQuickWebEngineViewCall40>(taken[40]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QQuickWebEngineView::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK19QQuickWebEngineView10metaObjectEv(
    const QQuickWebEngineView *self) {
  return self->metaObject();
}

//  void *QQuickWebEngineView::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN19QQuickWebEngineView11qt_metacastEPKc(
    QQuickWebEngineView *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QQuickWebEngineView::qt_metacall(QMetaObject::Call a0, int a1, void
//      **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN19QQuickWebEngineView11qt_metacallEN11QMetaObject4CallEiPPv(
    QQuickWebEngineView *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QQuickWebEngineView::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN19QQuickWebEngineView2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuickWebEngineView::tr(s, c, n));
}

//  QQuickWebEngineView::QQuickWebEngineView(QQuickItem *parent)
extern "C" Q_DECL_EXPORT
QQuickWebEngineView *ritual_ZN19QQuickWebEngineViewC1EP10QQuickItem(
    QQuickItem *parent) {
  return new CuteQQuickWebEngineView(parent);
}

//  QQuickWebEngineView::~QQuickWebEngineView()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickWebEngineViewD1Ev(QQuickWebEngineView *self) {
  delete self;
}

//  QUrl QQuickWebEngineView::url() const
extern "C" Q_DECL_EXPORT
QUrl *ritual_ZNK19QQuickWebEngineView3urlEv(
    const QQuickWebEngineView *self) {
  return new QUrl(self->url());
}

//  void QQuickWebEngineView::setUrl(const QUrl &a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickWebEngineView6setUrlERK4QUrl(
    QQuickWebEngineView *self,
    const QUrl *a0) {
  self->setUrl(*a0);
}

//  QUrl QQuickWebEngineView::icon() const
extern "C" Q_DECL_EXPORT
QUrl *ritual_ZNK19QQuickWebEngineView4iconEv(
    const QQuickWebEngineView *self) {
  return new QUrl(self->icon());
}

//  bool QQuickWebEngineView::isLoading() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK19QQuickWebEngineView9isLoadingEv(
    const QQuickWebEngineView *self) {
  return self->isLoading();
}

//  int QQuickWebEngineView::loadProgress() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK19QQuickWebEngineView12loadProgressEv(
    const QQuickWebEngineView *self) {
  return self->loadProgress();
}

//  QString QQuickWebEngineView::title() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK19QQuickWebEngineView5titleEv(
    const QQuickWebEngineView *self) {
  return new QString(self->title());
}

//  bool QQuickWebEngineView::canGoBack() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK19QQuickWebEngineView9canGoBackEv(
    const QQuickWebEngineView *self) {
  return self->canGoBack();
}

//  bool QQuickWebEngineView::canGoForward() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK19QQuickWebEngineView12canGoForwardEv(
    const QQuickWebEngineView *self) {
  return self->canGoForward();
}

//  bool QQuickWebEngineView::isFullScreen() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK19QQuickWebEngineView12isFullScreenEv(
    const QQuickWebEngineView *self) {
  return self->isFullScreen();
}

//  qreal QQuickWebEngineView::zoomFactor() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK19QQuickWebEngineView10zoomFactorEv(
    const QQuickWebEngineView *self) {
  return self->zoomFactor();
}

//  void QQuickWebEngineView::setZoomFactor(qreal arg)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickWebEngineView13setZoomFactorEd(
    QQuickWebEngineView *self,
    qreal arg) {
  self->setZoomFactor(arg);
}

//  QColor QQuickWebEngineView::backgroundColor() const
extern "C" Q_DECL_EXPORT
QColor *ritual_ZNK19QQuickWebEngineView15backgroundColorEv(
    const QQuickWebEngineView *self) {
  return new QColor(self->backgroundColor());
}

//  void QQuickWebEngineView::setBackgroundColor(const QColor &color)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickWebEngineView18setBackgroundColorERK6QColor(
    QQuickWebEngineView *self,
    const QColor *color) {
  self->setBackgroundColor(*color);
}

//  QSizeF QQuickWebEngineView::contentsSize() const
extern "C" Q_DECL_EXPORT
QSizeF *ritual_ZNK19QQuickWebEngineView12contentsSizeEv(
    const QQuickWebEngineView *self) {
  return new QSizeF(self->contentsSize());
}

//  QPointF QQuickWebEngineView::scrollPosition() const
extern "C" Q_DECL_EXPORT
QPointF *ritual_ZNK19QQuickWebEngineView14scrollPositionEv(
    const QQuickWebEngineView *self) {
  return new QPointF(self->scrollPosition());
}

//  void QQuickWebEngineView::componentComplete()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickWebEngineView17componentCompleteEv(
    QQuickWebEngineView *self) {
  self->componentComplete();
}

//  QQuickWebEngineProfile *QQuickWebEngineView::profile()
extern "C" Q_DECL_EXPORT
QQuickWebEngineProfile *ritual_ZN19QQuickWebEngineView7profileEv(
    QQuickWebEngineView *self) {
  return self->profile();
}

//  void QQuickWebEngineView::setProfile(QQuickWebEngineProfile *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickWebEngineView10setProfileEP22QQuickWebEngineProfile(
    QQuickWebEngineView *self,
    QQuickWebEngineProfile *a0) {
  self->setProfile(a0);
}

//  QQuickWebEngineScriptCollection *QQuickWebEngineView::userScripts()
extern "C" Q_DECL_EXPORT
QQuickWebEngineScriptCollection *ritual_ZN19QQuickWebEngineView11userScriptsEv(
    QQuickWebEngineView *self) {
  return self->userScripts();
}

//  QQuickWebEngineSettings *QQuickWebEngineView::settings()
extern "C" Q_DECL_EXPORT
QQuickWebEngineSettings *ritual_ZN19QQuickWebEngineView8settingsEv(
    QQuickWebEngineView *self) {
  return self->settings();
}

//  QQmlWebChannel *QQuickWebEngineView::webChannel()
extern "C" Q_DECL_EXPORT
QQmlWebChannel *ritual_ZN19QQuickWebEngineView10webChannelEv(
    QQuickWebEngineView *self) {
  return self->webChannel();
}

//  void QQuickWebEngineView::setWebChannel(QQmlWebChannel *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickWebEngineView13setWebChannelEP14QQmlWebChannel(
    QQuickWebEngineView *self,
    QQmlWebChannel *a0) {
  self->setWebChannel(a0);
}

//  QWebEngineHistory *QQuickWebEngineView::history() const
extern "C" Q_DECL_EXPORT
QWebEngineHistory *ritual_ZNK19QQuickWebEngineView7historyEv(
    const QQuickWebEngineView *self) {
  return self->history();
}

//  uint QQuickWebEngineView::webChannelWorld() const
extern "C" Q_DECL_EXPORT
uint ritual_ZNK19QQuickWebEngineView15webChannelWorldEv(
    const QQuickWebEngineView *self) {
  return self->webChannelWorld();
}

//  void QQuickWebEngineView::setWebChannelWorld(uint a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickWebEngineView18setWebChannelWorldEj(
    QQuickWebEngineView *self,
    uint a0) {
  self->setWebChannelWorld(a0);
}

//  QQuickWebEngineAction *QQuickWebEngineView::action(WebAction action)
extern "C" Q_DECL_EXPORT
QQuickWebEngineAction *ritual_ZN19QQuickWebEngineView6actionENS_9WebActionE(
    QQuickWebEngineView *self,
    QQuickWebEngineView::WebAction action) {
  return self->action(action);
}

//  void QQuickWebEngineView::acceptAsNewWindow(QWebEngineNewWindowRequest
//      *request)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickWebEngineView17acceptAsNewWindowEP26QWebEngineNewWindowRequest(
    QQuickWebEngineView *self,
    QWebEngineNewWindowRequest *request) {
  self->acceptAsNewWindow(request);
}

//  bool QQuickWebEngineView::isAudioMuted() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK19QQuickWebEngineView12isAudioMutedEv(
    const QQuickWebEngineView *self) {
  return self->isAudioMuted();
}

//  void QQuickWebEngineView::setAudioMuted(bool muted)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickWebEngineView13setAudioMutedEb(
    QQuickWebEngineView *self,
    bool muted) {
  self->setAudioMuted(muted);
}

//  bool QQuickWebEngineView::recentlyAudible() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK19QQuickWebEngineView15recentlyAudibleEv(
    const QQuickWebEngineView *self) {
  return self->recentlyAudible();
}

//  qint64 QQuickWebEngineView::renderProcessPid() const
extern "C" Q_DECL_EXPORT
qint64 ritual_ZNK19QQuickWebEngineView16renderProcessPidEv(
    const QQuickWebEngineView *self) {
  return self->renderProcessPid();
}

//  bool QQuickWebEngineView::activeFocusOnPress() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK19QQuickWebEngineView18activeFocusOnPressEv(
    const QQuickWebEngineView *self) {
  return self->activeFocusOnPress();
}

//  void QQuickWebEngineView::setInspectedView(QQuickWebEngineView *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickWebEngineView16setInspectedViewEPS_(
    QQuickWebEngineView *self,
    QQuickWebEngineView *a0) {
  self->setInspectedView(a0);
}

//  QQuickWebEngineView *QQuickWebEngineView::inspectedView() const
extern "C" Q_DECL_EXPORT
QQuickWebEngineView *ritual_ZNK19QQuickWebEngineView13inspectedViewEv(
    const QQuickWebEngineView *self) {
  return self->inspectedView();
}

//  void QQuickWebEngineView::setDevToolsView(QQuickWebEngineView *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickWebEngineView15setDevToolsViewEPS_(
    QQuickWebEngineView *self,
    QQuickWebEngineView *a0) {
  self->setDevToolsView(a0);
}

//  QQuickWebEngineView *QQuickWebEngineView::devToolsView() const
extern "C" Q_DECL_EXPORT
QQuickWebEngineView *ritual_ZNK19QQuickWebEngineView12devToolsViewEv(
    const QQuickWebEngineView *self) {
  return self->devToolsView();
}

//  QString QQuickWebEngineView::devToolsId()
extern "C" Q_DECL_EXPORT
QString *ritual_ZN19QQuickWebEngineView10devToolsIdEv(
    QQuickWebEngineView *self) {
  return new QString(self->devToolsId());
}

//  LifecycleState QQuickWebEngineView::lifecycleState() const
extern "C" Q_DECL_EXPORT
QQuickWebEngineView::LifecycleState ritual_ZNK19QQuickWebEngineView14lifecycleStateEv(
    const QQuickWebEngineView *self) {
  return self->lifecycleState();
}

//  void QQuickWebEngineView::setLifecycleState(LifecycleState state)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickWebEngineView17setLifecycleStateENS_14LifecycleStateE(
    QQuickWebEngineView *self,
    QQuickWebEngineView::LifecycleState state) {
  self->setLifecycleState(state);
}

//  LifecycleState QQuickWebEngineView::recommendedState() const
extern "C" Q_DECL_EXPORT
QQuickWebEngineView::LifecycleState ritual_ZNK19QQuickWebEngineView16recommendedStateEv(
    const QQuickWebEngineView *self) {
  return self->recommendedState();
}

//  QQmlComponent *QQuickWebEngineView::touchHandleDelegate() const
extern "C" Q_DECL_EXPORT
QQmlComponent *ritual_ZNK19QQuickWebEngineView19touchHandleDelegateEv(
    const QQuickWebEngineView *self) {
  return self->touchHandleDelegate();
}

//  void QQuickWebEngineView::setTouchHandleDelegate(QQmlComponent
//      *delegagte)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickWebEngineView22setTouchHandleDelegateEP13QQmlComponent(
    QQuickWebEngineView *self,
    QQmlComponent *delegagte) {
  self->setTouchHandleDelegate(delegagte);
}

//  QQuickWebEngineFrame QQuickWebEngineView::mainFrame()
extern "C" Q_DECL_EXPORT
QQuickWebEngineFrame *ritual_ZN19QQuickWebEngineView9mainFrameEv(
    QQuickWebEngineView *self) {
  return new QQuickWebEngineFrame(self->mainFrame());
}

//  QQuickWebEngineFrame QQuickWebEngineView::findFrameByName(const QString
//      &name)
extern "C" Q_DECL_EXPORT
QQuickWebEngineFrame *ritual_ZN19QQuickWebEngineView15findFrameByNameERK7QString(
    QQuickWebEngineView *self,
    const QString *name) {
  return new QQuickWebEngineFrame(self->findFrameByName(*name));
}

//  void QQuickWebEngineView::runJavaScript(const QString &script, const
//      std::function<void (const QVariant &)> &resultCallback)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickWebEngineView13runJavaScriptERK7QStringRKSt8functionIFvRK8QVariantEE(
    QQuickWebEngineView *self,
    const QString *script,
    const std::function<void (const QVariant &)> *resultCallback) {
  self->runJavaScript(*script, *resultCallback);
}

//  void QQuickWebEngineView::runJavaScript(const QString &a0, const QJSValue
//      &a1)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickWebEngineView13runJavaScriptERK7QStringRK8QJSValue(
    QQuickWebEngineView *self,
    const QString *a0,
    const QJSValue *a1) {
  self->runJavaScript(*a0, *a1);
}

//  void QQuickWebEngineView::runJavaScript(const QString &a0, quint32
//      worldId, const QJSValue &a2)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickWebEngineView13runJavaScriptERK7QStringjRK8QJSValue(
    QQuickWebEngineView *self,
    const QString *a0,
    quint32 worldId,
    const QJSValue *a2) {
  self->runJavaScript(*a0, worldId, *a2);
}

//  void QQuickWebEngineView::loadHtml(const QString &html, const QUrl
//      &baseUrl)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickWebEngineView8loadHtmlERK7QStringRK4QUrl(
    QQuickWebEngineView *self,
    const QString *html,
    const QUrl *baseUrl) {
  self->loadHtml(*html, *baseUrl);
}

//  void QQuickWebEngineView::goBack()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickWebEngineView6goBackEv(QQuickWebEngineView *self) {
  self->goBack();
}

//  void QQuickWebEngineView::goForward()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickWebEngineView9goForwardEv(QQuickWebEngineView *self) {
  self->goForward();
}

//  void QQuickWebEngineView::goBackOrForward(int index)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickWebEngineView15goBackOrForwardEi(
    QQuickWebEngineView *self,
    int index) {
  self->goBackOrForward(index);
}

//  void QQuickWebEngineView::reload()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickWebEngineView6reloadEv(QQuickWebEngineView *self) {
  self->reload();
}

//  void QQuickWebEngineView::reloadAndBypassCache()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickWebEngineView20reloadAndBypassCacheEv(
    QQuickWebEngineView *self) {
  self->reloadAndBypassCache();
}

//  void QQuickWebEngineView::stop()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickWebEngineView4stopEv(QQuickWebEngineView *self) {
  self->stop();
}

//  void QQuickWebEngineView::findText(const QString &subString, FindFlags
//      options, const QJSValue &callback)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickWebEngineView8findTextERK7QString6QFlagsINS_8FindFlagEERK8QJSValue(
    QQuickWebEngineView *self,
    const QString *subString,
    int options,
    const QJSValue *callback) {
  self->findText(
      *subString,
      QFlags<QQuickWebEngineView::FindFlag>::fromInt(options),
      *callback);
}

//  void QQuickWebEngineView::fullScreenCancelled()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickWebEngineView19fullScreenCancelledEv(
    QQuickWebEngineView *self) {
  self->fullScreenCancelled();
}

#if QT_DEPRECATED_SINCE(6, 8)
//  void QQuickWebEngineView::grantFeaturePermission(const QUrl
//      &securityOrigin, QQuickWebEngineView::Feature a1, bool granted)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickWebEngineView22grantFeaturePermissionERK4QUrlNS_7FeatureEb(
    QQuickWebEngineView *self,
    const QUrl *securityOrigin,
    QQuickWebEngineView::Feature a1,
    bool granted) {
  self->grantFeaturePermission(*securityOrigin, a1, granted);
}
#endif  // QT_DEPRECATED_SINCE(6, 8)

//  void QQuickWebEngineView::setActiveFocusOnPress(bool arg)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickWebEngineView21setActiveFocusOnPressEb(
    QQuickWebEngineView *self,
    bool arg) {
  self->setActiveFocusOnPress(arg);
}

//  void QQuickWebEngineView::triggerWebAction(WebAction action)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickWebEngineView16triggerWebActionENS_9WebActionE(
    QQuickWebEngineView *self,
    QQuickWebEngineView::WebAction action) {
  self->triggerWebAction(action);
}

//  void QQuickWebEngineView::printToPdf(const QString &filePath,
//      PrintedPageSizeId pageSizeId, PrintedPageOrientation orientation)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickWebEngineView10printToPdfERK7QStringNS_17PrintedPageSizeIdENS_22PrintedPageOrientationE(
    QQuickWebEngineView *self,
    const QString *filePath,
    QQuickWebEngineView::PrintedPageSizeId pageSizeId,
    QQuickWebEngineView::PrintedPageOrientation orientation) {
  self->printToPdf(*filePath, pageSizeId, orientation);
}

//  void QQuickWebEngineView::printToPdf(const QJSValue &callback,
//      PrintedPageSizeId pageSizeId, PrintedPageOrientation orientation)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickWebEngineView10printToPdfERK8QJSValueNS_17PrintedPageSizeIdENS_22PrintedPageOrientationE(
    QQuickWebEngineView *self,
    const QJSValue *callback,
    QQuickWebEngineView::PrintedPageSizeId pageSizeId,
    QQuickWebEngineView::PrintedPageOrientation orientation) {
  self->printToPdf(*callback, pageSizeId, orientation);
}

//  void QQuickWebEngineView::replaceMisspelledWord(const QString
//      &replacement)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickWebEngineView21replaceMisspelledWordERK7QString(
    QQuickWebEngineView *self,
    const QString *replacement) {
  self->replaceMisspelledWord(*replacement);
}

//  void QQuickWebEngineView::save(const QString &filePath,
//      QWebEngineDownloadRequest::SavePageFormat format) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK19QQuickWebEngineView4saveERK7QStringN25QWebEngineDownloadRequest14SavePageFormatE(
    const QQuickWebEngineView *self,
    const QString *filePath,
    QWebEngineDownloadRequest::SavePageFormat format) {
  self->save(*filePath, format);
}

//  void QQuickWebEngineView::lazyInitialize()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickWebEngineView14lazyInitializeEv(
    QQuickWebEngineView *self) {
  self->lazyInitialize();
}

//  void QQuickWebEngineView::titleChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickWebEngineView12titleChangedEv(
    QQuickWebEngineView *self) {
  self->titleChanged();
}

//  void QQuickWebEngineView::urlChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickWebEngineView10urlChangedEv(
    QQuickWebEngineView *self) {
  self->urlChanged();
}

//  void QQuickWebEngineView::iconChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickWebEngineView11iconChangedEv(
    QQuickWebEngineView *self) {
  self->iconChanged();
}

//  void QQuickWebEngineView::loadingChanged(const QWebEngineLoadingInfo
//      &loadingInfo)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickWebEngineView14loadingChangedERK21QWebEngineLoadingInfo(
    QQuickWebEngineView *self,
    const QWebEngineLoadingInfo *loadingInfo) {
  self->loadingChanged(*loadingInfo);
}

//  void QQuickWebEngineView::loadProgressChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickWebEngineView19loadProgressChangedEv(
    QQuickWebEngineView *self) {
  self->loadProgressChanged();
}

//  void QQuickWebEngineView::linkHovered(const QUrl &hoveredUrl)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickWebEngineView11linkHoveredERK4QUrl(
    QQuickWebEngineView *self,
    const QUrl *hoveredUrl) {
  self->linkHovered(*hoveredUrl);
}

//  void QQuickWebEngineView::navigationRequested(QWebEngineNavigationRequest
//      *request)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickWebEngineView19navigationRequestedEP27QWebEngineNavigationRequest(
    QQuickWebEngineView *self,
    QWebEngineNavigationRequest *request) {
  self->navigationRequested(request);
}

//  void QQuickWebEngineView::javaScriptConsoleMessage(QQuickWebEngineView::J
//      avaScriptConsoleMessageLevel level, const QString &message, int
//      lineNumber, const QString &sourceID)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickWebEngineView24javaScriptConsoleMessageENS_29JavaScriptConsoleMessageLevelERK7QStringiS3_(
    QQuickWebEngineView *self,
    QQuickWebEngineView::JavaScriptConsoleMessageLevel level,
    const QString *message,
    int lineNumber,
    const QString *sourceID) {
  self->javaScriptConsoleMessage(level, *message, lineNumber, *sourceID);
}

//  void QQuickWebEngineView::certificateError(const
//      QWebEngineCertificateError &error)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickWebEngineView16certificateErrorERK26QWebEngineCertificateError(
    QQuickWebEngineView *self,
    const QWebEngineCertificateError *error) {
  self->certificateError(*error);
}

//  void QQuickWebEngineView::fullScreenRequested(const
//      QWebEngineFullScreenRequest &request)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickWebEngineView19fullScreenRequestedERK27QWebEngineFullScreenRequest(
    QQuickWebEngineView *self,
    const QWebEngineFullScreenRequest *request) {
  self->fullScreenRequested(*request);
}

//  void QQuickWebEngineView::isFullScreenChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickWebEngineView19isFullScreenChangedEv(
    QQuickWebEngineView *self) {
  self->isFullScreenChanged();
}

#if QT_DEPRECATED_SINCE(6, 8)
//  void QQuickWebEngineView::featurePermissionRequested(const QUrl
//      &securityOrigin, QQuickWebEngineView::Feature feature)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickWebEngineView26featurePermissionRequestedERK4QUrlNS_7FeatureE(
    QQuickWebEngineView *self,
    const QUrl *securityOrigin,
    QQuickWebEngineView::Feature feature) {
  self->featurePermissionRequested(*securityOrigin, feature);
}
#endif  // QT_DEPRECATED_SINCE(6, 8)

//  void QQuickWebEngineView::zoomFactorChanged(qreal arg)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickWebEngineView17zoomFactorChangedEd(
    QQuickWebEngineView *self,
    qreal arg) {
  self->zoomFactorChanged(arg);
}

//  void QQuickWebEngineView::profileChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickWebEngineView14profileChangedEv(
    QQuickWebEngineView *self) {
  self->profileChanged();
}

//  void QQuickWebEngineView::webChannelChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickWebEngineView17webChannelChangedEv(
    QQuickWebEngineView *self) {
  self->webChannelChanged();
}

//  void QQuickWebEngineView::activeFocusOnPressChanged(bool a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickWebEngineView25activeFocusOnPressChangedEb(
    QQuickWebEngineView *self,
    bool a0) {
  self->activeFocusOnPressChanged(a0);
}

//  void QQuickWebEngineView::backgroundColorChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickWebEngineView22backgroundColorChangedEv(
    QQuickWebEngineView *self) {
  self->backgroundColorChanged();
}

//  void QQuickWebEngineView::renderProcessTerminated(QQuickWebEngineView::Re
//      nderProcessTerminationStatus terminationStatus, int exitCode)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickWebEngineView23renderProcessTerminatedENS_30RenderProcessTerminationStatusEi(
    QQuickWebEngineView *self,
    QQuickWebEngineView::RenderProcessTerminationStatus terminationStatus,
    int exitCode) {
  self->renderProcessTerminated(terminationStatus, exitCode);
}

//  void QQuickWebEngineView::windowCloseRequested()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickWebEngineView20windowCloseRequestedEv(
    QQuickWebEngineView *self) {
  self->windowCloseRequested();
}

//  void QQuickWebEngineView::contentsSizeChanged(const QSizeF &size)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickWebEngineView19contentsSizeChangedERK6QSizeF(
    QQuickWebEngineView *self,
    const QSizeF *size) {
  self->contentsSizeChanged(*size);
}

//  void QQuickWebEngineView::scrollPositionChanged(const QPointF &position)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickWebEngineView21scrollPositionChangedERK7QPointF(
    QQuickWebEngineView *self,
    const QPointF *position) {
  self->scrollPositionChanged(*position);
}

//  void QQuickWebEngineView::audioMutedChanged(bool muted)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickWebEngineView17audioMutedChangedEb(
    QQuickWebEngineView *self,
    bool muted) {
  self->audioMutedChanged(muted);
}

//  void QQuickWebEngineView::recentlyAudibleChanged(bool recentlyAudible)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickWebEngineView22recentlyAudibleChangedEb(
    QQuickWebEngineView *self,
    bool recentlyAudible) {
  self->recentlyAudibleChanged(recentlyAudible);
}

//  void QQuickWebEngineView::webChannelWorldChanged(uint a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickWebEngineView22webChannelWorldChangedEj(
    QQuickWebEngineView *self,
    uint a0) {
  self->webChannelWorldChanged(a0);
}

//  void
//      QQuickWebEngineView::contextMenuRequested(QWebEngineContextMenuReques
//      t *request)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickWebEngineView20contextMenuRequestedEP28QWebEngineContextMenuRequest(
    QQuickWebEngineView *self,
    QWebEngineContextMenuRequest *request) {
  self->contextMenuRequested(request);
}

//  void QQuickWebEngineView::authenticationDialogRequested(QQuickWebEngineAu
//      thenticationDialogRequest *request)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickWebEngineView29authenticationDialogRequestedEP42QQuickWebEngineAuthenticationDialogRequest(
    QQuickWebEngineView *self,
    QQuickWebEngineAuthenticationDialogRequest *request) {
  self->authenticationDialogRequested(request);
}

//  void QQuickWebEngineView::javaScriptDialogRequested(QQuickWebEngineJavaSc
//      riptDialogRequest *request)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickWebEngineView25javaScriptDialogRequestedEP38QQuickWebEngineJavaScriptDialogRequest(
    QQuickWebEngineView *self,
    QQuickWebEngineJavaScriptDialogRequest *request) {
  self->javaScriptDialogRequested(request);
}

//  void QQuickWebEngineView::colorDialogRequested(QQuickWebEngineColorDialog
//      Request *request)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickWebEngineView20colorDialogRequestedEP33QQuickWebEngineColorDialogRequest(
    QQuickWebEngineView *self,
    QQuickWebEngineColorDialogRequest *request) {
  self->colorDialogRequested(request);
}

//  void
//      QQuickWebEngineView::fileDialogRequested(QQuickWebEngineFileDialogReq
//      uest *request)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickWebEngineView19fileDialogRequestedEP32QQuickWebEngineFileDialogRequest(
    QQuickWebEngineView *self,
    QQuickWebEngineFileDialogRequest *request) {
  self->fileDialogRequested(request);
}

//  void QQuickWebEngineView::pdfPrintingFinished(const QString &filePath,
//      bool success)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickWebEngineView19pdfPrintingFinishedERK7QStringb(
    QQuickWebEngineView *self,
    const QString *filePath,
    bool success) {
  self->pdfPrintingFinished(*filePath, success);
}

#if QT_DEPRECATED_SINCE(6, 5)
//  void QQuickWebEngineView::quotaRequested(const QWebEngineQuotaRequest
//      &request)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickWebEngineView14quotaRequestedERK22QWebEngineQuotaRequest(
    QQuickWebEngineView *self,
    const QWebEngineQuotaRequest *request) {
  self->quotaRequested(*request);
}
#endif  // QT_DEPRECATED_SINCE(6, 5)

//  void QQuickWebEngineView::geometryChangeRequested(const QRect &geometry,
//      const QRect &frameGeometry)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickWebEngineView23geometryChangeRequestedERK5QRectS2_(
    QQuickWebEngineView *self,
    const QRect *geometry,
    const QRect *frameGeometry) {
  self->geometryChangeRequested(*geometry, *frameGeometry);
}

//  void QQuickWebEngineView::inspectedViewChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickWebEngineView20inspectedViewChangedEv(
    QQuickWebEngineView *self) {
  self->inspectedViewChanged();
}

//  void QQuickWebEngineView::devToolsViewChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickWebEngineView19devToolsViewChangedEv(
    QQuickWebEngineView *self) {
  self->devToolsViewChanged();
}

//  void QQuickWebEngineView::registerProtocolHandlerRequested(const
//      QWebEngineRegisterProtocolHandlerRequest &request)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickWebEngineView32registerProtocolHandlerRequestedERK40QWebEngineRegisterProtocolHandlerRequest(
    QQuickWebEngineView *self,
    const QWebEngineRegisterProtocolHandlerRequest *request) {
  self->registerProtocolHandlerRequested(*request);
}

//  void QQuickWebEngineView::printRequested()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickWebEngineView14printRequestedEv(
    QQuickWebEngineView *self) {
  self->printRequested();
}

//  void QQuickWebEngineView::selectClientCertificate(QQuickWebEngineClientCe
//      rtificateSelection *clientCertSelection)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickWebEngineView23selectClientCertificateEP41QQuickWebEngineClientCertificateSelection(
    QQuickWebEngineView *self,
    QQuickWebEngineClientCertificateSelection *clientCertSelection) {
  self->selectClientCertificate(clientCertSelection);
}

//  void QQuickWebEngineView::tooltipRequested(QQuickWebEngineTooltipRequest
//      *request)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickWebEngineView16tooltipRequestedEP29QQuickWebEngineTooltipRequest(
    QQuickWebEngineView *self,
    QQuickWebEngineTooltipRequest *request) {
  self->tooltipRequested(request);
}

//  void QQuickWebEngineView::lifecycleStateChanged(QQuickWebEngineView::Life
//      cycleState state)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickWebEngineView21lifecycleStateChangedENS_14LifecycleStateE(
    QQuickWebEngineView *self,
    QQuickWebEngineView::LifecycleState state) {
  self->lifecycleStateChanged(state);
}

//  void QQuickWebEngineView::recommendedStateChanged(QQuickWebEngineView::Li
//      fecycleState state)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickWebEngineView23recommendedStateChangedENS_14LifecycleStateE(
    QQuickWebEngineView *self,
    QQuickWebEngineView::LifecycleState state) {
  self->recommendedStateChanged(state);
}

//  void QQuickWebEngineView::findTextFinished(const QWebEngineFindTextResult
//      &result)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickWebEngineView16findTextFinishedERK24QWebEngineFindTextResult(
    QQuickWebEngineView *self,
    const QWebEngineFindTextResult *result) {
  self->findTextFinished(*result);
}

//  void QQuickWebEngineView::renderProcessPidChanged(qint64 pid)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickWebEngineView23renderProcessPidChangedEx(
    QQuickWebEngineView *self,
    qint64 pid) {
  self->renderProcessPidChanged(pid);
}

//  void QQuickWebEngineView::canGoBackChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickWebEngineView16canGoBackChangedEv(
    QQuickWebEngineView *self) {
  self->canGoBackChanged();
}

//  void QQuickWebEngineView::canGoForwardChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickWebEngineView19canGoForwardChangedEv(
    QQuickWebEngineView *self) {
  self->canGoForwardChanged();
}

//  void
//      QQuickWebEngineView::newWindowRequested(QQuickWebEngineNewWindowReque
//      st *request)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickWebEngineView18newWindowRequestedEP31QQuickWebEngineNewWindowRequest(
    QQuickWebEngineView *self,
    QQuickWebEngineNewWindowRequest *request) {
  self->newWindowRequested(request);
}

//  void QQuickWebEngineView::touchSelectionMenuRequested(QQuickWebEngineTouc
//      hSelectionMenuRequest *request)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickWebEngineView27touchSelectionMenuRequestedEP40QQuickWebEngineTouchSelectionMenuRequest(
    QQuickWebEngineView *self,
    QQuickWebEngineTouchSelectionMenuRequest *request) {
  self->touchSelectionMenuRequested(request);
}

//  void QQuickWebEngineView::touchHandleDelegateChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickWebEngineView26touchHandleDelegateChangedEv(
    QQuickWebEngineView *self) {
  self->touchHandleDelegateChanged();
}

//  void QQuickWebEngineView::fileSystemAccessRequested(const
//      QWebEngineFileSystemAccessRequest &request)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickWebEngineView25fileSystemAccessRequestedERK33QWebEngineFileSystemAccessRequest(
    QQuickWebEngineView *self,
    const QWebEngineFileSystemAccessRequest *request) {
  self->fileSystemAccessRequested(*request);
}

//  void QQuickWebEngineView::webAuthUxRequested(QWebEngineWebAuthUxRequest
//      *request)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickWebEngineView18webAuthUxRequestedEP26QWebEngineWebAuthUxRequest(
    QQuickWebEngineView *self,
    QWebEngineWebAuthUxRequest *request) {
  self->webAuthUxRequested(request);
}

//  void QQuickWebEngineView::desktopMediaRequested(const
//      QWebEngineDesktopMediaRequest &request)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickWebEngineView21desktopMediaRequestedERK29QWebEngineDesktopMediaRequest(
    QQuickWebEngineView *self,
    const QWebEngineDesktopMediaRequest *request) {
  self->desktopMediaRequested(*request);
}

//  void QQuickWebEngineView::printRequestedByFrame(QQuickWebEngineFrame
//      frame)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickWebEngineView21printRequestedByFrameE20QQuickWebEngineFrame(
    QQuickWebEngineView *self,
    const QQuickWebEngineFrame *frame) {
  self->printRequestedByFrame(*frame);
}

//  void QQuickWebEngineView::permissionRequested(QWebEnginePermission
//      permissionRequest)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickWebEngineView19permissionRequestedE20QWebEnginePermission(
    QQuickWebEngineView *self,
    const QWebEnginePermission *permissionRequest) {
  self->permissionRequested(*permissionRequest);
}

//  void QQuickWebEngineView::geometryChange(const QRectF &newGeometry, const
//      QRectF &oldGeometry)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickWebEngineView14geometryChangeERK6QRectFS2_(
    QQuickWebEngineView *self,
    const QRectF *newGeometry,
    const QRectF *oldGeometry) {
  self->geometryChange(*newGeometry, *oldGeometry);
}

//  void QQuickWebEngineView::itemChange(ItemChange a0, const ItemChangeData
//      &a1)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickWebEngineView10itemChangeEN10QQuickItem10ItemChangeERKNS0_14ItemChangeDataE(
    QQuickWebEngineView *self,
    QQuickItem::ItemChange a0,
    const QQuickItem::ItemChangeData *a1) {
  self->itemChange(a0, *a1);
}

#if QT_CONFIG(draganddrop)
//  void QQuickWebEngineView::dragEnterEvent(QDragEnterEvent *e)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickWebEngineView14dragEnterEventEP15QDragEnterEvent(
    QQuickWebEngineView *self,
    QDragEnterEvent *e) {
  self->dragEnterEvent(e);
}
#endif  // QT_CONFIG(draganddrop)

#if QT_CONFIG(draganddrop)
//  void QQuickWebEngineView::dragLeaveEvent(QDragLeaveEvent *e)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickWebEngineView14dragLeaveEventEP15QDragLeaveEvent(
    QQuickWebEngineView *self,
    QDragLeaveEvent *e) {
  self->dragLeaveEvent(e);
}
#endif  // QT_CONFIG(draganddrop)

#if QT_CONFIG(draganddrop)
//  void QQuickWebEngineView::dragMoveEvent(QDragMoveEvent *e)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickWebEngineView13dragMoveEventEP14QDragMoveEvent(
    QQuickWebEngineView *self,
    QDragMoveEvent *e) {
  self->dragMoveEvent(e);
}
#endif  // QT_CONFIG(draganddrop)

#if QT_CONFIG(draganddrop)
//  void QQuickWebEngineView::dropEvent(QDropEvent *e)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickWebEngineView9dropEventEP10QDropEvent(
    QQuickWebEngineView *self,
    QDropEvent *e) {
  self->dropEvent(e);
}
#endif  // QT_CONFIG(draganddrop)

//  QQuickWebEngineViewPrivate *QQuickWebEngineView::d_func()
extern "C" Q_DECL_EXPORT
QQuickWebEngineViewPrivate *ritual_ZN19QQuickWebEngineView6d_funcEv(
    QQuickWebEngineView *self) {
  return self->d_func();
}

//  const QQuickWebEngineViewPrivate *QQuickWebEngineView::d_func() const
extern "C" Q_DECL_EXPORT
const QQuickWebEngineViewPrivate *ritual_ZNK19QQuickWebEngineView6d_funcEv(
    const QQuickWebEngineView *self) {
  return self->d_func();
}

//  a Python function taken by a CuteQQuickWebEngineView, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQuickWebEngineView(
    QQuickWebEngineView *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQuickWebEngineView *>(self)->take(key, call);
}

//  void QQuickWebEngineView::componentComplete()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QQuickWebEngineView17componentCompleteEv(
    QQuickWebEngineView *self) {
  self->QQuickWebEngineView::componentComplete();
}

//  void QQuickWebEngineView::geometryChange(const QRectF &newGeometry, const
//      QRectF &oldGeometry)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QQuickWebEngineView14geometryChangeERK6QRectFS2_(
    QQuickWebEngineView *self,
    const QRectF *newGeometry,
    const QRectF *oldGeometry) {
  static_cast<OwnQQuickWebEngineView *>(self)->OwnQQuickWebEngineView::geometryChange(
      *newGeometry,
      *oldGeometry);
}

//  void QQuickWebEngineView::itemChange(ItemChange a0, const ItemChangeData
//      &a1)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QQuickWebEngineView10itemChangeEN10QQuickItem10ItemChangeERKNS0_14ItemChangeDataE(
    QQuickWebEngineView *self,
    QQuickItem::ItemChange a0,
    const QQuickItem::ItemChangeData *a1) {
  static_cast<OwnQQuickWebEngineView *>(self)->OwnQQuickWebEngineView::itemChange(
      a0,
      *a1);
}

#if QT_CONFIG(draganddrop)
//  void QQuickWebEngineView::dragEnterEvent(QDragEnterEvent *e)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QQuickWebEngineView14dragEnterEventEP15QDragEnterEvent(
    QQuickWebEngineView *self,
    QDragEnterEvent *e) {
  static_cast<OwnQQuickWebEngineView *>(self)->OwnQQuickWebEngineView::dragEnterEvent(
      e);
}
#endif  // QT_CONFIG(draganddrop)

#if QT_CONFIG(draganddrop)
//  void QQuickWebEngineView::dragLeaveEvent(QDragLeaveEvent *e)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QQuickWebEngineView14dragLeaveEventEP15QDragLeaveEvent(
    QQuickWebEngineView *self,
    QDragLeaveEvent *e) {
  static_cast<OwnQQuickWebEngineView *>(self)->OwnQQuickWebEngineView::dragLeaveEvent(
      e);
}
#endif  // QT_CONFIG(draganddrop)

#if QT_CONFIG(draganddrop)
//  void QQuickWebEngineView::dragMoveEvent(QDragMoveEvent *e)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QQuickWebEngineView13dragMoveEventEP14QDragMoveEvent(
    QQuickWebEngineView *self,
    QDragMoveEvent *e) {
  static_cast<OwnQQuickWebEngineView *>(self)->OwnQQuickWebEngineView::dragMoveEvent(
      e);
}
#endif  // QT_CONFIG(draganddrop)

#if QT_CONFIG(draganddrop)
//  void QQuickWebEngineView::dropEvent(QDropEvent *e)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QQuickWebEngineView9dropEventEP10QDropEvent(
    QQuickWebEngineView *self,
    QDropEvent *e) {
  static_cast<OwnQQuickWebEngineView *>(self)->OwnQQuickWebEngineView::dropEvent(
      e);
}
#endif  // QT_CONFIG(draganddrop)
