//  Written by dev_tooling.RitualGenerator from the records of
//  QtLocation/6.12.0/QtLocation/private/qdeclarativegeomap_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtGui/qtguiglobal.h>
#include <QtQuick/qtquickglobal.h>
#include <QtLocation/6.12.0/QtLocation/private/qlocationglobal_p.h>
#include <QtLocation/QtLocation>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtLocation/6.12.0/QtLocation/private/qdeclarativegeomap_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtLocation/6.12.0/QtLocation/private/qgeomaptype_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtPositioning/qgeocoordinate.h>
#include <QtPositioning/qgeoshape.h>
#include <QtGui/qcolor.h>
#include <QtCore/qrect.h>
#include <QtCore/qpoint.h>
#include <QtCore/qobject.h>
#include <QtCore/qvariant.h>
#include <QtCore/qmargins.h>
#include <QtQuick/QtQuick>
#include <QtQuick/qquickitem.h>
#include <QtGui/qimage.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtLocation/6.12.0/QtLocation/private/qgeocameracapabilities_p.h>
#include <QtLocation/6.12.0/QtLocation/private/qgeocameradata_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qmetaobject.h>
#include <QtCore/qlist.h>
#include <cstring>

//  Only a class built on QDeclarativeGeoMap may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQDeclarativeGeoMap : QDeclarativeGeoMap {
  using QDeclarativeGeoMap::componentComplete;
  using QDeclarativeGeoMap::updatePaintNode;
  using QDeclarativeGeoMap::geometryChange;
};

//  A QDeclarativeGeoMap that Python can take functions over in. Every QDeclarativeGeoMap
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQDeclarativeGeoMapCall0)(const void *, int, const QQuickItem::ItemChangeData *, int *);
typedef void (*CuteQDeclarativeGeoMapCall1)(const void *, int *);
typedef void * (*CuteQDeclarativeGeoMapCall2)(const void *, QSGNode *, QQuickItem::UpdatePaintNodeData *, int *);
typedef void (*CuteQDeclarativeGeoMapCall3)(const void *, const QRectF *, const QRectF *, int *);
typedef const QRectF * (*CuteQDeclarativeGeoMapCall4)(const void *, int *);
typedef const QRectF * (*CuteQDeclarativeGeoMapCall5)(const void *, int *);
typedef bool (*CuteQDeclarativeGeoMapCall6)(const void *, const QPointF *, int *);
#if QT_CONFIG(im)
typedef const QVariant * (*CuteQDeclarativeGeoMapCall7)(const void *, int, int *);
#endif  // QT_CONFIG(im)
typedef bool (*CuteQDeclarativeGeoMapCall8)(const void *, int *);
typedef void * (*CuteQDeclarativeGeoMapCall9)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQDeclarativeGeoMapCall10)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
typedef void (*CuteQDeclarativeGeoMapCall11)(const void *, int *);
typedef void (*CuteQDeclarativeGeoMapCall12)(const void *, QKeyEvent *, int *);
typedef void (*CuteQDeclarativeGeoMapCall13)(const void *, QKeyEvent *, int *);
#if QT_CONFIG(im)
typedef void (*CuteQDeclarativeGeoMapCall14)(const void *, QInputMethodEvent *, int *);
#endif  // QT_CONFIG(im)
typedef void (*CuteQDeclarativeGeoMapCall15)(const void *, QFocusEvent *, int *);
typedef void (*CuteQDeclarativeGeoMapCall16)(const void *, QFocusEvent *, int *);
typedef void (*CuteQDeclarativeGeoMapCall17)(const void *, QMouseEvent *, int *);
typedef void (*CuteQDeclarativeGeoMapCall18)(const void *, QMouseEvent *, int *);
typedef void (*CuteQDeclarativeGeoMapCall19)(const void *, QMouseEvent *, int *);
typedef void (*CuteQDeclarativeGeoMapCall20)(const void *, QMouseEvent *, int *);
typedef void (*CuteQDeclarativeGeoMapCall21)(const void *, int *);
typedef void (*CuteQDeclarativeGeoMapCall22)(const void *, int *);
#if QT_CONFIG(wheelevent)
typedef void (*CuteQDeclarativeGeoMapCall23)(const void *, QWheelEvent *, int *);
#endif  // QT_CONFIG(wheelevent)
typedef void (*CuteQDeclarativeGeoMapCall24)(const void *, QTouchEvent *, int *);
typedef void (*CuteQDeclarativeGeoMapCall25)(const void *, QHoverEvent *, int *);
typedef void (*CuteQDeclarativeGeoMapCall26)(const void *, QHoverEvent *, int *);
typedef void (*CuteQDeclarativeGeoMapCall27)(const void *, QHoverEvent *, int *);
#if QT_CONFIG(quick_draganddrop)
typedef void (*CuteQDeclarativeGeoMapCall28)(const void *, QDragEnterEvent *, int *);
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
typedef void (*CuteQDeclarativeGeoMapCall29)(const void *, QDragMoveEvent *, int *);
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
typedef void (*CuteQDeclarativeGeoMapCall30)(const void *, QDragLeaveEvent *, int *);
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
typedef void (*CuteQDeclarativeGeoMapCall31)(const void *, QDropEvent *, int *);
#endif  // QT_CONFIG(quick_draganddrop)
typedef bool (*CuteQDeclarativeGeoMapCall32)(const void *, QQuickItem *, QEvent *, int *);
typedef void (*CuteQDeclarativeGeoMapCall33)(const void *, int *);
typedef void (*CuteQDeclarativeGeoMapCall34)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQDeclarativeGeoMapCall35)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQDeclarativeGeoMapCall36)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQDeclarativeGeoMapCall37)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQDeclarativeGeoMapCall38)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQDeclarativeGeoMapCall39)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQDeclarativeGeoMapCall40)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQDeclarativeGeoMap : public QDeclarativeGeoMap {
public:
  using QDeclarativeGeoMap::QDeclarativeGeoMap;
  void *taken[41] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN10QQuickItem10itemChangeENS_10ItemChangeERKNS_14ItemChangeDataE")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQmlParserStatus17componentCompleteEv")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem15updatePaintNodeEP7QSGNodePNS_19UpdatePaintNodeDataE")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem14geometryChangeERK6QRectFS2_")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK10QQuickItem12boundingRectEv")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK10QQuickItem8clipRectEv")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK10QQuickItem8containsERK7QPointF")) {
      taken[6] = call;
      return true;
    }
#if QT_CONFIG(im)
    if (!std::strcmp(key, "_ZNK10QQuickItem16inputMethodQueryEN2Qt16InputMethodQueryE")) {
      taken[7] = call;
      return true;
    }
#endif  // QT_CONFIG(im)
    if (!std::strcmp(key, "_ZNK10QQuickItem17isTextureProviderEv")) {
      taken[8] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK10QQuickItem15textureProviderEv")) {
      taken[9] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[10] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN16QQmlParserStatus10classBeginEv")) {
      taken[11] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem13keyPressEventEP9QKeyEvent")) {
      taken[12] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem15keyReleaseEventEP9QKeyEvent")) {
      taken[13] = call;
      return true;
    }
#if QT_CONFIG(im)
    if (!std::strcmp(key, "_ZN10QQuickItem16inputMethodEventEP17QInputMethodEvent")) {
      taken[14] = call;
      return true;
    }
