//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/6.12.0/QtQuick/private/qquickloader_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtGui/qtguiglobal.h>
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qquickloader_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qurl.h>
#include <QtQml/QtQml>
#include <QtQml/qjsvalue.h>
#include <QtCore/qrect.h>
#include <QtQuick/qquickitem.h>
#include <QtCore/qpoint.h>
#include <QtCore/qvariant.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  Only a class built on QQuickLoader may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQQuickLoader : QQuickLoader {
  using QQuickLoader::geometryChange;
  using QQuickLoader::componentComplete;
  using QQuickLoader::itemChange;
};

//  A QQuickLoader that Python can take functions over in. Every QQuickLoader
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQQuickLoaderCall0)(const void *, const QRectF *, const QRectF *, int *);
typedef void (*CuteQQuickLoaderCall1)(const void *, int *);
typedef void (*CuteQQuickLoaderCall2)(const void *, int, const QQuickItem::ItemChangeData *, int *);
typedef const QRectF * (*CuteQQuickLoaderCall3)(const void *, int *);
typedef const QRectF * (*CuteQQuickLoaderCall4)(const void *, int *);
typedef bool (*CuteQQuickLoaderCall5)(const void *, const QPointF *, int *);
#if QT_CONFIG(im)
typedef const QVariant * (*CuteQQuickLoaderCall6)(const void *, int, int *);
#endif  // QT_CONFIG(im)
typedef bool (*CuteQQuickLoaderCall7)(const void *, int *);
typedef void * (*CuteQQuickLoaderCall8)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickLoaderCall9)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickLoaderCall10)(const void *, int *);
typedef void (*CuteQQuickLoaderCall11)(const void *, QKeyEvent *, int *);
typedef void (*CuteQQuickLoaderCall12)(const void *, QKeyEvent *, int *);
#if QT_CONFIG(im)
typedef void (*CuteQQuickLoaderCall13)(const void *, QInputMethodEvent *, int *);
#endif  // QT_CONFIG(im)
typedef void (*CuteQQuickLoaderCall14)(const void *, QFocusEvent *, int *);
typedef void (*CuteQQuickLoaderCall15)(const void *, QFocusEvent *, int *);
typedef void (*CuteQQuickLoaderCall16)(const void *, QMouseEvent *, int *);
typedef void (*CuteQQuickLoaderCall17)(const void *, QMouseEvent *, int *);
typedef void (*CuteQQuickLoaderCall18)(const void *, QMouseEvent *, int *);
typedef void (*CuteQQuickLoaderCall19)(const void *, QMouseEvent *, int *);
typedef void (*CuteQQuickLoaderCall20)(const void *, int *);
typedef void (*CuteQQuickLoaderCall21)(const void *, int *);
#if QT_CONFIG(wheelevent)
typedef void (*CuteQQuickLoaderCall22)(const void *, QWheelEvent *, int *);
#endif  // QT_CONFIG(wheelevent)
typedef void (*CuteQQuickLoaderCall23)(const void *, QTouchEvent *, int *);
typedef void (*CuteQQuickLoaderCall24)(const void *, QHoverEvent *, int *);
typedef void (*CuteQQuickLoaderCall25)(const void *, QHoverEvent *, int *);
typedef void (*CuteQQuickLoaderCall26)(const void *, QHoverEvent *, int *);
#if QT_CONFIG(quick_draganddrop)
typedef void (*CuteQQuickLoaderCall27)(const void *, QDragEnterEvent *, int *);
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
typedef void (*CuteQQuickLoaderCall28)(const void *, QDragMoveEvent *, int *);
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
typedef void (*CuteQQuickLoaderCall29)(const void *, QDragLeaveEvent *, int *);
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
typedef void (*CuteQQuickLoaderCall30)(const void *, QDropEvent *, int *);
#endif  // QT_CONFIG(quick_draganddrop)
typedef bool (*CuteQQuickLoaderCall31)(const void *, QQuickItem *, QEvent *, int *);
typedef void * (*CuteQQuickLoaderCall32)(const void *, QSGNode *, QQuickItem::UpdatePaintNodeData *, int *);
typedef void (*CuteQQuickLoaderCall33)(const void *, int *);
typedef void (*CuteQQuickLoaderCall34)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickLoaderCall35)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickLoaderCall36)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickLoaderCall37)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickLoaderCall38)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickLoaderCall39)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickLoaderCall40)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQQuickLoader : public QQuickLoader {
public:
  using QQuickLoader::QQuickLoader;
  void *taken[41] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN10QQuickItem14geometryChangeERK6QRectFS2_")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQmlParserStatus17componentCompleteEv")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem10itemChangeENS_10ItemChangeERKNS_14ItemChangeDataE")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK10QQuickItem12boundingRectEv")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK10QQuickItem8clipRectEv")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK10QQuickItem8containsERK7QPointF")) {
      taken[5] = call;
      return true;
    }
