//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick3D/6.12.0/QtQuick3D/private/qquick3dtexture_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtQuick3D/6.12.0/QtQuick3D/private/qtquick3dglobal_p.h>
#include <QtQuick3D/QtQuick3D>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick3D/6.12.0/QtQuick3D/private/qquick3dtexture_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qurl.h>
#include <QtQuick3D/qquick3dobject.h>
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qquickitemchangelistener_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qrect.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  Only a class built on QQuick3DTexture may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQQuick3DTexture : QQuick3DTexture {
  using QQuick3DTexture::updateSpatialNode;
  using QQuick3DTexture::markAllDirty;
  using QQuick3DTexture::itemChange;
  using QQuick3DTexture::itemGeometryChanged;
};

//  A QQuick3DTexture that Python can take functions over in. Every QQuick3DTexture
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void * (*CuteQQuick3DTextureCall0)(const void *, QSSGRenderGraphObject *, int *);
typedef void (*CuteQQuick3DTextureCall1)(const void *, int *);
typedef void (*CuteQQuick3DTextureCall2)(const void *, int, const QQuick3DObject::ItemChangeData *, int *);
typedef void (*CuteQQuick3DTextureCall3)(const void *, QQuickItem *, const QQuickGeometryChange *, const QRectF *, int *);
typedef void (*CuteQQuick3DTextureCall4)(const void *, int *);
typedef void (*CuteQQuick3DTextureCall5)(const void *, int *);
typedef void (*CuteQQuick3DTextureCall6)(const void *, int *);
typedef void (*CuteQQuick3DTextureCall7)(const void *, QQuickItem *, int *);
typedef void (*CuteQQuick3DTextureCall8)(const void *, QQuickItem *, int *);
typedef void (*CuteQQuick3DTextureCall9)(const void *, QQuickItem *, int *);
typedef void (*CuteQQuick3DTextureCall10)(const void *, QQuickItem *, int *);
typedef void (*CuteQQuick3DTextureCall11)(const void *, QQuickItem *, int *);
typedef void (*CuteQQuick3DTextureCall12)(const void *, QQuickItem *, QQuickItem *, int *);
typedef void (*CuteQQuick3DTextureCall13)(const void *, QQuickItem *, QQuickItem *, int *);
typedef void (*CuteQQuick3DTextureCall14)(const void *, QQuickItem *, QQuickItem *, int *);
typedef void (*CuteQQuick3DTextureCall15)(const void *, QQuickItem *, int *);
typedef void (*CuteQQuick3DTextureCall16)(const void *, QQuickItem *, int *);
typedef void (*CuteQQuick3DTextureCall17)(const void *, QQuickItem *, int *);
typedef void (*CuteQQuick3DTextureCall18)(const void *, QQuickItem *, int, int *);
typedef void (*CuteQQuick3DTextureCall19)(const void *, QQuickItem *, int *);
typedef void (*CuteQQuick3DTextureCall20)(const void *, QQuickItem *, QQuickItem *, int *);
typedef void * (*CuteQQuick3DTextureCall21)(const void *, int *);
typedef bool (*CuteQQuick3DTextureCall22)(const void *, const QObject *, int *);
typedef QString * (*CuteQQuick3DTextureCall23)(const void *, int *);
typedef void (*CuteQQuick3DTextureCall24)(const void *, QQuickItem *, int *);
typedef void (*CuteQQuick3DTextureCall25)(const void *, QQuickItem *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuick3DTextureCall26)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuick3DTextureCall27)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuick3DTextureCall28)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuick3DTextureCall29)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuick3DTextureCall30)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuick3DTextureCall31)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuick3DTextureCall32)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQQuick3DTexture : public QQuick3DTexture {
public:
  using QQuick3DTexture::QQuick3DTexture;
  void *taken[33] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN14QQuick3DObject17updateSpatialNodeEP21QSSGRenderGraphObject")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QQuick3DObject12markAllDirtyEv")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QQuick3DObject10itemChangeENS_10ItemChangeERKNS_14ItemChangeDataE")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN24QQuickItemChangeListener19itemGeometryChangedEP10QQuickItem20QQuickGeometryChangeRK6QRectF")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQmlParserStatus10classBeginEv")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQmlParserStatus17componentCompleteEv")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QQuick3DObject7preSyncEv")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN24QQuickItemChangeListener23itemSiblingOrderChangedEP10QQuickItem")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN24QQuickItemChangeListener21itemVisibilityChangedEP10QQuickItem")) {
      taken[8] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN24QQuickItemChangeListener18itemEnabledChangedEP10QQuickItem")) {
      taken[9] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN24QQuickItemChangeListener18itemOpacityChangedEP10QQuickItem")) {
      taken[10] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN24QQuickItemChangeListener13itemDestroyedEP10QQuickItem")) {
      taken[11] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN24QQuickItemChangeListener14itemChildAddedEP10QQuickItemS1_")) {
      taken[12] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN24QQuickItemChangeListener16itemChildRemovedEP10QQuickItemS1_")) {
      taken[13] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN24QQuickItemChangeListener17itemParentChangedEP10QQuickItemS1_")) {
      taken[14] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN24QQuickItemChangeListener19itemRotationChangedEP10QQuickItem")) {
      taken[15] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN24QQuickItemChangeListener24itemImplicitWidthChangedEP10QQuickItem")) {
      taken[16] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN24QQuickItemChangeListener25itemImplicitHeightChangedEP10QQuickItem")) {
      taken[17] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN24QQuickItemChangeListener16itemFocusChangedEP10QQuickItemN2Qt11FocusReasonE")) {
      taken[18] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN24QQuickItemChangeListener16itemScaleChangedEP10QQuickItem")) {
      taken[19] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN24QQuickItemChangeListener20itemTransformChangedEP10QQuickItemS1_")) {
      taken[20] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN24QQuickItemChangeListener13anchorPrivateEv")) {
      taken[21] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK24QQuickItemChangeListener11baseDeletedEPK7QObject")) {
      taken[22] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK24QQuickItemChangeListener9debugNameEv")) {
      taken[23] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN24QQuickItemChangeListener13addSourceItemEP10QQuickItem")) {
      taken[24] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN24QQuickItemChangeListener16removeSourceItemEP10QQuickItem")) {
      taken[25] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[26] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[27] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[28] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[29] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[30] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[31] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[32] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

  //  QSSGRenderGraphObject
  //      *QQuick3DTexture::updateSpatialNode(QSSGRenderGraphObject *node)
  QSSGRenderGraphObject *updateSpatialNode(
      QSSGRenderGraphObject *node) override {
    if (taken[0]) {
      int handled = 0;
      CuteQQuick3DTextureCall0 call = reinterpret_cast<CuteQQuick3DTextureCall0>(taken[0]);
      void * given = call(this, node, &handled);
      if (handled) return static_cast<QSSGRenderGraphObject *>(given);
    }
    return QQuick3DTexture::updateSpatialNode(node);
  }

  //  void QQuick3DTexture::markAllDirty()
  void markAllDirty() override {
    if (taken[1]) {
      int handled = 0;
      CuteQQuick3DTextureCall1 call = reinterpret_cast<CuteQQuick3DTextureCall1>(taken[1]);
      call(this, &handled);
      if (handled) return;
    }
    QQuick3DTexture::markAllDirty();
  }

  //  void QQuick3DTexture::itemChange(ItemChange change, const
  //      ItemChangeData &value)
  void itemChange(
      QQuick3DObject::ItemChange change,
      const QQuick3DObject::ItemChangeData &value) override {
    if (taken[2]) {
      int handled = 0;
      CuteQQuick3DTextureCall2 call = reinterpret_cast<CuteQQuick3DTextureCall2>(taken[2]);
      call(this, static_cast<int>(change), &value, &handled);
      if (handled) return;
    }
    QQuick3DTexture::itemChange(change, value);
  }

  //  void QQuick3DTexture::itemGeometryChanged(QQuickItem *item,
  //      QQuickGeometryChange change, const QRectF &geometry)
  void itemGeometryChanged(
      QQuickItem *item,
      QQuickGeometryChange change,
      const QRectF &geometry) override {
    if (taken[3]) {
      int handled = 0;
      CuteQQuick3DTextureCall3 call = reinterpret_cast<CuteQQuick3DTextureCall3>(taken[3]);
      call(this, item, &change, &geometry, &handled);
      if (handled) return;
    }
    QQuick3DTexture::itemGeometryChanged(item, change, geometry);
  }

  //  void QQuick3DObject::classBegin()
  void classBegin() override {
    if (taken[4]) {
      int handled = 0;
      CuteQQuick3DTextureCall4 call = reinterpret_cast<CuteQQuick3DTextureCall4>(taken[4]);
      call(this, &handled);
      if (handled) return;
    }
    QQuick3DObject::classBegin();
  }

  //  void QQuick3DObject::componentComplete()
  void componentComplete() override {
    if (taken[5]) {
      int handled = 0;
      CuteQQuick3DTextureCall5 call = reinterpret_cast<CuteQQuick3DTextureCall5>(taken[5]);
      call(this, &handled);
      if (handled) return;
    }
    QQuick3DObject::componentComplete();
  }

  //  void QQuick3DObject::preSync()
  void preSync() override {
    if (taken[6]) {
      int handled = 0;
      CuteQQuick3DTextureCall6 call = reinterpret_cast<CuteQQuick3DTextureCall6>(taken[6]);
      call(this, &handled);
      if (handled) return;
    }
    QQuick3DObject::preSync();
  }

  //  void QQuickItemChangeListener::itemSiblingOrderChanged(QQuickItem
  //      *a0)
  void itemSiblingOrderChanged(QQuickItem *a0) override {
    if (taken[7]) {
      int handled = 0;
      CuteQQuick3DTextureCall7 call = reinterpret_cast<CuteQQuick3DTextureCall7>(taken[7]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItemChangeListener::itemSiblingOrderChanged(a0);
  }

  //  void QQuickItemChangeListener::itemVisibilityChanged(QQuickItem *a0)
  void itemVisibilityChanged(QQuickItem *a0) override {
    if (taken[8]) {
      int handled = 0;
      CuteQQuick3DTextureCall8 call = reinterpret_cast<CuteQQuick3DTextureCall8>(taken[8]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItemChangeListener::itemVisibilityChanged(a0);
  }

  //  void QQuickItemChangeListener::itemEnabledChanged(QQuickItem *a0)
  void itemEnabledChanged(QQuickItem *a0) override {
    if (taken[9]) {
      int handled = 0;
      CuteQQuick3DTextureCall9 call = reinterpret_cast<CuteQQuick3DTextureCall9>(taken[9]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItemChangeListener::itemEnabledChanged(a0);
  }

  //  void QQuickItemChangeListener::itemOpacityChanged(QQuickItem *a0)
  void itemOpacityChanged(QQuickItem *a0) override {
    if (taken[10]) {
      int handled = 0;
      CuteQQuick3DTextureCall10 call = reinterpret_cast<CuteQQuick3DTextureCall10>(taken[10]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItemChangeListener::itemOpacityChanged(a0);
  }

  //  void QQuickItemChangeListener::itemDestroyed(QQuickItem *a0)
  void itemDestroyed(QQuickItem *a0) override {
    if (taken[11]) {
      int handled = 0;
      CuteQQuick3DTextureCall11 call = reinterpret_cast<CuteQQuick3DTextureCall11>(taken[11]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItemChangeListener::itemDestroyed(a0);
  }

  //  void QQuickItemChangeListener::itemChildAdded(QQuickItem *a0,
  //      QQuickItem *a1)
  void itemChildAdded(QQuickItem *a0, QQuickItem *a1) override {
    if (taken[12]) {
      int handled = 0;
      CuteQQuick3DTextureCall12 call = reinterpret_cast<CuteQQuick3DTextureCall12>(taken[12]);
      call(this, a0, a1, &handled);
      if (handled) return;
    }
    QQuickItemChangeListener::itemChildAdded(a0, a1);
  }

  //  void QQuickItemChangeListener::itemChildRemoved(QQuickItem *a0,
  //      QQuickItem *a1)
  void itemChildRemoved(QQuickItem *a0, QQuickItem *a1) override {
    if (taken[13]) {
      int handled = 0;
      CuteQQuick3DTextureCall13 call = reinterpret_cast<CuteQQuick3DTextureCall13>(taken[13]);
      call(this, a0, a1, &handled);
      if (handled) return;
    }
    QQuickItemChangeListener::itemChildRemoved(a0, a1);
  }

  //  void QQuickItemChangeListener::itemParentChanged(QQuickItem *a0,
  //      QQuickItem *a1)
  void itemParentChanged(QQuickItem *a0, QQuickItem *a1) override {
    if (taken[14]) {
      int handled = 0;
      CuteQQuick3DTextureCall14 call = reinterpret_cast<CuteQQuick3DTextureCall14>(taken[14]);
      call(this, a0, a1, &handled);
      if (handled) return;
    }
    QQuickItemChangeListener::itemParentChanged(a0, a1);
  }

  //  void QQuickItemChangeListener::itemRotationChanged(QQuickItem *a0)
  void itemRotationChanged(QQuickItem *a0) override {
    if (taken[15]) {
      int handled = 0;
      CuteQQuick3DTextureCall15 call = reinterpret_cast<CuteQQuick3DTextureCall15>(taken[15]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItemChangeListener::itemRotationChanged(a0);
  }

  //  void QQuickItemChangeListener::itemImplicitWidthChanged(QQuickItem
  //      *a0)
  void itemImplicitWidthChanged(QQuickItem *a0) override {
    if (taken[16]) {
      int handled = 0;
      CuteQQuick3DTextureCall16 call = reinterpret_cast<CuteQQuick3DTextureCall16>(taken[16]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItemChangeListener::itemImplicitWidthChanged(a0);
  }

  //  void QQuickItemChangeListener::itemImplicitHeightChanged(QQuickItem
  //      *a0)
  void itemImplicitHeightChanged(QQuickItem *a0) override {
    if (taken[17]) {
      int handled = 0;
      CuteQQuick3DTextureCall17 call = reinterpret_cast<CuteQQuick3DTextureCall17>(taken[17]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItemChangeListener::itemImplicitHeightChanged(a0);
  }

  //  void QQuickItemChangeListener::itemFocusChanged(QQuickItem *a0,
  //      Qt::FocusReason a1)
  void itemFocusChanged(QQuickItem *a0, Qt::FocusReason a1) override {
    if (taken[18]) {
      int handled = 0;
      CuteQQuick3DTextureCall18 call = reinterpret_cast<CuteQQuick3DTextureCall18>(taken[18]);
      call(this, a0, static_cast<int>(a1), &handled);
      if (handled) return;
    }
    QQuickItemChangeListener::itemFocusChanged(a0, a1);
  }

  //  void QQuickItemChangeListener::itemScaleChanged(QQuickItem *a0)
  void itemScaleChanged(QQuickItem *a0) override {
    if (taken[19]) {
      int handled = 0;
      CuteQQuick3DTextureCall19 call = reinterpret_cast<CuteQQuick3DTextureCall19>(taken[19]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItemChangeListener::itemScaleChanged(a0);
  }

  //  void QQuickItemChangeListener::itemTransformChanged(QQuickItem *a0,
  //      QQuickItem *a1)
  void itemTransformChanged(QQuickItem *a0, QQuickItem *a1) override {
    if (taken[20]) {
      int handled = 0;
      CuteQQuick3DTextureCall20 call = reinterpret_cast<CuteQQuick3DTextureCall20>(taken[20]);
      call(this, a0, a1, &handled);
      if (handled) return;
    }
    QQuickItemChangeListener::itemTransformChanged(a0, a1);
  }

  //  QQuickAnchorsPrivate *QQuickItemChangeListener::anchorPrivate()
  QQuickAnchorsPrivate *anchorPrivate() override {
    if (taken[21]) {
      int handled = 0;
      CuteQQuick3DTextureCall21 call = reinterpret_cast<CuteQQuick3DTextureCall21>(taken[21]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QQuickAnchorsPrivate *>(given);
    }
    return QQuickItemChangeListener::anchorPrivate();
  }

  //  bool QQuickItemChangeListener::baseDeleted(const QObject *caller)
  //      const
  bool baseDeleted(const QObject *caller) const override {
    if (taken[22]) {
      int handled = 0;
      CuteQQuick3DTextureCall22 call = reinterpret_cast<CuteQQuick3DTextureCall22>(taken[22]);
      bool given = call(this, caller, &handled);
      if (handled) return given;
    }
    return QQuickItemChangeListener::baseDeleted(caller);
  }

  //  QString QQuickItemChangeListener::debugName() const
  QString debugName() const override {
    if (taken[23]) {
      int handled = 0;
      CuteQQuick3DTextureCall23 call = reinterpret_cast<CuteQQuick3DTextureCall23>(taken[23]);
      QString * given = call(this, &handled);
      if (handled && given) {
        QString back(*given);
        delete given;
        return back;
      }
    }
    return QQuickItemChangeListener::debugName();
  }

  //  void QQuickItemChangeListener::addSourceItem(QQuickItem *a0)
  void addSourceItem(QQuickItem *a0) override {
    if (taken[24]) {
      int handled = 0;
      CuteQQuick3DTextureCall24 call = reinterpret_cast<CuteQQuick3DTextureCall24>(taken[24]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItemChangeListener::addSourceItem(a0);
  }

  //  void QQuickItemChangeListener::removeSourceItem(QQuickItem *a0)
  void removeSourceItem(QQuickItem *a0) override {
    if (taken[25]) {
      int handled = 0;
      CuteQQuick3DTextureCall25 call = reinterpret_cast<CuteQQuick3DTextureCall25>(taken[25]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItemChangeListener::removeSourceItem(a0);
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[26]) {
      int handled = 0;
      CuteQQuick3DTextureCall26 call = reinterpret_cast<CuteQQuick3DTextureCall26>(taken[26]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[27]) {
      int handled = 0;
      CuteQQuick3DTextureCall27 call = reinterpret_cast<CuteQQuick3DTextureCall27>(taken[27]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[28]) {
      int handled = 0;
      CuteQQuick3DTextureCall28 call = reinterpret_cast<CuteQQuick3DTextureCall28>(taken[28]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[29]) {
      int handled = 0;
      CuteQQuick3DTextureCall29 call = reinterpret_cast<CuteQQuick3DTextureCall29>(taken[29]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[30]) {
      int handled = 0;
      CuteQQuick3DTextureCall30 call = reinterpret_cast<CuteQQuick3DTextureCall30>(taken[30]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[31]) {
      int handled = 0;
      CuteQQuick3DTextureCall31 call = reinterpret_cast<CuteQQuick3DTextureCall31>(taken[31]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[32]) {
      int handled = 0;
      CuteQQuick3DTextureCall32 call = reinterpret_cast<CuteQQuick3DTextureCall32>(taken[32]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QQuick3DTexture::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK15QQuick3DTexture10metaObjectEv(
    const QQuick3DTexture *self) {
  return self->metaObject();
}

//  void *QQuick3DTexture::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN15QQuick3DTexture11qt_metacastEPKc(
    QQuick3DTexture *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QQuick3DTexture::qt_metacall(QMetaObject::Call a0, int a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN15QQuick3DTexture11qt_metacallEN11QMetaObject4CallEiPPv(
    QQuick3DTexture *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QQuick3DTexture::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN15QQuick3DTexture2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuick3DTexture::tr(s, c, n));
}

//  QQuick3DTexture::QQuick3DTexture(QQuick3DObject *parent)
extern "C" Q_DECL_EXPORT
QQuick3DTexture *ritual_ZN15QQuick3DTextureC1EP14QQuick3DObject(
    QQuick3DObject *parent) {
  return new CuteQQuick3DTexture(parent);
}

//  QQuick3DTexture::~QQuick3DTexture()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuick3DTextureD1Ev(QQuick3DTexture *self) {
  delete self;
}

//  QUrl QQuick3DTexture::source() const
extern "C" Q_DECL_EXPORT
QUrl *ritual_ZNK15QQuick3DTexture6sourceEv(const QQuick3DTexture *self) {
  return new QUrl(self->source());
}

//  QQuickItem *QQuick3DTexture::sourceItem() const
extern "C" Q_DECL_EXPORT
QQuickItem *ritual_ZNK15QQuick3DTexture10sourceItemEv(
    const QQuick3DTexture *self) {
  return self->sourceItem();
}

//  float QQuick3DTexture::scaleU() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK15QQuick3DTexture6scaleUEv(const QQuick3DTexture *self) {
  return self->scaleU();
}

//  float QQuick3DTexture::scaleV() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK15QQuick3DTexture6scaleVEv(const QQuick3DTexture *self) {
  return self->scaleV();
}

//  MappingMode QQuick3DTexture::mappingMode() const
extern "C" Q_DECL_EXPORT
QQuick3DTexture::MappingMode ritual_ZNK15QQuick3DTexture11mappingModeEv(
    const QQuick3DTexture *self) {
  return self->mappingMode();
}

//  TilingMode QQuick3DTexture::horizontalTiling() const
extern "C" Q_DECL_EXPORT
QQuick3DTexture::TilingMode ritual_ZNK15QQuick3DTexture16horizontalTilingEv(
    const QQuick3DTexture *self) {
  return self->horizontalTiling();
}

//  TilingMode QQuick3DTexture::verticalTiling() const
extern "C" Q_DECL_EXPORT
QQuick3DTexture::TilingMode ritual_ZNK15QQuick3DTexture14verticalTilingEv(
    const QQuick3DTexture *self) {
  return self->verticalTiling();
}

//  TilingMode QQuick3DTexture::depthTiling() const
extern "C" Q_DECL_EXPORT
QQuick3DTexture::TilingMode ritual_ZNK15QQuick3DTexture11depthTilingEv(
    const QQuick3DTexture *self) {
  return self->depthTiling();
}

//  float QQuick3DTexture::rotationUV() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK15QQuick3DTexture10rotationUVEv(
    const QQuick3DTexture *self) {
  return self->rotationUV();
}

//  float QQuick3DTexture::positionU() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK15QQuick3DTexture9positionUEv(const QQuick3DTexture *self) {
  return self->positionU();
}

//  float QQuick3DTexture::positionV() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK15QQuick3DTexture9positionVEv(const QQuick3DTexture *self) {
  return self->positionV();
}

//  float QQuick3DTexture::pivotU() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK15QQuick3DTexture6pivotUEv(const QQuick3DTexture *self) {
  return self->pivotU();
}

//  float QQuick3DTexture::pivotV() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK15QQuick3DTexture6pivotVEv(const QQuick3DTexture *self) {
  return self->pivotV();
}

//  bool QQuick3DTexture::flipU() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK15QQuick3DTexture5flipUEv(const QQuick3DTexture *self) {
  return self->flipU();
}

//  bool QQuick3DTexture::flipV() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK15QQuick3DTexture5flipVEv(const QQuick3DTexture *self) {
  return self->flipV();
}

//  int QQuick3DTexture::indexUV() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK15QQuick3DTexture7indexUVEv(const QQuick3DTexture *self) {
  return self->indexUV();
}

//  Filter QQuick3DTexture::magFilter() const
extern "C" Q_DECL_EXPORT
QQuick3DTexture::Filter ritual_ZNK15QQuick3DTexture9magFilterEv(
    const QQuick3DTexture *self) {
  return self->magFilter();
}

//  Filter QQuick3DTexture::minFilter() const
extern "C" Q_DECL_EXPORT
QQuick3DTexture::Filter ritual_ZNK15QQuick3DTexture9minFilterEv(
    const QQuick3DTexture *self) {
  return self->minFilter();
}

//  Filter QQuick3DTexture::mipFilter() const
extern "C" Q_DECL_EXPORT
QQuick3DTexture::Filter ritual_ZNK15QQuick3DTexture9mipFilterEv(
    const QQuick3DTexture *self) {
  return self->mipFilter();
}

//  QQuick3DTextureData *QQuick3DTexture::textureData() const
extern "C" Q_DECL_EXPORT
QQuick3DTextureData *ritual_ZNK15QQuick3DTexture11textureDataEv(
    const QQuick3DTexture *self) {
  return self->textureData();
}

//  bool QQuick3DTexture::generateMipmaps() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK15QQuick3DTexture15generateMipmapsEv(
    const QQuick3DTexture *self) {
  return self->generateMipmaps();
}

//  bool QQuick3DTexture::autoOrientation() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK15QQuick3DTexture15autoOrientationEv(
    const QQuick3DTexture *self) {
  return self->autoOrientation();
}

//  QSSGRenderImage *QQuick3DTexture::getRenderImage()
extern "C" Q_DECL_EXPORT
QSSGRenderImage *ritual_ZN15QQuick3DTexture14getRenderImageEv(
    QQuick3DTexture *self) {
  return self->getRenderImage();
}

//  QQuick3DRenderExtension *QQuick3DTexture::textureProvider() const
extern "C" Q_DECL_EXPORT
QQuick3DRenderExtension *ritual_ZNK15QQuick3DTexture15textureProviderEv(
    const QQuick3DTexture *self) {
  return self->textureProvider();
}

//  void QQuick3DTexture::setTextureProvider(QQuick3DRenderExtension
//      *newRenderTexture)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuick3DTexture18setTextureProviderEP23QQuick3DRenderExtension(
    QQuick3DTexture *self,
    QQuick3DRenderExtension *newRenderTexture) {
  self->setTextureProvider(newRenderTexture);
}

//  bool QQuick3DTexture::hasSourceData() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK15QQuick3DTexture13hasSourceDataEv(
    const QQuick3DTexture *self) {
  return self->hasSourceData();
}

//  void QQuick3DTexture::setSource(const QUrl &source)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuick3DTexture9setSourceERK4QUrl(
    QQuick3DTexture *self,
    const QUrl *source) {
  self->setSource(*source);
}

//  void QQuick3DTexture::setSourceItem(QQuickItem *sourceItem)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuick3DTexture13setSourceItemEP10QQuickItem(
    QQuick3DTexture *self,
    QQuickItem *sourceItem) {
  self->setSourceItem(sourceItem);
}

//  void QQuick3DTexture::setScaleU(float scaleU)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuick3DTexture9setScaleUEf(
    QQuick3DTexture *self,
    float scaleU) {
  self->setScaleU(scaleU);
}

//  void QQuick3DTexture::setScaleV(float scaleV)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuick3DTexture9setScaleVEf(
    QQuick3DTexture *self,
    float scaleV) {
  self->setScaleV(scaleV);
}

//  void QQuick3DTexture::setMappingMode(QQuick3DTexture::MappingMode
//      mappingMode)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuick3DTexture14setMappingModeENS_11MappingModeE(
    QQuick3DTexture *self,
    QQuick3DTexture::MappingMode mappingMode) {
  self->setMappingMode(mappingMode);
}

//  void QQuick3DTexture::setHorizontalTiling(QQuick3DTexture::TilingMode
//      tilingModeHorizontal)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuick3DTexture19setHorizontalTilingENS_10TilingModeE(
    QQuick3DTexture *self,
    QQuick3DTexture::TilingMode tilingModeHorizontal) {
  self->setHorizontalTiling(tilingModeHorizontal);
}

//  void QQuick3DTexture::setVerticalTiling(QQuick3DTexture::TilingMode
//      tilingModeVertical)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuick3DTexture17setVerticalTilingENS_10TilingModeE(
    QQuick3DTexture *self,
    QQuick3DTexture::TilingMode tilingModeVertical) {
  self->setVerticalTiling(tilingModeVertical);
}

//  void QQuick3DTexture::setDepthTiling(QQuick3DTexture::TilingMode
//      tilingModeDepth)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuick3DTexture14setDepthTilingENS_10TilingModeE(
    QQuick3DTexture *self,
    QQuick3DTexture::TilingMode tilingModeDepth) {
  self->setDepthTiling(tilingModeDepth);
}

//  void QQuick3DTexture::setRotationUV(float rotationUV)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuick3DTexture13setRotationUVEf(
    QQuick3DTexture *self,
    float rotationUV) {
  self->setRotationUV(rotationUV);
}

//  void QQuick3DTexture::setPositionU(float positionU)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuick3DTexture12setPositionUEf(
    QQuick3DTexture *self,
    float positionU) {
  self->setPositionU(positionU);
}

//  void QQuick3DTexture::setPositionV(float positionV)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuick3DTexture12setPositionVEf(
    QQuick3DTexture *self,
    float positionV) {
  self->setPositionV(positionV);
}

//  void QQuick3DTexture::setPivotU(float pivotU)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuick3DTexture9setPivotUEf(
    QQuick3DTexture *self,
    float pivotU) {
  self->setPivotU(pivotU);
}

//  void QQuick3DTexture::setPivotV(float pivotV)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuick3DTexture9setPivotVEf(
    QQuick3DTexture *self,
    float pivotV) {
  self->setPivotV(pivotV);
}

//  void QQuick3DTexture::setFlipU(bool flipU)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuick3DTexture8setFlipUEb(
    QQuick3DTexture *self,
    bool flipU) {
  self->setFlipU(flipU);
}

//  void QQuick3DTexture::setFlipV(bool flipV)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuick3DTexture8setFlipVEb(
    QQuick3DTexture *self,
    bool flipV) {
  self->setFlipV(flipV);
}

//  void QQuick3DTexture::setIndexUV(int indexUV)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuick3DTexture10setIndexUVEi(
    QQuick3DTexture *self,
    int indexUV) {
  self->setIndexUV(indexUV);
}

