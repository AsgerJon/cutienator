//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick3D/6.12.0/QtQuick3D/private/qquick3ditem2d_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtQuick3D/6.12.0/QtQuick3D/private/qtquick3dglobal_p.h>
#include <QtQuick3D/QtQuick3D>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick3D/6.12.0/QtQuick3D/private/qquick3ditem2d_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qmetaobject.h>
#include <QtQuick3D/qquick3dobject.h>
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qquickitemchangelistener_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qrect.h>
#include <QtCore/qstring.h>
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick3D/qquick3dobject.h>
#include <QtQuick3D/private/qquick3ditem2d_p.h>
#include <QtQuick/private/qquickitem_p.h>
#include <QtQuick/private/qsgrenderer_p.h>
#include <QtQuick/private/qquickwindow_p.h>
#include <QtQuick3DRuntimeRender/private/qssgrenderitem2d_p.h>
#include <QtQuick3D/private/qquick3dnode_p_p.h>
#include <QtGui/rhi/qrhi.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtquick3d/src/quick3d/qquick3ditem2d.cpp, line 73, as _ZN14QQuick3DItem2D13updatePickingEv
inline void QQuick3DItem2D::updatePicking()
{
    m_pickingDirty = true;
    update();
}

//  from ../qtquick3d/src/quick3d/qquick3ditem2d.cpp, line 68, as _ZN14QQuick3DItem2D13itemDestroyedEP10QQuickItem
inline void QQuick3DItem2D::itemDestroyed(QQuickItem *item)
{
    removeChildItem(item);
}

//  from ../qtquick3d/src/quick3d/qquick3ditem2d.cpp, line 133, as _ZN14QQuick3DItem2D7preSyncEv
inline void QQuick3DItem2D::preSync()
{
    const auto &manager = QQuick3DObjectPrivate::get(this)->sceneManager;
    auto *sourcePrivate = QQuickItemPrivate::get(m_contentItem);
    auto *window = manager->window();
    if (m_window != window) {
        update(); // Just schedule an upate immediately.
        if (m_window) {
            disconnect(m_window, SIGNAL(destroyed(QObject*)), this, SLOT(derefWindow(QObject*)));
            sourcePrivate->derefWindow();
        }
        m_window = window;
        sourcePrivate->refWindow(window);
        connect(window, SIGNAL(destroyed(QObject*)), this, SLOT(derefWindow(QObject*)));
        sourcePrivate->refFromEffectItem(true);
    }
}

//  from ../qtquick3d/src/quick3d/qquick3ditem2d.cpp, line 79, as _ZN14QQuick3DItem2D17updateSpatialNodeEP21QSSGRenderGraphObject
inline QSSGRenderGraphObject *QQuick3DItem2D::updateSpatialNode(QSSGRenderGraphObject *node)
{
    auto *sourceItemPrivate = QQuickItemPrivate::get(m_contentItem);
    QQuickWindow *window = m_contentItem->window();

    if (!window) {
        const auto &manager = QQuick3DObjectPrivate::get(this)->sceneManager;
        window = manager->window();
    }

    if (!node) {
        markAllDirty();
        auto *backEndNode = new QSSGRenderItem2D();
        backEndNode->m_frontEndObject = this;
        node = backEndNode;
    }

    QQuick3DNode::updateSpatialNode(node);

    auto itemNode = static_cast<QSSGRenderItem2D *>(node);

    itemNode->m_rootNode = sourceItemPrivate->rootNode();
    if (!itemNode->m_rootNode) {
        QQuickWindowPrivate::get(window)->updateDirtyNode(m_contentItem);
        itemNode->m_rootNode = sourceItemPrivate->rootNode();
        if (!itemNode->m_rootNode) {
            qWarning() << "Item2D is not initialized. It will not be shown.";
            return nullptr;
        }
    }

    if (m_pickingDirty) {
        m_pickingDirty = false;
        bool isPickable = false;
        for (const auto &item : std::as_const(m_sourceItems)) {
            // Enable picking for Item2D if any of its child is visible and enabled.
            if (item->isVisible() && item->isEnabled()) {
                isPickable = true;
                break;
            }
        }
        itemNode->setState(QSSGRenderNode::LocalState::Pickable, isPickable);
    }

    return node;
}

