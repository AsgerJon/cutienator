//  Written by dev_tooling.RitualGenerator from the records of
//  QtLocation/6.12.0/QtLocation/private/qdeclarativegeomapitembase_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtGui/qtguiglobal.h>
#include <QtQuick/qtquickglobal.h>
#include <QtLocation/6.12.0/QtLocation/private/qlocationglobal_p.h>
#include <QtLocation/QtLocation>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtLocation/6.12.0/QtLocation/private/qdeclarativegeomapitembase_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtPositioning/qgeocoordinate.h>
#include <QtCore/qpoint.h>
#include <QtPositioning/qgeoshape.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtLocation/6.12.0/QtLocation/private/qgeocameradata_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qrect.h>
#include <QtCore/qvariant.h>
#include <QtQuick/QtQuick>
#include <QtQuick/qquickitem.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  Only a class built on QDeclarativeGeoMapItemBase may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQDeclarativeGeoMapItemBase : QDeclarativeGeoMapItemBase {
  using QDeclarativeGeoMapItemBase::afterChildrenChanged;
};

//  A QDeclarativeGeoMapItemBase that Python can take functions over in. Every QDeclarativeGeoMapItemBase
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQDeclarativeGeoMapItemBaseCall0)(const void *, QDeclarativeGeoMap *, QGeoMap *, int *);
typedef void (*CuteQDeclarativeGeoMapItemBaseCall1)(const void *, const QGeoCoordinate *, const QPointF *, int *);
typedef const QGeoShape * (*CuteQDeclarativeGeoMapItemBaseCall2)(const void *, int *);
typedef void (*CuteQDeclarativeGeoMapItemBaseCall3)(const void *, const QGeoShape *, int *);
typedef void * (*CuteQDeclarativeGeoMapItemBaseCall4)(const void *, QSGNode *, QQuickItem::UpdatePaintNodeData *, int *);
typedef void * (*CuteQDeclarativeGeoMapItemBaseCall5)(const void *, QSGNode *, QQuickItem::UpdatePaintNodeData *, int *);
typedef void (*CuteQDeclarativeGeoMapItemBaseCall6)(const void *, int *);
typedef void (*CuteQDeclarativeGeoMapItemBaseCall7)(const void *, const QGeoMapViewportChangeEvent *, int *);
typedef const QRectF * (*CuteQDeclarativeGeoMapItemBaseCall8)(const void *, int *);
typedef const QRectF * (*CuteQDeclarativeGeoMapItemBaseCall9)(const void *, int *);
typedef bool (*CuteQDeclarativeGeoMapItemBaseCall10)(const void *, const QPointF *, int *);
#if QT_CONFIG(im)
typedef const QVariant * (*CuteQDeclarativeGeoMapItemBaseCall11)(const void *, int, int *);
#endif  // QT_CONFIG(im)
typedef bool (*CuteQDeclarativeGeoMapItemBaseCall12)(const void *, int *);
typedef void * (*CuteQDeclarativeGeoMapItemBaseCall13)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQDeclarativeGeoMapItemBaseCall14)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
typedef void (*CuteQDeclarativeGeoMapItemBaseCall15)(const void *, int, const QQuickItem::ItemChangeData *, int *);
typedef void (*CuteQDeclarativeGeoMapItemBaseCall16)(const void *, const QRectF *, const QRectF *, int *);
typedef void (*CuteQDeclarativeGeoMapItemBaseCall17)(const void *, int *);
typedef void (*CuteQDeclarativeGeoMapItemBaseCall18)(const void *, int *);
typedef void (*CuteQDeclarativeGeoMapItemBaseCall19)(const void *, QKeyEvent *, int *);
typedef void (*CuteQDeclarativeGeoMapItemBaseCall20)(const void *, QKeyEvent *, int *);
#if QT_CONFIG(im)
typedef void (*CuteQDeclarativeGeoMapItemBaseCall21)(const void *, QInputMethodEvent *, int *);
#endif  // QT_CONFIG(im)
typedef void (*CuteQDeclarativeGeoMapItemBaseCall22)(const void *, QFocusEvent *, int *);
typedef void (*CuteQDeclarativeGeoMapItemBaseCall23)(const void *, QFocusEvent *, int *);
typedef void (*CuteQDeclarativeGeoMapItemBaseCall24)(const void *, QMouseEvent *, int *);
typedef void (*CuteQDeclarativeGeoMapItemBaseCall25)(const void *, QMouseEvent *, int *);
typedef void (*CuteQDeclarativeGeoMapItemBaseCall26)(const void *, QMouseEvent *, int *);
typedef void (*CuteQDeclarativeGeoMapItemBaseCall27)(const void *, QMouseEvent *, int *);
typedef void (*CuteQDeclarativeGeoMapItemBaseCall28)(const void *, int *);
typedef void (*CuteQDeclarativeGeoMapItemBaseCall29)(const void *, int *);
#if QT_CONFIG(wheelevent)
typedef void (*CuteQDeclarativeGeoMapItemBaseCall30)(const void *, QWheelEvent *, int *);
#endif  // QT_CONFIG(wheelevent)
typedef void (*CuteQDeclarativeGeoMapItemBaseCall31)(const void *, QTouchEvent *, int *);
typedef void (*CuteQDeclarativeGeoMapItemBaseCall32)(const void *, QHoverEvent *, int *);
typedef void (*CuteQDeclarativeGeoMapItemBaseCall33)(const void *, QHoverEvent *, int *);
typedef void (*CuteQDeclarativeGeoMapItemBaseCall34)(const void *, QHoverEvent *, int *);
#if QT_CONFIG(quick_draganddrop)
typedef void (*CuteQDeclarativeGeoMapItemBaseCall35)(const void *, QDragEnterEvent *, int *);
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
typedef void (*CuteQDeclarativeGeoMapItemBaseCall36)(const void *, QDragMoveEvent *, int *);
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
typedef void (*CuteQDeclarativeGeoMapItemBaseCall37)(const void *, QDragLeaveEvent *, int *);
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
typedef void (*CuteQDeclarativeGeoMapItemBaseCall38)(const void *, QDropEvent *, int *);
#endif  // QT_CONFIG(quick_draganddrop)
typedef bool (*CuteQDeclarativeGeoMapItemBaseCall39)(const void *, QQuickItem *, QEvent *, int *);
typedef void (*CuteQDeclarativeGeoMapItemBaseCall40)(const void *, int *);
typedef void (*CuteQDeclarativeGeoMapItemBaseCall41)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQDeclarativeGeoMapItemBaseCall42)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQDeclarativeGeoMapItemBaseCall43)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQDeclarativeGeoMapItemBaseCall44)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQDeclarativeGeoMapItemBaseCall45)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQDeclarativeGeoMapItemBaseCall46)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQDeclarativeGeoMapItemBaseCall47)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQDeclarativeGeoMapItemBase : public QDeclarativeGeoMapItemBase {
public:
  using QDeclarativeGeoMapItemBase::QDeclarativeGeoMapItemBase;
  void *taken[48] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN26QDeclarativeGeoMapItemBase6setMapEP18QDeclarativeGeoMapP7QGeoMap")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN26QDeclarativeGeoMapItemBase16setPositionOnMapERK14QGeoCoordinateRK7QPointF")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK26QDeclarativeGeoMapItemBase8geoShapeEv")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN26QDeclarativeGeoMapItemBase11setGeoShapeERK9QGeoShape")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem15updatePaintNodeEP7QSGNodePNS_19UpdatePaintNodeDataE")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN26QDeclarativeGeoMapItemBase22updateMapItemPaintNodeEP7QSGNodePN10QQuickItem19UpdatePaintNodeDataE")) {
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
    if (!std::strcmp(key, "_ZNK10QQuickItem12boundingRectEv")) {
      taken[8] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK10QQuickItem8clipRectEv")) {
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
    if (!std::strcmp(key, "_ZN10QQuickItem10itemChangeENS_10ItemChangeERKNS_14ItemChangeDataE")) {
      taken[15] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem14geometryChangeERK6QRectFS2_")) {
      taken[16] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQmlParserStatus10classBeginEv")) {
      taken[17] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQmlParserStatus17componentCompleteEv")) {
      taken[18] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem13keyPressEventEP9QKeyEvent")) {
      taken[19] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem15keyReleaseEventEP9QKeyEvent")) {
      taken[20] = call;
      return true;
    }
#if QT_CONFIG(im)
    if (!std::strcmp(key, "_ZN10QQuickItem16inputMethodEventEP17QInputMethodEvent")) {
      taken[21] = call;
      return true;
    }
#endif  // QT_CONFIG(im)
    if (!std::strcmp(key, "_ZN10QQuickItem12focusInEventEP11QFocusEvent")) {
      taken[22] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem13focusOutEventEP11QFocusEvent")) {
      taken[23] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem15mousePressEventEP11QMouseEvent")) {
      taken[24] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem14mouseMoveEventEP11QMouseEvent")) {
      taken[25] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem17mouseReleaseEventEP11QMouseEvent")) {
      taken[26] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem21mouseDoubleClickEventEP11QMouseEvent")) {
      taken[27] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem16mouseUngrabEventEv")) {
      taken[28] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem16touchUngrabEventEv")) {
      taken[29] = call;
      return true;
    }
#if QT_CONFIG(wheelevent)
    if (!std::strcmp(key, "_ZN10QQuickItem10wheelEventEP11QWheelEvent")) {
      taken[30] = call;
      return true;
    }
#endif  // QT_CONFIG(wheelevent)
    if (!std::strcmp(key, "_ZN10QQuickItem10touchEventEP11QTouchEvent")) {
      taken[31] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem15hoverEnterEventEP11QHoverEvent")) {
      taken[32] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem14hoverMoveEventEP11QHoverEvent")) {
      taken[33] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem15hoverLeaveEventEP11QHoverEvent")) {
      taken[34] = call;
      return true;
    }
#if QT_CONFIG(quick_draganddrop)
    if (!std::strcmp(key, "_ZN10QQuickItem14dragEnterEventEP15QDragEnterEvent")) {
      taken[35] = call;
      return true;
    }
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
    if (!std::strcmp(key, "_ZN10QQuickItem13dragMoveEventEP14QDragMoveEvent")) {
      taken[36] = call;
      return true;
    }
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
    if (!std::strcmp(key, "_ZN10QQuickItem14dragLeaveEventEP15QDragLeaveEvent")) {
      taken[37] = call;
      return true;
    }
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
    if (!std::strcmp(key, "_ZN10QQuickItem9dropEventEP10QDropEvent")) {
      taken[38] = call;
      return true;
    }
#endif  // QT_CONFIG(quick_draganddrop)
    if (!std::strcmp(key, "_ZN10QQuickItem21childMouseEventFilterEPS_P6QEvent")) {
      taken[39] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem16releaseResourcesEv")) {
      taken[40] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem12updatePolishEv")) {
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

  //  void QDeclarativeGeoMapItemBase::setMap(QDeclarativeGeoMap *quickMap,
  //      QGeoMap *map)
  void setMap(QDeclarativeGeoMap *quickMap, QGeoMap *map) override {
    if (taken[0]) {
      int handled = 0;
      CuteQDeclarativeGeoMapItemBaseCall0 call = reinterpret_cast<CuteQDeclarativeGeoMapItemBaseCall0>(taken[0]);
      call(this, quickMap, map, &handled);
      if (handled) return;
    }
    QDeclarativeGeoMapItemBase::setMap(quickMap, map);
  }

  //  void QDeclarativeGeoMapItemBase::setPositionOnMap(const
  //      QGeoCoordinate &coordinate, const QPointF &offset)
  void setPositionOnMap(
      const QGeoCoordinate &coordinate,
      const QPointF &offset) override {
    if (taken[1]) {
      int handled = 0;
      CuteQDeclarativeGeoMapItemBaseCall1 call = reinterpret_cast<CuteQDeclarativeGeoMapItemBaseCall1>(taken[1]);
      call(this, &coordinate, &offset, &handled);
      if (handled) return;
    }
    QDeclarativeGeoMapItemBase::setPositionOnMap(coordinate, offset);
  }

  //  const QGeoShape &QDeclarativeGeoMapItemBase::geoShape() const
  const QGeoShape &geoShape() const override {
    if (taken[2]) {
      int handled = 0;
      CuteQDeclarativeGeoMapItemBaseCall2 call = reinterpret_cast<CuteQDeclarativeGeoMapItemBaseCall2>(taken[2]);
      const QGeoShape * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return {};
  }

  //  void QDeclarativeGeoMapItemBase::setGeoShape(const QGeoShape &shape)
  void setGeoShape(const QGeoShape &shape) override {
    if (taken[3]) {
      int handled = 0;
      CuteQDeclarativeGeoMapItemBaseCall3 call = reinterpret_cast<CuteQDeclarativeGeoMapItemBaseCall3>(taken[3]);
      call(this, &shape, &handled);
      if (handled) return;
    }
  }

  //  QSGNode *QDeclarativeGeoMapItemBase::updatePaintNode(QSGNode *a0,
  //      UpdatePaintNodeData *a1)
  QSGNode *updatePaintNode(
      QSGNode *a0,
      QQuickItem::UpdatePaintNodeData *a1) override {
    if (taken[4]) {
      int handled = 0;
      CuteQDeclarativeGeoMapItemBaseCall4 call = reinterpret_cast<CuteQDeclarativeGeoMapItemBaseCall4>(taken[4]);
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
    if (taken[5]) {
      int handled = 0;
      CuteQDeclarativeGeoMapItemBaseCall5 call = reinterpret_cast<CuteQDeclarativeGeoMapItemBaseCall5>(taken[5]);
      void * given = call(this, a0, a1, &handled);
      if (handled) return static_cast<QSGNode *>(given);
    }
    return QDeclarativeGeoMapItemBase::updateMapItemPaintNode(a0, a1);
  }

  //  void QDeclarativeGeoMapItemBase::afterChildrenChanged()
  void afterChildrenChanged() override {
    if (taken[6]) {
      int handled = 0;
      CuteQDeclarativeGeoMapItemBaseCall6 call = reinterpret_cast<CuteQDeclarativeGeoMapItemBaseCall6>(taken[6]);
      call(this, &handled);
      if (handled) return;
    }
    QDeclarativeGeoMapItemBase::afterChildrenChanged();
  }

  //  void QDeclarativeGeoMapItemBase::afterViewportChanged(const
  //      QGeoMapViewportChangeEvent &event)
  void afterViewportChanged(
      const QGeoMapViewportChangeEvent &event) override {
    if (taken[7]) {
      int handled = 0;
      CuteQDeclarativeGeoMapItemBaseCall7 call = reinterpret_cast<CuteQDeclarativeGeoMapItemBaseCall7>(taken[7]);
      call(this, &event, &handled);
      if (handled) return;
    }
  }

  //  QRectF QQuickItem::boundingRect() const
  QRectF boundingRect() const override {
    if (taken[8]) {
      int handled = 0;
      CuteQDeclarativeGeoMapItemBaseCall8 call = reinterpret_cast<CuteQDeclarativeGeoMapItemBaseCall8>(taken[8]);
      const QRectF * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QQuickItem::boundingRect();
  }

  //  QRectF QQuickItem::clipRect() const
  QRectF clipRect() const override {
    if (taken[9]) {
      int handled = 0;
      CuteQDeclarativeGeoMapItemBaseCall9 call = reinterpret_cast<CuteQDeclarativeGeoMapItemBaseCall9>(taken[9]);
      const QRectF * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QQuickItem::clipRect();
  }

  //  bool QQuickItem::contains(const QPointF &point) const
  bool contains(const QPointF &point) const override {
    if (taken[10]) {
      int handled = 0;
      CuteQDeclarativeGeoMapItemBaseCall10 call = reinterpret_cast<CuteQDeclarativeGeoMapItemBaseCall10>(taken[10]);
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
      CuteQDeclarativeGeoMapItemBaseCall11 call = reinterpret_cast<CuteQDeclarativeGeoMapItemBaseCall11>(taken[11]);
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
      CuteQDeclarativeGeoMapItemBaseCall12 call = reinterpret_cast<CuteQDeclarativeGeoMapItemBaseCall12>(taken[12]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QQuickItem::isTextureProvider();
  }

  //  QSGTextureProvider *QQuickItem::textureProvider() const
  QSGTextureProvider *textureProvider() const override {
    if (taken[13]) {
      int handled = 0;
      CuteQDeclarativeGeoMapItemBaseCall13 call = reinterpret_cast<CuteQDeclarativeGeoMapItemBaseCall13>(taken[13]);
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
      CuteQDeclarativeGeoMapItemBaseCall14 call = reinterpret_cast<CuteQDeclarativeGeoMapItemBaseCall14>(taken[14]);
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
    if (taken[15]) {
      int handled = 0;
      CuteQDeclarativeGeoMapItemBaseCall15 call = reinterpret_cast<CuteQDeclarativeGeoMapItemBaseCall15>(taken[15]);
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
    if (taken[16]) {
      int handled = 0;
      CuteQDeclarativeGeoMapItemBaseCall16 call = reinterpret_cast<CuteQDeclarativeGeoMapItemBaseCall16>(taken[16]);
      call(this, &newGeometry, &oldGeometry, &handled);
      if (handled) return;
    }
    QQuickItem::geometryChange(newGeometry, oldGeometry);
  }

  //  void QQuickItem::classBegin()
  void classBegin() override {
    if (taken[17]) {
      int handled = 0;
      CuteQDeclarativeGeoMapItemBaseCall17 call = reinterpret_cast<CuteQDeclarativeGeoMapItemBaseCall17>(taken[17]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItem::classBegin();
  }

  //  void QQuickItem::componentComplete()
  void componentComplete() override {
    if (taken[18]) {
      int handled = 0;
      CuteQDeclarativeGeoMapItemBaseCall18 call = reinterpret_cast<CuteQDeclarativeGeoMapItemBaseCall18>(taken[18]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItem::componentComplete();
  }

  //  void QQuickItem::keyPressEvent(QKeyEvent *event)
  void keyPressEvent(QKeyEvent *event) override {
    if (taken[19]) {
      int handled = 0;
      CuteQDeclarativeGeoMapItemBaseCall19 call = reinterpret_cast<CuteQDeclarativeGeoMapItemBaseCall19>(taken[19]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::keyPressEvent(event);
  }

  //  void QQuickItem::keyReleaseEvent(QKeyEvent *event)
  void keyReleaseEvent(QKeyEvent *event) override {
    if (taken[20]) {
      int handled = 0;
      CuteQDeclarativeGeoMapItemBaseCall20 call = reinterpret_cast<CuteQDeclarativeGeoMapItemBaseCall20>(taken[20]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::keyReleaseEvent(event);
  }

#if QT_CONFIG(im)
  //  void QQuickItem::inputMethodEvent(QInputMethodEvent *a0)
  void inputMethodEvent(QInputMethodEvent *a0) override {
    if (taken[21]) {
      int handled = 0;
      CuteQDeclarativeGeoMapItemBaseCall21 call = reinterpret_cast<CuteQDeclarativeGeoMapItemBaseCall21>(taken[21]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItem::inputMethodEvent(a0);
  }
#endif  // QT_CONFIG(im)

  //  void QQuickItem::focusInEvent(QFocusEvent *a0)
  void focusInEvent(QFocusEvent *a0) override {
    if (taken[22]) {
      int handled = 0;
      CuteQDeclarativeGeoMapItemBaseCall22 call = reinterpret_cast<CuteQDeclarativeGeoMapItemBaseCall22>(taken[22]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItem::focusInEvent(a0);
  }

  //  void QQuickItem::focusOutEvent(QFocusEvent *a0)
  void focusOutEvent(QFocusEvent *a0) override {
    if (taken[23]) {
      int handled = 0;
      CuteQDeclarativeGeoMapItemBaseCall23 call = reinterpret_cast<CuteQDeclarativeGeoMapItemBaseCall23>(taken[23]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItem::focusOutEvent(a0);
  }

  //  void QQuickItem::mousePressEvent(QMouseEvent *event)
  void mousePressEvent(QMouseEvent *event) override {
    if (taken[24]) {
      int handled = 0;
      CuteQDeclarativeGeoMapItemBaseCall24 call = reinterpret_cast<CuteQDeclarativeGeoMapItemBaseCall24>(taken[24]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::mousePressEvent(event);
  }

  //  void QQuickItem::mouseMoveEvent(QMouseEvent *event)
  void mouseMoveEvent(QMouseEvent *event) override {
    if (taken[25]) {
      int handled = 0;
      CuteQDeclarativeGeoMapItemBaseCall25 call = reinterpret_cast<CuteQDeclarativeGeoMapItemBaseCall25>(taken[25]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::mouseMoveEvent(event);
  }

  //  void QQuickItem::mouseReleaseEvent(QMouseEvent *event)
  void mouseReleaseEvent(QMouseEvent *event) override {
    if (taken[26]) {
      int handled = 0;
      CuteQDeclarativeGeoMapItemBaseCall26 call = reinterpret_cast<CuteQDeclarativeGeoMapItemBaseCall26>(taken[26]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::mouseReleaseEvent(event);
  }

  //  void QQuickItem::mouseDoubleClickEvent(QMouseEvent *event)
  void mouseDoubleClickEvent(QMouseEvent *event) override {
    if (taken[27]) {
      int handled = 0;
      CuteQDeclarativeGeoMapItemBaseCall27 call = reinterpret_cast<CuteQDeclarativeGeoMapItemBaseCall27>(taken[27]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::mouseDoubleClickEvent(event);
  }

  //  void QQuickItem::mouseUngrabEvent()
  void mouseUngrabEvent() override {
    if (taken[28]) {
      int handled = 0;
      CuteQDeclarativeGeoMapItemBaseCall28 call = reinterpret_cast<CuteQDeclarativeGeoMapItemBaseCall28>(taken[28]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItem::mouseUngrabEvent();
  }

  //  void QQuickItem::touchUngrabEvent()
  void touchUngrabEvent() override {
    if (taken[29]) {
      int handled = 0;
      CuteQDeclarativeGeoMapItemBaseCall29 call = reinterpret_cast<CuteQDeclarativeGeoMapItemBaseCall29>(taken[29]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItem::touchUngrabEvent();
  }

#if QT_CONFIG(wheelevent)
  //  void QQuickItem::wheelEvent(QWheelEvent *event)
  void wheelEvent(QWheelEvent *event) override {
    if (taken[30]) {
      int handled = 0;
      CuteQDeclarativeGeoMapItemBaseCall30 call = reinterpret_cast<CuteQDeclarativeGeoMapItemBaseCall30>(taken[30]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::wheelEvent(event);
  }
#endif  // QT_CONFIG(wheelevent)

  //  void QQuickItem::touchEvent(QTouchEvent *event)
  void touchEvent(QTouchEvent *event) override {
    if (taken[31]) {
      int handled = 0;
      CuteQDeclarativeGeoMapItemBaseCall31 call = reinterpret_cast<CuteQDeclarativeGeoMapItemBaseCall31>(taken[31]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::touchEvent(event);
  }

  //  void QQuickItem::hoverEnterEvent(QHoverEvent *event)
  void hoverEnterEvent(QHoverEvent *event) override {
    if (taken[32]) {
      int handled = 0;
      CuteQDeclarativeGeoMapItemBaseCall32 call = reinterpret_cast<CuteQDeclarativeGeoMapItemBaseCall32>(taken[32]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::hoverEnterEvent(event);
  }

  //  void QQuickItem::hoverMoveEvent(QHoverEvent *event)
  void hoverMoveEvent(QHoverEvent *event) override {
    if (taken[33]) {
      int handled = 0;
      CuteQDeclarativeGeoMapItemBaseCall33 call = reinterpret_cast<CuteQDeclarativeGeoMapItemBaseCall33>(taken[33]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::hoverMoveEvent(event);
  }

  //  void QQuickItem::hoverLeaveEvent(QHoverEvent *event)
  void hoverLeaveEvent(QHoverEvent *event) override {
    if (taken[34]) {
      int handled = 0;
      CuteQDeclarativeGeoMapItemBaseCall34 call = reinterpret_cast<CuteQDeclarativeGeoMapItemBaseCall34>(taken[34]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::hoverLeaveEvent(event);
  }

#if QT_CONFIG(quick_draganddrop)
  //  void QQuickItem::dragEnterEvent(QDragEnterEvent *a0)
  void dragEnterEvent(QDragEnterEvent *a0) override {
    if (taken[35]) {
      int handled = 0;
      CuteQDeclarativeGeoMapItemBaseCall35 call = reinterpret_cast<CuteQDeclarativeGeoMapItemBaseCall35>(taken[35]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItem::dragEnterEvent(a0);
  }
#endif  // QT_CONFIG(quick_draganddrop)

#if QT_CONFIG(quick_draganddrop)
  //  void QQuickItem::dragMoveEvent(QDragMoveEvent *a0)
  void dragMoveEvent(QDragMoveEvent *a0) override {
    if (taken[36]) {
      int handled = 0;
      CuteQDeclarativeGeoMapItemBaseCall36 call = reinterpret_cast<CuteQDeclarativeGeoMapItemBaseCall36>(taken[36]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItem::dragMoveEvent(a0);
  }
#endif  // QT_CONFIG(quick_draganddrop)

#if QT_CONFIG(quick_draganddrop)
  //  void QQuickItem::dragLeaveEvent(QDragLeaveEvent *a0)
  void dragLeaveEvent(QDragLeaveEvent *a0) override {
    if (taken[37]) {
      int handled = 0;
      CuteQDeclarativeGeoMapItemBaseCall37 call = reinterpret_cast<CuteQDeclarativeGeoMapItemBaseCall37>(taken[37]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItem::dragLeaveEvent(a0);
  }
#endif  // QT_CONFIG(quick_draganddrop)

#if QT_CONFIG(quick_draganddrop)
  //  void QQuickItem::dropEvent(QDropEvent *a0)
  void dropEvent(QDropEvent *a0) override {
    if (taken[38]) {
      int handled = 0;
      CuteQDeclarativeGeoMapItemBaseCall38 call = reinterpret_cast<CuteQDeclarativeGeoMapItemBaseCall38>(taken[38]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItem::dropEvent(a0);
  }
#endif  // QT_CONFIG(quick_draganddrop)

  //  bool QQuickItem::childMouseEventFilter(QQuickItem *a0, QEvent *a1)
  bool childMouseEventFilter(QQuickItem *a0, QEvent *a1) override {
    if (taken[39]) {
      int handled = 0;
      CuteQDeclarativeGeoMapItemBaseCall39 call = reinterpret_cast<CuteQDeclarativeGeoMapItemBaseCall39>(taken[39]);
      bool given = call(this, a0, a1, &handled);
      if (handled) return given;
    }
    return QQuickItem::childMouseEventFilter(a0, a1);
  }

  //  void QQuickItem::releaseResources()
  void releaseResources() override {
    if (taken[40]) {
      int handled = 0;
      CuteQDeclarativeGeoMapItemBaseCall40 call = reinterpret_cast<CuteQDeclarativeGeoMapItemBaseCall40>(taken[40]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItem::releaseResources();
  }

  //  void QQuickItem::updatePolish()
  void updatePolish() override {
    if (taken[41]) {
      int handled = 0;
      CuteQDeclarativeGeoMapItemBaseCall41 call = reinterpret_cast<CuteQDeclarativeGeoMapItemBaseCall41>(taken[41]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItem::updatePolish();
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[42]) {
      int handled = 0;
      CuteQDeclarativeGeoMapItemBaseCall42 call = reinterpret_cast<CuteQDeclarativeGeoMapItemBaseCall42>(taken[42]);
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
      CuteQDeclarativeGeoMapItemBaseCall43 call = reinterpret_cast<CuteQDeclarativeGeoMapItemBaseCall43>(taken[43]);
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
      CuteQDeclarativeGeoMapItemBaseCall44 call = reinterpret_cast<CuteQDeclarativeGeoMapItemBaseCall44>(taken[44]);
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
      CuteQDeclarativeGeoMapItemBaseCall45 call = reinterpret_cast<CuteQDeclarativeGeoMapItemBaseCall45>(taken[45]);
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
      CuteQDeclarativeGeoMapItemBaseCall46 call = reinterpret_cast<CuteQDeclarativeGeoMapItemBaseCall46>(taken[46]);
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
      CuteQDeclarativeGeoMapItemBaseCall47 call = reinterpret_cast<CuteQDeclarativeGeoMapItemBaseCall47>(taken[47]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QDeclarativeGeoMapItemBase::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK26QDeclarativeGeoMapItemBase10metaObjectEv(
    const QDeclarativeGeoMapItemBase *self) {
  return self->metaObject();
}

//  void *QDeclarativeGeoMapItemBase::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN26QDeclarativeGeoMapItemBase11qt_metacastEPKc(
    QDeclarativeGeoMapItemBase *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QDeclarativeGeoMapItemBase::qt_metacall(QMetaObject::Call a0, int a1,
//      void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN26QDeclarativeGeoMapItemBase11qt_metacallEN11QMetaObject4CallEiPPv(
    QDeclarativeGeoMapItemBase *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QDeclarativeGeoMapItemBase::tr(const char *s, const char *c, int
//      n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN26QDeclarativeGeoMapItemBase2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QDeclarativeGeoMapItemBase::tr(s, c, n));
}

//  void QDeclarativeGeoMapItemBase::qt_qmlMarker_uncreatable()
extern "C" Q_DECL_EXPORT
void ritual_ZN26QDeclarativeGeoMapItemBase24qt_qmlMarker_uncreatableEv(
    QDeclarativeGeoMapItemBase *self) {
  self->qt_qmlMarker_uncreatable();
}

//  QDeclarativeGeoMapItemBase::QDeclarativeGeoMapItemBase(QQuickItem
//      *parent)
extern "C" Q_DECL_EXPORT
QDeclarativeGeoMapItemBase *ritual_ZN26QDeclarativeGeoMapItemBaseC1EP10QQuickItem(
    QQuickItem *parent) {
  return new CuteQDeclarativeGeoMapItemBase(parent);
}

//  QDeclarativeGeoMapItemBase::~QDeclarativeGeoMapItemBase()
extern "C" Q_DECL_EXPORT
void ritual_ZN26QDeclarativeGeoMapItemBaseD1Ev(
    QDeclarativeGeoMapItemBase *self) {
  delete self;
}

//  void QDeclarativeGeoMapItemBase::setMap(QDeclarativeGeoMap *quickMap,
//      QGeoMap *map)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QDeclarativeGeoMapItemBase6setMapEP18QDeclarativeGeoMapP7QGeoMap(
    QDeclarativeGeoMapItemBase *self,
    QDeclarativeGeoMap *quickMap,
    QGeoMap *map) {
  self->setMap(quickMap, map);
}

//  void QDeclarativeGeoMapItemBase::setPositionOnMap(const QGeoCoordinate
//      &coordinate, const QPointF &offset)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QDeclarativeGeoMapItemBase16setPositionOnMapERK14QGeoCoordinateRK7QPointF(
    QDeclarativeGeoMapItemBase *self,
    const QGeoCoordinate *coordinate,
    const QPointF *offset) {
  self->setPositionOnMap(*coordinate, *offset);
}

//  QDeclarativeGeoMap *QDeclarativeGeoMapItemBase::quickMap() const
extern "C" Q_DECL_EXPORT
QDeclarativeGeoMap *ritual_ZNK26QDeclarativeGeoMapItemBase8quickMapEv(
    const QDeclarativeGeoMapItemBase *self) {
  return self->quickMap();
}

//  QGeoMap *QDeclarativeGeoMapItemBase::map() const
extern "C" Q_DECL_EXPORT
QGeoMap *ritual_ZNK26QDeclarativeGeoMapItemBase3mapEv(
    const QDeclarativeGeoMapItemBase *self) {
  return self->map();
}

//  const QGeoShape &QDeclarativeGeoMapItemBase::geoShape() const
extern "C" Q_DECL_EXPORT
QGeoShape *ritual_ZNK26QDeclarativeGeoMapItemBase8geoShapeEv(
    const QDeclarativeGeoMapItemBase *self) {
  return new QGeoShape(self->geoShape());
}

//  void QDeclarativeGeoMapItemBase::setGeoShape(const QGeoShape &shape)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QDeclarativeGeoMapItemBase11setGeoShapeERK9QGeoShape(
    QDeclarativeGeoMapItemBase *self,
    const QGeoShape *shape) {
  self->setGeoShape(*shape);
}

//  bool QDeclarativeGeoMapItemBase::autoFadeIn() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK26QDeclarativeGeoMapItemBase10autoFadeInEv(
    const QDeclarativeGeoMapItemBase *self) {
  return self->autoFadeIn();
}

//  void QDeclarativeGeoMapItemBase::setAutoFadeIn(bool fadeIn)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QDeclarativeGeoMapItemBase13setAutoFadeInEb(
    QDeclarativeGeoMapItemBase *self,
    bool fadeIn) {
  self->setAutoFadeIn(fadeIn);
}

//  QLocation::ReferenceSurface
//      QDeclarativeGeoMapItemBase::referenceSurface() const
extern "C" Q_DECL_EXPORT
QLocation::ReferenceSurface ritual_ZNK26QDeclarativeGeoMapItemBase16referenceSurfaceEv(
    const QDeclarativeGeoMapItemBase *self) {
  return self->referenceSurface();
}

//  void QDeclarativeGeoMapItemBase::setReferenceSurface(QLocation::Reference
//      Surface referenceSurface)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QDeclarativeGeoMapItemBase19setReferenceSurfaceEN9QLocation16ReferenceSurfaceE(
    QDeclarativeGeoMapItemBase *self,
    QLocation::ReferenceSurface referenceSurface) {
  self->setReferenceSurface(referenceSurface);
}

//  int QDeclarativeGeoMapItemBase::lodThreshold() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK26QDeclarativeGeoMapItemBase12lodThresholdEv(
    const QDeclarativeGeoMapItemBase *self) {
  return self->lodThreshold();
}

//  void QDeclarativeGeoMapItemBase::setLodThreshold(int lt)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QDeclarativeGeoMapItemBase15setLodThresholdEi(
    QDeclarativeGeoMapItemBase *self,
    int lt) {
  self->setLodThreshold(lt);
}

//  unsigned int QDeclarativeGeoMapItemBase::zoomForLOD(int zoom) const
extern "C" Q_DECL_EXPORT
unsigned int ritual_ZNK26QDeclarativeGeoMapItemBase10zoomForLODEi(
    const QDeclarativeGeoMapItemBase *self,
    int zoom) {
  return self->zoomForLOD(zoom);
}

//  QSGNode *QDeclarativeGeoMapItemBase::updatePaintNode(QSGNode *a0,
//      UpdatePaintNodeData *a1)
extern "C" Q_DECL_EXPORT
QSGNode *ritual_ZN26QDeclarativeGeoMapItemBase15updatePaintNodeEP7QSGNodePN10QQuickItem19UpdatePaintNodeDataE(
    QDeclarativeGeoMapItemBase *self,
    QSGNode *a0,
    QQuickItem::UpdatePaintNodeData *a1) {
  return self->updatePaintNode(a0, a1);
}

//  QSGNode *QDeclarativeGeoMapItemBase::updateMapItemPaintNode(QSGNode *a0,
//      UpdatePaintNodeData *a1)
extern "C" Q_DECL_EXPORT
QSGNode *ritual_ZN26QDeclarativeGeoMapItemBase22updateMapItemPaintNodeEP7QSGNodePN10QQuickItem19UpdatePaintNodeDataE(
    QDeclarativeGeoMapItemBase *self,
    QSGNode *a0,
    QQuickItem::UpdatePaintNodeData *a1) {
  return self->updateMapItemPaintNode(a0, a1);
}

//  QGeoMap::ItemType QDeclarativeGeoMapItemBase::itemType() const
extern "C" Q_DECL_EXPORT
QGeoMap::ItemType ritual_ZNK26QDeclarativeGeoMapItemBase8itemTypeEv(
    const QDeclarativeGeoMapItemBase *self) {
  return self->itemType();
}

//  qreal QDeclarativeGeoMapItemBase::mapItemOpacity() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK26QDeclarativeGeoMapItemBase14mapItemOpacityEv(
    const QDeclarativeGeoMapItemBase *self) {
  return self->mapItemOpacity();
}

//  void
//      QDeclarativeGeoMapItemBase::setParentGroup(QDeclarativeGeoMapItemGrou
//      p &parentGroup)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QDeclarativeGeoMapItemBase14setParentGroupER27QDeclarativeGeoMapItemGroup(
    QDeclarativeGeoMapItemBase *self,
    QDeclarativeGeoMapItemGroup *parentGroup) {
  self->setParentGroup(*parentGroup);
}

//  void QDeclarativeGeoMapItemBase::setShapeTriangulationScale(QQuickShape
//      *shape, qreal maxCoord) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK26QDeclarativeGeoMapItemBase26setShapeTriangulationScaleEP11QQuickShaped(
    const QDeclarativeGeoMapItemBase *self,
    QQuickShape *shape,
    qreal maxCoord) {
  self->setShapeTriangulationScale(shape, maxCoord);
}

//  void QDeclarativeGeoMapItemBase::mapItemOpacityChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN26QDeclarativeGeoMapItemBase21mapItemOpacityChangedEv(
    QDeclarativeGeoMapItemBase *self) {
  self->mapItemOpacityChanged();
}

//  void QDeclarativeGeoMapItemBase::addTransitionFinished()
extern "C" Q_DECL_EXPORT
void ritual_ZN26QDeclarativeGeoMapItemBase21addTransitionFinishedEv(
    QDeclarativeGeoMapItemBase *self) {
  self->addTransitionFinished();
}

//  void QDeclarativeGeoMapItemBase::removeTransitionFinished()
extern "C" Q_DECL_EXPORT
void ritual_ZN26QDeclarativeGeoMapItemBase24removeTransitionFinishedEv(
    QDeclarativeGeoMapItemBase *self) {
  self->removeTransitionFinished();
}

//  void QDeclarativeGeoMapItemBase::referenceSurfaceChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN26QDeclarativeGeoMapItemBase23referenceSurfaceChangedEv(
    QDeclarativeGeoMapItemBase *self) {
  self->referenceSurfaceChanged();
}

//  void QDeclarativeGeoMapItemBase::lodThresholdChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN26QDeclarativeGeoMapItemBase19lodThresholdChangedEv(
    QDeclarativeGeoMapItemBase *self) {
  self->lodThresholdChanged();
}

//  void QDeclarativeGeoMapItemBase::afterChildrenChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN26QDeclarativeGeoMapItemBase20afterChildrenChangedEv(
    QDeclarativeGeoMapItemBase *self) {
  self->afterChildrenChanged();
}

//  void QDeclarativeGeoMapItemBase::afterViewportChanged(const
//      QGeoMapViewportChangeEvent &event)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QDeclarativeGeoMapItemBase20afterViewportChangedERK26QGeoMapViewportChangeEvent(
    QDeclarativeGeoMapItemBase *self,
    const QGeoMapViewportChangeEvent *event) {
  self->afterViewportChanged(*event);
}

//  void QDeclarativeGeoMapItemBase::polishAndUpdate()
extern "C" Q_DECL_EXPORT
void ritual_ZN26QDeclarativeGeoMapItemBase15polishAndUpdateEv(
    QDeclarativeGeoMapItemBase *self) {
  self->polishAndUpdate();
}

//  float QDeclarativeGeoMapItemBase::zoomLevelOpacity() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK26QDeclarativeGeoMapItemBase16zoomLevelOpacityEv(
    const QDeclarativeGeoMapItemBase *self) {
  return self->zoomLevelOpacity();
}

//  bool QDeclarativeGeoMapItemBase::isPolishScheduled() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK26QDeclarativeGeoMapItemBase17isPolishScheduledEv(
    const QDeclarativeGeoMapItemBase *self) {
  return self->isPolishScheduled();
}

//  void QDeclarativeGeoMapItemBase::baseCameraDataChanged(const
//      QGeoCameraData &camera)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QDeclarativeGeoMapItemBase21baseCameraDataChangedERK14QGeoCameraData(
    QDeclarativeGeoMapItemBase *self,
    const QGeoCameraData *camera) {
  self->baseCameraDataChanged(*camera);
}

//  void QDeclarativeGeoMapItemBase::visibleAreaChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN26QDeclarativeGeoMapItemBase18visibleAreaChangedEv(
    QDeclarativeGeoMapItemBase *self) {
  self->visibleAreaChanged();
}

//  a Python function taken by a CuteQDeclarativeGeoMapItemBase, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QDeclarativeGeoMapItemBase(
    QDeclarativeGeoMapItemBase *self,
    const char *key,
    void *call) {
  return static_cast<CuteQDeclarativeGeoMapItemBase *>(self)->take(key, call);
}

//  void QDeclarativeGeoMapItemBase::setMap(QDeclarativeGeoMap *quickMap,
//      QGeoMap *map)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN26QDeclarativeGeoMapItemBase6setMapEP18QDeclarativeGeoMapP7QGeoMap(
    QDeclarativeGeoMapItemBase *self,
    QDeclarativeGeoMap *quickMap,
    QGeoMap *map) {
  self->QDeclarativeGeoMapItemBase::setMap(quickMap, map);
}

//  void QDeclarativeGeoMapItemBase::setPositionOnMap(const QGeoCoordinate
//      &coordinate, const QPointF &offset)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN26QDeclarativeGeoMapItemBase16setPositionOnMapERK14QGeoCoordinateRK7QPointF(
    QDeclarativeGeoMapItemBase *self,
    const QGeoCoordinate *coordinate,
    const QPointF *offset) {
  self->QDeclarativeGeoMapItemBase::setPositionOnMap(*coordinate, *offset);
}

//  QSGNode *QDeclarativeGeoMapItemBase::updatePaintNode(QSGNode *a0,
//      UpdatePaintNodeData *a1)
extern "C" Q_DECL_EXPORT
QSGNode *ritual_own_ZN26QDeclarativeGeoMapItemBase15updatePaintNodeEP7QSGNodePN10QQuickItem19UpdatePaintNodeDataE(
    QDeclarativeGeoMapItemBase *self,
    QSGNode *a0,
    QQuickItem::UpdatePaintNodeData *a1) {
  return self->QDeclarativeGeoMapItemBase::updatePaintNode(a0, a1);
}

//  QSGNode *QDeclarativeGeoMapItemBase::updateMapItemPaintNode(QSGNode *a0,
//      UpdatePaintNodeData *a1)
extern "C" Q_DECL_EXPORT
QSGNode *ritual_own_ZN26QDeclarativeGeoMapItemBase22updateMapItemPaintNodeEP7QSGNodePN10QQuickItem19UpdatePaintNodeDataE(
    QDeclarativeGeoMapItemBase *self,
    QSGNode *a0,
    QQuickItem::UpdatePaintNodeData *a1) {
  return self->QDeclarativeGeoMapItemBase::updateMapItemPaintNode(a0, a1);
}

//  void QDeclarativeGeoMapItemBase::afterChildrenChanged()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN26QDeclarativeGeoMapItemBase20afterChildrenChangedEv(
    QDeclarativeGeoMapItemBase *self) {
  static_cast<OwnQDeclarativeGeoMapItemBase *>(self)->OwnQDeclarativeGeoMapItemBase::afterChildrenChanged();
}