//  void QQuick3DTexture::setMagFilter(QQuick3DTexture::Filter magFilter)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuick3DTexture12setMagFilterENS_6FilterE(
    QQuick3DTexture *self,
    QQuick3DTexture::Filter magFilter) {
  self->setMagFilter(magFilter);
}

//  void QQuick3DTexture::setMinFilter(QQuick3DTexture::Filter minFilter)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuick3DTexture12setMinFilterENS_6FilterE(
    QQuick3DTexture *self,
    QQuick3DTexture::Filter minFilter) {
  self->setMinFilter(minFilter);
}

//  void QQuick3DTexture::setMipFilter(QQuick3DTexture::Filter mipFilter)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuick3DTexture12setMipFilterENS_6FilterE(
    QQuick3DTexture *self,
    QQuick3DTexture::Filter mipFilter) {
  self->setMipFilter(mipFilter);
}

//  void QQuick3DTexture::setTextureData(QQuick3DTextureData *textureData)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuick3DTexture14setTextureDataEP19QQuick3DTextureData(
    QQuick3DTexture *self,
    QQuick3DTextureData *textureData) {
  self->setTextureData(textureData);
}

//  void QQuick3DTexture::setGenerateMipmaps(bool generateMipmaps)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuick3DTexture18setGenerateMipmapsEb(
    QQuick3DTexture *self,
    bool generateMipmaps) {
  self->setGenerateMipmaps(generateMipmaps);
}