//  from ../qtquick3d/src/quick3d/qquick3ditem2d.cpp, line 126, as _ZN14QQuick3DItem2D12markAllDirtyEv
inline void QQuick3DItem2D::markAllDirty()
{
    m_pickingDirty = true;

    QQuick3DNode::markAllDirty();
}

//  from ../qtquick3d/src/quick3d/qquick3ditem2d.cpp, line 52, as _ZN14QQuick3DItem2D15removeChildItemEP10QQuickItem
inline void QQuick3DItem2D::removeChildItem(QQuickItem *item)
{
    m_sourceItems.removeOne(item);
    if (item)
        QQuickItemPrivate::get(item)->removeItemChangeListener(this, QQuickItemPrivate::ChangeType::Destroyed);
    if (m_sourceItems.isEmpty())
        emit allChildrenRemoved();
    else
        update();
}

//  from ../qtquick3d/src/quick3d/qquick3ditem2d.cpp, line 63, as _ZNK14QQuick3DItem2D11contentItemEv
inline QQuickItem *QQuick3DItem2D::contentItem() const
{
    return m_contentItem;
}
//  -----------------------------------------------------------------------

//  Only a class built on QQuick3DItem2D may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQQuick3DItem2D : QQuick3DItem2D {
  using QQuick3DItem2D::preSync;
};