#endif  // QT_CONFIG(im)
    if (!std::strcmp(key, "_ZN10QQuickItem12focusInEventEP11QFocusEvent")) {
      taken[15] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem13focusOutEventEP11QFocusEvent")) {
      taken[16] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem15mousePressEventEP11QMouseEvent")) {
      taken[17] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem14mouseMoveEventEP11QMouseEvent")) {
      taken[18] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem17mouseReleaseEventEP11QMouseEvent")) {
      taken[19] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem21mouseDoubleClickEventEP11QMouseEvent")) {
      taken[20] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem16mouseUngrabEventEv")) {
      taken[21] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem16touchUngrabEventEv")) {
      taken[22] = call;
      return true;
    }
#if QT_CONFIG(wheelevent)
    if (!std::strcmp(key, "_ZN10QQuickItem10wheelEventEP11QWheelEvent")) {
      taken[23] = call;
      return true;
    }
#endif  // QT_CONFIG(wheelevent)
    if (!std::strcmp(key, "_ZN10QQuickItem10touchEventEP11QTouchEvent")) {
      taken[24] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem15hoverEnterEventEP11QHoverEvent")) {
      taken[25] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem14hoverMoveEventEP11QHoverEvent")) {
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

  //  void QDeclarativeGeoMap::itemChange(ItemChange a0, const
  //      ItemChangeData &a1)
  void itemChange(
      QQuickItem::ItemChange a0,
      const QQuickItem::ItemChangeData &a1) override {
    if (taken[0]) {
      int handled = 0;
      CuteQDeclarativeGeoMapCall0 call = reinterpret_cast<CuteQDeclarativeGeoMapCall0>(taken[0]);
      call(this, static_cast<int>(a0), &a1, &handled);
      if (handled) return;
    }
    QDeclarativeGeoMap::itemChange(a0, a1);
  }

  //  void QDeclarativeGeoMap::componentComplete()
  void componentComplete() override {
    if (taken[1]) {
      int handled = 0;
      CuteQDeclarativeGeoMapCall1 call = reinterpret_cast<CuteQDeclarativeGeoMapCall1>(taken[1]);
      call(this, &handled);
      if (handled) return;
    }
    QDeclarativeGeoMap::componentComplete();
  }

  //  QSGNode *QDeclarativeGeoMap::updatePaintNode(QSGNode *a0,
  //      UpdatePaintNodeData *a1)
  QSGNode *updatePaintNode(
      QSGNode *a0,
      QQuickItem::UpdatePaintNodeData *a1) override {
    if (taken[2]) {
      int handled = 0;
      CuteQDeclarativeGeoMapCall2 call = reinterpret_cast<CuteQDeclarativeGeoMapCall2>(taken[2]);
      void * given = call(this, a0, a1, &handled);
      if (handled) return static_cast<QSGNode *>(given);
    }
    return QDeclarativeGeoMap::updatePaintNode(a0, a1);
  }

  //  void QDeclarativeGeoMap::geometryChange(const QRectF &newGeometry,
  //      const QRectF &oldGeometry)
  void geometryChange(
      const QRectF &newGeometry,
      const QRectF &oldGeometry) override {
    if (taken[3]) {
      int handled = 0;
      CuteQDeclarativeGeoMapCall3 call = reinterpret_cast<CuteQDeclarativeGeoMapCall3>(taken[3]);
      call(this, &newGeometry, &oldGeometry, &handled);
      if (handled) return;
    }
    QDeclarativeGeoMap::geometryChange(newGeometry, oldGeometry);
  }

  //  QRectF QQuickItem::boundingRect() const
  QRectF boundingRect() const override {
    if (taken[4]) {
      int handled = 0;
      CuteQDeclarativeGeoMapCall4 call = reinterpret_cast<CuteQDeclarativeGeoMapCall4>(taken[4]);
      const QRectF * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QQuickItem::boundingRect();
  }

  //  QRectF QQuickItem::clipRect() const
  QRectF clipRect() const override {
    if (taken[5]) {
      int handled = 0;
      CuteQDeclarativeGeoMapCall5 call = reinterpret_cast<CuteQDeclarativeGeoMapCall5>(taken[5]);
      const QRectF * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QQuickItem::clipRect();
  }

  //  bool QQuickItem::contains(const QPointF &point) const
  bool contains(const QPointF &point) const override {
    if (taken[6]) {
      int handled = 0;
      CuteQDeclarativeGeoMapCall6 call = reinterpret_cast<CuteQDeclarativeGeoMapCall6>(taken[6]);
      bool given = call(this, &point, &handled);
      if (handled) return given;
    }
    return QQuickItem::contains(point);
  }

#if QT_CONFIG(im)
  //  QVariant QQuickItem::inputMethodQuery(Qt::InputMethodQuery query)
  //      const
  QVariant inputMethodQuery(Qt::InputMethodQuery query) const override {
    if (taken[7]) {
      int handled = 0;
      CuteQDeclarativeGeoMapCall7 call = reinterpret_cast<CuteQDeclarativeGeoMapCall7>(taken[7]);
      const QVariant * given = call(this, static_cast<int>(query), &handled);
      if (handled && given) return *given;
    }
    return QQuickItem::inputMethodQuery(query);
  }
#endif  // QT_CONFIG(im)

  //  bool QQuickItem::isTextureProvider() const
  bool isTextureProvider() const override {
    if (taken[8]) {
      int handled = 0;
      CuteQDeclarativeGeoMapCall8 call = reinterpret_cast<CuteQDeclarativeGeoMapCall8>(taken[8]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QQuickItem::isTextureProvider();
  }

  //  QSGTextureProvider *QQuickItem::textureProvider() const
  QSGTextureProvider *textureProvider() const override {
    if (taken[9]) {
      int handled = 0;
      CuteQDeclarativeGeoMapCall9 call = reinterpret_cast<CuteQDeclarativeGeoMapCall9>(taken[9]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QSGTextureProvider *>(given);
    }
    return QQuickItem::textureProvider();
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QQuickItem::event(QEvent *a0)
  bool event(QEvent *a0) override {
    if (taken[10]) {
      int handled = 0;
      CuteQDeclarativeGeoMapCall10 call = reinterpret_cast<CuteQDeclarativeGeoMapCall10>(taken[10]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQuickItem::event(a0);
  }
#endif  // !defined(QT_NO_QOBJECT)

  //  void QQuickItem::classBegin()
  void classBegin() override {
    if (taken[11]) {
      int handled = 0;
      CuteQDeclarativeGeoMapCall11 call = reinterpret_cast<CuteQDeclarativeGeoMapCall11>(taken[11]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItem::classBegin();
  }

  //  void QQuickItem::keyPressEvent(QKeyEvent *event)
  void keyPressEvent(QKeyEvent *event) override {
    if (taken[12]) {
      int handled = 0;
      CuteQDeclarativeGeoMapCall12 call = reinterpret_cast<CuteQDeclarativeGeoMapCall12>(taken[12]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::keyPressEvent(event);
  }

  //  void QQuickItem::keyReleaseEvent(QKeyEvent *event)
  void keyReleaseEvent(QKeyEvent *event) override {
    if (taken[13]) {
      int handled = 0;
      CuteQDeclarativeGeoMapCall13 call = reinterpret_cast<CuteQDeclarativeGeoMapCall13>(taken[13]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::keyReleaseEvent(event);
  }

#if QT_CONFIG(im)
  //  void QQuickItem::inputMethodEvent(QInputMethodEvent *a0)
  void inputMethodEvent(QInputMethodEvent *a0) override {
    if (taken[14]) {
      int handled = 0;
      CuteQDeclarativeGeoMapCall14 call = reinterpret_cast<CuteQDeclarativeGeoMapCall14>(taken[14]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItem::inputMethodEvent(a0);
  }
#endif  // QT_CONFIG(im)

  //  void QQuickItem::focusInEvent(QFocusEvent *a0)
  void focusInEvent(QFocusEvent *a0) override {
    if (taken[15]) {
      int handled = 0;
      CuteQDeclarativeGeoMapCall15 call = reinterpret_cast<CuteQDeclarativeGeoMapCall15>(taken[15]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItem::focusInEvent(a0);
  }

  //  void QQuickItem::focusOutEvent(QFocusEvent *a0)
  void focusOutEvent(QFocusEvent *a0) override {
    if (taken[16]) {
      int handled = 0;
      CuteQDeclarativeGeoMapCall16 call = reinterpret_cast<CuteQDeclarativeGeoMapCall16>(taken[16]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItem::focusOutEvent(a0);
  }

  //  void QQuickItem::mousePressEvent(QMouseEvent *event)
  void mousePressEvent(QMouseEvent *event) override {
    if (taken[17]) {
      int handled = 0;
      CuteQDeclarativeGeoMapCall17 call = reinterpret_cast<CuteQDeclarativeGeoMapCall17>(taken[17]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::mousePressEvent(event);
  }

  //  void QQuickItem::mouseMoveEvent(QMouseEvent *event)
  void mouseMoveEvent(QMouseEvent *event) override {
    if (taken[18]) {
      int handled = 0;
      CuteQDeclarativeGeoMapCall18 call = reinterpret_cast<CuteQDeclarativeGeoMapCall18>(taken[18]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::mouseMoveEvent(event);
  }

  //  void QQuickItem::mouseReleaseEvent(QMouseEvent *event)
  void mouseReleaseEvent(QMouseEvent *event) override {
    if (taken[19]) {
      int handled = 0;
      CuteQDeclarativeGeoMapCall19 call = reinterpret_cast<CuteQDeclarativeGeoMapCall19>(taken[19]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::mouseReleaseEvent(event);
  }

  //  void QQuickItem::mouseDoubleClickEvent(QMouseEvent *event)
  void mouseDoubleClickEvent(QMouseEvent *event) override {
    if (taken[20]) {
      int handled = 0;
      CuteQDeclarativeGeoMapCall20 call = reinterpret_cast<CuteQDeclarativeGeoMapCall20>(taken[20]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::mouseDoubleClickEvent(event);
  }

  //  void QQuickItem::mouseUngrabEvent()
  void mouseUngrabEvent() override {
    if (taken[21]) {
      int handled = 0;
      CuteQDeclarativeGeoMapCall21 call = reinterpret_cast<CuteQDeclarativeGeoMapCall21>(taken[21]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItem::mouseUngrabEvent();
  }

  //  void QQuickItem::touchUngrabEvent()
  void touchUngrabEvent() override {
    if (taken[22]) {
      int handled = 0;
      CuteQDeclarativeGeoMapCall22 call = reinterpret_cast<CuteQDeclarativeGeoMapCall22>(taken[22]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItem::touchUngrabEvent();
  }

#if QT_CONFIG(wheelevent)
  //  void QQuickItem::wheelEvent(QWheelEvent *event)
  void wheelEvent(QWheelEvent *event) override {
    if (taken[23]) {
      int handled = 0;
      CuteQDeclarativeGeoMapCall23 call = reinterpret_cast<CuteQDeclarativeGeoMapCall23>(taken[23]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::wheelEvent(event);
  }
#endif  // QT_CONFIG(wheelevent)

  //  void QQuickItem::touchEvent(QTouchEvent *event)
  void touchEvent(QTouchEvent *event) override {
    if (taken[24]) {
      int handled = 0;
      CuteQDeclarativeGeoMapCall24 call = reinterpret_cast<CuteQDeclarativeGeoMapCall24>(taken[24]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::touchEvent(event);
  }

  //  void QQuickItem::hoverEnterEvent(QHoverEvent *event)
  void hoverEnterEvent(QHoverEvent *event) override {
    if (taken[25]) {
      int handled = 0;
      CuteQDeclarativeGeoMapCall25 call = reinterpret_cast<CuteQDeclarativeGeoMapCall25>(taken[25]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::hoverEnterEvent(event);
  }

  //  void QQuickItem::hoverMoveEvent(QHoverEvent *event)
  void hoverMoveEvent(QHoverEvent *event) override {
    if (taken[26]) {
      int handled = 0;
      CuteQDeclarativeGeoMapCall26 call = reinterpret_cast<CuteQDeclarativeGeoMapCall26>(taken[26]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::hoverMoveEvent(event);
  }

  //  void QQuickItem::hoverLeaveEvent(QHoverEvent *event)
  void hoverLeaveEvent(QHoverEvent *event) override {
    if (taken[27]) {
      int handled = 0;
      CuteQDeclarativeGeoMapCall27 call = reinterpret_cast<CuteQDeclarativeGeoMapCall27>(taken[27]);
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
      CuteQDeclarativeGeoMapCall28 call = reinterpret_cast<CuteQDeclarativeGeoMapCall28>(taken[28]);
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
      CuteQDeclarativeGeoMapCall29 call = reinterpret_cast<CuteQDeclarativeGeoMapCall29>(taken[29]);
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
      CuteQDeclarativeGeoMapCall30 call = reinterpret_cast<CuteQDeclarativeGeoMapCall30>(taken[30]);
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
      CuteQDeclarativeGeoMapCall31 call = reinterpret_cast<CuteQDeclarativeGeoMapCall31>(taken[31]);
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
      CuteQDeclarativeGeoMapCall32 call = reinterpret_cast<CuteQDeclarativeGeoMapCall32>(taken[32]);
      bool given = call(this, a0, a1, &handled);
      if (handled) return given;
    }
    return QQuickItem::childMouseEventFilter(a0, a1);
  }

  //  void QQuickItem::releaseResources()
  void releaseResources() override {
    if (taken[33]) {
      int handled = 0;
      CuteQDeclarativeGeoMapCall33 call = reinterpret_cast<CuteQDeclarativeGeoMapCall33>(taken[33]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItem::releaseResources();
  }

  //  void QQuickItem::updatePolish()
  void updatePolish() override {
    if (taken[34]) {
      int handled = 0;
      CuteQDeclarativeGeoMapCall34 call = reinterpret_cast<CuteQDeclarativeGeoMapCall34>(taken[34]);
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
      CuteQDeclarativeGeoMapCall35 call = reinterpret_cast<CuteQDeclarativeGeoMapCall35>(taken[35]);
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
      CuteQDeclarativeGeoMapCall36 call = reinterpret_cast<CuteQDeclarativeGeoMapCall36>(taken[36]);
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
      CuteQDeclarativeGeoMapCall37 call = reinterpret_cast<CuteQDeclarativeGeoMapCall37>(taken[37]);
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
      CuteQDeclarativeGeoMapCall38 call = reinterpret_cast<CuteQDeclarativeGeoMapCall38>(taken[38]);
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
      CuteQDeclarativeGeoMapCall39 call = reinterpret_cast<CuteQDeclarativeGeoMapCall39>(taken[39]);
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
      CuteQDeclarativeGeoMapCall40 call = reinterpret_cast<CuteQDeclarativeGeoMapCall40>(taken[40]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QDeclarativeGeoMap::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK18QDeclarativeGeoMap10metaObjectEv(
    const QDeclarativeGeoMap *self) {
  return self->metaObject();
}

//  void *QDeclarativeGeoMap::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN18QDeclarativeGeoMap11qt_metacastEPKc(
    QDeclarativeGeoMap *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QDeclarativeGeoMap::qt_metacall(QMetaObject::Call a0, int a1, void
//      **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN18QDeclarativeGeoMap11qt_metacallEN11QMetaObject4CallEiPPv(
    QDeclarativeGeoMap *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QDeclarativeGeoMap::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN18QDeclarativeGeoMap2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QDeclarativeGeoMap::tr(s, c, n));
}

//  QDeclarativeGeoMap::QDeclarativeGeoMap(QQuickItem *parent)
extern "C" Q_DECL_EXPORT
QDeclarativeGeoMap *ritual_ZN18QDeclarativeGeoMapC1EP10QQuickItem(
    QQuickItem *parent) {
  return new CuteQDeclarativeGeoMap(parent);
}

//  QDeclarativeGeoMap::~QDeclarativeGeoMap()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QDeclarativeGeoMapD1Ev(QDeclarativeGeoMap *self) {
  delete self;
}

//  void QDeclarativeGeoMap::setPlugin(QDeclarativeGeoServiceProvider
//      *plugin)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QDeclarativeGeoMap9setPluginEP30QDeclarativeGeoServiceProvider(
    QDeclarativeGeoMap *self,
    QDeclarativeGeoServiceProvider *plugin) {
  self->setPlugin(plugin);
}

//  QDeclarativeGeoServiceProvider *QDeclarativeGeoMap::plugin() const
extern "C" Q_DECL_EXPORT
QDeclarativeGeoServiceProvider *ritual_ZNK18QDeclarativeGeoMap6pluginEv(
    const QDeclarativeGeoMap *self) {
  return self->plugin();
}

//  void QDeclarativeGeoMap::setActiveMapType(const QGeoMapType &mapType)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QDeclarativeGeoMap16setActiveMapTypeERK11QGeoMapType(
    QDeclarativeGeoMap *self,
    const QGeoMapType *mapType) {
  self->setActiveMapType(*mapType);
}

//  QGeoMapType QDeclarativeGeoMap::activeMapType() const
extern "C" Q_DECL_EXPORT
QGeoMapType *ritual_ZNK18QDeclarativeGeoMap13activeMapTypeEv(
    const QDeclarativeGeoMap *self) {
  return new QGeoMapType(self->activeMapType());
}

//  void QDeclarativeGeoMap::setMinimumZoomLevel(qreal minimumZoomLevel, bool
//      userSet)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QDeclarativeGeoMap19setMinimumZoomLevelEdb(
    QDeclarativeGeoMap *self,
    qreal minimumZoomLevel,
    bool userSet) {
  self->setMinimumZoomLevel(minimumZoomLevel, userSet);
}

//  qreal QDeclarativeGeoMap::minimumZoomLevel() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK18QDeclarativeGeoMap16minimumZoomLevelEv(
    const QDeclarativeGeoMap *self) {
  return self->minimumZoomLevel();
}

//  void QDeclarativeGeoMap::setMaximumZoomLevel(qreal maximumZoomLevel, bool
//      userSet)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QDeclarativeGeoMap19setMaximumZoomLevelEdb(
    QDeclarativeGeoMap *self,
    qreal maximumZoomLevel,
    bool userSet) {
  self->setMaximumZoomLevel(maximumZoomLevel, userSet);
}

//  qreal QDeclarativeGeoMap::maximumZoomLevel() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK18QDeclarativeGeoMap16maximumZoomLevelEv(
    const QDeclarativeGeoMap *self) {
  return self->maximumZoomLevel();
}

//  void QDeclarativeGeoMap::setZoomLevel(qreal zoomLevel)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QDeclarativeGeoMap12setZoomLevelEd(
    QDeclarativeGeoMap *self,
    qreal zoomLevel) {
  self->setZoomLevel(zoomLevel);
}

//  qreal QDeclarativeGeoMap::zoomLevel() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK18QDeclarativeGeoMap9zoomLevelEv(
    const QDeclarativeGeoMap *self) {
  return self->zoomLevel();
}

//  void QDeclarativeGeoMap::setBearing(qreal bearing)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QDeclarativeGeoMap10setBearingEd(
    QDeclarativeGeoMap *self,
    qreal bearing) {
  self->setBearing(bearing);
}

//  qreal QDeclarativeGeoMap::bearing() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK18QDeclarativeGeoMap7bearingEv(
    const QDeclarativeGeoMap *self) {
  return self->bearing();
}

//  void QDeclarativeGeoMap::setTilt(qreal tilt)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QDeclarativeGeoMap7setTiltEd(
    QDeclarativeGeoMap *self,
    qreal tilt) {
  self->setTilt(tilt);
}

//  qreal QDeclarativeGeoMap::tilt() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK18QDeclarativeGeoMap4tiltEv(const QDeclarativeGeoMap *self) {
  return self->tilt();
}

//  void QDeclarativeGeoMap::setMinimumTilt(qreal minimumTilt, bool userSet)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QDeclarativeGeoMap14setMinimumTiltEdb(
    QDeclarativeGeoMap *self,
    qreal minimumTilt,
    bool userSet) {
  self->setMinimumTilt(minimumTilt, userSet);
}

//  qreal QDeclarativeGeoMap::minimumTilt() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK18QDeclarativeGeoMap11minimumTiltEv(
    const QDeclarativeGeoMap *self) {
  return self->minimumTilt();
}

//  void QDeclarativeGeoMap::setMaximumTilt(qreal maximumTilt, bool userSet)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QDeclarativeGeoMap14setMaximumTiltEdb(
    QDeclarativeGeoMap *self,
    qreal maximumTilt,
    bool userSet) {
  self->setMaximumTilt(maximumTilt, userSet);
}

//  qreal QDeclarativeGeoMap::maximumTilt() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK18QDeclarativeGeoMap11maximumTiltEv(
    const QDeclarativeGeoMap *self) {
  return self->maximumTilt();
}

//  void QDeclarativeGeoMap::setFieldOfView(qreal fieldOfView)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QDeclarativeGeoMap14setFieldOfViewEd(
    QDeclarativeGeoMap *self,
    qreal fieldOfView) {
  self->setFieldOfView(fieldOfView);
}

//  qreal QDeclarativeGeoMap::fieldOfView() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK18QDeclarativeGeoMap11fieldOfViewEv(
    const QDeclarativeGeoMap *self) {
  return self->fieldOfView();
}

//  void QDeclarativeGeoMap::setMinimumFieldOfView(qreal minimumFieldOfView,
//      bool userSet)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QDeclarativeGeoMap21setMinimumFieldOfViewEdb(
    QDeclarativeGeoMap *self,
    qreal minimumFieldOfView,
    bool userSet) {
  self->setMinimumFieldOfView(minimumFieldOfView, userSet);
}

//  qreal QDeclarativeGeoMap::minimumFieldOfView() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK18QDeclarativeGeoMap18minimumFieldOfViewEv(
    const QDeclarativeGeoMap *self) {
  return self->minimumFieldOfView();
}

//  void QDeclarativeGeoMap::setMaximumFieldOfView(qreal maximumFieldOfView,
//      bool userSet)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QDeclarativeGeoMap21setMaximumFieldOfViewEdb(
    QDeclarativeGeoMap *self,
    qreal maximumFieldOfView,
    bool userSet) {
  self->setMaximumFieldOfView(maximumFieldOfView, userSet);
}

//  qreal QDeclarativeGeoMap::maximumFieldOfView() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK18QDeclarativeGeoMap18maximumFieldOfViewEv(
    const QDeclarativeGeoMap *self) {
  return self->maximumFieldOfView();
}

//  void QDeclarativeGeoMap::setCenter(const QGeoCoordinate &center)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QDeclarativeGeoMap9setCenterERK14QGeoCoordinate(
    QDeclarativeGeoMap *self,
    const QGeoCoordinate *center) {
  self->setCenter(*center);
}

//  QGeoCoordinate QDeclarativeGeoMap::center() const
extern "C" Q_DECL_EXPORT
QGeoCoordinate *ritual_ZNK18QDeclarativeGeoMap6centerEv(
    const QDeclarativeGeoMap *self) {
  return new QGeoCoordinate(self->center());
}

//  void QDeclarativeGeoMap::setVisibleRegion(const QGeoShape &shape)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QDeclarativeGeoMap16setVisibleRegionERK9QGeoShape(
    QDeclarativeGeoMap *self,
    const QGeoShape *shape) {
  self->setVisibleRegion(*shape);
}

//  QGeoShape QDeclarativeGeoMap::visibleRegion() const
extern "C" Q_DECL_EXPORT
QGeoShape *ritual_ZNK18QDeclarativeGeoMap13visibleRegionEv(
    const QDeclarativeGeoMap *self) {
  return new QGeoShape(self->visibleRegion());
}

//  void QDeclarativeGeoMap::setCopyrightsVisible(bool visible)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QDeclarativeGeoMap20setCopyrightsVisibleEb(
    QDeclarativeGeoMap *self,
    bool visible) {
  self->setCopyrightsVisible(visible);
}

//  bool QDeclarativeGeoMap::copyrightsVisible() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK18QDeclarativeGeoMap17copyrightsVisibleEv(
    const QDeclarativeGeoMap *self) {
  return self->copyrightsVisible();
}

//  void QDeclarativeGeoMap::setColor(const QColor &color)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QDeclarativeGeoMap8setColorERK6QColor(
    QDeclarativeGeoMap *self,
    const QColor *color) {
  self->setColor(*color);
}

//  QColor QDeclarativeGeoMap::color() const
extern "C" Q_DECL_EXPORT
QColor *ritual_ZNK18QDeclarativeGeoMap5colorEv(
    const QDeclarativeGeoMap *self) {
  return new QColor(self->color());
}

//  QRectF QDeclarativeGeoMap::visibleArea() const
extern "C" Q_DECL_EXPORT
QRectF *ritual_ZNK18QDeclarativeGeoMap11visibleAreaEv(
    const QDeclarativeGeoMap *self) {
  return new QRectF(self->visibleArea());
}

//  void QDeclarativeGeoMap::setVisibleArea(const QRectF &visibleArea)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QDeclarativeGeoMap14setVisibleAreaERK6QRectF(
    QDeclarativeGeoMap *self,
    const QRectF *visibleArea) {
  self->setVisibleArea(*visibleArea);
}

//  bool QDeclarativeGeoMap::mapReady() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK18QDeclarativeGeoMap8mapReadyEv(
    const QDeclarativeGeoMap *self) {
  return self->mapReady();
}

//  QList<QGeoMapType> QDeclarativeGeoMap::supportedMapTypes()
extern "C" Q_DECL_EXPORT
QList<QGeoMapType> *ritual_ZN18QDeclarativeGeoMap17supportedMapTypesEv(
    QDeclarativeGeoMap *self) {
  return new QList<QGeoMapType>(self->supportedMapTypes());
}

//  void QDeclarativeGeoMap::setBearing(qreal bearing, const QGeoCoordinate
//      &coordinate)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QDeclarativeGeoMap10setBearingEdRK14QGeoCoordinate(
    QDeclarativeGeoMap *self,
    qreal bearing,
    const QGeoCoordinate *coordinate) {
  self->setBearing(bearing, *coordinate);
}

//  void QDeclarativeGeoMap::alignCoordinateToPoint(const QGeoCoordinate
//      &coordinate, const QPointF &point)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QDeclarativeGeoMap22alignCoordinateToPointERK14QGeoCoordinateRK7QPointF(
    QDeclarativeGeoMap *self,
    const QGeoCoordinate *coordinate,
    const QPointF *point) {
  self->alignCoordinateToPoint(*coordinate, *point);
}

//  void QDeclarativeGeoMap::removeMapItem(QDeclarativeGeoMapItemBase *item)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QDeclarativeGeoMap13removeMapItemEP26QDeclarativeGeoMapItemBase(
    QDeclarativeGeoMap *self,
    QDeclarativeGeoMapItemBase *item) {
  self->removeMapItem(item);
}

//  void QDeclarativeGeoMap::addMapItem(QDeclarativeGeoMapItemBase *item)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QDeclarativeGeoMap10addMapItemEP26QDeclarativeGeoMapItemBase(
    QDeclarativeGeoMap *self,
    QDeclarativeGeoMapItemBase *item) {
  self->addMapItem(item);
}

//  void QDeclarativeGeoMap::addMapItemGroup(QDeclarativeGeoMapItemGroup
//      *itemGroup)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QDeclarativeGeoMap15addMapItemGroupEP27QDeclarativeGeoMapItemGroup(
    QDeclarativeGeoMap *self,
    QDeclarativeGeoMapItemGroup *itemGroup) {
  self->addMapItemGroup(itemGroup);
}

//  void QDeclarativeGeoMap::removeMapItemGroup(QDeclarativeGeoMapItemGroup
//      *itemGroup)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QDeclarativeGeoMap18removeMapItemGroupEP27QDeclarativeGeoMapItemGroup(
    QDeclarativeGeoMap *self,
    QDeclarativeGeoMapItemGroup *itemGroup) {
  self->removeMapItemGroup(itemGroup);
}

//  void QDeclarativeGeoMap::removeMapItemView(QDeclarativeGeoMapItemView
//      *itemView)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QDeclarativeGeoMap17removeMapItemViewEP26QDeclarativeGeoMapItemView(
    QDeclarativeGeoMap *self,
    QDeclarativeGeoMapItemView *itemView) {
  self->removeMapItemView(itemView);
}

//  void QDeclarativeGeoMap::addMapItemView(QDeclarativeGeoMapItemView
//      *itemView)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QDeclarativeGeoMap14addMapItemViewEP26QDeclarativeGeoMapItemView(
    QDeclarativeGeoMap *self,
    QDeclarativeGeoMapItemView *itemView) {
  self->addMapItemView(itemView);
}

//  void QDeclarativeGeoMap::clearMapItems()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QDeclarativeGeoMap13clearMapItemsEv(
    QDeclarativeGeoMap *self) {
  self->clearMapItems();
}

//  QList<QObject *> QDeclarativeGeoMap::mapItems()
extern "C" Q_DECL_EXPORT
QList<QObject *> *ritual_ZN18QDeclarativeGeoMap8mapItemsEv(
    QDeclarativeGeoMap *self) {
  return new QList<QObject *>(self->mapItems());
}

//  QGeoCoordinate QDeclarativeGeoMap::toCoordinate(const QPointF &position,
//      bool clipToViewPort) const
extern "C" Q_DECL_EXPORT
QGeoCoordinate *ritual_ZNK18QDeclarativeGeoMap12toCoordinateERK7QPointFb(
    const QDeclarativeGeoMap *self,
    const QPointF *position,
    bool clipToViewPort) {
  return new QGeoCoordinate(self->toCoordinate(*position, clipToViewPort));
}

//  QPointF QDeclarativeGeoMap::fromCoordinate(const QGeoCoordinate
//      &coordinate, bool clipToViewPort) const
extern "C" Q_DECL_EXPORT
QPointF *ritual_ZNK18QDeclarativeGeoMap14fromCoordinateERK14QGeoCoordinateb(
    const QDeclarativeGeoMap *self,
    const QGeoCoordinate *coordinate,
    bool clipToViewPort) {
  return new QPointF(self->fromCoordinate(*coordinate, clipToViewPort));
}

//  void QDeclarativeGeoMap::fitViewportToMapItems(const QVariantList &items)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QDeclarativeGeoMap21fitViewportToMapItemsERK5QListI8QVariantE(
    QDeclarativeGeoMap *self,
    const QList<QVariant> *items) {
  self->fitViewportToMapItems(*items);
}

//  void QDeclarativeGeoMap::fitViewportToVisibleMapItems()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QDeclarativeGeoMap28fitViewportToVisibleMapItemsEv(
    QDeclarativeGeoMap *self) {
  self->fitViewportToVisibleMapItems();
}

//  void QDeclarativeGeoMap::pan(int dx, int dy)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QDeclarativeGeoMap3panEii(
    QDeclarativeGeoMap *self,
    int dx,
    int dy) {
  self->pan(dx, dy);
}

//  void QDeclarativeGeoMap::prefetchData()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QDeclarativeGeoMap12prefetchDataEv(
    QDeclarativeGeoMap *self) {
  self->prefetchData();
}

//  void QDeclarativeGeoMap::clearData()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QDeclarativeGeoMap9clearDataEv(QDeclarativeGeoMap *self) {
  self->clearData();
}

//  void QDeclarativeGeoMap::fitViewportToGeoShape(const QGeoShape &shape,
//      QVariant margins)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QDeclarativeGeoMap21fitViewportToGeoShapeERK9QGeoShape8QVariant(
    QDeclarativeGeoMap *self,
    const QGeoShape *shape,
    const QVariant *margins) {
  self->fitViewportToGeoShape(*shape, *margins);
}