//  void QQuick3DTexture::setAutoOrientation(bool autoOrientation)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuick3DTexture18setAutoOrientationEb(
    QQuick3DTexture *self,
    bool autoOrientation) {
  self->setAutoOrientation(autoOrientation);
}

//  void QQuick3DTexture::sourceChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuick3DTexture13sourceChangedEv(QQuick3DTexture *self) {
  self->sourceChanged();
}

//  void QQuick3DTexture::sourceItemChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuick3DTexture17sourceItemChangedEv(QQuick3DTexture *self) {
  self->sourceItemChanged();
}

//  void QQuick3DTexture::scaleUChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuick3DTexture13scaleUChangedEv(QQuick3DTexture *self) {
  self->scaleUChanged();
}

//  void QQuick3DTexture::scaleVChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuick3DTexture13scaleVChangedEv(QQuick3DTexture *self) {
  self->scaleVChanged();
}

//  void QQuick3DTexture::mappingModeChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuick3DTexture18mappingModeChangedEv(
    QQuick3DTexture *self) {
  self->mappingModeChanged();
}

//  void QQuick3DTexture::horizontalTilingChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuick3DTexture23horizontalTilingChangedEv(
    QQuick3DTexture *self) {
  self->horizontalTilingChanged();
}