//  A QQuick3DItem2D that Python can take functions over in. Every QQuick3DItem2D
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQQuick3DItem2DCall0)(const void *, QQuickItem *, int *);
typedef void (*CuteQQuick3DItem2DCall1)(const void *, int *);
typedef void * (*CuteQQuick3DItem2DCall2)(const void *, QSSGRenderGraphObject *, int *);
typedef void (*CuteQQuick3DItem2DCall3)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuick3DItem2DCall4)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuick3DItem2DCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuick3DItem2DCall6)(const void *, int *);
typedef void (*CuteQQuick3DItem2DCall7)(const void *, int, const QQuick3DObject::ItemChangeData *, int *);
typedef void (*CuteQQuick3DItem2DCall8)(const void *, int *);
typedef void (*CuteQQuick3DItem2DCall9)(const void *, QQuickItem *, const QQuickGeometryChange *, const QRectF *, int *);
typedef void (*CuteQQuick3DItem2DCall10)(const void *, QQuickItem *, int *);
typedef void (*CuteQQuick3DItem2DCall11)(const void *, QQuickItem *, int *);
typedef void (*CuteQQuick3DItem2DCall12)(const void *, QQuickItem *, int *);
typedef void (*CuteQQuick3DItem2DCall13)(const void *, QQuickItem *, int *);
typedef void (*CuteQQuick3DItem2DCall14)(const void *, QQuickItem *, QQuickItem *, int *);
typedef void (*CuteQQuick3DItem2DCall15)(const void *, QQuickItem *, QQuickItem *, int *);
typedef void (*CuteQQuick3DItem2DCall16)(const void *, QQuickItem *, QQuickItem *, int *);
typedef void (*CuteQQuick3DItem2DCall17)(const void *, QQuickItem *, int *);
typedef void (*CuteQQuick3DItem2DCall18)(const void *, QQuickItem *, int *);
typedef void (*CuteQQuick3DItem2DCall19)(const void *, QQuickItem *, int *);
typedef void (*CuteQQuick3DItem2DCall20)(const void *, QQuickItem *, int, int *);
typedef void (*CuteQQuick3DItem2DCall21)(const void *, QQuickItem *, int *);
typedef void (*CuteQQuick3DItem2DCall22)(const void *, QQuickItem *, QQuickItem *, int *);
typedef void * (*CuteQQuick3DItem2DCall23)(const void *, int *);
typedef bool (*CuteQQuick3DItem2DCall24)(const void *, const QObject *, int *);
typedef QString * (*CuteQQuick3DItem2DCall25)(const void *, int *);
typedef void (*CuteQQuick3DItem2DCall26)(const void *, QQuickItem *, int *);
typedef void (*CuteQQuick3DItem2DCall27)(const void *, QQuickItem *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuick3DItem2DCall28)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuick3DItem2DCall29)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuick3DItem2DCall30)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuick3DItem2DCall31)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuick3DItem2DCall32)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQQuick3DItem2D : public QQuick3DItem2D {
public:
  using QQuick3DItem2D::QQuick3DItem2D;
  void *taken[33] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN24QQuickItemChangeListener13itemDestroyedEP10QQuickItem")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QQuick3DObject7preSyncEv")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QQuick3DObject17updateSpatialNodeEP21QSSGRenderGraphObject")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QQuick3DObject12markAllDirtyEv")) {
      taken[3] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[4] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[5] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN16QQmlParserStatus17componentCompleteEv")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QQuick3DObject10itemChangeENS_10ItemChangeERKNS_14ItemChangeDataE")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQmlParserStatus10classBeginEv")) {
      taken[8] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN24QQuickItemChangeListener19itemGeometryChangedEP10QQuickItem20QQuickGeometryChangeRK6QRectF")) {
      taken[9] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN24QQuickItemChangeListener23itemSiblingOrderChangedEP10QQuickItem")) {
      taken[10] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN24QQuickItemChangeListener21itemVisibilityChangedEP10QQuickItem")) {
      taken[11] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN24QQuickItemChangeListener18itemEnabledChangedEP10QQuickItem")) {
      taken[12] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN24QQuickItemChangeListener18itemOpacityChangedEP10QQuickItem")) {
      taken[13] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN24QQuickItemChangeListener14itemChildAddedEP10QQuickItemS1_")) {
      taken[14] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN24QQuickItemChangeListener16itemChildRemovedEP10QQuickItemS1_")) {
      taken[15] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN24QQuickItemChangeListener17itemParentChangedEP10QQuickItemS1_")) {
      taken[16] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN24QQuickItemChangeListener19itemRotationChangedEP10QQuickItem")) {
      taken[17] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN24QQuickItemChangeListener24itemImplicitWidthChangedEP10QQuickItem")) {
      taken[18] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN24QQuickItemChangeListener25itemImplicitHeightChangedEP10QQuickItem")) {
      taken[19] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN24QQuickItemChangeListener16itemFocusChangedEP10QQuickItemN2Qt11FocusReasonE")) {
      taken[20] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN24QQuickItemChangeListener16itemScaleChangedEP10QQuickItem")) {
      taken[21] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN24QQuickItemChangeListener20itemTransformChangedEP10QQuickItemS1_")) {
      taken[22] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN24QQuickItemChangeListener13anchorPrivateEv")) {
      taken[23] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK24QQuickItemChangeListener11baseDeletedEPK7QObject")) {
      taken[24] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK24QQuickItemChangeListener9debugNameEv")) {
      taken[25] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN24QQuickItemChangeListener13addSourceItemEP10QQuickItem")) {
      taken[26] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN24QQuickItemChangeListener16removeSourceItemEP10QQuickItem")) {
      taken[27] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[28] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[29] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[30] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[31] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[32] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

  //  void QQuick3DItem2D::itemDestroyed(QQuickItem *item)
  void itemDestroyed(QQuickItem *item) override {
    if (taken[0]) {
      int handled = 0;
      CuteQQuick3DItem2DCall0 call = reinterpret_cast<CuteQQuick3DItem2DCall0>(taken[0]);
      call(this, item, &handled);
      if (handled) return;
    }
    QQuick3DItem2D::itemDestroyed(item);
  }

  //  void QQuick3DItem2D::preSync()
  void preSync() override {
    if (taken[1]) {
      int handled = 0;
      CuteQQuick3DItem2DCall1 call = reinterpret_cast<CuteQQuick3DItem2DCall1>(taken[1]);
      call(this, &handled);
      if (handled) return;
    }
    QQuick3DItem2D::preSync();
  }

  //  QSSGRenderGraphObject
  //      *QQuick3DItem2D::updateSpatialNode(QSSGRenderGraphObject *node)
  QSSGRenderGraphObject *updateSpatialNode(
      QSSGRenderGraphObject *node) override {
    if (taken[2]) {
      int handled = 0;
      CuteQQuick3DItem2DCall2 call = reinterpret_cast<CuteQQuick3DItem2DCall2>(taken[2]);
      void * given = call(this, node, &handled);
      if (handled) return static_cast<QSSGRenderGraphObject *>(given);
    }
    return QQuick3DItem2D::updateSpatialNode(node);
  }

  //  void QQuick3DItem2D::markAllDirty()
  void markAllDirty() override {
    if (taken[3]) {
      int handled = 0;
      CuteQQuick3DItem2DCall3 call = reinterpret_cast<CuteQQuick3DItem2DCall3>(taken[3]);
      call(this, &handled);
      if (handled) return;
    }
    QQuick3DItem2D::markAllDirty();
  }