//  void QDeclarativeGeoMap::fitViewportToGeoShape(const QGeoShape &shape,
//      const QMargins &borders)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QDeclarativeGeoMap21fitViewportToGeoShapeERK9QGeoShapeRK8QMargins(
    QDeclarativeGeoMap *self,
    const QGeoShape *shape,
    const QMargins *borders) {
  self->fitViewportToGeoShape(*shape, *borders);
}

//  QString QDeclarativeGeoMap::errorString() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK18QDeclarativeGeoMap11errorStringEv(
    const QDeclarativeGeoMap *self) {
  return new QString(self->errorString());
}

//  QGeoServiceProvider::Error QDeclarativeGeoMap::error() const
extern "C" Q_DECL_EXPORT
QGeoServiceProvider::Error ritual_ZNK18QDeclarativeGeoMap5errorEv(
    const QDeclarativeGeoMap *self) {
  return self->error();
}

//  QGeoMap *QDeclarativeGeoMap::map() const
extern "C" Q_DECL_EXPORT
QGeoMap *ritual_ZNK18QDeclarativeGeoMap3mapEv(
    const QDeclarativeGeoMap *self) {
  return self->map();
}

//  void QDeclarativeGeoMap::itemChange(ItemChange a0, const ItemChangeData
//      &a1)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QDeclarativeGeoMap10itemChangeEN10QQuickItem10ItemChangeERKNS0_14ItemChangeDataE(
    QDeclarativeGeoMap *self,
    QQuickItem::ItemChange a0,
    const QQuickItem::ItemChangeData *a1) {
  self->itemChange(a0, *a1);
}