//  void QQuick3DTexture::verticalTilingChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuick3DTexture21verticalTilingChangedEv(
    QQuick3DTexture *self) {
  self->verticalTilingChanged();
}

//  void QQuick3DTexture::depthTilingChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuick3DTexture18depthTilingChangedEv(
    QQuick3DTexture *self) {
  self->depthTilingChanged();
}

//  void QQuick3DTexture::rotationUVChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuick3DTexture17rotationUVChangedEv(QQuick3DTexture *self) {
  self->rotationUVChanged();
}

//  void QQuick3DTexture::positionUChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuick3DTexture16positionUChangedEv(QQuick3DTexture *self) {
  self->positionUChanged();
}

//  void QQuick3DTexture::positionVChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuick3DTexture16positionVChangedEv(QQuick3DTexture *self) {
  self->positionVChanged();
}

//  void QQuick3DTexture::pivotUChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuick3DTexture13pivotUChangedEv(QQuick3DTexture *self) {
  self->pivotUChanged();
}

//  void QQuick3DTexture::pivotVChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuick3DTexture13pivotVChangedEv(QQuick3DTexture *self) {
  self->pivotVChanged();
}

//  void QQuick3DTexture::flipUChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuick3DTexture12flipUChangedEv(QQuick3DTexture *self) {
  self->flipUChanged();
}