#if QT_CONFIG(im)
    if (!std::strcmp(key, "_ZNK10QQuickItem16inputMethodQueryEN2Qt16InputMethodQueryE")) {
      taken[6] = call;
      return true;
    }
#endif  // QT_CONFIG(im)
    if (!std::strcmp(key, "_ZNK10QQuickItem17isTextureProviderEv")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK10QQuickItem15textureProviderEv")) {
      taken[8] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[9] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN16QQmlParserStatus10classBeginEv")) {
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

  //  void QQuickLoader::geometryChange(const QRectF &newGeometry, const
  //      QRectF &oldGeometry)
  void geometryChange(
      const QRectF &newGeometry,
      const QRectF &oldGeometry) override {
    if (taken[0]) {
      int handled = 0;
      CuteQQuickLoaderCall0 call = reinterpret_cast<CuteQQuickLoaderCall0>(taken[0]);
      call(this, &newGeometry, &oldGeometry, &handled);
      if (handled) return;
    }
    QQuickLoader::geometryChange(newGeometry, oldGeometry);
  }

  //  void QQuickLoader::componentComplete()
  void componentComplete() override {
    if (taken[1]) {
      int handled = 0;
      CuteQQuickLoaderCall1 call = reinterpret_cast<CuteQQuickLoaderCall1>(taken[1]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickLoader::componentComplete();
  }

  //  void QQuickLoader::itemChange(ItemChange change, const ItemChangeData
  //      &value)
  void itemChange(
      QQuickItem::ItemChange change,
      const QQuickItem::ItemChangeData &value) override {
    if (taken[2]) {
      int handled = 0;
      CuteQQuickLoaderCall2 call = reinterpret_cast<CuteQQuickLoaderCall2>(taken[2]);
      call(this, static_cast<int>(change), &value, &handled);
      if (handled) return;
    }
    QQuickLoader::itemChange(change, value);
  }

  //  QRectF QQuickItem::boundingRect() const
  QRectF boundingRect() const override {
    if (taken[3]) {
      int handled = 0;
      CuteQQuickLoaderCall3 call = reinterpret_cast<CuteQQuickLoaderCall3>(taken[3]);
      const QRectF * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QQuickItem::boundingRect();
  }

  //  QRectF QQuickItem::clipRect() const
  QRectF clipRect() const override {
    if (taken[4]) {
      int handled = 0;
      CuteQQuickLoaderCall4 call = reinterpret_cast<CuteQQuickLoaderCall4>(taken[4]);
      const QRectF * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QQuickItem::clipRect();
  }

  //  bool QQuickItem::contains(const QPointF &point) const
  bool contains(const QPointF &point) const override {
    if (taken[5]) {
      int handled = 0;
      CuteQQuickLoaderCall5 call = reinterpret_cast<CuteQQuickLoaderCall5>(taken[5]);
      bool given = call(this, &point, &handled);
      if (handled) return given;
    }
    return QQuickItem::contains(point);
  }

#if QT_CONFIG(im)
  //  QVariant QQuickItem::inputMethodQuery(Qt::InputMethodQuery query)
  //      const
  QVariant inputMethodQuery(Qt::InputMethodQuery query) const override {
    if (taken[6]) {
      int handled = 0;
      CuteQQuickLoaderCall6 call = reinterpret_cast<CuteQQuickLoaderCall6>(taken[6]);
      const QVariant * given = call(this, static_cast<int>(query), &handled);
      if (handled && given) return *given;
    }
    return QQuickItem::inputMethodQuery(query);
  }
#endif  // QT_CONFIG(im)

  //  bool QQuickItem::isTextureProvider() const
  bool isTextureProvider() const override {
    if (taken[7]) {
      int handled = 0;
      CuteQQuickLoaderCall7 call = reinterpret_cast<CuteQQuickLoaderCall7>(taken[7]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QQuickItem::isTextureProvider();
  }

  //  QSGTextureProvider *QQuickItem::textureProvider() const
  QSGTextureProvider *textureProvider() const override {
    if (taken[8]) {
      int handled = 0;
      CuteQQuickLoaderCall8 call = reinterpret_cast<CuteQQuickLoaderCall8>(taken[8]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QSGTextureProvider *>(given);
    }
    return QQuickItem::textureProvider();
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QQuickItem::event(QEvent *a0)
  bool event(QEvent *a0) override {
    if (taken[9]) {
      int handled = 0;
      CuteQQuickLoaderCall9 call = reinterpret_cast<CuteQQuickLoaderCall9>(taken[9]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQuickItem::event(a0);
  }
#endif  // !defined(QT_NO_QOBJECT)

  //  void QQuickItem::classBegin()
  void classBegin() override {
    if (taken[10]) {
      int handled = 0;
      CuteQQuickLoaderCall10 call = reinterpret_cast<CuteQQuickLoaderCall10>(taken[10]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItem::classBegin();
  }

  //  void QQuickItem::keyPressEvent(QKeyEvent *event)
  void keyPressEvent(QKeyEvent *event) override {
    if (taken[11]) {
      int handled = 0;
      CuteQQuickLoaderCall11 call = reinterpret_cast<CuteQQuickLoaderCall11>(taken[11]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::keyPressEvent(event);
  }

  //  void QQuickItem::keyReleaseEvent(QKeyEvent *event)
  void keyReleaseEvent(QKeyEvent *event) override {
    if (taken[12]) {
      int handled = 0;
      CuteQQuickLoaderCall12 call = reinterpret_cast<CuteQQuickLoaderCall12>(taken[12]);
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
      CuteQQuickLoaderCall13 call = reinterpret_cast<CuteQQuickLoaderCall13>(taken[13]);
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
      CuteQQuickLoaderCall14 call = reinterpret_cast<CuteQQuickLoaderCall14>(taken[14]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItem::focusInEvent(a0);
  }

  //  void QQuickItem::focusOutEvent(QFocusEvent *a0)
  void focusOutEvent(QFocusEvent *a0) override {
    if (taken[15]) {
      int handled = 0;
      CuteQQuickLoaderCall15 call = reinterpret_cast<CuteQQuickLoaderCall15>(taken[15]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItem::focusOutEvent(a0);
  }

  //  void QQuickItem::mousePressEvent(QMouseEvent *event)
  void mousePressEvent(QMouseEvent *event) override {
    if (taken[16]) {
      int handled = 0;
      CuteQQuickLoaderCall16 call = reinterpret_cast<CuteQQuickLoaderCall16>(taken[16]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::mousePressEvent(event);
  }

  //  void QQuickItem::mouseMoveEvent(QMouseEvent *event)
  void mouseMoveEvent(QMouseEvent *event) override {
    if (taken[17]) {
      int handled = 0;
      CuteQQuickLoaderCall17 call = reinterpret_cast<CuteQQuickLoaderCall17>(taken[17]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::mouseMoveEvent(event);
  }

  //  void QQuickItem::mouseReleaseEvent(QMouseEvent *event)
  void mouseReleaseEvent(QMouseEvent *event) override {
    if (taken[18]) {
      int handled = 0;
      CuteQQuickLoaderCall18 call = reinterpret_cast<CuteQQuickLoaderCall18>(taken[18]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::mouseReleaseEvent(event);
  }

  //  void QQuickItem::mouseDoubleClickEvent(QMouseEvent *event)
  void mouseDoubleClickEvent(QMouseEvent *event) override {
    if (taken[19]) {
      int handled = 0;
      CuteQQuickLoaderCall19 call = reinterpret_cast<CuteQQuickLoaderCall19>(taken[19]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::mouseDoubleClickEvent(event);
  }

  //  void QQuickItem::mouseUngrabEvent()
  void mouseUngrabEvent() override {
    if (taken[20]) {
      int handled = 0;
      CuteQQuickLoaderCall20 call = reinterpret_cast<CuteQQuickLoaderCall20>(taken[20]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItem::mouseUngrabEvent();
  }

  //  void QQuickItem::touchUngrabEvent()
  void touchUngrabEvent() override {
    if (taken[21]) {
      int handled = 0;
      CuteQQuickLoaderCall21 call = reinterpret_cast<CuteQQuickLoaderCall21>(taken[21]);
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
      CuteQQuickLoaderCall22 call = reinterpret_cast<CuteQQuickLoaderCall22>(taken[22]);
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
      CuteQQuickLoaderCall23 call = reinterpret_cast<CuteQQuickLoaderCall23>(taken[23]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::touchEvent(event);
  }

  //  void QQuickItem::hoverEnterEvent(QHoverEvent *event)
  void hoverEnterEvent(QHoverEvent *event) override {
    if (taken[24]) {
      int handled = 0;
      CuteQQuickLoaderCall24 call = reinterpret_cast<CuteQQuickLoaderCall24>(taken[24]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::hoverEnterEvent(event);
  }

  //  void QQuickItem::hoverMoveEvent(QHoverEvent *event)
  void hoverMoveEvent(QHoverEvent *event) override {
    if (taken[25]) {
      int handled = 0;
      CuteQQuickLoaderCall25 call = reinterpret_cast<CuteQQuickLoaderCall25>(taken[25]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::hoverMoveEvent(event);
  }

  //  void QQuickItem::hoverLeaveEvent(QHoverEvent *event)
  void hoverLeaveEvent(QHoverEvent *event) override {
    if (taken[26]) {
      int handled = 0;
      CuteQQuickLoaderCall26 call = reinterpret_cast<CuteQQuickLoaderCall26>(taken[26]);
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
      CuteQQuickLoaderCall27 call = reinterpret_cast<CuteQQuickLoaderCall27>(taken[27]);
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
      CuteQQuickLoaderCall28 call = reinterpret_cast<CuteQQuickLoaderCall28>(taken[28]);
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
      CuteQQuickLoaderCall29 call = reinterpret_cast<CuteQQuickLoaderCall29>(taken[29]);
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
      CuteQQuickLoaderCall30 call = reinterpret_cast<CuteQQuickLoaderCall30>(taken[30]);
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
      CuteQQuickLoaderCall31 call = reinterpret_cast<CuteQQuickLoaderCall31>(taken[31]);
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
      CuteQQuickLoaderCall32 call = reinterpret_cast<CuteQQuickLoaderCall32>(taken[32]);
      void * given = call(this, a0, a1, &handled);
      if (handled) return static_cast<QSGNode *>(given);
    }
    return QQuickItem::updatePaintNode(a0, a1);
  }

  //  void QQuickItem::releaseResources()
  void releaseResources() override {
    if (taken[33]) {
      int handled = 0;
      CuteQQuickLoaderCall33 call = reinterpret_cast<CuteQQuickLoaderCall33>(taken[33]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItem::releaseResources();
  }

  //  void QQuickItem::updatePolish()
  void updatePolish() override {
    if (taken[34]) {
      int handled = 0;
      CuteQQuickLoaderCall34 call = reinterpret_cast<CuteQQuickLoaderCall34>(taken[34]);
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
      CuteQQuickLoaderCall35 call = reinterpret_cast<CuteQQuickLoaderCall35>(taken[35]);
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
      CuteQQuickLoaderCall36 call = reinterpret_cast<CuteQQuickLoaderCall36>(taken[36]);
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
      CuteQQuickLoaderCall37 call = reinterpret_cast<CuteQQuickLoaderCall37>(taken[37]);
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
      CuteQQuickLoaderCall38 call = reinterpret_cast<CuteQQuickLoaderCall38>(taken[38]);
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
      CuteQQuickLoaderCall39 call = reinterpret_cast<CuteQQuickLoaderCall39>(taken[39]);
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
      CuteQQuickLoaderCall40 call = reinterpret_cast<CuteQQuickLoaderCall40>(taken[40]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QQuickLoader::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK12QQuickLoader10metaObjectEv(
    const QQuickLoader *self) {
  return self->metaObject();
}

//  void *QQuickLoader::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN12QQuickLoader11qt_metacastEPKc(
    QQuickLoader *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QQuickLoader::qt_metacall(QMetaObject::Call a0, int a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN12QQuickLoader11qt_metacallEN11QMetaObject4CallEiPPv(
    QQuickLoader *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QQuickLoader::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN12QQuickLoader2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuickLoader::tr(s, c, n));
}

//  QQuickLoader::QQuickLoader(QQuickItem *parent)
extern "C" Q_DECL_EXPORT
QQuickLoader *ritual_ZN12QQuickLoaderC1EP10QQuickItem(QQuickItem *parent) {
  return new CuteQQuickLoader(parent);
}

//  QQuickLoader::~QQuickLoader()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QQuickLoaderD1Ev(QQuickLoader *self) {
  delete self;
}

//  bool QQuickLoader::active() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK12QQuickLoader6activeEv(const QQuickLoader *self) {
  return self->active();
}

//  void QQuickLoader::setActive(bool newVal)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QQuickLoader9setActiveEb(QQuickLoader *self, bool newVal) {
  self->setActive(newVal);
}

//  void QQuickLoader::setSource(const QUrl &source, QJSValue
//      initialProperties)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QQuickLoader9setSourceERK4QUrl8QJSValue(
    QQuickLoader *self,
    const QUrl *source,
    const QJSValue *initialProperties) {
  self->setSource(*source, *initialProperties);
}

//  void QQuickLoader::setSource(const QUrl &source)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QQuickLoader9setSourceERK4QUrl(
    QQuickLoader *self,
    const QUrl *source) {
  self->setSource(*source);
}

//  QUrl QQuickLoader::source() const
extern "C" Q_DECL_EXPORT
QUrl *ritual_ZNK12QQuickLoader6sourceEv(const QQuickLoader *self) {
  return new QUrl(self->source());
}

//  void QQuickLoader::setSourceWithoutResolve(const QUrl &source)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QQuickLoader23setSourceWithoutResolveERK4QUrl(
    QQuickLoader *self,
    const QUrl *source) {
  self->setSourceWithoutResolve(*source);
}

//  QQmlComponent *QQuickLoader::sourceComponent() const
extern "C" Q_DECL_EXPORT
QQmlComponent *ritual_ZNK12QQuickLoader15sourceComponentEv(
    const QQuickLoader *self) {
  return self->sourceComponent();
}

//  void QQuickLoader::setSourceComponent(QQmlComponent *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QQuickLoader18setSourceComponentEP13QQmlComponent(
    QQuickLoader *self,
    QQmlComponent *a0) {
  self->setSourceComponent(a0);
}

//  void QQuickLoader::resetSourceComponent()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QQuickLoader20resetSourceComponentEv(QQuickLoader *self) {
  self->resetSourceComponent();
}

//  Status QQuickLoader::status() const
extern "C" Q_DECL_EXPORT
QQuickLoader::Status ritual_ZNK12QQuickLoader6statusEv(
    const QQuickLoader *self) {
  return self->status();
}

//  qreal QQuickLoader::progress() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK12QQuickLoader8progressEv(const QQuickLoader *self) {
  return self->progress();
}

//  bool QQuickLoader::asynchronous() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK12QQuickLoader12asynchronousEv(const QQuickLoader *self) {
  return self->asynchronous();
}

//  void QQuickLoader::setAsynchronous(bool a)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QQuickLoader15setAsynchronousEb(QQuickLoader *self, bool a) {
  self->setAsynchronous(a);
}

//  QObject *QQuickLoader::item() const
extern "C" Q_DECL_EXPORT
QObject *ritual_ZNK12QQuickLoader4itemEv(const QQuickLoader *self) {
  return self->item();
}

//  void QQuickLoader::itemChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QQuickLoader11itemChangedEv(QQuickLoader *self) {
  self->itemChanged();
}

//  void QQuickLoader::activeChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QQuickLoader13activeChangedEv(QQuickLoader *self) {
  self->activeChanged();
}

//  void QQuickLoader::sourceChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QQuickLoader13sourceChangedEv(QQuickLoader *self) {
  self->sourceChanged();
}

//  void QQuickLoader::sourceComponentChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QQuickLoader22sourceComponentChangedEv(QQuickLoader *self) {
  self->sourceComponentChanged();
}

//  void QQuickLoader::statusChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QQuickLoader13statusChangedEv(QQuickLoader *self) {
  self->statusChanged();
}

//  void QQuickLoader::progressChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QQuickLoader15progressChangedEv(QQuickLoader *self) {
  self->progressChanged();
}

//  void QQuickLoader::loaded()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QQuickLoader6loadedEv(QQuickLoader *self) {
  self->loaded();
}

//  void QQuickLoader::asynchronousChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QQuickLoader19asynchronousChangedEv(QQuickLoader *self) {
  self->asynchronousChanged();
}

//  void QQuickLoader::geometryChange(const QRectF &newGeometry, const QRectF
//      &oldGeometry)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QQuickLoader14geometryChangeERK6QRectFS2_(
    QQuickLoader *self,
    const QRectF *newGeometry,
    const QRectF *oldGeometry) {
  self->geometryChange(*newGeometry, *oldGeometry);
}

//  void QQuickLoader::componentComplete()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QQuickLoader17componentCompleteEv(QQuickLoader *self) {
  self->componentComplete();
}

//  void QQuickLoader::itemChange(ItemChange change, const ItemChangeData
//      &value)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QQuickLoader10itemChangeEN10QQuickItem10ItemChangeERKNS0_14ItemChangeDataE(
    QQuickLoader *self,
    QQuickItem::ItemChange change,
    const QQuickItem::ItemChangeData *value) {
  self->itemChange(change, *value);
}

//  QUrl QQuickLoader::setSourceUrlHelper(const QUrl &unresolvedUrl)
extern "C" Q_DECL_EXPORT
QUrl *ritual_ZN12QQuickLoader18setSourceUrlHelperERK4QUrl(
    QQuickLoader *self,
    const QUrl *unresolvedUrl) {
  return new QUrl(self->setSourceUrlHelper(*unresolvedUrl));
}

//  void QQuickLoader::setSource(const QUrl &sourceUrl, bool needsClear)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QQuickLoader9setSourceERK4QUrlb(
    QQuickLoader *self,
    const QUrl *sourceUrl,
    bool needsClear) {
  self->setSource(*sourceUrl, needsClear);
}

//  void QQuickLoader::loadFromSource()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QQuickLoader14loadFromSourceEv(QQuickLoader *self) {
  self->loadFromSource();
}

//  void QQuickLoader::loadFromSourceComponent()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QQuickLoader23loadFromSourceComponentEv(QQuickLoader *self) {
  self->loadFromSourceComponent();
}

//  QQuickLoaderPrivate *QQuickLoader::d_func()
extern "C" Q_DECL_EXPORT
QQuickLoaderPrivate *ritual_ZN12QQuickLoader6d_funcEv(QQuickLoader *self) {
  return self->d_func();
}

//  const QQuickLoaderPrivate *QQuickLoader::d_func() const
extern "C" Q_DECL_EXPORT
const QQuickLoaderPrivate *ritual_ZNK12QQuickLoader6d_funcEv(
    const QQuickLoader *self) {
  return self->d_func();
}

//  a Python function taken by a CuteQQuickLoader, for the function named by
//      the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQuickLoader(
    QQuickLoader *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQuickLoader *>(self)->take(key, call);
}

//  void QQuickLoader::geometryChange(const QRectF &newGeometry, const QRectF
//      &oldGeometry)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN12QQuickLoader14geometryChangeERK6QRectFS2_(
    QQuickLoader *self,
    const QRectF *newGeometry,
    const QRectF *oldGeometry) {
  static_cast<OwnQQuickLoader *>(self)->OwnQQuickLoader::geometryChange(
      *newGeometry,
      *oldGeometry);
}

//  void QQuickLoader::componentComplete()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN12QQuickLoader17componentCompleteEv(QQuickLoader *self) {
  static_cast<OwnQQuickLoader *>(self)->OwnQQuickLoader::componentComplete();
}

//  void QQuickLoader::itemChange(ItemChange change, const ItemChangeData
//      &value)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN12QQuickLoader10itemChangeEN10QQuickItem10ItemChangeERKNS0_14ItemChangeDataE(
    QQuickLoader *self,
    QQuickItem::ItemChange change,
    const QQuickItem::ItemChangeData *value) {
  static_cast<OwnQQuickLoader *>(self)->OwnQQuickLoader::itemChange(
      change,
      *value);
}