//  void QDeclarativeGeoMap::pluginChanged(QDeclarativeGeoServiceProvider
//      *plugin)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QDeclarativeGeoMap13pluginChangedEP30QDeclarativeGeoServiceProvider(
    QDeclarativeGeoMap *self,
    QDeclarativeGeoServiceProvider *plugin) {
  self->pluginChanged(plugin);
}

//  void QDeclarativeGeoMap::zoomLevelChanged(qreal zoomLevel)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QDeclarativeGeoMap16zoomLevelChangedEd(
    QDeclarativeGeoMap *self,
    qreal zoomLevel) {
  self->zoomLevelChanged(zoomLevel);
}

//  void QDeclarativeGeoMap::centerChanged(const QGeoCoordinate &coordinate)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QDeclarativeGeoMap13centerChangedERK14QGeoCoordinate(
    QDeclarativeGeoMap *self,
    const QGeoCoordinate *coordinate) {
  self->centerChanged(*coordinate);
}

//  void QDeclarativeGeoMap::activeMapTypeChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QDeclarativeGeoMap20activeMapTypeChangedEv(
    QDeclarativeGeoMap *self) {
  self->activeMapTypeChanged();
}

//  void QDeclarativeGeoMap::supportedMapTypesChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QDeclarativeGeoMap24supportedMapTypesChangedEv(
    QDeclarativeGeoMap *self) {
  self->supportedMapTypesChanged();
}