//  void QQuick3DTexture::flipVChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuick3DTexture12flipVChangedEv(QQuick3DTexture *self) {
  self->flipVChanged();
}

//  void QQuick3DTexture::indexUVChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuick3DTexture14indexUVChangedEv(QQuick3DTexture *self) {
  self->indexUVChanged();
}

//  void QQuick3DTexture::magFilterChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuick3DTexture16magFilterChangedEv(QQuick3DTexture *self) {
  self->magFilterChanged();
}

//  void QQuick3DTexture::minFilterChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuick3DTexture16minFilterChangedEv(QQuick3DTexture *self) {
  self->minFilterChanged();
}

//  void QQuick3DTexture::mipFilterChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuick3DTexture16mipFilterChangedEv(QQuick3DTexture *self) {
  self->mipFilterChanged();
}

//  void QQuick3DTexture::textureDataChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuick3DTexture18textureDataChangedEv(
    QQuick3DTexture *self) {
  self->textureDataChanged();
}

//  void QQuick3DTexture::generateMipmapsChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuick3DTexture22generateMipmapsChangedEv(
    QQuick3DTexture *self) {
  self->generateMipmapsChanged();
}

//  void QQuick3DTexture::autoOrientationChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuick3DTexture22autoOrientationChangedEv(
    QQuick3DTexture *self) {
  self->autoOrientationChanged();
}

