//  Written by dev_tooling.RitualGenerator from the records of
//  QtLocation/6.12.0/QtLocation/private/qdeclarativerectanglemapitem_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtGui/qtguiglobal.h>
#include <QtQuick/qtquickglobal.h>
#include <QtLocation/6.12.0/QtLocation/private/qlocationglobal_p.h>
#include <QtLocation/QtLocation>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtLocation/6.12.0/QtLocation/private/qdeclarativerectanglemapitem_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtPositioning/qgeocoordinate.h>
#include <QtGui/qcolor.h>
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

//  Only a class built on QDeclarativeRectangleMapItem may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQDeclarativeRectangleMapItem : QDeclarativeRectangleMapItem {
  using QDeclarativeRectangleMapItem::geometryChange;
  using QDeclarativeRectangleMapItem::updatePolish;
  using QDeclarativeRectangleMapItem::afterViewportChanged;
};

//  A QDeclarativeRectangleMapItem that Python can take functions over in. Every QDeclarativeRectangleMapItem
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQDeclarativeRectangleMapItemCall0)(const void *, QDeclarativeGeoMap *, QGeoMap *, int *);
typedef void * (*CuteQDeclarativeRectangleMapItemCall1)(const void *, QSGNode *, QQuickItem::UpdatePaintNodeData *, int *);
typedef bool (*CuteQDeclarativeRectangleMapItemCall2)(const void *, const QPointF *, int *);
typedef const QGeoShape * (*CuteQDeclarativeRectangleMapItemCall3)(const void *, int *);
typedef void (*CuteQDeclarativeRectangleMapItemCall4)(const void *, const QGeoShape *, int *);
typedef void (*CuteQDeclarativeRectangleMapItemCall5)(const void *, const QRectF *, const QRectF *, int *);
typedef void (*CuteQDeclarativeRectangleMapItemCall6)(const void *, int *);
typedef void (*CuteQDeclarativeRectangleMapItemCall7)(const void *, const QGeoMapViewportChangeEvent *, int *);
typedef void (*CuteQDeclarativeRectangleMapItemCall8)(const void *, const QGeoCoordinate *, const QPointF *, int *);
typedef void * (*CuteQDeclarativeRectangleMapItemCall9)(const void *, QSGNode *, QQuickItem::UpdatePaintNodeData *, int *);
typedef void (*CuteQDeclarativeRectangleMapItemCall10)(const void *, int *);
typedef const QRectF * (*CuteQDeclarativeRectangleMapItemCall11)(const void *, int *);
typedef const QRectF * (*CuteQDeclarativeRectangleMapItemCall12)(const void *, int *);
#if QT_CONFIG(im)
typedef const QVariant * (*CuteQDeclarativeRectangleMapItemCall13)(const void *, int, int *);
#endif  // QT_CONFIG(im)
typedef bool (*CuteQDeclarativeRectangleMapItemCall14)(const void *, int *);
typedef void * (*CuteQDeclarativeRectangleMapItemCall15)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQDeclarativeRectangleMapItemCall16)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
typedef void (*CuteQDeclarativeRectangleMapItemCall17)(const void *, int, const QQuickItem::ItemChangeData *, int *);
typedef void (*CuteQDeclarativeRectangleMapItemCall18)(const void *, int *);
typedef void (*CuteQDeclarativeRectangleMapItemCall19)(const void *, int *);
typedef void (*CuteQDeclarativeRectangleMapItemCall20)(const void *, QKeyEvent *, int *);
typedef void (*CuteQDeclarativeRectangleMapItemCall21)(const void *, QKeyEvent *, int *);
#if QT_CONFIG(im)
typedef void (*CuteQDeclarativeRectangleMapItemCall22)(const void *, QInputMethodEvent *, int *);
#endif  // QT_CONFIG(im)
typedef void (*CuteQDeclarativeRectangleMapItemCall23)(const void *, QFocusEvent *, int *);
typedef void (*CuteQDeclarativeRectangleMapItemCall24)(const void *, QFocusEvent *, int *);
typedef void (*CuteQDeclarativeRectangleMapItemCall25)(const void *, QMouseEvent *, int *);
typedef void (*CuteQDeclarativeRectangleMapItemCall26)(const void *, QMouseEvent *, int *);
typedef void (*CuteQDeclarativeRectangleMapItemCall27)(const void *, QMouseEvent *, int *);
typedef void (*CuteQDeclarativeRectangleMapItemCall28)(const void *, QMouseEvent *, int *);
typedef void (*CuteQDeclarativeRectangleMapItemCall29)(const void *, int *);
typedef void (*CuteQDeclarativeRectangleMapItemCall30)(const void *, int *);
#if QT_CONFIG(wheelevent)
typedef void (*CuteQDeclarativeRectangleMapItemCall31)(const void *, QWheelEvent *, int *);
#endif  // QT_CONFIG(wheelevent)
typedef void (*CuteQDeclarativeRectangleMapItemCall32)(const void *, QTouchEvent *, int *);
typedef void (*CuteQDeclarativeRectangleMapItemCall33)(const void *, QHoverEvent *, int *);
typedef void (*CuteQDeclarativeRectangleMapItemCall34)(const void *, QHoverEvent *, int *);
typedef void (*CuteQDeclarativeRectangleMapItemCall35)(const void *, QHoverEvent *, int *);
#if QT_CONFIG(quick_draganddrop)
typedef void (*CuteQDeclarativeRectangleMapItemCall36)(const void *, QDragEnterEvent *, int *);
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
typedef void (*CuteQDeclarativeRectangleMapItemCall37)(const void *, QDragMoveEvent *, int *);
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
typedef void (*CuteQDeclarativeRectangleMapItemCall38)(const void *, QDragLeaveEvent *, int *);
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
typedef void (*CuteQDeclarativeRectangleMapItemCall39)(const void *, QDropEvent *, int *);
#endif  // QT_CONFIG(quick_draganddrop)
typedef bool (*CuteQDeclarativeRectangleMapItemCall40)(const void *, QQuickItem *, QEvent *, int *);
typedef void (*CuteQDeclarativeRectangleMapItemCall41)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQDeclarativeRectangleMapItemCall42)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQDeclarativeRectangleMapItemCall43)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQDeclarativeRectangleMapItemCall44)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQDeclarativeRectangleMapItemCall45)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQDeclarativeRectangleMapItemCall46)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQDeclarativeRectangleMapItemCall47)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQDeclarativeRectangleMapItem : public QDeclarativeRectangleMapItem {
public:
  using QDeclarativeRectangleMapItem::QDeclarativeRectangleMapItem;
  void *taken[48] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN26QDeclarativeGeoMapItemBase6setMapEP18QDeclarativeGeoMapP7QGeoMap")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN26QDeclarativeGeoMapItemBase22updateMapItemPaintNodeEP7QSGNodePN10QQuickItem19UpdatePaintNodeDataE")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK10QQuickItem8containsERK7QPointF")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK26QDeclarativeGeoMapItemBase8geoShapeEv")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN26QDeclarativeGeoMapItemBase11setGeoShapeERK9QGeoShape")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem14geometryChangeERK6QRectFS2_")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem12updatePolishEv")) {
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
    if (!std::strcmp(key, "_ZN26QDeclarativeGeoMapItemBase20afterChildrenChangedEv")) {
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

  //  void QDeclarativeRectangleMapItem::setMap(QDeclarativeGeoMap
  //      *quickMap, QGeoMap *map)
  void setMap(QDeclarativeGeoMap *quickMap, QGeoMap *map) override {
    if (taken[0]) {
      int handled = 0;
      CuteQDeclarativeRectangleMapItemCall0 call = reinterpret_cast<CuteQDeclarativeRectangleMapItemCall0>(taken[0]);
      call(this, quickMap, map, &handled);
      if (handled) return;
    }
    QDeclarativeRectangleMapItem::setMap(quickMap, map);
  }

  //  QSGNode *QDeclarativeRectangleMapItem::updateMapItemPaintNode(QSGNode
  //      *a0, UpdatePaintNodeData *a1)
  QSGNode *updateMapItemPaintNode(
      QSGNode *a0,
      QQuickItem::UpdatePaintNodeData *a1) override {
    if (taken[1]) {
      int handled = 0;
      CuteQDeclarativeRectangleMapItemCall1 call = reinterpret_cast<CuteQDeclarativeRectangleMapItemCall1>(taken[1]);
      void * given = call(this, a0, a1, &handled);
      if (handled) return static_cast<QSGNode *>(given);
    }
    return QDeclarativeRectangleMapItem::updateMapItemPaintNode(a0, a1);
  }

  //  bool QDeclarativeRectangleMapItem::contains(const QPointF &point)
  //      const
  bool contains(const QPointF &point) const override {
    if (taken[2]) {
      int handled = 0;
      CuteQDeclarativeRectangleMapItemCall2 call = reinterpret_cast<CuteQDeclarativeRectangleMapItemCall2>(taken[2]);
      bool given = call(this, &point, &handled);
      if (handled) return given;
    }
    return QDeclarativeRectangleMapItem::contains(point);
  }

  //  const QGeoShape &QDeclarativeRectangleMapItem::geoShape() const
  const QGeoShape &geoShape() const override {
    if (taken[3]) {
      int handled = 0;
      CuteQDeclarativeRectangleMapItemCall3 call = reinterpret_cast<CuteQDeclarativeRectangleMapItemCall3>(taken[3]);
      const QGeoShape * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QDeclarativeRectangleMapItem::geoShape();
  }

  //  void QDeclarativeRectangleMapItem::setGeoShape(const QGeoShape
  //      &shape)
  void setGeoShape(const QGeoShape &shape) override {
    if (taken[4]) {
      int handled = 0;
      CuteQDeclarativeRectangleMapItemCall4 call = reinterpret_cast<CuteQDeclarativeRectangleMapItemCall4>(taken[4]);
      call(this, &shape, &handled);
      if (handled) return;
    }
    QDeclarativeRectangleMapItem::setGeoShape(shape);
  }

  //  void QDeclarativeRectangleMapItem::geometryChange(const QRectF
  //      &newGeometry, const QRectF &oldGeometry)
  void geometryChange(
      const QRectF &newGeometry,
      const QRectF &oldGeometry) override {
    if (taken[5]) {
      int handled = 0;
      CuteQDeclarativeRectangleMapItemCall5 call = reinterpret_cast<CuteQDeclarativeRectangleMapItemCall5>(taken[5]);
      call(this, &newGeometry, &oldGeometry, &handled);
      if (handled) return;
    }
    QDeclarativeRectangleMapItem::geometryChange(newGeometry, oldGeometry);
  }

  //  void QDeclarativeRectangleMapItem::updatePolish()
  void updatePolish() override {
    if (taken[6]) {
      int handled = 0;
      CuteQDeclarativeRectangleMapItemCall6 call = reinterpret_cast<CuteQDeclarativeRectangleMapItemCall6>(taken[6]);
      call(this, &handled);
      if (handled) return;
    }
    QDeclarativeRectangleMapItem::updatePolish();
  }

  //  void QDeclarativeRectangleMapItem::afterViewportChanged(const
  //      QGeoMapViewportChangeEvent &event)
  void afterViewportChanged(
      const QGeoMapViewportChangeEvent &event) override {
    if (taken[7]) {
      int handled = 0;
      CuteQDeclarativeRectangleMapItemCall7 call = reinterpret_cast<CuteQDeclarativeRectangleMapItemCall7>(taken[7]);
      call(this, &event, &handled);
      if (handled) return;
    }
    QDeclarativeRectangleMapItem::afterViewportChanged(event);
  }

  //  void QDeclarativeGeoMapItemBase::setPositionOnMap(const
  //      QGeoCoordinate &coordinate, const QPointF &offset)
  void setPositionOnMap(
      const QGeoCoordinate &coordinate,
      const QPointF &offset) override {
    if (taken[8]) {
      int handled = 0;
      CuteQDeclarativeRectangleMapItemCall8 call = reinterpret_cast<CuteQDeclarativeRectangleMapItemCall8>(taken[8]);
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
      CuteQDeclarativeRectangleMapItemCall9 call = reinterpret_cast<CuteQDeclarativeRectangleMapItemCall9>(taken[9]);
      void * given = call(this, a0, a1, &handled);
      if (handled) return static_cast<QSGNode *>(given);
    }
    return QDeclarativeGeoMapItemBase::updatePaintNode(a0, a1);
  }

  //  void QDeclarativeGeoMapItemBase::afterChildrenChanged()
  void afterChildrenChanged() override {
    if (taken[10]) {
      int handled = 0;
      CuteQDeclarativeRectangleMapItemCall10 call = reinterpret_cast<CuteQDeclarativeRectangleMapItemCall10>(taken[10]);
      call(this, &handled);
      if (handled) return;
    }
    QDeclarativeGeoMapItemBase::afterChildrenChanged();
  }

  //  QRectF QQuickItem::boundingRect() const
  QRectF boundingRect() const override {
    if (taken[11]) {
      int handled = 0;
      CuteQDeclarativeRectangleMapItemCall11 call = reinterpret_cast<CuteQDeclarativeRectangleMapItemCall11>(taken[11]);
      const QRectF * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QQuickItem::boundingRect();
  }

  //  QRectF QQuickItem::clipRect() const
  QRectF clipRect() const override {
    if (taken[12]) {
      int handled = 0;
      CuteQDeclarativeRectangleMapItemCall12 call = reinterpret_cast<CuteQDeclarativeRectangleMapItemCall12>(taken[12]);
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
      CuteQDeclarativeRectangleMapItemCall13 call = reinterpret_cast<CuteQDeclarativeRectangleMapItemCall13>(taken[13]);
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
      CuteQDeclarativeRectangleMapItemCall14 call = reinterpret_cast<CuteQDeclarativeRectangleMapItemCall14>(taken[14]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QQuickItem::isTextureProvider();
  }

  //  QSGTextureProvider *QQuickItem::textureProvider() const
  QSGTextureProvider *textureProvider() const override {
    if (taken[15]) {
      int handled = 0;
      CuteQDeclarativeRectangleMapItemCall15 call = reinterpret_cast<CuteQDeclarativeRectangleMapItemCall15>(taken[15]);
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
      CuteQDeclarativeRectangleMapItemCall16 call = reinterpret_cast<CuteQDeclarativeRectangleMapItemCall16>(taken[16]);
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
      CuteQDeclarativeRectangleMapItemCall17 call = reinterpret_cast<CuteQDeclarativeRectangleMapItemCall17>(taken[17]);
      call(this, static_cast<int>(a0), &a1, &handled);
      if (handled) return;
    }
    QQuickItem::itemChange(a0, a1);
  }

  //  void QQuickItem::classBegin()
  void classBegin() override {
    if (taken[18]) {
      int handled = 0;
      CuteQDeclarativeRectangleMapItemCall18 call = reinterpret_cast<CuteQDeclarativeRectangleMapItemCall18>(taken[18]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItem::classBegin();
  }

  //  void QQuickItem::componentComplete()
  void componentComplete() override {
    if (taken[19]) {
      int handled = 0;
      CuteQDeclarativeRectangleMapItemCall19 call = reinterpret_cast<CuteQDeclarativeRectangleMapItemCall19>(taken[19]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItem::componentComplete();
  }

  //  void QQuickItem::keyPressEvent(QKeyEvent *event)
  void keyPressEvent(QKeyEvent *event) override {
    if (taken[20]) {
      int handled = 0;
      CuteQDeclarativeRectangleMapItemCall20 call = reinterpret_cast<CuteQDeclarativeRectangleMapItemCall20>(taken[20]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::keyPressEvent(event);
  }

  //  void QQuickItem::keyReleaseEvent(QKeyEvent *event)
  void keyReleaseEvent(QKeyEvent *event) override {
    if (taken[21]) {
      int handled = 0;
      CuteQDeclarativeRectangleMapItemCall21 call = reinterpret_cast<CuteQDeclarativeRectangleMapItemCall21>(taken[21]);
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
      CuteQDeclarativeRectangleMapItemCall22 call = reinterpret_cast<CuteQDeclarativeRectangleMapItemCall22>(taken[22]);
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
      CuteQDeclarativeRectangleMapItemCall23 call = reinterpret_cast<CuteQDeclarativeRectangleMapItemCall23>(taken[23]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItem::focusInEvent(a0);
  }

  //  void QQuickItem::focusOutEvent(QFocusEvent *a0)
  void focusOutEvent(QFocusEvent *a0) override {
    if (taken[24]) {
      int handled = 0;
      CuteQDeclarativeRectangleMapItemCall24 call = reinterpret_cast<CuteQDeclarativeRectangleMapItemCall24>(taken[24]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItem::focusOutEvent(a0);
  }

  //  void QQuickItem::mousePressEvent(QMouseEvent *event)
  void mousePressEvent(QMouseEvent *event) override {
    if (taken[25]) {
      int handled = 0;
      CuteQDeclarativeRectangleMapItemCall25 call = reinterpret_cast<CuteQDeclarativeRectangleMapItemCall25>(taken[25]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::mousePressEvent(event);
  }

  //  void QQuickItem::mouseMoveEvent(QMouseEvent *event)
  void mouseMoveEvent(QMouseEvent *event) override {
    if (taken[26]) {
      int handled = 0;
      CuteQDeclarativeRectangleMapItemCall26 call = reinterpret_cast<CuteQDeclarativeRectangleMapItemCall26>(taken[26]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::mouseMoveEvent(event);
  }

  //  void QQuickItem::mouseReleaseEvent(QMouseEvent *event)
  void mouseReleaseEvent(QMouseEvent *event) override {
    if (taken[27]) {
      int handled = 0;
      CuteQDeclarativeRectangleMapItemCall27 call = reinterpret_cast<CuteQDeclarativeRectangleMapItemCall27>(taken[27]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::mouseReleaseEvent(event);
  }

  //  void QQuickItem::mouseDoubleClickEvent(QMouseEvent *event)
  void mouseDoubleClickEvent(QMouseEvent *event) override {
    if (taken[28]) {
      int handled = 0;
      CuteQDeclarativeRectangleMapItemCall28 call = reinterpret_cast<CuteQDeclarativeRectangleMapItemCall28>(taken[28]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::mouseDoubleClickEvent(event);
  }

  //  void QQuickItem::mouseUngrabEvent()
  void mouseUngrabEvent() override {
    if (taken[29]) {
      int handled = 0;
      CuteQDeclarativeRectangleMapItemCall29 call = reinterpret_cast<CuteQDeclarativeRectangleMapItemCall29>(taken[29]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItem::mouseUngrabEvent();
  }

  //  void QQuickItem::touchUngrabEvent()
  void touchUngrabEvent() override {
    if (taken[30]) {
      int handled = 0;
      CuteQDeclarativeRectangleMapItemCall30 call = reinterpret_cast<CuteQDeclarativeRectangleMapItemCall30>(taken[30]);
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
      CuteQDeclarativeRectangleMapItemCall31 call = reinterpret_cast<CuteQDeclarativeRectangleMapItemCall31>(taken[31]);
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
      CuteQDeclarativeRectangleMapItemCall32 call = reinterpret_cast<CuteQDeclarativeRectangleMapItemCall32>(taken[32]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::touchEvent(event);
  }

  //  void QQuickItem::hoverEnterEvent(QHoverEvent *event)
  void hoverEnterEvent(QHoverEvent *event) override {
    if (taken[33]) {
      int handled = 0;
      CuteQDeclarativeRectangleMapItemCall33 call = reinterpret_cast<CuteQDeclarativeRectangleMapItemCall33>(taken[33]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::hoverEnterEvent(event);
  }

  //  void QQuickItem::hoverMoveEvent(QHoverEvent *event)
  void hoverMoveEvent(QHoverEvent *event) override {
    if (taken[34]) {
      int handled = 0;
      CuteQDeclarativeRectangleMapItemCall34 call = reinterpret_cast<CuteQDeclarativeRectangleMapItemCall34>(taken[34]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::hoverMoveEvent(event);
  }

  //  void QQuickItem::hoverLeaveEvent(QHoverEvent *event)
  void hoverLeaveEvent(QHoverEvent *event) override {
    if (taken[35]) {
      int handled = 0;
      CuteQDeclarativeRectangleMapItemCall35 call = reinterpret_cast<CuteQDeclarativeRectangleMapItemCall35>(taken[35]);
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
      CuteQDeclarativeRectangleMapItemCall36 call = reinterpret_cast<CuteQDeclarativeRectangleMapItemCall36>(taken[36]);
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
      CuteQDeclarativeRectangleMapItemCall37 call = reinterpret_cast<CuteQDeclarativeRectangleMapItemCall37>(taken[37]);
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
      CuteQDeclarativeRectangleMapItemCall38 call = reinterpret_cast<CuteQDeclarativeRectangleMapItemCall38>(taken[38]);
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
      CuteQDeclarativeRectangleMapItemCall39 call = reinterpret_cast<CuteQDeclarativeRectangleMapItemCall39>(taken[39]);
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
      CuteQDeclarativeRectangleMapItemCall40 call = reinterpret_cast<CuteQDeclarativeRectangleMapItemCall40>(taken[40]);
      bool given = call(this, a0, a1, &handled);
      if (handled) return given;
    }
    return QQuickItem::childMouseEventFilter(a0, a1);
  }

  //  void QQuickItem::releaseResources()
  void releaseResources() override {
    if (taken[41]) {
      int handled = 0;
      CuteQDeclarativeRectangleMapItemCall41 call = reinterpret_cast<CuteQDeclarativeRectangleMapItemCall41>(taken[41]);
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
      CuteQDeclarativeRectangleMapItemCall42 call = reinterpret_cast<CuteQDeclarativeRectangleMapItemCall42>(taken[42]);
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
      CuteQDeclarativeRectangleMapItemCall43 call = reinterpret_cast<CuteQDeclarativeRectangleMapItemCall43>(taken[43]);
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
      CuteQDeclarativeRectangleMapItemCall44 call = reinterpret_cast<CuteQDeclarativeRectangleMapItemCall44>(taken[44]);
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
      CuteQDeclarativeRectangleMapItemCall45 call = reinterpret_cast<CuteQDeclarativeRectangleMapItemCall45>(taken[45]);
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
      CuteQDeclarativeRectangleMapItemCall46 call = reinterpret_cast<CuteQDeclarativeRectangleMapItemCall46>(taken[46]);
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
      CuteQDeclarativeRectangleMapItemCall47 call = reinterpret_cast<CuteQDeclarativeRectangleMapItemCall47>(taken[47]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QDeclarativeRectangleMapItem::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK28QDeclarativeRectangleMapItem10metaObjectEv(
    const QDeclarativeRectangleMapItem *self) {
  return self->metaObject();
}

//  void *QDeclarativeRectangleMapItem::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN28QDeclarativeRectangleMapItem11qt_metacastEPKc(
    QDeclarativeRectangleMapItem *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QDeclarativeRectangleMapItem::qt_metacall(QMetaObject::Call a0, int
//      a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN28QDeclarativeRectangleMapItem11qt_metacallEN11QMetaObject4CallEiPPv(
    QDeclarativeRectangleMapItem *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QDeclarativeRectangleMapItem::tr(const char *s, const char *c,
//      int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN28QDeclarativeRectangleMapItem2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QDeclarativeRectangleMapItem::tr(s, c, n));
}

//  QDeclarativeRectangleMapItem::QDeclarativeRectangleMapItem(QQuickItem
//      *parent)
extern "C" Q_DECL_EXPORT
QDeclarativeRectangleMapItem *ritual_ZN28QDeclarativeRectangleMapItemC1EP10QQuickItem(
    QQuickItem *parent) {
  return new CuteQDeclarativeRectangleMapItem(parent);
}

//  QDeclarativeRectangleMapItem::~QDeclarativeRectangleMapItem()
extern "C" Q_DECL_EXPORT
void ritual_ZN28QDeclarativeRectangleMapItemD1Ev(
    QDeclarativeRectangleMapItem *self) {
  delete self;
}

//  void QDeclarativeRectangleMapItem::setMap(QDeclarativeGeoMap *quickMap,
//      QGeoMap *map)
extern "C" Q_DECL_EXPORT
void ritual_ZN28QDeclarativeRectangleMapItem6setMapEP18QDeclarativeGeoMapP7QGeoMap(
    QDeclarativeRectangleMapItem *self,
    QDeclarativeGeoMap *quickMap,
    QGeoMap *map) {
  self->setMap(quickMap, map);
}

//  QSGNode *QDeclarativeRectangleMapItem::updateMapItemPaintNode(QSGNode
//      *a0, UpdatePaintNodeData *a1)
extern "C" Q_DECL_EXPORT
QSGNode *ritual_ZN28QDeclarativeRectangleMapItem22updateMapItemPaintNodeEP7QSGNodePN10QQuickItem19UpdatePaintNodeDataE(
    QDeclarativeRectangleMapItem *self,
    QSGNode *a0,
    QQuickItem::UpdatePaintNodeData *a1) {
  return self->updateMapItemPaintNode(a0, a1);
}

//  QGeoCoordinate QDeclarativeRectangleMapItem::topLeft()
extern "C" Q_DECL_EXPORT
QGeoCoordinate *ritual_ZN28QDeclarativeRectangleMapItem7topLeftEv(
    QDeclarativeRectangleMapItem *self) {
  return new QGeoCoordinate(self->topLeft());
}

//  void QDeclarativeRectangleMapItem::setTopLeft(const QGeoCoordinate
//      &center)
extern "C" Q_DECL_EXPORT
void ritual_ZN28QDeclarativeRectangleMapItem10setTopLeftERK14QGeoCoordinate(
    QDeclarativeRectangleMapItem *self,
    const QGeoCoordinate *center) {
  self->setTopLeft(*center);
}

//  QGeoCoordinate QDeclarativeRectangleMapItem::bottomRight()
extern "C" Q_DECL_EXPORT
QGeoCoordinate *ritual_ZN28QDeclarativeRectangleMapItem11bottomRightEv(
    QDeclarativeRectangleMapItem *self) {
  return new QGeoCoordinate(self->bottomRight());
}

//  void QDeclarativeRectangleMapItem::setBottomRight(const QGeoCoordinate
//      &center)
extern "C" Q_DECL_EXPORT
void ritual_ZN28QDeclarativeRectangleMapItem14setBottomRightERK14QGeoCoordinate(
    QDeclarativeRectangleMapItem *self,
    const QGeoCoordinate *center) {
  self->setBottomRight(*center);
}

//  QColor QDeclarativeRectangleMapItem::color() const
extern "C" Q_DECL_EXPORT
QColor *ritual_ZNK28QDeclarativeRectangleMapItem5colorEv(
    const QDeclarativeRectangleMapItem *self) {
  return new QColor(self->color());
}

//  void QDeclarativeRectangleMapItem::setColor(const QColor &color)
extern "C" Q_DECL_EXPORT
void ritual_ZN28QDeclarativeRectangleMapItem8setColorERK6QColor(
    QDeclarativeRectangleMapItem *self,
    const QColor *color) {
  self->setColor(*color);
}

//  QDeclarativeMapLineProperties *QDeclarativeRectangleMapItem::border()
extern "C" Q_DECL_EXPORT
QDeclarativeMapLineProperties *ritual_ZN28QDeclarativeRectangleMapItem6borderEv(
    QDeclarativeRectangleMapItem *self) {
  return self->border();
}

//  bool QDeclarativeRectangleMapItem::contains(const QPointF &point) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK28QDeclarativeRectangleMapItem8containsERK7QPointF(
    const QDeclarativeRectangleMapItem *self,
    const QPointF *point) {
  return self->contains(*point);
}

//  const QGeoShape &QDeclarativeRectangleMapItem::geoShape() const
extern "C" Q_DECL_EXPORT
QGeoShape *ritual_ZNK28QDeclarativeRectangleMapItem8geoShapeEv(
    const QDeclarativeRectangleMapItem *self) {
  return new QGeoShape(self->geoShape());
}

//  void QDeclarativeRectangleMapItem::setGeoShape(const QGeoShape &shape)
extern "C" Q_DECL_EXPORT
void ritual_ZN28QDeclarativeRectangleMapItem11setGeoShapeERK9QGeoShape(
    QDeclarativeRectangleMapItem *self,
    const QGeoShape *shape) {
  self->setGeoShape(*shape);
}

//  void QDeclarativeRectangleMapItem::topLeftChanged(const QGeoCoordinate
//      &topLeft)
extern "C" Q_DECL_EXPORT
void ritual_ZN28QDeclarativeRectangleMapItem14topLeftChangedERK14QGeoCoordinate(
    QDeclarativeRectangleMapItem *self,
    const QGeoCoordinate *topLeft) {
  self->topLeftChanged(*topLeft);
}

//  void QDeclarativeRectangleMapItem::bottomRightChanged(const
//      QGeoCoordinate &bottomRight)
extern "C" Q_DECL_EXPORT
void ritual_ZN28QDeclarativeRectangleMapItem18bottomRightChangedERK14QGeoCoordinate(
    QDeclarativeRectangleMapItem *self,
    const QGeoCoordinate *bottomRight) {
  self->bottomRightChanged(*bottomRight);
}

//  void QDeclarativeRectangleMapItem::colorChanged(const QColor &color)
extern "C" Q_DECL_EXPORT
void ritual_ZN28QDeclarativeRectangleMapItem12colorChangedERK6QColor(
    QDeclarativeRectangleMapItem *self,
    const QColor *color) {
  self->colorChanged(*color);
}

//  void QDeclarativeRectangleMapItem::geometryChange(const QRectF
//      &newGeometry, const QRectF &oldGeometry)
extern "C" Q_DECL_EXPORT
void ritual_ZN28QDeclarativeRectangleMapItem14geometryChangeERK6QRectFS2_(
    QDeclarativeRectangleMapItem *self,
    const QRectF *newGeometry,
    const QRectF *oldGeometry) {
  self->geometryChange(*newGeometry, *oldGeometry);
}

//  void QDeclarativeRectangleMapItem::updatePolish()
extern "C" Q_DECL_EXPORT
void ritual_ZN28QDeclarativeRectangleMapItem12updatePolishEv(
    QDeclarativeRectangleMapItem *self) {
  self->updatePolish();
}

//  void QDeclarativeRectangleMapItem::markSourceDirtyAndUpdate()
extern "C" Q_DECL_EXPORT
void ritual_ZN28QDeclarativeRectangleMapItem24markSourceDirtyAndUpdateEv(
    QDeclarativeRectangleMapItem *self) {
  self->markSourceDirtyAndUpdate();
}

//  void QDeclarativeRectangleMapItem::onLinePropertiesChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN28QDeclarativeRectangleMapItem23onLinePropertiesChangedEv(
    QDeclarativeRectangleMapItem *self) {
  self->onLinePropertiesChanged();
}

//  void QDeclarativeRectangleMapItem::afterViewportChanged(const
//      QGeoMapViewportChangeEvent &event)
extern "C" Q_DECL_EXPORT
void ritual_ZN28QDeclarativeRectangleMapItem20afterViewportChangedERK26QGeoMapViewportChangeEvent(
    QDeclarativeRectangleMapItem *self,
    const QGeoMapViewportChangeEvent *event) {
  self->afterViewportChanged(*event);
}

//  a Python function taken by a CuteQDeclarativeRectangleMapItem, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QDeclarativeRectangleMapItem(
    QDeclarativeRectangleMapItem *self,
    const char *key,
    void *call) {
  return static_cast<CuteQDeclarativeRectangleMapItem *>(self)->take(key, call);
}

//  void QDeclarativeRectangleMapItem::setMap(QDeclarativeGeoMap *quickMap,
//      QGeoMap *map)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN28QDeclarativeRectangleMapItem6setMapEP18QDeclarativeGeoMapP7QGeoMap(
    QDeclarativeRectangleMapItem *self,
    QDeclarativeGeoMap *quickMap,
    QGeoMap *map) {
  self->QDeclarativeRectangleMapItem::setMap(quickMap, map);
}

//  QSGNode *QDeclarativeRectangleMapItem::updateMapItemPaintNode(QSGNode
//      *a0, UpdatePaintNodeData *a1)
extern "C" Q_DECL_EXPORT
QSGNode *ritual_own_ZN28QDeclarativeRectangleMapItem22updateMapItemPaintNodeEP7QSGNodePN10QQuickItem19UpdatePaintNodeDataE(
    QDeclarativeRectangleMapItem *self,
    QSGNode *a0,
    QQuickItem::UpdatePaintNodeData *a1) {
  return self->QDeclarativeRectangleMapItem::updateMapItemPaintNode(a0, a1);
}

//  bool QDeclarativeRectangleMapItem::contains(const QPointF &point) const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK28QDeclarativeRectangleMapItem8containsERK7QPointF(
    const QDeclarativeRectangleMapItem *self,
    const QPointF *point) {
  return self->QDeclarativeRectangleMapItem::contains(*point);
}

//  const QGeoShape &QDeclarativeRectangleMapItem::geoShape() const
extern "C" Q_DECL_EXPORT
QGeoShape *ritual_own_ZNK28QDeclarativeRectangleMapItem8geoShapeEv(
    const QDeclarativeRectangleMapItem *self) {
  return new QGeoShape(self->QDeclarativeRectangleMapItem::geoShape());
}

//  void QDeclarativeRectangleMapItem::setGeoShape(const QGeoShape &shape)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN28QDeclarativeRectangleMapItem11setGeoShapeERK9QGeoShape(
    QDeclarativeRectangleMapItem *self,
    const QGeoShape *shape) {
  self->QDeclarativeRectangleMapItem::setGeoShape(*shape);
}

//  void QDeclarativeRectangleMapItem::geometryChange(const QRectF
//      &newGeometry, const QRectF &oldGeometry)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN28QDeclarativeRectangleMapItem14geometryChangeERK6QRectFS2_(
    QDeclarativeRectangleMapItem *self,
    const QRectF *newGeometry,
    const QRectF *oldGeometry) {
  static_cast<OwnQDeclarativeRectangleMapItem *>(self)->OwnQDeclarativeRectangleMapItem::geometryChange(
      *newGeometry,
      *oldGeometry);
}

//  void QDeclarativeRectangleMapItem::updatePolish()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN28QDeclarativeRectangleMapItem12updatePolishEv(
    QDeclarativeRectangleMapItem *self) {
  static_cast<OwnQDeclarativeRectangleMapItem *>(self)->OwnQDeclarativeRectangleMapItem::updatePolish();
}

//  void QDeclarativeRectangleMapItem::afterViewportChanged(const
//      QGeoMapViewportChangeEvent &event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN28QDeclarativeRectangleMapItem20afterViewportChangedERK26QGeoMapViewportChangeEvent(
    QDeclarativeRectangleMapItem *self,
    const QGeoMapViewportChangeEvent *event) {
  static_cast<OwnQDeclarativeRectangleMapItem *>(self)->OwnQDeclarativeRectangleMapItem::afterViewportChanged(
      *event);
}