//  void QDeclarativeGeoMap::minimumZoomLevelChanged(qreal minimumZoomLevel)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QDeclarativeGeoMap23minimumZoomLevelChangedEd(
    QDeclarativeGeoMap *self,
    qreal minimumZoomLevel) {
  self->minimumZoomLevelChanged(minimumZoomLevel);
}

//  void QDeclarativeGeoMap::maximumZoomLevelChanged(qreal maximumZoomLevel)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QDeclarativeGeoMap23maximumZoomLevelChangedEd(
    QDeclarativeGeoMap *self,
    qreal maximumZoomLevel) {
  self->maximumZoomLevelChanged(maximumZoomLevel);
}

//  void QDeclarativeGeoMap::mapItemsChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QDeclarativeGeoMap15mapItemsChangedEv(
    QDeclarativeGeoMap *self) {
  self->mapItemsChanged();
}

//  void QDeclarativeGeoMap::errorChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QDeclarativeGeoMap12errorChangedEv(
    QDeclarativeGeoMap *self) {
  self->errorChanged();
}

//  void QDeclarativeGeoMap::copyrightLinkActivated(const QString &link)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QDeclarativeGeoMap22copyrightLinkActivatedERK7QString(
    QDeclarativeGeoMap *self,
    const QString *link) {
  self->copyrightLinkActivated(*link);
}