//  void QQuick3DTexture::textureProviderChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuick3DTexture22textureProviderChangedEv(
    QQuick3DTexture *self) {
  self->textureProviderChanged();
}

//  void QQuick3DTexture::textureInternalChange(QQuick3DTextureInternalChange
//      a0, QPrivateSignal a1)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuick3DTexture21textureInternalChangeE29QQuick3DTextureInternalChangeNS_14QPrivateSignalE(
    QQuick3DTexture *self,
    const QQuick3DTextureInternalChange *a0) {
  self->textureInternalChange(*a0, QQuick3DTexture::QPrivateSignal());
}

//  QSSGRenderGraphObject
//      *QQuick3DTexture::updateSpatialNode(QSSGRenderGraphObject *node)
extern "C" Q_DECL_EXPORT
QSSGRenderGraphObject *ritual_ZN15QQuick3DTexture17updateSpatialNodeEP21QSSGRenderGraphObject(
    QQuick3DTexture *self,
    QSSGRenderGraphObject *node) {
  return self->updateSpatialNode(node);
}

//  void QQuick3DTexture::markAllDirty()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuick3DTexture12markAllDirtyEv(QQuick3DTexture *self) {
  self->markAllDirty();
}

//  void QQuick3DTexture::itemChange(ItemChange change, const ItemChangeData
//      &value)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuick3DTexture10itemChangeEN14QQuick3DObject10ItemChangeERKNS0_14ItemChangeDataE(
    QQuick3DTexture *self,
    QQuick3DObject::ItemChange change,
    const QQuick3DObject::ItemChangeData *value) {
  self->itemChange(change, *value);
}