#if !defined(QT_NO_QOBJECT)
  //  void QQuick3DNode::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[4]) {
      int handled = 0;
      CuteQQuick3DItem2DCall4 call = reinterpret_cast<CuteQQuick3DItem2DCall4>(taken[4]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QQuick3DNode::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QQuick3DNode::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[5]) {
      int handled = 0;
      CuteQQuick3DItem2DCall5 call = reinterpret_cast<CuteQQuick3DItem2DCall5>(taken[5]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QQuick3DNode::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

  //  void QQuick3DNode::componentComplete()
  void componentComplete() override {
    if (taken[6]) {
      int handled = 0;
      CuteQQuick3DItem2DCall6 call = reinterpret_cast<CuteQQuick3DItem2DCall6>(taken[6]);
      call(this, &handled);
      if (handled) return;
    }
    QQuick3DNode::componentComplete();
  }

  //  void QQuick3DNode::itemChange(ItemChange a0, const ItemChangeData
  //      &a1)
  void itemChange(
      QQuick3DObject::ItemChange a0,
      const QQuick3DObject::ItemChangeData &a1) override {
    if (taken[7]) {
      int handled = 0;
      CuteQQuick3DItem2DCall7 call = reinterpret_cast<CuteQQuick3DItem2DCall7>(taken[7]);
      call(this, static_cast<int>(a0), &a1, &handled);
      if (handled) return;
    }
    QQuick3DNode::itemChange(a0, a1);
  }

  //  void QQuick3DObject::classBegin()
  void classBegin() override {
    if (taken[8]) {
      int handled = 0;
      CuteQQuick3DItem2DCall8 call = reinterpret_cast<CuteQQuick3DItem2DCall8>(taken[8]);
      call(this, &handled);
      if (handled) return;
    }
    QQuick3DObject::classBegin();
  }

  //  void QQuickItemChangeListener::itemGeometryChanged(QQuickItem *a0,
  //      QQuickGeometryChange a1, const QRectF &a2)
  void itemGeometryChanged(
      QQuickItem *a0,
      QQuickGeometryChange a1,
      const QRectF &a2) override {
    if (taken[9]) {
      int handled = 0;
      CuteQQuick3DItem2DCall9 call = reinterpret_cast<CuteQQuick3DItem2DCall9>(taken[9]);
      call(this, a0, &a1, &a2, &handled);
      if (handled) return;
    }
    QQuickItemChangeListener::itemGeometryChanged(a0, a1, a2);
  }

  //  void QQuickItemChangeListener::itemSiblingOrderChanged(QQuickItem
  //      *a0)
  void itemSiblingOrderChanged(QQuickItem *a0) override {
    if (taken[10]) {
      int handled = 0;
      CuteQQuick3DItem2DCall10 call = reinterpret_cast<CuteQQuick3DItem2DCall10>(taken[10]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItemChangeListener::itemSiblingOrderChanged(a0);
  }

  //  void QQuickItemChangeListener::itemVisibilityChanged(QQuickItem *a0)
  void itemVisibilityChanged(QQuickItem *a0) override {
    if (taken[11]) {
      int handled = 0;
      CuteQQuick3DItem2DCall11 call = reinterpret_cast<CuteQQuick3DItem2DCall11>(taken[11]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItemChangeListener::itemVisibilityChanged(a0);
  }

  //  void QQuickItemChangeListener::itemEnabledChanged(QQuickItem *a0)
  void itemEnabledChanged(QQuickItem *a0) override {
    if (taken[12]) {
      int handled = 0;
      CuteQQuick3DItem2DCall12 call = reinterpret_cast<CuteQQuick3DItem2DCall12>(taken[12]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItemChangeListener::itemEnabledChanged(a0);
  }

  //  void QQuickItemChangeListener::itemOpacityChanged(QQuickItem *a0)
  void itemOpacityChanged(QQuickItem *a0) override {
    if (taken[13]) {
      int handled = 0;
      CuteQQuick3DItem2DCall13 call = reinterpret_cast<CuteQQuick3DItem2DCall13>(taken[13]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItemChangeListener::itemOpacityChanged(a0);
  }

  //  void QQuickItemChangeListener::itemChildAdded(QQuickItem *a0,
  //      QQuickItem *a1)
  void itemChildAdded(QQuickItem *a0, QQuickItem *a1) override {
    if (taken[14]) {
      int handled = 0;
      CuteQQuick3DItem2DCall14 call = reinterpret_cast<CuteQQuick3DItem2DCall14>(taken[14]);
      call(this, a0, a1, &handled);
      if (handled) return;
    }
    QQuickItemChangeListener::itemChildAdded(a0, a1);
  }

  //  void QQuickItemChangeListener::itemChildRemoved(QQuickItem *a0,
  //      QQuickItem *a1)
  void itemChildRemoved(QQuickItem *a0, QQuickItem *a1) override {
    if (taken[15]) {
      int handled = 0;
      CuteQQuick3DItem2DCall15 call = reinterpret_cast<CuteQQuick3DItem2DCall15>(taken[15]);
      call(this, a0, a1, &handled);
      if (handled) return;
    }
    QQuickItemChangeListener::itemChildRemoved(a0, a1);
  }

  //  void QQuickItemChangeListener::itemParentChanged(QQuickItem *a0,
  //      QQuickItem *a1)
  void itemParentChanged(QQuickItem *a0, QQuickItem *a1) override {
    if (taken[16]) {
      int handled = 0;
      CuteQQuick3DItem2DCall16 call = reinterpret_cast<CuteQQuick3DItem2DCall16>(taken[16]);
      call(this, a0, a1, &handled);
      if (handled) return;
    }
    QQuickItemChangeListener::itemParentChanged(a0, a1);
  }

  //  void QQuickItemChangeListener::itemRotationChanged(QQuickItem *a0)
  void itemRotationChanged(QQuickItem *a0) override {
    if (taken[17]) {
      int handled = 0;
      CuteQQuick3DItem2DCall17 call = reinterpret_cast<CuteQQuick3DItem2DCall17>(taken[17]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItemChangeListener::itemRotationChanged(a0);
  }

  //  void QQuickItemChangeListener::itemImplicitWidthChanged(QQuickItem
  //      *a0)
  void itemImplicitWidthChanged(QQuickItem *a0) override {
    if (taken[18]) {
      int handled = 0;
      CuteQQuick3DItem2DCall18 call = reinterpret_cast<CuteQQuick3DItem2DCall18>(taken[18]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItemChangeListener::itemImplicitWidthChanged(a0);
  }

  //  void QQuickItemChangeListener::itemImplicitHeightChanged(QQuickItem
  //      *a0)
  void itemImplicitHeightChanged(QQuickItem *a0) override {
    if (taken[19]) {
      int handled = 0;
      CuteQQuick3DItem2DCall19 call = reinterpret_cast<CuteQQuick3DItem2DCall19>(taken[19]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItemChangeListener::itemImplicitHeightChanged(a0);
  }

  //  void QQuickItemChangeListener::itemFocusChanged(QQuickItem *a0,
  //      Qt::FocusReason a1)
  void itemFocusChanged(QQuickItem *a0, Qt::FocusReason a1) override {
    if (taken[20]) {
      int handled = 0;
      CuteQQuick3DItem2DCall20 call = reinterpret_cast<CuteQQuick3DItem2DCall20>(taken[20]);
      call(this, a0, static_cast<int>(a1), &handled);
      if (handled) return;
    }
    QQuickItemChangeListener::itemFocusChanged(a0, a1);
  }

  //  void QQuickItemChangeListener::itemScaleChanged(QQuickItem *a0)
  void itemScaleChanged(QQuickItem *a0) override {
    if (taken[21]) {
      int handled = 0;
      CuteQQuick3DItem2DCall21 call = reinterpret_cast<CuteQQuick3DItem2DCall21>(taken[21]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItemChangeListener::itemScaleChanged(a0);
  }

  //  void QQuickItemChangeListener::itemTransformChanged(QQuickItem *a0,
  //      QQuickItem *a1)
  void itemTransformChanged(QQuickItem *a0, QQuickItem *a1) override {
    if (taken[22]) {
      int handled = 0;
      CuteQQuick3DItem2DCall22 call = reinterpret_cast<CuteQQuick3DItem2DCall22>(taken[22]);
      call(this, a0, a1, &handled);
      if (handled) return;
    }
    QQuickItemChangeListener::itemTransformChanged(a0, a1);
  }

  //  QQuickAnchorsPrivate *QQuickItemChangeListener::anchorPrivate()
  QQuickAnchorsPrivate *anchorPrivate() override {
    if (taken[23]) {
      int handled = 0;
      CuteQQuick3DItem2DCall23 call = reinterpret_cast<CuteQQuick3DItem2DCall23>(taken[23]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QQuickAnchorsPrivate *>(given);
    }
    return QQuickItemChangeListener::anchorPrivate();
  }

  //  bool QQuickItemChangeListener::baseDeleted(const QObject *caller)
  //      const
  bool baseDeleted(const QObject *caller) const override {
    if (taken[24]) {
      int handled = 0;
      CuteQQuick3DItem2DCall24 call = reinterpret_cast<CuteQQuick3DItem2DCall24>(taken[24]);
      bool given = call(this, caller, &handled);
      if (handled) return given;
    }
    return QQuickItemChangeListener::baseDeleted(caller);
  }

  //  QString QQuickItemChangeListener::debugName() const
  QString debugName() const override {
    if (taken[25]) {
      int handled = 0;
      CuteQQuick3DItem2DCall25 call = reinterpret_cast<CuteQQuick3DItem2DCall25>(taken[25]);
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
    if (taken[26]) {
      int handled = 0;
      CuteQQuick3DItem2DCall26 call = reinterpret_cast<CuteQQuick3DItem2DCall26>(taken[26]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItemChangeListener::addSourceItem(a0);
  }

  //  void QQuickItemChangeListener::removeSourceItem(QQuickItem *a0)
  void removeSourceItem(QQuickItem *a0) override {
    if (taken[27]) {
      int handled = 0;
      CuteQQuick3DItem2DCall27 call = reinterpret_cast<CuteQQuick3DItem2DCall27>(taken[27]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItemChangeListener::removeSourceItem(a0);
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[28]) {
      int handled = 0;
      CuteQQuick3DItem2DCall28 call = reinterpret_cast<CuteQQuick3DItem2DCall28>(taken[28]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[29]) {
      int handled = 0;
      CuteQQuick3DItem2DCall29 call = reinterpret_cast<CuteQQuick3DItem2DCall29>(taken[29]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[30]) {
      int handled = 0;
      CuteQQuick3DItem2DCall30 call = reinterpret_cast<CuteQQuick3DItem2DCall30>(taken[30]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[31]) {
      int handled = 0;
      CuteQQuick3DItem2DCall31 call = reinterpret_cast<CuteQQuick3DItem2DCall31>(taken[31]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[32]) {
      int handled = 0;
      CuteQQuick3DItem2DCall32 call = reinterpret_cast<CuteQQuick3DItem2DCall32>(taken[32]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QQuick3DItem2D::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK14QQuick3DItem2D10metaObjectEv(
    const QQuick3DItem2D *self) {
  return self->metaObject();
}

//  void *QQuick3DItem2D::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN14QQuick3DItem2D11qt_metacastEPKc(
    QQuick3DItem2D *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QQuick3DItem2D::qt_metacall(QMetaObject::Call a0, int a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN14QQuick3DItem2D11qt_metacallEN11QMetaObject4CallEiPPv(
    QQuick3DItem2D *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QQuick3DItem2D::~QQuick3DItem2D()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuick3DItem2DD1Ev(QQuick3DItem2D *self) {
  delete self;
}

//  QQuickItem *QQuick3DItem2D::contentItem() const
extern "C" Q_DECL_EXPORT
QQuickItem *ritual_ZNK14QQuick3DItem2D11contentItemEv(
    const QQuick3DItem2D *self) {
  return self->contentItem();
}

//  void QQuick3DItem2D::itemDestroyed(QQuickItem *item)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuick3DItem2D13itemDestroyedEP10QQuickItem(
    QQuick3DItem2D *self,
    QQuickItem *item) {
  self->itemDestroyed(item);
}

//  void QQuick3DItem2D::updatePicking()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuick3DItem2D13updatePickingEv(QQuick3DItem2D *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQuick3DItem2D")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "updatePicking()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "updatePicking()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QQuick3DItem2D::derefWindow(QObject *win)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuick3DItem2D11derefWindowEP7QObject(
    QQuick3DItem2D *self,
    QObject *win) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQuick3DItem2D")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "derefWindow(QObject *)").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "derefWindow(QObject *)");
  void *arguments[] = {
      nullptr,
      const_cast<void *>(static_cast<const void *>(&win)),
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QQuick3DItem2D::allChildrenRemoved()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuick3DItem2D18allChildrenRemovedEv(QQuick3DItem2D *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQuick3DItem2D")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "allChildrenRemoved()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "allChildrenRemoved()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QQuick3DItem2D::preSync()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuick3DItem2D7preSyncEv(QQuick3DItem2D *self) {
  self->preSync();
}

//  QSSGRenderGraphObject
//      *QQuick3DItem2D::updateSpatialNode(QSSGRenderGraphObject *node)
extern "C" Q_DECL_EXPORT
QSSGRenderGraphObject *ritual_ZN14QQuick3DItem2D17updateSpatialNodeEP21QSSGRenderGraphObject(
    QQuick3DItem2D *self,
    QSSGRenderGraphObject *node) {
  return self->updateSpatialNode(node);
}

//  void QQuick3DItem2D::markAllDirty()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuick3DItem2D12markAllDirtyEv(QQuick3DItem2D *self) {
  self->markAllDirty();
}

//  QQuick3DItem2D as the QQuickItemChangeListener it is built on
extern "C" Q_DECL_EXPORT
QQuickItemChangeListener *ritual_cast_QQuick3DItem2D_QQuickItemChangeListener(
    QQuick3DItem2D *self) {
  return static_cast<QQuickItemChangeListener *>(self);
}

//  a Python function taken by a CuteQQuick3DItem2D, for the function named
//      by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQuick3DItem2D(
    QQuick3DItem2D *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQuick3DItem2D *>(self)->take(key, call);
}

//  void QQuick3DItem2D::preSync()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN14QQuick3DItem2D7preSyncEv(QQuick3DItem2D *self) {
  static_cast<OwnQQuick3DItem2D *>(self)->OwnQQuick3DItem2D::preSync();
}

//  QSSGRenderGraphObject
//      *QQuick3DItem2D::updateSpatialNode(QSSGRenderGraphObject *node)
extern "C" Q_DECL_EXPORT
QSSGRenderGraphObject *ritual_own_ZN14QQuick3DItem2D17updateSpatialNodeEP21QSSGRenderGraphObject(
    QQuick3DItem2D *self,
    QSSGRenderGraphObject *node) {
  return self->QQuick3DItem2D::updateSpatialNode(node);
}

//  void QQuick3DItem2D::markAllDirty()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN14QQuick3DItem2D12markAllDirtyEv(QQuick3DItem2D *self) {
  self->QQuick3DItem2D::markAllDirty();
}