//  void QDeclarativeGeoMap::copyrightsVisibleChanged(bool visible)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QDeclarativeGeoMap24copyrightsVisibleChangedEb(
    QDeclarativeGeoMap *self,
    bool visible) {
  self->copyrightsVisibleChanged(visible);
}

//  void QDeclarativeGeoMap::colorChanged(const QColor &color)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QDeclarativeGeoMap12colorChangedERK6QColor(
    QDeclarativeGeoMap *self,
    const QColor *color) {
  self->colorChanged(*color);
}

//  void QDeclarativeGeoMap::bearingChanged(qreal bearing)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QDeclarativeGeoMap14bearingChangedEd(
    QDeclarativeGeoMap *self,
    qreal bearing) {
  self->bearingChanged(bearing);
}

//  void QDeclarativeGeoMap::tiltChanged(qreal tilt)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QDeclarativeGeoMap11tiltChangedEd(
    QDeclarativeGeoMap *self,
    qreal tilt) {
  self->tiltChanged(tilt);
}

//  void QDeclarativeGeoMap::fieldOfViewChanged(qreal fieldOfView)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QDeclarativeGeoMap18fieldOfViewChangedEd(
    QDeclarativeGeoMap *self,
    qreal fieldOfView) {
  self->fieldOfViewChanged(fieldOfView);
}