//  void QQuick3DTexture::itemGeometryChanged(QQuickItem *item,
//      QQuickGeometryChange change, const QRectF &geometry)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuick3DTexture19itemGeometryChangedEP10QQuickItem20QQuickGeometryChangeRK6QRectF(
    QQuick3DTexture *self,
    QQuickItem *item,
    const QQuickGeometryChange *change,
    const QRectF *geometry) {
  self->itemGeometryChanged(item, *change, *geometry);
}

//  QQuick3DTexture::QQuick3DTexture(QQuick3DObjectPrivate &dd,
//      QQuick3DObject *parent)
extern "C" Q_DECL_EXPORT
QQuick3DTexture *ritual_ZN15QQuick3DTextureC1ER21QQuick3DObjectPrivateP14QQuick3DObject(
    QQuick3DObjectPrivate *dd,
    QQuick3DObject *parent) {
  return new CuteQQuick3DTexture(*dd, parent);
}

//  void QQuick3DTexture::sourceItemDestroyed(QObject *item)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuick3DTexture19sourceItemDestroyedEP7QObject(
    QQuick3DTexture *self,
    QObject *item) {
  self->sourceItemDestroyed(item);
}

//  void QQuick3DTexture::sourceItemWindowChanged(QQuickWindow *window)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuick3DTexture23sourceItemWindowChangedEP12QQuickWindow(
    QQuick3DTexture *self,
    QQuickWindow *window) {
  self->sourceItemWindowChanged(window);
}

