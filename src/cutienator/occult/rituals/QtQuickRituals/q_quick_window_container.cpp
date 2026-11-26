//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/6.12.0/QtQuick/private/qquickwindowcontainer_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtGui/qtguiglobal.h>
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qquickwindowcontainer_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qrect.h>
#include <QtQuick/qquickitem.h>
#include <QtCore/qpoint.h>
#include <QtCore/qvariant.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  Only a class built on QQuickWindowContainer may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQQuickWindowContainer : QQuickWindowContainer {
  using QQuickWindowContainer::classBegin;
  using QQuickWindowContainer::componentComplete;
  using QQuickWindowContainer::geometryChange;
  using QQuickWindowContainer::itemChange;
  using QQuickWindowContainer::updatePolish;
  using QQuickWindowContainer::eventFilter;
  using QQuickWindowContainer::focusInEvent;
  using QQuickWindowContainer::clipRect;
  using QQuickWindowContainer::releaseResources;
};

//  A QQuickWindowContainer that Python can take functions over in. Every QQuickWindowContainer
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQQuickWindowContainerCall0)(const void *, int *);
typedef void (*CuteQQuickWindowContainerCall1)(const void *, int *);
typedef void (*CuteQQuickWindowContainerCall2)(const void *, const QRectF *, const QRectF *, int *);
typedef void (*CuteQQuickWindowContainerCall3)(const void *, int, const QQuickItem::ItemChangeData *, int *);
typedef void (*CuteQQuickWindowContainerCall4)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickWindowContainerCall5)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickWindowContainerCall6)(const void *, QFocusEvent *, int *);
typedef const QRectF * (*CuteQQuickWindowContainerCall7)(const void *, int *);
typedef void (*CuteQQuickWindowContainerCall8)(const void *, int *);
typedef const QRectF * (*CuteQQuickWindowContainerCall9)(const void *, int *);
typedef bool (*CuteQQuickWindowContainerCall10)(const void *, const QPointF *, int *);
#if QT_CONFIG(im)
typedef const QVariant * (*CuteQQuickWindowContainerCall11)(const void *, int, int *);
#endif  // QT_CONFIG(im)
typedef bool (*CuteQQuickWindowContainerCall12)(const void *, int *);
typedef void * (*CuteQQuickWindowContainerCall13)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickWindowContainerCall14)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickWindowContainerCall15)(const void *, QKeyEvent *, int *);
typedef void (*CuteQQuickWindowContainerCall16)(const void *, QKeyEvent *, int *);
#if QT_CONFIG(im)
typedef void (*CuteQQuickWindowContainerCall17)(const void *, QInputMethodEvent *, int *);
#endif  // QT_CONFIG(im)
typedef void (*CuteQQuickWindowContainerCall18)(const void *, QFocusEvent *, int *);
typedef void (*CuteQQuickWindowContainerCall19)(const void *, QMouseEvent *, int *);
typedef void (*CuteQQuickWindowContainerCall20)(const void *, QMouseEvent *, int *);
typedef void (*CuteQQuickWindowContainerCall21)(const void *, QMouseEvent *, int *);
typedef void (*CuteQQuickWindowContainerCall22)(const void *, QMouseEvent *, int *);
typedef void (*CuteQQuickWindowContainerCall23)(const void *, int *);
typedef void (*CuteQQuickWindowContainerCall24)(const void *, int *);
#if QT_CONFIG(wheelevent)
typedef void (*CuteQQuickWindowContainerCall25)(const void *, QWheelEvent *, int *);
#endif  // QT_CONFIG(wheelevent)
typedef void (*CuteQQuickWindowContainerCall26)(const void *, QTouchEvent *, int *);
typedef void (*CuteQQuickWindowContainerCall27)(const void *, QHoverEvent *, int *);
typedef void (*CuteQQuickWindowContainerCall28)(const void *, QHoverEvent *, int *);
typedef void (*CuteQQuickWindowContainerCall29)(const void *, QHoverEvent *, int *);
#if QT_CONFIG(quick_draganddrop)
typedef void (*CuteQQuickWindowContainerCall30)(const void *, QDragEnterEvent *, int *);
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
typedef void (*CuteQQuickWindowContainerCall31)(const void *, QDragMoveEvent *, int *);
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
typedef void (*CuteQQuickWindowContainerCall32)(const void *, QDragLeaveEvent *, int *);
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
typedef void (*CuteQQuickWindowContainerCall33)(const void *, QDropEvent *, int *);
#endif  // QT_CONFIG(quick_draganddrop)
typedef bool (*CuteQQuickWindowContainerCall34)(const void *, QQuickItem *, QEvent *, int *);
typedef void * (*CuteQQuickWindowContainerCall35)(const void *, QSGNode *, QQuickItem::UpdatePaintNodeData *, int *);
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickWindowContainerCall36)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickWindowContainerCall37)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickWindowContainerCall38)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickWindowContainerCall39)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickWindowContainerCall40)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQQuickWindowContainer : public QQuickWindowContainer {
public:
  using QQuickWindowContainer::QQuickWindowContainer;
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

  //  void QQuickWindowContainer::classBegin()
  void classBegin() override {
    if (taken[0]) {
      int handled = 0;
      CuteQQuickWindowContainerCall0 call = reinterpret_cast<CuteQQuickWindowContainerCall0>(taken[0]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickWindowContainer::classBegin();
  }

  //  void QQuickWindowContainer::componentComplete()
  void componentComplete() override {
    if (taken[1]) {
      int handled = 0;
      CuteQQuickWindowContainerCall1 call = reinterpret_cast<CuteQQuickWindowContainerCall1>(taken[1]);
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
      CuteQQuickWindowContainerCall2 call = reinterpret_cast<CuteQQuickWindowContainerCall2>(taken[2]);
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
      CuteQQuickWindowContainerCall3 call = reinterpret_cast<CuteQQuickWindowContainerCall3>(taken[3]);
      call(this, static_cast<int>(a0), &a1, &handled);
      if (handled) return;
    }
    QQuickWindowContainer::itemChange(a0, a1);
  }

  //  void QQuickWindowContainer::updatePolish()
  void updatePolish() override {
    if (taken[4]) {
      int handled = 0;
      CuteQQuickWindowContainerCall4 call = reinterpret_cast<CuteQQuickWindowContainerCall4>(taken[4]);
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
      CuteQQuickWindowContainerCall5 call = reinterpret_cast<CuteQQuickWindowContainerCall5>(taken[5]);
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
      CuteQQuickWindowContainerCall6 call = reinterpret_cast<CuteQQuickWindowContainerCall6>(taken[6]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickWindowContainer::focusInEvent(a0);
  }

  //  QRectF QQuickWindowContainer::clipRect() const
  QRectF clipRect() const override {
    if (taken[7]) {
      int handled = 0;
      CuteQQuickWindowContainerCall7 call = reinterpret_cast<CuteQQuickWindowContainerCall7>(taken[7]);
      const QRectF * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QQuickWindowContainer::clipRect();
  }

  //  void QQuickWindowContainer::releaseResources()
  void releaseResources() override {
    if (taken[8]) {
      int handled = 0;
      CuteQQuickWindowContainerCall8 call = reinterpret_cast<CuteQQuickWindowContainerCall8>(taken[8]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickWindowContainer::releaseResources();
  }

  //  QRectF QQuickItem::boundingRect() const
  QRectF boundingRect() const override {
    if (taken[9]) {
      int handled = 0;
      CuteQQuickWindowContainerCall9 call = reinterpret_cast<CuteQQuickWindowContainerCall9>(taken[9]);
      const QRectF * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QQuickItem::boundingRect();
  }

  //  bool QQuickItem::contains(const QPointF &point) const
  bool contains(const QPointF &point) const override {
    if (taken[10]) {
      int handled = 0;
      CuteQQuickWindowContainerCall10 call = reinterpret_cast<CuteQQuickWindowContainerCall10>(taken[10]);
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
      CuteQQuickWindowContainerCall11 call = reinterpret_cast<CuteQQuickWindowContainerCall11>(taken[11]);
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
      CuteQQuickWindowContainerCall12 call = reinterpret_cast<CuteQQuickWindowContainerCall12>(taken[12]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QQuickItem::isTextureProvider();
  }

  //  QSGTextureProvider *QQuickItem::textureProvider() const
  QSGTextureProvider *textureProvider() const override {
    if (taken[13]) {
      int handled = 0;
      CuteQQuickWindowContainerCall13 call = reinterpret_cast<CuteQQuickWindowContainerCall13>(taken[13]);
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
      CuteQQuickWindowContainerCall14 call = reinterpret_cast<CuteQQuickWindowContainerCall14>(taken[14]);
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
      CuteQQuickWindowContainerCall15 call = reinterpret_cast<CuteQQuickWindowContainerCall15>(taken[15]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::keyPressEvent(event);
  }

  //  void QQuickItem::keyReleaseEvent(QKeyEvent *event)
  void keyReleaseEvent(QKeyEvent *event) override {
    if (taken[16]) {
      int handled = 0;
      CuteQQuickWindowContainerCall16 call = reinterpret_cast<CuteQQuickWindowContainerCall16>(taken[16]);
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
      CuteQQuickWindowContainerCall17 call = reinterpret_cast<CuteQQuickWindowContainerCall17>(taken[17]);
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
      CuteQQuickWindowContainerCall18 call = reinterpret_cast<CuteQQuickWindowContainerCall18>(taken[18]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItem::focusOutEvent(a0);
  }

  //  void QQuickItem::mousePressEvent(QMouseEvent *event)
  void mousePressEvent(QMouseEvent *event) override {
    if (taken[19]) {
      int handled = 0;
      CuteQQuickWindowContainerCall19 call = reinterpret_cast<CuteQQuickWindowContainerCall19>(taken[19]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::mousePressEvent(event);
  }

  //  void QQuickItem::mouseMoveEvent(QMouseEvent *event)
  void mouseMoveEvent(QMouseEvent *event) override {
    if (taken[20]) {
      int handled = 0;
      CuteQQuickWindowContainerCall20 call = reinterpret_cast<CuteQQuickWindowContainerCall20>(taken[20]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::mouseMoveEvent(event);
  }

  //  void QQuickItem::mouseReleaseEvent(QMouseEvent *event)
  void mouseReleaseEvent(QMouseEvent *event) override {
    if (taken[21]) {
      int handled = 0;
      CuteQQuickWindowContainerCall21 call = reinterpret_cast<CuteQQuickWindowContainerCall21>(taken[21]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::mouseReleaseEvent(event);
  }

  //  void QQuickItem::mouseDoubleClickEvent(QMouseEvent *event)
  void mouseDoubleClickEvent(QMouseEvent *event) override {
    if (taken[22]) {
      int handled = 0;
      CuteQQuickWindowContainerCall22 call = reinterpret_cast<CuteQQuickWindowContainerCall22>(taken[22]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::mouseDoubleClickEvent(event);
  }

  //  void QQuickItem::mouseUngrabEvent()
  void mouseUngrabEvent() override {
    if (taken[23]) {
      int handled = 0;
      CuteQQuickWindowContainerCall23 call = reinterpret_cast<CuteQQuickWindowContainerCall23>(taken[23]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItem::mouseUngrabEvent();
  }

  //  void QQuickItem::touchUngrabEvent()
  void touchUngrabEvent() override {
    if (taken[24]) {
      int handled = 0;
      CuteQQuickWindowContainerCall24 call = reinterpret_cast<CuteQQuickWindowContainerCall24>(taken[24]);
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
      CuteQQuickWindowContainerCall25 call = reinterpret_cast<CuteQQuickWindowContainerCall25>(taken[25]);
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
      CuteQQuickWindowContainerCall26 call = reinterpret_cast<CuteQQuickWindowContainerCall26>(taken[26]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::touchEvent(event);
  }

  //  void QQuickItem::hoverEnterEvent(QHoverEvent *event)
  void hoverEnterEvent(QHoverEvent *event) override {
    if (taken[27]) {
      int handled = 0;
      CuteQQuickWindowContainerCall27 call = reinterpret_cast<CuteQQuickWindowContainerCall27>(taken[27]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::hoverEnterEvent(event);
  }

  //  void QQuickItem::hoverMoveEvent(QHoverEvent *event)
  void hoverMoveEvent(QHoverEvent *event) override {
    if (taken[28]) {
      int handled = 0;
      CuteQQuickWindowContainerCall28 call = reinterpret_cast<CuteQQuickWindowContainerCall28>(taken[28]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::hoverMoveEvent(event);
  }

  //  void QQuickItem::hoverLeaveEvent(QHoverEvent *event)
  void hoverLeaveEvent(QHoverEvent *event) override {
    if (taken[29]) {
      int handled = 0;
      CuteQQuickWindowContainerCall29 call = reinterpret_cast<CuteQQuickWindowContainerCall29>(taken[29]);
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
      CuteQQuickWindowContainerCall30 call = reinterpret_cast<CuteQQuickWindowContainerCall30>(taken[30]);
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
      CuteQQuickWindowContainerCall31 call = reinterpret_cast<CuteQQuickWindowContainerCall31>(taken[31]);
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
      CuteQQuickWindowContainerCall32 call = reinterpret_cast<CuteQQuickWindowContainerCall32>(taken[32]);
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
      CuteQQuickWindowContainerCall33 call = reinterpret_cast<CuteQQuickWindowContainerCall33>(taken[33]);
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
      CuteQQuickWindowContainerCall34 call = reinterpret_cast<CuteQQuickWindowContainerCall34>(taken[34]);
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
      CuteQQuickWindowContainerCall35 call = reinterpret_cast<CuteQQuickWindowContainerCall35>(taken[35]);
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
      CuteQQuickWindowContainerCall36 call = reinterpret_cast<CuteQQuickWindowContainerCall36>(taken[36]);
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
      CuteQQuickWindowContainerCall37 call = reinterpret_cast<CuteQQuickWindowContainerCall37>(taken[37]);
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
      CuteQQuickWindowContainerCall38 call = reinterpret_cast<CuteQQuickWindowContainerCall38>(taken[38]);
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
      CuteQQuickWindowContainerCall39 call = reinterpret_cast<CuteQQuickWindowContainerCall39>(taken[39]);
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
      CuteQQuickWindowContainerCall40 call = reinterpret_cast<CuteQQuickWindowContainerCall40>(taken[40]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QQuickWindowContainer::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK21QQuickWindowContainer10metaObjectEv(
    const QQuickWindowContainer *self) {
  return self->metaObject();
}

//  void *QQuickWindowContainer::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN21QQuickWindowContainer11qt_metacastEPKc(
    QQuickWindowContainer *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QQuickWindowContainer::qt_metacall(QMetaObject::Call a0, int a1, void
//      **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN21QQuickWindowContainer11qt_metacallEN11QMetaObject4CallEiPPv(
    QQuickWindowContainer *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QQuickWindowContainer::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN21QQuickWindowContainer2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuickWindowContainer::tr(s, c, n));
}

//  QQuickWindowContainer::QQuickWindowContainer(QQuickItem *parent,
//      ContainerMode containerMode)
extern "C" Q_DECL_EXPORT
QQuickWindowContainer *ritual_ZN21QQuickWindowContainerC1EP10QQuickItemNS_13ContainerModeE(
    QQuickItem *parent,
    QQuickWindowContainer::ContainerMode containerMode) {
  return new CuteQQuickWindowContainer(parent, containerMode);
}

//  QQuickWindowContainer::~QQuickWindowContainer()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuickWindowContainerD1Ev(QQuickWindowContainer *self) {
  delete self;
}

//  QWindow *QQuickWindowContainer::containedWindow() const
extern "C" Q_DECL_EXPORT
QWindow *ritual_ZNK21QQuickWindowContainer15containedWindowEv(
    const QQuickWindowContainer *self) {
  return self->containedWindow();
}

//  void QQuickWindowContainer::setContainedWindow(QWindow *window)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuickWindowContainer18setContainedWindowEP7QWindow(
    QQuickWindowContainer *self,
    QWindow *window) {
  self->setContainedWindow(window);
}

//  void QQuickWindowContainer::containedWindowChanged(QWindow *window)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuickWindowContainer22containedWindowChangedEP7QWindow(
    QQuickWindowContainer *self,
    QWindow *window) {
  self->containedWindowChanged(window);
}

//  void QQuickWindowContainer::classBegin()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuickWindowContainer10classBeginEv(
    QQuickWindowContainer *self) {
  self->classBegin();
}

//  void QQuickWindowContainer::componentComplete()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuickWindowContainer17componentCompleteEv(
    QQuickWindowContainer *self) {
  self->componentComplete();
}

//  void QQuickWindowContainer::geometryChange(const QRectF &newGeometry,
//      const QRectF &oldGeometry)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuickWindowContainer14geometryChangeERK6QRectFS2_(
    QQuickWindowContainer *self,
    const QRectF *newGeometry,
    const QRectF *oldGeometry) {
  self->geometryChange(*newGeometry, *oldGeometry);
}

//  void QQuickWindowContainer::itemChange(QQuickItem::ItemChange a0, const
//      QQuickItem::ItemChangeData &a1)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuickWindowContainer10itemChangeEN10QQuickItem10ItemChangeERKNS0_14ItemChangeDataE(
    QQuickWindowContainer *self,
    QQuickItem::ItemChange a0,
    const QQuickItem::ItemChangeData *a1) {
  self->itemChange(a0, *a1);
}

//  void QQuickWindowContainer::updatePolish()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuickWindowContainer12updatePolishEv(
    QQuickWindowContainer *self) {
  self->updatePolish();
}

//  bool QQuickWindowContainer::eventFilter(QObject *object, QEvent *event)
extern "C" Q_DECL_EXPORT
bool ritual_ZN21QQuickWindowContainer11eventFilterEP7QObjectP6QEvent(
    QQuickWindowContainer *self,
    QObject *object,
    QEvent *event) {
  return self->eventFilter(object, event);
}

//  void QQuickWindowContainer::focusInEvent(QFocusEvent *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuickWindowContainer12focusInEventEP11QFocusEvent(
    QQuickWindowContainer *self,
    QFocusEvent *a0) {
  self->focusInEvent(a0);
}

//  QRectF QQuickWindowContainer::clipRect() const
extern "C" Q_DECL_EXPORT
QRectF *ritual_ZNK21QQuickWindowContainer8clipRectEv(
    const QQuickWindowContainer *self) {
  return new QRectF(self->clipRect());
}

//  void QQuickWindowContainer::releaseResources()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuickWindowContainer16releaseResourcesEv(
    QQuickWindowContainer *self) {
  self->releaseResources();
}

//  QQuickWindowContainerPrivate *QQuickWindowContainer::d_func()
extern "C" Q_DECL_EXPORT
QQuickWindowContainerPrivate *ritual_ZN21QQuickWindowContainer6d_funcEv(
    QQuickWindowContainer *self) {
  return self->d_func();
}

//  const QQuickWindowContainerPrivate *QQuickWindowContainer::d_func() const
extern "C" Q_DECL_EXPORT
const QQuickWindowContainerPrivate *ritual_ZNK21QQuickWindowContainer6d_funcEv(
    const QQuickWindowContainer *self) {
  return self->d_func();
}

//  void QQuickWindowContainer::initializeContainedWindow()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuickWindowContainer25initializeContainedWindowEv(
    QQuickWindowContainer *self) {
  self->initializeContainedWindow();
}

//  void QQuickWindowContainer::windowUpdated()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuickWindowContainer13windowUpdatedEv(
    QQuickWindowContainer *self) {
  self->windowUpdated();
}

//  void QQuickWindowContainer::syncWindowToItem()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuickWindowContainer16syncWindowToItemEv(
    QQuickWindowContainer *self) {
  self->syncWindowToItem();
}

//  void QQuickWindowContainer::parentWindowChanged(QQuickWindow *window)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuickWindowContainer19parentWindowChangedEP12QQuickWindow(
    QQuickWindowContainer *self,
    QQuickWindow *window) {
  self->parentWindowChanged(window);
}

//  void QQuickWindowContainer::windowDestroyed()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuickWindowContainer15windowDestroyedEv(
    QQuickWindowContainer *self) {
  self->windowDestroyed();
}

//  a Python function taken by a CuteQQuickWindowContainer, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQuickWindowContainer(
    QQuickWindowContainer *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQuickWindowContainer *>(self)->take(key, call);
}

//  void QQuickWindowContainer::classBegin()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN21QQuickWindowContainer10classBeginEv(
    QQuickWindowContainer *self) {
  static_cast<OwnQQuickWindowContainer *>(self)->OwnQQuickWindowContainer::classBegin();
}

//  void QQuickWindowContainer::componentComplete()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN21QQuickWindowContainer17componentCompleteEv(
    QQuickWindowContainer *self) {
  static_cast<OwnQQuickWindowContainer *>(self)->OwnQQuickWindowContainer::componentComplete();
}

//  void QQuickWindowContainer::geometryChange(const QRectF &newGeometry,
//      const QRectF &oldGeometry)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN21QQuickWindowContainer14geometryChangeERK6QRectFS2_(
    QQuickWindowContainer *self,
    const QRectF *newGeometry,
    const QRectF *oldGeometry) {
  static_cast<OwnQQuickWindowContainer *>(self)->OwnQQuickWindowContainer::geometryChange(
      *newGeometry,
      *oldGeometry);
}

//  void QQuickWindowContainer::itemChange(QQuickItem::ItemChange a0, const
//      QQuickItem::ItemChangeData &a1)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN21QQuickWindowContainer10itemChangeEN10QQuickItem10ItemChangeERKNS0_14ItemChangeDataE(
    QQuickWindowContainer *self,
    QQuickItem::ItemChange a0,
    const QQuickItem::ItemChangeData *a1) {
  static_cast<OwnQQuickWindowContainer *>(self)->OwnQQuickWindowContainer::itemChange(
      a0,
      *a1);
}

//  void QQuickWindowContainer::updatePolish()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN21QQuickWindowContainer12updatePolishEv(
    QQuickWindowContainer *self) {
  static_cast<OwnQQuickWindowContainer *>(self)->OwnQQuickWindowContainer::updatePolish();
}

//  bool QQuickWindowContainer::eventFilter(QObject *object, QEvent *event)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN21QQuickWindowContainer11eventFilterEP7QObjectP6QEvent(
    QQuickWindowContainer *self,
    QObject *object,
    QEvent *event) {
  return static_cast<OwnQQuickWindowContainer *>(self)->OwnQQuickWindowContainer::eventFilter(
      object,
      event);
}

//  void QQuickWindowContainer::focusInEvent(QFocusEvent *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN21QQuickWindowContainer12focusInEventEP11QFocusEvent(
    QQuickWindowContainer *self,
    QFocusEvent *a0) {
  static_cast<OwnQQuickWindowContainer *>(self)->OwnQQuickWindowContainer::focusInEvent(
      a0);
}

//  QRectF QQuickWindowContainer::clipRect() const
extern "C" Q_DECL_EXPORT
QRectF *ritual_own_ZNK21QQuickWindowContainer8clipRectEv(
    const QQuickWindowContainer *self) {
  return new QRectF(
      static_cast<const OwnQQuickWindowContainer *>(self)->OwnQQuickWindowContainer::clipRect());
}

//  void QQuickWindowContainer::releaseResources()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN21QQuickWindowContainer16releaseResourcesEv(
    QQuickWindowContainer *self) {
  static_cast<OwnQQuickWindowContainer *>(self)->OwnQQuickWindowContainer::releaseResources();
}