//  void QDeclarativeGeoMap::minimumTiltChanged(qreal minimumTilt)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QDeclarativeGeoMap18minimumTiltChangedEd(
    QDeclarativeGeoMap *self,
    qreal minimumTilt) {
  self->minimumTiltChanged(minimumTilt);
}

//  void QDeclarativeGeoMap::maximumTiltChanged(qreal maximumTilt)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QDeclarativeGeoMap18maximumTiltChangedEd(
    QDeclarativeGeoMap *self,
    qreal maximumTilt) {
  self->maximumTiltChanged(maximumTilt);
}

//  void QDeclarativeGeoMap::minimumFieldOfViewChanged(qreal
//      minimumFieldOfView)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QDeclarativeGeoMap25minimumFieldOfViewChangedEd(
    QDeclarativeGeoMap *self,
    qreal minimumFieldOfView) {
  self->minimumFieldOfViewChanged(minimumFieldOfView);
}

//  void QDeclarativeGeoMap::maximumFieldOfViewChanged(qreal
//      maximumFieldOfView)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QDeclarativeGeoMap25maximumFieldOfViewChangedEd(
    QDeclarativeGeoMap *self,
    qreal maximumFieldOfView) {
  self->maximumFieldOfViewChanged(maximumFieldOfView);
}

//  void QDeclarativeGeoMap::copyrightsImageChanged(const QImage
//      &copyrightsImage)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QDeclarativeGeoMap22copyrightsImageChangedERK6QImage(
    QDeclarativeGeoMap *self,
    const QImage *copyrightsImage) {
  self->copyrightsImageChanged(*copyrightsImage);
}

//  void QDeclarativeGeoMap::copyrightsChanged(const QString &copyrightsHtml)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QDeclarativeGeoMap17copyrightsChangedERK7QString(
    QDeclarativeGeoMap *self,
    const QString *copyrightsHtml) {
  self->copyrightsChanged(*copyrightsHtml);
}

//  void QDeclarativeGeoMap::mapReadyChanged(bool ready)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QDeclarativeGeoMap15mapReadyChangedEb(
    QDeclarativeGeoMap *self,
    bool ready) {
  self->mapReadyChanged(ready);
}

//  void QDeclarativeGeoMap::visibleAreaChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QDeclarativeGeoMap18visibleAreaChangedEv(
    QDeclarativeGeoMap *self) {
  self->visibleAreaChanged();
}

//  void QDeclarativeGeoMap::visibleRegionChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QDeclarativeGeoMap20visibleRegionChangedEv(
    QDeclarativeGeoMap *self) {
  self->visibleRegionChanged();
}

//  void QDeclarativeGeoMap::componentComplete()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QDeclarativeGeoMap17componentCompleteEv(
    QDeclarativeGeoMap *self) {
  self->componentComplete();
}

//  QSGNode *QDeclarativeGeoMap::updatePaintNode(QSGNode *a0,
//      UpdatePaintNodeData *a1)
extern "C" Q_DECL_EXPORT
QSGNode *ritual_ZN18QDeclarativeGeoMap15updatePaintNodeEP7QSGNodePN10QQuickItem19UpdatePaintNodeDataE(
    QDeclarativeGeoMap *self,
    QSGNode *a0,
    QQuickItem::UpdatePaintNodeData *a1) {
  return self->updatePaintNode(a0, a1);
}

//  void QDeclarativeGeoMap::geometryChange(const QRectF &newGeometry, const
//      QRectF &oldGeometry)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QDeclarativeGeoMap14geometryChangeERK6QRectFS2_(
    QDeclarativeGeoMap *self,
    const QRectF *newGeometry,
    const QRectF *oldGeometry) {
  self->geometryChange(*newGeometry, *oldGeometry);
}

//  void QDeclarativeGeoMap::setError(QGeoServiceProvider::Error error, const
//      QString &errorString)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QDeclarativeGeoMap8setErrorEN19QGeoServiceProvider5ErrorERK7QString(
    QDeclarativeGeoMap *self,
    QGeoServiceProvider::Error error,
    const QString *errorString) {
  self->setError(error, *errorString);
}

//  void QDeclarativeGeoMap::initialize()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QDeclarativeGeoMap10initializeEv(QDeclarativeGeoMap *self) {
  self->initialize();
}

//  void QDeclarativeGeoMap::setZoomLevel(qreal zoomLevel, bool overzoom)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QDeclarativeGeoMap12setZoomLevelEdb(
    QDeclarativeGeoMap *self,
    qreal zoomLevel,
    bool overzoom) {
  self->setZoomLevel(zoomLevel, overzoom);
}

//  bool QDeclarativeGeoMap::addMapChild(QObject *child)
extern "C" Q_DECL_EXPORT
bool ritual_ZN18QDeclarativeGeoMap11addMapChildEP7QObject(
    QDeclarativeGeoMap *self,
    QObject *child) {
  return self->addMapChild(child);
}

//  bool QDeclarativeGeoMap::removeMapChild(QObject *child)
extern "C" Q_DECL_EXPORT
bool ritual_ZN18QDeclarativeGeoMap14removeMapChildEP7QObject(
    QDeclarativeGeoMap *self,
    QObject *child) {
  return self->removeMapChild(child);
}

//  bool QDeclarativeGeoMap::isGroupNested(QDeclarativeGeoMapItemGroup
//      *group) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK18QDeclarativeGeoMap13isGroupNestedEP27QDeclarativeGeoMapItemGroup(
    const QDeclarativeGeoMap *self,
    QDeclarativeGeoMapItemGroup *group) {
  return self->isGroupNested(group);
}

//  bool QDeclarativeGeoMap::addMapItem_real(QDeclarativeGeoMapItemBase
//      *item)
extern "C" Q_DECL_EXPORT
bool ritual_ZN18QDeclarativeGeoMap15addMapItem_realEP26QDeclarativeGeoMapItemBase(
    QDeclarativeGeoMap *self,
    QDeclarativeGeoMapItemBase *item) {
  return self->addMapItem_real(item);
}

//  bool QDeclarativeGeoMap::removeMapItem_real(QDeclarativeGeoMapItemBase
//      *item)
extern "C" Q_DECL_EXPORT
bool ritual_ZN18QDeclarativeGeoMap18removeMapItem_realEP26QDeclarativeGeoMapItemBase(
    QDeclarativeGeoMap *self,
    QDeclarativeGeoMapItemBase *item) {
  return self->removeMapItem_real(item);
}

//  bool QDeclarativeGeoMap::addMapItemGroup_real(QDeclarativeGeoMapItemGroup
//      *itemGroup)
extern "C" Q_DECL_EXPORT
bool ritual_ZN18QDeclarativeGeoMap20addMapItemGroup_realEP27QDeclarativeGeoMapItemGroup(
    QDeclarativeGeoMap *self,
    QDeclarativeGeoMapItemGroup *itemGroup) {
  return self->addMapItemGroup_real(itemGroup);
}

//  bool
//      QDeclarativeGeoMap::removeMapItemGroup_real(QDeclarativeGeoMapItemGro
//      up *itemGroup)
extern "C" Q_DECL_EXPORT
bool ritual_ZN18QDeclarativeGeoMap23removeMapItemGroup_realEP27QDeclarativeGeoMapItemGroup(
    QDeclarativeGeoMap *self,
    QDeclarativeGeoMapItemGroup *itemGroup) {
  return self->removeMapItemGroup_real(itemGroup);
}