//  void QQuick3DTexture::markDirty(DirtyFlag type, bool
//      requestSecondaryUpdate)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuick3DTexture9markDirtyENS_9DirtyFlagEb(
    QQuick3DTexture *self,
    QQuick3DTexture::DirtyFlag type,
    bool requestSecondaryUpdate) {
  self->markDirty(type, requestSecondaryUpdate);
}

//  void QQuick3DTexture::trySetSourceParent()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuick3DTexture18trySetSourceParentEv(
    QQuick3DTexture *self) {
  self->trySetSourceParent();
}

//  bool QQuick3DTexture::effectiveFlipV(const QSSGRenderImage &imageNode)
//      const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK15QQuick3DTexture14effectiveFlipVERK15QSSGRenderImage(
    const QQuick3DTexture *self,
    const QSSGRenderImage *imageNode) {
  return self->effectiveFlipV(*imageNode);
}

//  QQuick3DTexture as the QQuickItemChangeListener it is built on
extern "C" Q_DECL_EXPORT
QQuickItemChangeListener *ritual_cast_QQuick3DTexture_QQuickItemChangeListener(
    QQuick3DTexture *self) {
  return static_cast<QQuickItemChangeListener *>(self);
}

//  a Python function taken by a CuteQQuick3DTexture, for the function named
//      by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQuick3DTexture(
    QQuick3DTexture *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQuick3DTexture *>(self)->take(key, call);
}

//  QSSGRenderGraphObject
//      *QQuick3DTexture::updateSpatialNode(QSSGRenderGraphObject *node)
extern "C" Q_DECL_EXPORT
QSSGRenderGraphObject *ritual_own_ZN15QQuick3DTexture17updateSpatialNodeEP21QSSGRenderGraphObject(
    QQuick3DTexture *self,
    QSSGRenderGraphObject *node) {
  return static_cast<OwnQQuick3DTexture *>(self)->OwnQQuick3DTexture::updateSpatialNode(
      node);
}

//  void QQuick3DTexture::markAllDirty()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN15QQuick3DTexture12markAllDirtyEv(QQuick3DTexture *self) {
  static_cast<OwnQQuick3DTexture *>(self)->OwnQQuick3DTexture::markAllDirty();
}

//  void QQuick3DTexture::itemChange(ItemChange change, const ItemChangeData
//      &value)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN15QQuick3DTexture10itemChangeEN14QQuick3DObject10ItemChangeERKNS0_14ItemChangeDataE(
    QQuick3DTexture *self,
    QQuick3DObject::ItemChange change,
    const QQuick3DObject::ItemChangeData *value) {
  static_cast<OwnQQuick3DTexture *>(self)->OwnQQuick3DTexture::itemChange(
      change,
      *value);
}

//  void QQuick3DTexture::itemGeometryChanged(QQuickItem *item,
//      QQuickGeometryChange change, const QRectF &geometry)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN15QQuick3DTexture19itemGeometryChangedEP10QQuickItem20QQuickGeometryChangeRK6QRectF(
    QQuick3DTexture *self,
    QQuickItem *item,
    const QQuickGeometryChange *change,
    const QRectF *geometry) {
  static_cast<OwnQQuick3DTexture *>(self)->OwnQQuick3DTexture::itemGeometryChanged(
      item,
      *change,
      *geometry);
}
