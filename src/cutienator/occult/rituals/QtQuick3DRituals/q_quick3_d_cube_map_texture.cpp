//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick3D/6.12.0/QtQuick3D/private/qquick3dcubemaptexture_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtQuick3D/6.12.0/QtQuick3D/private/qtquick3dglobal_p.h>
#include <QtQuick3D/QtQuick3D>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick3D/6.12.0/QtQuick3D/private/qquick3dcubemaptexture_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtQuick3D/qquick3dobject.h>
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qquickitemchangelistener_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qrect.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A QQuick3DCubeMapTexture that Python can take functions over in. Every QQuick3DCubeMapTexture
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void * (*CuteQQuick3DCubeMapTextureCall0)(const void *, QSSGRenderGraphObject *, int *);
typedef void (*CuteQQuick3DCubeMapTextureCall1)(const void *, int *);
typedef void (*CuteQQuick3DCubeMapTextureCall2)(const void *, int, const QQuick3DObject::ItemChangeData *, int *);
typedef void (*CuteQQuick3DCubeMapTextureCall3)(const void *, QQuickItem *, const QQuickGeometryChange *, const QRectF *, int *);
typedef void (*CuteQQuick3DCubeMapTextureCall4)(const void *, int *);
typedef void (*CuteQQuick3DCubeMapTextureCall5)(const void *, int *);
typedef void (*CuteQQuick3DCubeMapTextureCall6)(const void *, int *);
typedef void (*CuteQQuick3DCubeMapTextureCall7)(const void *, QQuickItem *, int *);
typedef void (*CuteQQuick3DCubeMapTextureCall8)(const void *, QQuickItem *, int *);
typedef void (*CuteQQuick3DCubeMapTextureCall9)(const void *, QQuickItem *, int *);
typedef void (*CuteQQuick3DCubeMapTextureCall10)(const void *, QQuickItem *, int *);
typedef void (*CuteQQuick3DCubeMapTextureCall11)(const void *, QQuickItem *, int *);
typedef void (*CuteQQuick3DCubeMapTextureCall12)(const void *, QQuickItem *, QQuickItem *, int *);
typedef void (*CuteQQuick3DCubeMapTextureCall13)(const void *, QQuickItem *, QQuickItem *, int *);
typedef void (*CuteQQuick3DCubeMapTextureCall14)(const void *, QQuickItem *, QQuickItem *, int *);
typedef void (*CuteQQuick3DCubeMapTextureCall15)(const void *, QQuickItem *, int *);
typedef void (*CuteQQuick3DCubeMapTextureCall16)(const void *, QQuickItem *, int *);
typedef void (*CuteQQuick3DCubeMapTextureCall17)(const void *, QQuickItem *, int *);
typedef void (*CuteQQuick3DCubeMapTextureCall18)(const void *, QQuickItem *, int, int *);
typedef void (*CuteQQuick3DCubeMapTextureCall19)(const void *, QQuickItem *, int *);
typedef void (*CuteQQuick3DCubeMapTextureCall20)(const void *, QQuickItem *, QQuickItem *, int *);
typedef void * (*CuteQQuick3DCubeMapTextureCall21)(const void *, int *);
typedef bool (*CuteQQuick3DCubeMapTextureCall22)(const void *, const QObject *, int *);
typedef QString * (*CuteQQuick3DCubeMapTextureCall23)(const void *, int *);
typedef void (*CuteQQuick3DCubeMapTextureCall24)(const void *, QQuickItem *, int *);
typedef void (*CuteQQuick3DCubeMapTextureCall25)(const void *, QQuickItem *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuick3DCubeMapTextureCall26)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuick3DCubeMapTextureCall27)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuick3DCubeMapTextureCall28)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuick3DCubeMapTextureCall29)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuick3DCubeMapTextureCall30)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuick3DCubeMapTextureCall31)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuick3DCubeMapTextureCall32)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQQuick3DCubeMapTexture : public QQuick3DCubeMapTexture {
public:
  using QQuick3DCubeMapTexture::QQuick3DCubeMapTexture;
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
      CuteQQuick3DCubeMapTextureCall0 call = reinterpret_cast<CuteQQuick3DCubeMapTextureCall0>(taken[0]);
      void * given = call(this, node, &handled);
      if (handled) return static_cast<QSSGRenderGraphObject *>(given);
    }
    return QQuick3DTexture::updateSpatialNode(node);
  }

  //  void QQuick3DTexture::markAllDirty()
  void markAllDirty() override {
    if (taken[1]) {
      int handled = 0;
      CuteQQuick3DCubeMapTextureCall1 call = reinterpret_cast<CuteQQuick3DCubeMapTextureCall1>(taken[1]);
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
      CuteQQuick3DCubeMapTextureCall2 call = reinterpret_cast<CuteQQuick3DCubeMapTextureCall2>(taken[2]);
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
      CuteQQuick3DCubeMapTextureCall3 call = reinterpret_cast<CuteQQuick3DCubeMapTextureCall3>(taken[3]);
      call(this, item, &change, &geometry, &handled);
      if (handled) return;
    }
    QQuick3DTexture::itemGeometryChanged(item, change, geometry);
  }

  //  void QQuick3DObject::classBegin()
  void classBegin() override {
    if (taken[4]) {
      int handled = 0;
      CuteQQuick3DCubeMapTextureCall4 call = reinterpret_cast<CuteQQuick3DCubeMapTextureCall4>(taken[4]);
      call(this, &handled);
      if (handled) return;
    }
    QQuick3DObject::classBegin();
  }

  //  void QQuick3DObject::componentComplete()
  void componentComplete() override {
    if (taken[5]) {
      int handled = 0;
      CuteQQuick3DCubeMapTextureCall5 call = reinterpret_cast<CuteQQuick3DCubeMapTextureCall5>(taken[5]);
      call(this, &handled);
      if (handled) return;
    }
    QQuick3DObject::componentComplete();
  }

  //  void QQuick3DObject::preSync()
  void preSync() override {
    if (taken[6]) {
      int handled = 0;
      CuteQQuick3DCubeMapTextureCall6 call = reinterpret_cast<CuteQQuick3DCubeMapTextureCall6>(taken[6]);
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
      CuteQQuick3DCubeMapTextureCall7 call = reinterpret_cast<CuteQQuick3DCubeMapTextureCall7>(taken[7]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItemChangeListener::itemSiblingOrderChanged(a0);
  }

  //  void QQuickItemChangeListener::itemVisibilityChanged(QQuickItem *a0)
  void itemVisibilityChanged(QQuickItem *a0) override {
    if (taken[8]) {
      int handled = 0;
      CuteQQuick3DCubeMapTextureCall8 call = reinterpret_cast<CuteQQuick3DCubeMapTextureCall8>(taken[8]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItemChangeListener::itemVisibilityChanged(a0);
  }

  //  void QQuickItemChangeListener::itemEnabledChanged(QQuickItem *a0)
  void itemEnabledChanged(QQuickItem *a0) override {
    if (taken[9]) {
      int handled = 0;
      CuteQQuick3DCubeMapTextureCall9 call = reinterpret_cast<CuteQQuick3DCubeMapTextureCall9>(taken[9]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItemChangeListener::itemEnabledChanged(a0);
  }

  //  void QQuickItemChangeListener::itemOpacityChanged(QQuickItem *a0)
  void itemOpacityChanged(QQuickItem *a0) override {
    if (taken[10]) {
      int handled = 0;
      CuteQQuick3DCubeMapTextureCall10 call = reinterpret_cast<CuteQQuick3DCubeMapTextureCall10>(taken[10]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItemChangeListener::itemOpacityChanged(a0);
  }

  //  void QQuickItemChangeListener::itemDestroyed(QQuickItem *a0)
  void itemDestroyed(QQuickItem *a0) override {
    if (taken[11]) {
      int handled = 0;
      CuteQQuick3DCubeMapTextureCall11 call = reinterpret_cast<CuteQQuick3DCubeMapTextureCall11>(taken[11]);
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
      CuteQQuick3DCubeMapTextureCall12 call = reinterpret_cast<CuteQQuick3DCubeMapTextureCall12>(taken[12]);
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
      CuteQQuick3DCubeMapTextureCall13 call = reinterpret_cast<CuteQQuick3DCubeMapTextureCall13>(taken[13]);
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
      CuteQQuick3DCubeMapTextureCall14 call = reinterpret_cast<CuteQQuick3DCubeMapTextureCall14>(taken[14]);
      call(this, a0, a1, &handled);
      if (handled) return;
    }
    QQuickItemChangeListener::itemParentChanged(a0, a1);
  }

  //  void QQuickItemChangeListener::itemRotationChanged(QQuickItem *a0)
  void itemRotationChanged(QQuickItem *a0) override {
    if (taken[15]) {
      int handled = 0;
      CuteQQuick3DCubeMapTextureCall15 call = reinterpret_cast<CuteQQuick3DCubeMapTextureCall15>(taken[15]);
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
      CuteQQuick3DCubeMapTextureCall16 call = reinterpret_cast<CuteQQuick3DCubeMapTextureCall16>(taken[16]);
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
      CuteQQuick3DCubeMapTextureCall17 call = reinterpret_cast<CuteQQuick3DCubeMapTextureCall17>(taken[17]);
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
      CuteQQuick3DCubeMapTextureCall18 call = reinterpret_cast<CuteQQuick3DCubeMapTextureCall18>(taken[18]);
      call(this, a0, static_cast<int>(a1), &handled);
      if (handled) return;
    }
    QQuickItemChangeListener::itemFocusChanged(a0, a1);
  }

  //  void QQuickItemChangeListener::itemScaleChanged(QQuickItem *a0)
  void itemScaleChanged(QQuickItem *a0) override {
    if (taken[19]) {
      int handled = 0;
      CuteQQuick3DCubeMapTextureCall19 call = reinterpret_cast<CuteQQuick3DCubeMapTextureCall19>(taken[19]);
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
      CuteQQuick3DCubeMapTextureCall20 call = reinterpret_cast<CuteQQuick3DCubeMapTextureCall20>(taken[20]);
      call(this, a0, a1, &handled);
      if (handled) return;
    }
    QQuickItemChangeListener::itemTransformChanged(a0, a1);
  }

  //  QQuickAnchorsPrivate *QQuickItemChangeListener::anchorPrivate()
  QQuickAnchorsPrivate *anchorPrivate() override {
    if (taken[21]) {
      int handled = 0;
      CuteQQuick3DCubeMapTextureCall21 call = reinterpret_cast<CuteQQuick3DCubeMapTextureCall21>(taken[21]);
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
      CuteQQuick3DCubeMapTextureCall22 call = reinterpret_cast<CuteQQuick3DCubeMapTextureCall22>(taken[22]);
      bool given = call(this, caller, &handled);
      if (handled) return given;
    }
    return QQuickItemChangeListener::baseDeleted(caller);
  }

  //  QString QQuickItemChangeListener::debugName() const
  QString debugName() const override {
    if (taken[23]) {
      int handled = 0;
      CuteQQuick3DCubeMapTextureCall23 call = reinterpret_cast<CuteQQuick3DCubeMapTextureCall23>(taken[23]);
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
      CuteQQuick3DCubeMapTextureCall24 call = reinterpret_cast<CuteQQuick3DCubeMapTextureCall24>(taken[24]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItemChangeListener::addSourceItem(a0);
  }

  //  void QQuickItemChangeListener::removeSourceItem(QQuickItem *a0)
  void removeSourceItem(QQuickItem *a0) override {
    if (taken[25]) {
      int handled = 0;
      CuteQQuick3DCubeMapTextureCall25 call = reinterpret_cast<CuteQQuick3DCubeMapTextureCall25>(taken[25]);
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
      CuteQQuick3DCubeMapTextureCall26 call = reinterpret_cast<CuteQQuick3DCubeMapTextureCall26>(taken[26]);
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
      CuteQQuick3DCubeMapTextureCall27 call = reinterpret_cast<CuteQQuick3DCubeMapTextureCall27>(taken[27]);
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
      CuteQQuick3DCubeMapTextureCall28 call = reinterpret_cast<CuteQQuick3DCubeMapTextureCall28>(taken[28]);
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
      CuteQQuick3DCubeMapTextureCall29 call = reinterpret_cast<CuteQQuick3DCubeMapTextureCall29>(taken[29]);
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
      CuteQQuick3DCubeMapTextureCall30 call = reinterpret_cast<CuteQQuick3DCubeMapTextureCall30>(taken[30]);
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
      CuteQQuick3DCubeMapTextureCall31 call = reinterpret_cast<CuteQQuick3DCubeMapTextureCall31>(taken[31]);
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
      CuteQQuick3DCubeMapTextureCall32 call = reinterpret_cast<CuteQQuick3DCubeMapTextureCall32>(taken[32]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QQuick3DCubeMapTexture::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK22QQuick3DCubeMapTexture10metaObjectEv(
    const QQuick3DCubeMapTexture *self) {
  return self->metaObject();
}

//  void *QQuick3DCubeMapTexture::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN22QQuick3DCubeMapTexture11qt_metacastEPKc(
    QQuick3DCubeMapTexture *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QQuick3DCubeMapTexture::qt_metacall(QMetaObject::Call a0, int a1,
//      void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN22QQuick3DCubeMapTexture11qt_metacallEN11QMetaObject4CallEiPPv(
    QQuick3DCubeMapTexture *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QQuick3DCubeMapTexture::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN22QQuick3DCubeMapTexture2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuick3DCubeMapTexture::tr(s, c, n));
}

//  QQuick3DCubeMapTexture::QQuick3DCubeMapTexture(QQuick3DObject *parent)
extern "C" Q_DECL_EXPORT
QQuick3DCubeMapTexture *ritual_ZN22QQuick3DCubeMapTextureC1EP14QQuick3DObject(
    QQuick3DObject *parent) {
  return new CuteQQuick3DCubeMapTexture(parent);
}

//  QQuick3DCubeMapTexture::~QQuick3DCubeMapTexture()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuick3DCubeMapTextureD1Ev(QQuick3DCubeMapTexture *self) {
  delete self;
}

//  a Python function taken by a CuteQQuick3DCubeMapTexture, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQuick3DCubeMapTexture(
    QQuick3DCubeMapTexture *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQuick3DCubeMapTexture *>(self)->take(key, call);
}