//  bool QDeclarativeGeoMap::addMapItemView_real(QDeclarativeGeoMapItemView
//      *itemView)
extern "C" Q_DECL_EXPORT
bool ritual_ZN18QDeclarativeGeoMap19addMapItemView_realEP26QDeclarativeGeoMapItemView(
    QDeclarativeGeoMap *self,
    QDeclarativeGeoMapItemView *itemView) {
  return self->addMapItemView_real(itemView);
}

//  bool
//      QDeclarativeGeoMap::removeMapItemView_real(QDeclarativeGeoMapItemView
//      *itemView)
extern "C" Q_DECL_EXPORT
bool ritual_ZN18QDeclarativeGeoMap22removeMapItemView_realEP26QDeclarativeGeoMapItemView(
    QDeclarativeGeoMap *self,
    QDeclarativeGeoMapItemView *itemView) {
  return self->removeMapItemView_real(itemView);
}

//  void QDeclarativeGeoMap::updateItemToWindowTransform()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QDeclarativeGeoMap27updateItemToWindowTransformEv(
    QDeclarativeGeoMap *self) {
  self->updateItemToWindowTransform();
}

//  void QDeclarativeGeoMap::onSGNodeChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QDeclarativeGeoMap15onSGNodeChangedEv(
    QDeclarativeGeoMap *self) {
  self->onSGNodeChanged();
}

//  void QDeclarativeGeoMap::mappingManagerInitialized()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QDeclarativeGeoMap25mappingManagerInitializedEv(
    QDeclarativeGeoMap *self) {
  self->mappingManagerInitialized();
}

//  void QDeclarativeGeoMap::pluginReady()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QDeclarativeGeoMap11pluginReadyEv(QDeclarativeGeoMap *self) {
  self->pluginReady();
}

//  void QDeclarativeGeoMap::onSupportedMapTypesChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QDeclarativeGeoMap26onSupportedMapTypesChangedEv(
    QDeclarativeGeoMap *self) {
  self->onSupportedMapTypesChanged();
}

//  void QDeclarativeGeoMap::onCameraCapabilitiesChanged(const
//      QGeoCameraCapabilities &oldCameraCapabilities)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QDeclarativeGeoMap27onCameraCapabilitiesChangedERK22QGeoCameraCapabilities(
    QDeclarativeGeoMap *self,
    const QGeoCameraCapabilities *oldCameraCapabilities) {
  self->onCameraCapabilitiesChanged(*oldCameraCapabilities);
}

//  void QDeclarativeGeoMap::onAttachedCopyrightNoticeVisibilityChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QDeclarativeGeoMap42onAttachedCopyrightNoticeVisibilityChangedEv(
    QDeclarativeGeoMap *self) {
  self->onAttachedCopyrightNoticeVisibilityChanged();
}

//  void QDeclarativeGeoMap::onCameraDataChanged(const QGeoCameraData
//      &cameraData)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QDeclarativeGeoMap19onCameraDataChangedERK14QGeoCameraData(
    QDeclarativeGeoMap *self,
    const QGeoCameraData *cameraData) {
  self->onCameraDataChanged(*cameraData);
}

//  void QDeclarativeGeoMap::setupMapView(QDeclarativeGeoMapItemView *view)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QDeclarativeGeoMap12setupMapViewEP26QDeclarativeGeoMapItemView(
    QDeclarativeGeoMap *self,
    QDeclarativeGeoMapItemView *view) {
  self->setupMapView(view);
}

//  void QDeclarativeGeoMap::populateMap()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QDeclarativeGeoMap11populateMapEv(QDeclarativeGeoMap *self) {
  self->populateMap();
}

//  void QDeclarativeGeoMap::fitViewportToMapItemsRefine(const
//      QList<QPointer<QDeclarativeGeoMapItemBase>> &mapItems, bool refine,
//      bool onlyVisible)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QDeclarativeGeoMap27fitViewportToMapItemsRefineERK5QListI8QPointerI26QDeclarativeGeoMapItemBaseEEbb(
    QDeclarativeGeoMap *self,
    const QList<QPointer<QDeclarativeGeoMapItemBase>> *mapItems,
    bool refine,
    bool onlyVisible) {
  self->fitViewportToMapItemsRefine(*mapItems, refine, onlyVisible);
}

//  void QDeclarativeGeoMap::attachCopyrightNotice(bool initialVisibility)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QDeclarativeGeoMap21attachCopyrightNoticeEb(
    QDeclarativeGeoMap *self,
    bool initialVisibility) {
  self->attachCopyrightNotice(initialVisibility);
}

//  void QDeclarativeGeoMap::detachCopyrightNotice(bool currentVisibility)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QDeclarativeGeoMap21detachCopyrightNoticeEb(
    QDeclarativeGeoMap *self,
    bool currentVisibility) {
  self->detachCopyrightNotice(currentVisibility);
}

//  QMargins QDeclarativeGeoMap::mapMargins() const
extern "C" Q_DECL_EXPORT
QMargins *ritual_ZNK18QDeclarativeGeoMap10mapMarginsEv(
    const QDeclarativeGeoMap *self) {
  return new QMargins(self->mapMargins());
}

//  a Python function taken by a CuteQDeclarativeGeoMap, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QDeclarativeGeoMap(
    QDeclarativeGeoMap *self,
    const char *key,
    void *call) {
  return static_cast<CuteQDeclarativeGeoMap *>(self)->take(key, call);
}

//  void QDeclarativeGeoMap::itemChange(ItemChange a0, const ItemChangeData
//      &a1)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN18QDeclarativeGeoMap10itemChangeEN10QQuickItem10ItemChangeERKNS0_14ItemChangeDataE(
    QDeclarativeGeoMap *self,
    QQuickItem::ItemChange a0,
    const QQuickItem::ItemChangeData *a1) {
  self->QDeclarativeGeoMap::itemChange(a0, *a1);
}

//  void QDeclarativeGeoMap::componentComplete()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN18QDeclarativeGeoMap17componentCompleteEv(
    QDeclarativeGeoMap *self) {
  static_cast<OwnQDeclarativeGeoMap *>(self)->OwnQDeclarativeGeoMap::componentComplete();
}

//  QSGNode *QDeclarativeGeoMap::updatePaintNode(QSGNode *a0,
//      UpdatePaintNodeData *a1)
extern "C" Q_DECL_EXPORT
QSGNode *ritual_own_ZN18QDeclarativeGeoMap15updatePaintNodeEP7QSGNodePN10QQuickItem19UpdatePaintNodeDataE(
    QDeclarativeGeoMap *self,
    QSGNode *a0,
    QQuickItem::UpdatePaintNodeData *a1) {
  return static_cast<OwnQDeclarativeGeoMap *>(self)->OwnQDeclarativeGeoMap::updatePaintNode(
      a0,
      a1);
}

//  void QDeclarativeGeoMap::geometryChange(const QRectF &newGeometry, const
//      QRectF &oldGeometry)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN18QDeclarativeGeoMap14geometryChangeERK6QRectFS2_(
    QDeclarativeGeoMap *self,
    const QRectF *newGeometry,
    const QRectF *oldGeometry) {
  static_cast<OwnQDeclarativeGeoMap *>(self)->OwnQDeclarativeGeoMap::geometryChange(
      *newGeometry,
      *oldGeometry);
}
