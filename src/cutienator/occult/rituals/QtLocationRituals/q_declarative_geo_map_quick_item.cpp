//  Written by dev_tooling.RitualGenerator from the records of
//  QtLocation/6.12.0/QtLocation/private/qdeclarativegeomapquickitem_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtGui/qtguiglobal.h>
#include <QtQuick/qtquickglobal.h>
#include <QtLocation/6.12.0/QtLocation/private/qlocationglobal_p.h>
#include <QtLocation/QtLocation>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtLocation/6.12.0/QtLocation/private/qdeclarativegeomapquickitem_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtPositioning/qgeocoordinate.h>
#include <QtCore/qpoint.h>
#include <QtPositioning/qgeoshape.h>
#include <QtCore/qrect.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtLocation/6.12.0/QtLocation/private/qdeclarativegeomapitembase_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qvariant.h>
#include <QtQuick/QtQuick>
#include <QtQuick/qquickitem.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  Only a class built on QDeclarativeGeoMapQuickItem may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQDeclarativeGeoMapQuickItem : QDeclarativeGeoMapQuickItem {
  using QDeclarativeGeoMapQuickItem::geometryChange;
  using QDeclarativeGeoMapQuickItem::updatePolish;
  using QDeclarativeGeoMapQuickItem::afterChildrenChanged;
  using QDeclarativeGeoMapQuickItem::afterViewportChanged;
};

//  A QDeclarativeGeoMapQuickItem that Python can take functions over in. Every QDeclarativeGeoMapQuickItem
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQDeclarativeGeoMapQuickItemCall0)(const void *, QDeclarativeGeoMap *, QGeoMap *, int *);
typedef const QGeoShape * (*CuteQDeclarativeGeoMapQuickItemCall1)(const void *, int *);
typedef void (*CuteQDeclarativeGeoMapQuickItemCall2)(const void *, const QGeoShape *, int *);
typedef bool (*CuteQDeclarativeGeoMapQuickItemCall3)(const void *, const QPointF *, int *);
typedef void (*CuteQDeclarativeGeoMapQuickItemCall4)(const void *, const QRectF *, const QRectF *, int *);
typedef void (*CuteQDeclarativeGeoMapQuickItemCall5)(const void *, int *);
typedef void (*CuteQDeclarativeGeoMapQuickItemCall6)(const void *, int *);
typedef void (*CuteQDeclarativeGeoMapQuickItemCall7)(const void *, const QGeoMapViewportChangeEvent *, int *);
typedef void (*CuteQDeclarativeGeoMapQuickItemCall8)(const void *, const QGeoCoordinate *, const QPointF *, int *);
typedef void * (*CuteQDeclarativeGeoMapQuickItemCall9)(const void *, QSGNode *, QQuickItem::UpdatePaintNodeData *, int *);
typedef void * (*CuteQDeclarativeGeoMapQuickItemCall10)(const void *, QSGNode *, QQuickItem::UpdatePaintNodeData *, int *);
typedef const QRectF * (*CuteQDeclarativeGeoMapQuickItemCall11)(const void *, int *);
typedef const QRectF * (*CuteQDeclarativeGeoMapQuickItemCall12)(const void *, int *);
#if QT_CONFIG(im)
typedef const QVariant * (*CuteQDeclarativeGeoMapQuickItemCall13)(const void *, int, int *);
#endif  // QT_CONFIG(im)
typedef bool (*CuteQDeclarativeGeoMapQuickItemCall14)(const void *, int *);
typedef void * (*CuteQDeclarativeGeoMapQuickItemCall15)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQDeclarativeGeoMapQuickItemCall16)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
typedef void (*CuteQDeclarativeGeoMapQuickItemCall17)(const void *, int, const QQuickItem::ItemChangeData *, int *);
typedef void (*CuteQDeclarativeGeoMapQuickItemCall18)(const void *, int *);
typedef void (*CuteQDeclarativeGeoMapQuickItemCall19)(const void *, int *);
typedef void (*CuteQDeclarativeGeoMapQuickItemCall20)(const void *, QKeyEvent *, int *);
typedef void (*CuteQDeclarativeGeoMapQuickItemCall21)(const void *, QKeyEvent *, int *);
#if QT_CONFIG(im)
typedef void (*CuteQDeclarativeGeoMapQuickItemCall22)(const void *, QInputMethodEvent *, int *);
#endif  // QT_CONFIG(im)
typedef void (*CuteQDeclarativeGeoMapQuickItemCall23)(const void *, QFocusEvent *, int *);
typedef void (*CuteQDeclarativeGeoMapQuickItemCall24)(const void *, QFocusEvent *, int *);
typedef void (*CuteQDeclarativeGeoMapQuickItemCall25)(const void *, QMouseEvent *, int *);
typedef void (*CuteQDeclarativeGeoMapQuickItemCall26)(const void *, QMouseEvent *, int *);
typedef void (*CuteQDeclarativeGeoMapQuickItemCall27)(const void *, QMouseEvent *, int *);
typedef void (*CuteQDeclarativeGeoMapQuickItemCall28)(const void *, QMouseEvent *, int *);
typedef void (*CuteQDeclarativeGeoMapQuickItemCall29)(const void *, int *);
typedef void (*CuteQDeclarativeGeoMapQuickItemCall30)(const void *, int *);
#if QT_CONFIG(wheelevent)
typedef void (*CuteQDeclarativeGeoMapQuickItemCall31)(const void *, QWheelEvent *, int *);
#endif  // QT_CONFIG(wheelevent)
typedef void (*CuteQDeclarativeGeoMapQuickItemCall32)(const void *, QTouchEvent *, int *);
typedef void (*CuteQDeclarativeGeoMapQuickItemCall33)(const void *, QHoverEvent *, int *);
typedef void (*CuteQDeclarativeGeoMapQuickItemCall34)(const void *, QHoverEvent *, int *);
typedef void (*CuteQDeclarativeGeoMapQuickItemCall35)(const void *, QHoverEvent *, int *);
#if QT_CONFIG(quick_draganddrop)
typedef void (*CuteQDeclarativeGeoMapQuickItemCall36)(const void *, QDragEnterEvent *, int *);
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
typedef void (*CuteQDeclarativeGeoMapQuickItemCall37)(const void *, QDragMoveEvent *, int *);
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
typedef void (*CuteQDeclarativeGeoMapQuickItemCall38)(const void *, QDragLeaveEvent *, int *);
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
typedef void (*CuteQDeclarativeGeoMapQuickItemCall39)(const void *, QDropEvent *, int *);
#endif  // QT_CONFIG(quick_draganddrop)
typedef bool (*CuteQDeclarativeGeoMapQuickItemCall40)(const void *, QQuickItem *, QEvent *, int *);
typedef void (*CuteQDeclarativeGeoMapQuickItemCall41)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQDeclarativeGeoMapQuickItemCall42)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQDeclarativeGeoMapQuickItemCall43)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQDeclarativeGeoMapQuickItemCall44)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQDeclarativeGeoMapQuickItemCall45)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQDeclarativeGeoMapQuickItemCall46)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQDeclarativeGeoMapQuickItemCall47)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQDeclarativeGeoMapQuickItem : public QDeclarativeGeoMapQuickItem {
public:
  using QDeclarativeGeoMapQuickItem::QDeclarativeGeoMapQuickItem;
  void *taken[48] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN26QDeclarativeGeoMapItemBase6setMapEP18QDeclarativeGeoMapP7QGeoMap")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK26QDeclarativeGeoMapItemBase8geoShapeEv")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN26QDeclarativeGeoMapItemBase11setGeoShapeERK9QGeoShape")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK10QQuickItem8containsERK7QPointF")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem14geometryChangeERK6QRectFS2_")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem12updatePolishEv")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN26QDeclarativeGeoMapItemBase20afterChildrenChangedEv")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN26QDeclarativeGeoMapItemBase20afterViewportChangedERK26QGeoMapViewportChangeEvent")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN26QDeclarativeGeoMapItemBase16setPositionOnMapERK14QGeoCoordinateRK7QPointF")) {
      taken[8] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem15updatePaintNodeEP7QSGNodePNS_19UpdatePaintNodeDataE")) {
      taken[9] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN26QDeclarativeGeoMapItemBase22updateMapItemPaintNodeEP7QSGNodePN10QQuickItem19UpdatePaintNodeDataE")) {
      taken[10] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK10QQuickItem12boundingRectEv")) {
      taken[11] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK10QQuickItem8clipRectEv")) {
      taken[12] = call;
      return true;
    }
#if QT_CONFIG(im)
    if (!std::strcmp(key, "_ZNK10QQuickItem16inputMethodQueryEN2Qt16InputMethodQueryE")) {
      taken[13] = call;
      return true;
    }
#endif  // QT_CONFIG(im)
    if (!std::strcmp(key, "_ZNK10QQuickItem17isTextureProviderEv")) {
      taken[14] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK10QQuickItem15textureProviderEv")) {
      taken[15] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[16] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN10QQuickItem10itemChangeENS_10ItemChangeERKNS_14ItemChangeDataE")) {
      taken[17] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQmlParserStatus10classBeginEv")) {
      taken[18] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQmlParserStatus17componentCompleteEv")) {
      taken[19] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem13keyPressEventEP9QKeyEvent")) {
      taken[20] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem15keyReleaseEventEP9QKeyEvent")) {
      taken[21] = call;
      return true;
    }
#if QT_CONFIG(im)
    if (!std::strcmp(key, "_ZN10QQuickItem16inputMethodEventEP17QInputMethodEvent")) {
      taken[22] = call;
      return true;
    }
#endif  // QT_CONFIG(im)
    if (!std::strcmp(key, "_ZN10QQuickItem12focusInEventEP11QFocusEvent")) {
      taken[23] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem13focusOutEventEP11QFocusEvent")) {
      taken[24] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem15mousePressEventEP11QMouseEvent")) {
      taken[25] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem14mouseMoveEventEP11QMouseEvent")) {
      taken[26] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem17mouseReleaseEventEP11QMouseEvent")) {
      taken[27] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem21mouseDoubleClickEventEP11QMouseEvent")) {
      taken[28] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem16mouseUngrabEventEv")) {
      taken[29] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem16touchUngrabEventEv")) {
      taken[30] = call;
      return true;
    }
#if QT_CONFIG(wheelevent)
    if (!std::strcmp(key, "_ZN10QQuickItem10wheelEventEP11QWheelEvent")) {
      taken[31] = call;
      return true;
    }
#endif  // QT_CONFIG(wheelevent)
    if (!std::strcmp(key, "_ZN10QQuickItem10touchEventEP11QTouchEvent")) {
      taken[32] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem15hoverEnterEventEP11QHoverEvent")) {
      taken[33] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem14hoverMoveEventEP11QHoverEvent")) {
      taken[34] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem15hoverLeaveEventEP11QHoverEvent")) {
      taken[35] = call;
      return true;
    }
#if QT_CONFIG(quick_draganddrop)
    if (!std::strcmp(key, "_ZN10QQuickItem14dragEnterEventEP15QDragEnterEvent")) {
      taken[36] = call;
      return true;
    }
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
    if (!std::strcmp(key, "_ZN10QQuickItem13dragMoveEventEP14QDragMoveEvent")) {
      taken[37] = call;
      return true;
    }
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
    if (!std::strcmp(key, "_ZN10QQuickItem14dragLeaveEventEP15QDragLeaveEvent")) {
      taken[38] = call;
      return true;
    }
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
    if (!std::strcmp(key, "_ZN10QQuickItem9dropEventEP10QDropEvent")) {
      taken[39] = call;
      return true;
    }
#endif  // QT_CONFIG(quick_draganddrop)
    if (!std::strcmp(key, "_ZN10QQuickItem21childMouseEventFilterEPS_P6QEvent")) {
      taken[40] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem16releaseResourcesEv")) {
      taken[41] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[42] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[43] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[44] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[45] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[46] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[47] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

  //  void QDeclarativeGeoMapQuickItem::setMap(QDeclarativeGeoMap
  //      *quickMap, QGeoMap *map)
  void setMap(QDeclarativeGeoMap *quickMap, QGeoMap *map) override {
    if (taken[0]) {
      int handled = 0;
      CuteQDeclarativeGeoMapQuickItemCall0 call = reinterpret_cast<CuteQDeclarativeGeoMapQuickItemCall0>(taken[0]);
      call(this, quickMap, map, &handled);
      if (handled) return;
    }
    QDeclarativeGeoMapQuickItem::setMap(quickMap, map);
  }

  //  const QGeoShape &QDeclarativeGeoMapQuickItem::geoShape() const
  const QGeoShape &geoShape() const override {
    if (taken[1]) {
      int handled = 0;
      CuteQDeclarativeGeoMapQuickItemCall1 call = reinterpret_cast<CuteQDeclarativeGeoMapQuickItemCall1>(taken[1]);
      const QGeoShape * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QDeclarativeGeoMapQuickItem::geoShape();
  }

  //  void QDeclarativeGeoMapQuickItem::setGeoShape(const QGeoShape &shape)
  void setGeoShape(const QGeoShape &shape) override {
    if (taken[2]) {
      int handled = 0;
      CuteQDeclarativeGeoMapQuickItemCall2 call = reinterpret_cast<CuteQDeclarativeGeoMapQuickItemCall2>(taken[2]);
      call(this, &shape, &handled);
      if (handled) return;
    }
    QDeclarativeGeoMapQuickItem::setGeoShape(shape);
  }

  //  bool QDeclarativeGeoMapQuickItem::contains(const QPointF &point)
  //      const
  bool contains(const QPointF &point) const override {
    if (taken[3]) {
      int handled = 0;
      CuteQDeclarativeGeoMapQuickItemCall3 call = reinterpret_cast<CuteQDeclarativeGeoMapQuickItemCall3>(taken[3]);
      bool given = call(this, &point, &handled);
      if (handled) return given;
    }
    return QDeclarativeGeoMapQuickItem::contains(point);
  }

  //  void QDeclarativeGeoMapQuickItem::geometryChange(const QRectF
  //      &newGeometry, const QRectF &oldGeometry)
  void geometryChange(
      const QRectF &newGeometry,
      const QRectF &oldGeometry) override {
    if (taken[4]) {
      int handled = 0;
      CuteQDeclarativeGeoMapQuickItemCall4 call = reinterpret_cast<CuteQDeclarativeGeoMapQuickItemCall4>(taken[4]);
      call(this, &newGeometry, &oldGeometry, &handled);
      if (handled) return;
    }
    QDeclarativeGeoMapQuickItem::geometryChange(newGeometry, oldGeometry);
  }

  //  void QDeclarativeGeoMapQuickItem::updatePolish()
  void updatePolish() override {
    if (taken[5]) {
      int handled = 0;
      CuteQDeclarativeGeoMapQuickItemCall5 call = reinterpret_cast<CuteQDeclarativeGeoMapQuickItemCall5>(taken[5]);
      call(this, &handled);
      if (handled) return;
    }
    QDeclarativeGeoMapQuickItem::updatePolish();
  }

  //  void QDeclarativeGeoMapQuickItem::afterChildrenChanged()
  void afterChildrenChanged() override {
    if (taken[6]) {
      int handled = 0;
      CuteQDeclarativeGeoMapQuickItemCall6 call = reinterpret_cast<CuteQDeclarativeGeoMapQuickItemCall6>(taken[6]);
      call(this, &handled);
      if (handled) return;
    }
    QDeclarativeGeoMapQuickItem::afterChildrenChanged();
  }

  //  void QDeclarativeGeoMapQuickItem::afterViewportChanged(const
  //      QGeoMapViewportChangeEvent &event)
  void afterViewportChanged(
      const QGeoMapViewportChangeEvent &event) override {
    if (taken[7]) {
      int handled = 0;
      CuteQDeclarativeGeoMapQuickItemCall7 call = reinterpret_cast<CuteQDeclarativeGeoMapQuickItemCall7>(taken[7]);
      call(this, &event, &handled);
      if (handled) return;
    }
    QDeclarativeGeoMapQuickItem::afterViewportChanged(event);
  }

  //  void QDeclarativeGeoMapItemBase::setPositionOnMap(const
  //      QGeoCoordinate &coordinate, const QPointF &offset)
  void setPositionOnMap(
      const QGeoCoordinate &coordinate,
      const QPointF &offset) override {
    if (taken[8]) {
      int handled = 0;
      CuteQDeclarativeGeoMapQuickItemCall8 call = reinterpret_cast<CuteQDeclarativeGeoMapQuickItemCall8>(taken[8]);
      call(this, &coordinate, &offset, &handled);
      if (handled) return;
    }
    QDeclarativeGeoMapItemBase::setPositionOnMap(coordinate, offset);
  }

  //  QSGNode *QDeclarativeGeoMapItemBase::updatePaintNode(QSGNode *a0,
  //      UpdatePaintNodeData *a1)
  QSGNode *updatePaintNode(
      QSGNode *a0,
      QQuickItem::UpdatePaintNodeData *a1) override {
    if (taken[9]) {
      int handled = 0;
      CuteQDeclarativeGeoMapQuickItemCall9 call = reinterpret_cast<CuteQDeclarativeGeoMapQuickItemCall9>(taken[9]);
      void * given = call(this, a0, a1, &handled);
      if (handled) return static_cast<QSGNode *>(given);
    }
    return QDeclarativeGeoMapItemBase::updatePaintNode(a0, a1);
  }

  //  QSGNode *QDeclarativeGeoMapItemBase::updateMapItemPaintNode(QSGNode
  //      *a0, UpdatePaintNodeData *a1)
  QSGNode *updateMapItemPaintNode(
      QSGNode *a0,
      QQuickItem::UpdatePaintNodeData *a1) override {
    if (taken[10]) {
      int handled = 0;
      CuteQDeclarativeGeoMapQuickItemCall10 call = reinterpret_cast<CuteQDeclarativeGeoMapQuickItemCall10>(taken[10]);
      void * given = call(this, a0, a1, &handled);
      if (handled) return static_cast<QSGNode *>(given);
    }
    return QDeclarativeGeoMapItemBase::updateMapItemPaintNode(a0, a1);
  }

  //  QRectF QQuickItem::boundingRect() const
  QRectF boundingRect() const override {
    if (taken[11]) {
      int handled = 0;
      CuteQDeclarativeGeoMapQuickItemCall11 call = reinterpret_cast<CuteQDeclarativeGeoMapQuickItemCall11>(taken[11]);
      const QRectF * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QQuickItem::boundingRect();
  }

  //  QRectF QQuickItem::clipRect() const
  QRectF clipRect() const override {
    if (taken[12]) {
      int handled = 0;
      CuteQDeclarativeGeoMapQuickItemCall12 call = reinterpret_cast<CuteQDeclarativeGeoMapQuickItemCall12>(taken[12]);
      const QRectF * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QQuickItem::clipRect();
  }

#if QT_CONFIG(im)
  //  QVariant QQuickItem::inputMethodQuery(Qt::InputMethodQuery query)
  //      const
  QVariant inputMethodQuery(Qt::InputMethodQuery query) const override {
    if (taken[13]) {
      int handled = 0;
      CuteQDeclarativeGeoMapQuickItemCall13 call = reinterpret_cast<CuteQDeclarativeGeoMapQuickItemCall13>(taken[13]);
      const QVariant * given = call(this, static_cast<int>(query), &handled);
      if (handled && given) return *given;
    }
    return QQuickItem::inputMethodQuery(query);
  }
#endif  // QT_CONFIG(im)

  //  bool QQuickItem::isTextureProvider() const
  bool isTextureProvider() const override {
    if (taken[14]) {
      int handled = 0;
      CuteQDeclarativeGeoMapQuickItemCall14 call = reinterpret_cast<CuteQDeclarativeGeoMapQuickItemCall14>(taken[14]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QQuickItem::isTextureProvider();
  }

  //  QSGTextureProvider *QQuickItem::textureProvider() const
  QSGTextureProvider *textureProvider() const override {
    if (taken[15]) {
      int handled = 0;
      CuteQDeclarativeGeoMapQuickItemCall15 call = reinterpret_cast<CuteQDeclarativeGeoMapQuickItemCall15>(taken[15]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QSGTextureProvider *>(given);
    }
    return QQuickItem::textureProvider();
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QQuickItem::event(QEvent *a0)
  bool event(QEvent *a0) override {
    if (taken[16]) {
      int handled = 0;
      CuteQDeclarativeGeoMapQuickItemCall16 call = reinterpret_cast<CuteQDeclarativeGeoMapQuickItemCall16>(taken[16]);
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
    if (taken[17]) {
      int handled = 0;
      CuteQDeclarativeGeoMapQuickItemCall17 call = reinterpret_cast<CuteQDeclarativeGeoMapQuickItemCall17>(taken[17]);
      call(this, static_cast<int>(a0), &a1, &handled);
      if (handled) return;
    }
    QQuickItem::itemChange(a0, a1);
  }

  //  void QQuickItem::classBegin()
  void classBegin() override {
    if (taken[18]) {
      int handled = 0;
      CuteQDeclarativeGeoMapQuickItemCall18 call = reinterpret_cast<CuteQDeclarativeGeoMapQuickItemCall18>(taken[18]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItem::classBegin();
  }

  //  void QQuickItem::componentComplete()
  void componentComplete() override {
    if (taken[19]) {
      int handled = 0;
      CuteQDeclarativeGeoMapQuickItemCall19 call = reinterpret_cast<CuteQDeclarativeGeoMapQuickItemCall19>(taken[19]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItem::componentComplete();
  }

  //  void QQuickItem::keyPressEvent(QKeyEvent *event)
  void keyPressEvent(QKeyEvent *event) override {
    if (taken[20]) {
      int handled = 0;
      CuteQDeclarativeGeoMapQuickItemCall20 call = reinterpret_cast<CuteQDeclarativeGeoMapQuickItemCall20>(taken[20]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::keyPressEvent(event);
  }

  //  void QQuickItem::keyReleaseEvent(QKeyEvent *event)
  void keyReleaseEvent(QKeyEvent *event) override {
    if (taken[21]) {
      int handled = 0;
      CuteQDeclarativeGeoMapQuickItemCall21 call = reinterpret_cast<CuteQDeclarativeGeoMapQuickItemCall21>(taken[21]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::keyReleaseEvent(event);
  }

#if QT_CONFIG(im)
  //  void QQuickItem::inputMethodEvent(QInputMethodEvent *a0)
  void inputMethodEvent(QInputMethodEvent *a0) override {
    if (taken[22]) {
      int handled = 0;
      CuteQDeclarativeGeoMapQuickItemCall22 call = reinterpret_cast<CuteQDeclarativeGeoMapQuickItemCall22>(taken[22]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItem::inputMethodEvent(a0);
  }
#endif  // QT_CONFIG(im)

  //  void QQuickItem::focusInEvent(QFocusEvent *a0)
  void focusInEvent(QFocusEvent *a0) override {
    if (taken[23]) {
      int handled = 0;
      CuteQDeclarativeGeoMapQuickItemCall23 call = reinterpret_cast<CuteQDeclarativeGeoMapQuickItemCall23>(taken[23]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItem::focusInEvent(a0);
  }

  //  void QQuickItem::focusOutEvent(QFocusEvent *a0)
  void focusOutEvent(QFocusEvent *a0) override {
    if (taken[24]) {
      int handled = 0;
      CuteQDeclarativeGeoMapQuickItemCall24 call = reinterpret_cast<CuteQDeclarativeGeoMapQuickItemCall24>(taken[24]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItem::focusOutEvent(a0);
  }

  //  void QQuickItem::mousePressEvent(QMouseEvent *event)
  void mousePressEvent(QMouseEvent *event) override {
    if (taken[25]) {
      int handled = 0;
      CuteQDeclarativeGeoMapQuickItemCall25 call = reinterpret_cast<CuteQDeclarativeGeoMapQuickItemCall25>(taken[25]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::mousePressEvent(event);
  }

  //  void QQuickItem::mouseMoveEvent(QMouseEvent *event)
  void mouseMoveEvent(QMouseEvent *event) override {
    if (taken[26]) {
      int handled = 0;
      CuteQDeclarativeGeoMapQuickItemCall26 call = reinterpret_cast<CuteQDeclarativeGeoMapQuickItemCall26>(taken[26]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::mouseMoveEvent(event);
  }

  //  void QQuickItem::mouseReleaseEvent(QMouseEvent *event)
  void mouseReleaseEvent(QMouseEvent *event) override {
    if (taken[27]) {
      int handled = 0;
      CuteQDeclarativeGeoMapQuickItemCall27 call = reinterpret_cast<CuteQDeclarativeGeoMapQuickItemCall27>(taken[27]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::mouseReleaseEvent(event);
  }

  //  void QQuickItem::mouseDoubleClickEvent(QMouseEvent *event)
  void mouseDoubleClickEvent(QMouseEvent *event) override {
    if (taken[28]) {
      int handled = 0;
      CuteQDeclarativeGeoMapQuickItemCall28 call = reinterpret_cast<CuteQDeclarativeGeoMapQuickItemCall28>(taken[28]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::mouseDoubleClickEvent(event);
  }

  //  void QQuickItem::mouseUngrabEvent()
  void mouseUngrabEvent() override {
    if (taken[29]) {
      int handled = 0;
      CuteQDeclarativeGeoMapQuickItemCall29 call = reinterpret_cast<CuteQDeclarativeGeoMapQuickItemCall29>(taken[29]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItem::mouseUngrabEvent();
  }

  //  void QQuickItem::touchUngrabEvent()
  void touchUngrabEvent() override {
    if (taken[30]) {
      int handled = 0;
      CuteQDeclarativeGeoMapQuickItemCall30 call = reinterpret_cast<CuteQDeclarativeGeoMapQuickItemCall30>(taken[30]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItem::touchUngrabEvent();
  }

#if QT_CONFIG(wheelevent)
  //  void QQuickItem::wheelEvent(QWheelEvent *event)
  void wheelEvent(QWheelEvent *event) override {
    if (taken[31]) {
      int handled = 0;
      CuteQDeclarativeGeoMapQuickItemCall31 call = reinterpret_cast<CuteQDeclarativeGeoMapQuickItemCall31>(taken[31]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::wheelEvent(event);
  }
#endif  // QT_CONFIG(wheelevent)

  //  void QQuickItem::touchEvent(QTouchEvent *event)
  void touchEvent(QTouchEvent *event) override {
    if (taken[32]) {
      int handled = 0;
      CuteQDeclarativeGeoMapQuickItemCall32 call = reinterpret_cast<CuteQDeclarativeGeoMapQuickItemCall32>(taken[32]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::touchEvent(event);
  }

  //  void QQuickItem::hoverEnterEvent(QHoverEvent *event)
  void hoverEnterEvent(QHoverEvent *event) override {
    if (taken[33]) {
      int handled = 0;
      CuteQDeclarativeGeoMapQuickItemCall33 call = reinterpret_cast<CuteQDeclarativeGeoMapQuickItemCall33>(taken[33]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::hoverEnterEvent(event);
  }

  //  void QQuickItem::hoverMoveEvent(QHoverEvent *event)
  void hoverMoveEvent(QHoverEvent *event) override {
    if (taken[34]) {
      int handled = 0;
      CuteQDeclarativeGeoMapQuickItemCall34 call = reinterpret_cast<CuteQDeclarativeGeoMapQuickItemCall34>(taken[34]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::hoverMoveEvent(event);
  }

  //  void QQuickItem::hoverLeaveEvent(QHoverEvent *event)
  void hoverLeaveEvent(QHoverEvent *event) override {
    if (taken[35]) {
      int handled = 0;
      CuteQDeclarativeGeoMapQuickItemCall35 call = reinterpret_cast<CuteQDeclarativeGeoMapQuickItemCall35>(taken[35]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::hoverLeaveEvent(event);
  }

#if QT_CONFIG(quick_draganddrop)
  //  void QQuickItem::dragEnterEvent(QDragEnterEvent *a0)
  void dragEnterEvent(QDragEnterEvent *a0) override {
    if (taken[36]) {
      int handled = 0;
      CuteQDeclarativeGeoMapQuickItemCall36 call = reinterpret_cast<CuteQDeclarativeGeoMapQuickItemCall36>(taken[36]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItem::dragEnterEvent(a0);
  }
#endif  // QT_CONFIG(quick_draganddrop)

#if QT_CONFIG(quick_draganddrop)
  //  void QQuickItem::dragMoveEvent(QDragMoveEvent *a0)
  void dragMoveEvent(QDragMoveEvent *a0) override {
    if (taken[37]) {
      int handled = 0;
      CuteQDeclarativeGeoMapQuickItemCall37 call = reinterpret_cast<CuteQDeclarativeGeoMapQuickItemCall37>(taken[37]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItem::dragMoveEvent(a0);
  }
#endif  // QT_CONFIG(quick_draganddrop)

#if QT_CONFIG(quick_draganddrop)
  //  void QQuickItem::dragLeaveEvent(QDragLeaveEvent *a0)
  void dragLeaveEvent(QDragLeaveEvent *a0) override {
    if (taken[38]) {
      int handled = 0;
      CuteQDeclarativeGeoMapQuickItemCall38 call = reinterpret_cast<CuteQDeclarativeGeoMapQuickItemCall38>(taken[38]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItem::dragLeaveEvent(a0);
  }
#endif  // QT_CONFIG(quick_draganddrop)

#if QT_CONFIG(quick_draganddrop)
  //  void QQuickItem::dropEvent(QDropEvent *a0)
  void dropEvent(QDropEvent *a0) override {
    if (taken[39]) {
      int handled = 0;
      CuteQDeclarativeGeoMapQuickItemCall39 call = reinterpret_cast<CuteQDeclarativeGeoMapQuickItemCall39>(taken[39]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItem::dropEvent(a0);
  }
#endif  // QT_CONFIG(quick_draganddrop)

  //  bool QQuickItem::childMouseEventFilter(QQuickItem *a0, QEvent *a1)
  bool childMouseEventFilter(QQuickItem *a0, QEvent *a1) override {
    if (taken[40]) {
      int handled = 0;
      CuteQDeclarativeGeoMapQuickItemCall40 call = reinterpret_cast<CuteQDeclarativeGeoMapQuickItemCall40>(taken[40]);
      bool given = call(this, a0, a1, &handled);
      if (handled) return given;
    }
    return QQuickItem::childMouseEventFilter(a0, a1);
  }

  //  void QQuickItem::releaseResources()
  void releaseResources() override {
    if (taken[41]) {
      int handled = 0;
      CuteQDeclarativeGeoMapQuickItemCall41 call = reinterpret_cast<CuteQDeclarativeGeoMapQuickItemCall41>(taken[41]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItem::releaseResources();
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[42]) {
      int handled = 0;
      CuteQDeclarativeGeoMapQuickItemCall42 call = reinterpret_cast<CuteQDeclarativeGeoMapQuickItemCall42>(taken[42]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[43]) {
      int handled = 0;
      CuteQDeclarativeGeoMapQuickItemCall43 call = reinterpret_cast<CuteQDeclarativeGeoMapQuickItemCall43>(taken[43]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[44]) {
      int handled = 0;
      CuteQDeclarativeGeoMapQuickItemCall44 call = reinterpret_cast<CuteQDeclarativeGeoMapQuickItemCall44>(taken[44]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[45]) {
      int handled = 0;
      CuteQDeclarativeGeoMapQuickItemCall45 call = reinterpret_cast<CuteQDeclarativeGeoMapQuickItemCall45>(taken[45]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[46]) {
      int handled = 0;
      CuteQDeclarativeGeoMapQuickItemCall46 call = reinterpret_cast<CuteQDeclarativeGeoMapQuickItemCall46>(taken[46]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[47]) {
      int handled = 0;
      CuteQDeclarativeGeoMapQuickItemCall47 call = reinterpret_cast<CuteQDeclarativeGeoMapQuickItemCall47>(taken[47]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QDeclarativeGeoMapQuickItem::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK27QDeclarativeGeoMapQuickItem10metaObjectEv(
    const QDeclarativeGeoMapQuickItem *self) {
  return self->metaObject();
}

//  void *QDeclarativeGeoMapQuickItem::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN27QDeclarativeGeoMapQuickItem11qt_metacastEPKc(
    QDeclarativeGeoMapQuickItem *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QDeclarativeGeoMapQuickItem::qt_metacall(QMetaObject::Call a0, int
//      a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN27QDeclarativeGeoMapQuickItem11qt_metacallEN11QMetaObject4CallEiPPv(
    QDeclarativeGeoMapQuickItem *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QDeclarativeGeoMapQuickItem::tr(const char *s, const char *c, int
//      n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN27QDeclarativeGeoMapQuickItem2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QDeclarativeGeoMapQuickItem::tr(s, c, n));
}

//  QDeclarativeGeoMapQuickItem::QDeclarativeGeoMapQuickItem(QQuickItem
//      *parent)
extern "C" Q_DECL_EXPORT
QDeclarativeGeoMapQuickItem *ritual_ZN27QDeclarativeGeoMapQuickItemC1EP10QQuickItem(
    QQuickItem *parent) {
  return new CuteQDeclarativeGeoMapQuickItem(parent);
}

//  QDeclarativeGeoMapQuickItem::~QDeclarativeGeoMapQuickItem()
extern "C" Q_DECL_EXPORT
void ritual_ZN27QDeclarativeGeoMapQuickItemD1Ev(
    QDeclarativeGeoMapQuickItem *self) {
  delete self;
}

//  void QDeclarativeGeoMapQuickItem::setMap(QDeclarativeGeoMap *quickMap,
//      QGeoMap *map)
extern "C" Q_DECL_EXPORT
void ritual_ZN27QDeclarativeGeoMapQuickItem6setMapEP18QDeclarativeGeoMapP7QGeoMap(
    QDeclarativeGeoMapQuickItem *self,
    QDeclarativeGeoMap *quickMap,
    QGeoMap *map) {
  self->setMap(quickMap, map);
}

//  void QDeclarativeGeoMapQuickItem::setCoordinate(const QGeoCoordinate
//      &coordinate)
extern "C" Q_DECL_EXPORT
void ritual_ZN27QDeclarativeGeoMapQuickItem13setCoordinateERK14QGeoCoordinate(
    QDeclarativeGeoMapQuickItem *self,
    const QGeoCoordinate *coordinate) {
  self->setCoordinate(*coordinate);
}

//  QGeoCoordinate QDeclarativeGeoMapQuickItem::coordinate()
extern "C" Q_DECL_EXPORT
QGeoCoordinate *ritual_ZN27QDeclarativeGeoMapQuickItem10coordinateEv(
    QDeclarativeGeoMapQuickItem *self) {
  return new QGeoCoordinate(self->coordinate());
}

//  void QDeclarativeGeoMapQuickItem::setSourceItem(QQuickItem *sourceItem)
extern "C" Q_DECL_EXPORT
void ritual_ZN27QDeclarativeGeoMapQuickItem13setSourceItemEP10QQuickItem(
    QDeclarativeGeoMapQuickItem *self,
    QQuickItem *sourceItem) {
  self->setSourceItem(sourceItem);
}

//  QQuickItem *QDeclarativeGeoMapQuickItem::sourceItem()
extern "C" Q_DECL_EXPORT
QQuickItem *ritual_ZN27QDeclarativeGeoMapQuickItem10sourceItemEv(
    QDeclarativeGeoMapQuickItem *self) {
  return self->sourceItem();
}

//  void QDeclarativeGeoMapQuickItem::setAnchorPoint(const QPointF
//      &anchorPoint)
extern "C" Q_DECL_EXPORT
void ritual_ZN27QDeclarativeGeoMapQuickItem14setAnchorPointERK7QPointF(
    QDeclarativeGeoMapQuickItem *self,
    const QPointF *anchorPoint) {
  self->setAnchorPoint(*anchorPoint);
}

//  QPointF QDeclarativeGeoMapQuickItem::anchorPoint() const
extern "C" Q_DECL_EXPORT
QPointF *ritual_ZNK27QDeclarativeGeoMapQuickItem11anchorPointEv(
    const QDeclarativeGeoMapQuickItem *self) {
  return new QPointF(self->anchorPoint());
}

//  void QDeclarativeGeoMapQuickItem::setZoomLevel(qreal zoomLevel)
extern "C" Q_DECL_EXPORT
void ritual_ZN27QDeclarativeGeoMapQuickItem12setZoomLevelEd(
    QDeclarativeGeoMapQuickItem *self,
    qreal zoomLevel) {
  self->setZoomLevel(zoomLevel);
}

//  qreal QDeclarativeGeoMapQuickItem::zoomLevel() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK27QDeclarativeGeoMapQuickItem9zoomLevelEv(
    const QDeclarativeGeoMapQuickItem *self) {
  return self->zoomLevel();
}

//  const QGeoShape &QDeclarativeGeoMapQuickItem::geoShape() const
extern "C" Q_DECL_EXPORT
QGeoShape *ritual_ZNK27QDeclarativeGeoMapQuickItem8geoShapeEv(
    const QDeclarativeGeoMapQuickItem *self) {
  return new QGeoShape(self->geoShape());
}

//  void QDeclarativeGeoMapQuickItem::setGeoShape(const QGeoShape &shape)
extern "C" Q_DECL_EXPORT
void ritual_ZN27QDeclarativeGeoMapQuickItem11setGeoShapeERK9QGeoShape(
    QDeclarativeGeoMapQuickItem *self,
    const QGeoShape *shape) {
  self->setGeoShape(*shape);
}

//  bool QDeclarativeGeoMapQuickItem::contains(const QPointF &point) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK27QDeclarativeGeoMapQuickItem8containsERK7QPointF(
    const QDeclarativeGeoMapQuickItem *self,
    const QPointF *point) {
  return self->contains(*point);
}

//  void QDeclarativeGeoMapQuickItem::coordinateChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN27QDeclarativeGeoMapQuickItem17coordinateChangedEv(
    QDeclarativeGeoMapQuickItem *self) {
  self->coordinateChanged();
}

//  void QDeclarativeGeoMapQuickItem::sourceItemChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN27QDeclarativeGeoMapQuickItem17sourceItemChangedEv(
    QDeclarativeGeoMapQuickItem *self) {
  self->sourceItemChanged();
}

//  void QDeclarativeGeoMapQuickItem::anchorPointChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN27QDeclarativeGeoMapQuickItem18anchorPointChangedEv(
    QDeclarativeGeoMapQuickItem *self) {
  self->anchorPointChanged();
}

//  void QDeclarativeGeoMapQuickItem::zoomLevelChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN27QDeclarativeGeoMapQuickItem16zoomLevelChangedEv(
    QDeclarativeGeoMapQuickItem *self) {
  self->zoomLevelChanged();
}

//  void QDeclarativeGeoMapQuickItem::geometryChange(const QRectF
//      &newGeometry, const QRectF &oldGeometry)
extern "C" Q_DECL_EXPORT
void ritual_ZN27QDeclarativeGeoMapQuickItem14geometryChangeERK6QRectFS2_(
    QDeclarativeGeoMapQuickItem *self,
    const QRectF *newGeometry,
    const QRectF *oldGeometry) {
  self->geometryChange(*newGeometry, *oldGeometry);
}

//  void QDeclarativeGeoMapQuickItem::updatePolish()
extern "C" Q_DECL_EXPORT
void ritual_ZN27QDeclarativeGeoMapQuickItem12updatePolishEv(
    QDeclarativeGeoMapQuickItem *self) {
  self->updatePolish();
}

//  void QDeclarativeGeoMapQuickItem::afterChildrenChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN27QDeclarativeGeoMapQuickItem20afterChildrenChangedEv(
    QDeclarativeGeoMapQuickItem *self) {
  self->afterChildrenChanged();
}

//  void QDeclarativeGeoMapQuickItem::afterViewportChanged(const
//      QGeoMapViewportChangeEvent &event)
extern "C" Q_DECL_EXPORT
void ritual_ZN27QDeclarativeGeoMapQuickItem20afterViewportChangedERK26QGeoMapViewportChangeEvent(
    QDeclarativeGeoMapQuickItem *self,
    const QGeoMapViewportChangeEvent *event) {
  self->afterViewportChanged(*event);
}

//  qreal QDeclarativeGeoMapQuickItem::scaleFactor()
extern "C" Q_DECL_EXPORT
qreal ritual_ZN27QDeclarativeGeoMapQuickItem11scaleFactorEv(
    QDeclarativeGeoMapQuickItem *self) {
  return self->scaleFactor();
}

//  a Python function taken by a CuteQDeclarativeGeoMapQuickItem, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QDeclarativeGeoMapQuickItem(
    QDeclarativeGeoMapQuickItem *self,
    const char *key,
    void *call) {
  return static_cast<CuteQDeclarativeGeoMapQuickItem *>(self)->take(key, call);
}

//  void QDeclarativeGeoMapQuickItem::setMap(QDeclarativeGeoMap *quickMap,
//      QGeoMap *map)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN27QDeclarativeGeoMapQuickItem6setMapEP18QDeclarativeGeoMapP7QGeoMap(
    QDeclarativeGeoMapQuickItem *self,
    QDeclarativeGeoMap *quickMap,
    QGeoMap *map) {
  self->QDeclarativeGeoMapQuickItem::setMap(quickMap, map);
}

//  const QGeoShape &QDeclarativeGeoMapQuickItem::geoShape() const
extern "C" Q_DECL_EXPORT
QGeoShape *ritual_own_ZNK27QDeclarativeGeoMapQuickItem8geoShapeEv(
    const QDeclarativeGeoMapQuickItem *self) {
  return new QGeoShape(self->QDeclarativeGeoMapQuickItem::geoShape());
}

//  void QDeclarativeGeoMapQuickItem::setGeoShape(const QGeoShape &shape)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN27QDeclarativeGeoMapQuickItem11setGeoShapeERK9QGeoShape(
    QDeclarativeGeoMapQuickItem *self,
    const QGeoShape *shape) {
  self->QDeclarativeGeoMapQuickItem::setGeoShape(*shape);
}

//  bool QDeclarativeGeoMapQuickItem::contains(const QPointF &point) const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK27QDeclarativeGeoMapQuickItem8containsERK7QPointF(
    const QDeclarativeGeoMapQuickItem *self,
    const QPointF *point) {
  return self->QDeclarativeGeoMapQuickItem::contains(*point);
}

//  void QDeclarativeGeoMapQuickItem::geometryChange(const QRectF
//      &newGeometry, const QRectF &oldGeometry)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN27QDeclarativeGeoMapQuickItem14geometryChangeERK6QRectFS2_(
    QDeclarativeGeoMapQuickItem *self,
    const QRectF *newGeometry,
    const QRectF *oldGeometry) {
  static_cast<OwnQDeclarativeGeoMapQuickItem *>(self)->OwnQDeclarativeGeoMapQuickItem::geometryChange(
      *newGeometry,
      *oldGeometry);
}

//  void QDeclarativeGeoMapQuickItem::updatePolish()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN27QDeclarativeGeoMapQuickItem12updatePolishEv(
    QDeclarativeGeoMapQuickItem *self) {
  static_cast<OwnQDeclarativeGeoMapQuickItem *>(self)->OwnQDeclarativeGeoMapQuickItem::updatePolish();
}

//  void QDeclarativeGeoMapQuickItem::afterChildrenChanged()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN27QDeclarativeGeoMapQuickItem20afterChildrenChangedEv(
    QDeclarativeGeoMapQuickItem *self) {
  static_cast<OwnQDeclarativeGeoMapQuickItem *>(self)->OwnQDeclarativeGeoMapQuickItem::afterChildrenChanged();
}

//  void QDeclarativeGeoMapQuickItem::afterViewportChanged(const
//      QGeoMapViewportChangeEvent &event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN27QDeclarativeGeoMapQuickItem20afterViewportChangedERK26QGeoMapViewportChangeEvent(
    QDeclarativeGeoMapQuickItem *self,
    const QGeoMapViewportChangeEvent *event) {
  static_cast<OwnQDeclarativeGeoMapQuickItem *>(self)->OwnQDeclarativeGeoMapQuickItem::afterViewportChanged(
      *event);
}
