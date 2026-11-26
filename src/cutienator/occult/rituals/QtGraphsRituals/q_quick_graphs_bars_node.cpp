//  Written by dev_tooling.RitualGenerator from the records of
//  QtGraphs/6.12.0/QtGraphs/private/qquickgraphsbarsnode_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtGraphs/qgraphsglobal.h>
#include <QtGraphs/6.12.0/QtGraphs/private/qgraphsglobal_p.h>
#if (QT_CONFIG(graphs_3d)) && (!(!QT_CONFIG(graphs_3d_bars3d) && !QT_CONFIG(graphs_3d_scatter3d) && !QT_CONFIG(graphs_3d_surface3d))) && (QT_CONFIG(graphs_3d_bars3d))
#include <QtGraphs/6.12.0/QtGraphs/private/qgraphsglobal_p.h>
#include <QtGraphs/QtGraphs>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGraphs/6.12.0/QtGraphs/private/qquickgraphsbarsnode_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qsize.h>
#if (QT_CONFIG(graphs_3d)) && (!(!QT_CONFIG(graphs_3d_bars3d) && !QT_CONFIG(graphs_3d_scatter3d) && !QT_CONFIG(graphs_3d_surface3d))) && (QT_CONFIG(graphs_3d_bars3d))
#include <QtGraphs/QtGraphs>
#include <QtGraphs/qbar3dseries.h>
#endif
#include <QtCore/qpoint.h>
#include <QtGui/qvectornd.h>
#include <QtCore/qmetaobject.h>
#include <QtQuick3D/qquick3dobject.h>
#include <QtCore/qlist.h>
#include <cstring>
#include <QtQml/QQmlListProperty>
#include <QtGraphs/QBar3DSeries>

//  Only a class built on QQuickGraphsBarsNode may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQQuickGraphsBarsNode : QQuickGraphsBarsNode {
  using QQuickGraphsBarsNode::componentComplete;
};

//  A QQuickGraphsBarsNode that Python can take functions over in. Every QQuickGraphsBarsNode
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQQuickGraphsBarsNodeCall0)(const void *, int *);
typedef bool (*CuteQQuickGraphsBarsNodeCall1)(const void *, const QPointF *, int *);
typedef bool (*CuteQQuickGraphsBarsNodeCall2)(const void *, const QVector3D *, const QVector3D *, int *);
typedef void (*CuteQQuickGraphsBarsNodeCall3)(const void *, int *);
typedef void (*CuteQQuickGraphsBarsNodeCall4)(const void *, int, int *);
typedef bool (*CuteQQuickGraphsBarsNodeCall5)(const void *, QAbstract3DSeries *, int *);
typedef void (*CuteQQuickGraphsBarsNodeCall6)(const void *, QAbstract3DSeries *, int *);
typedef void (*CuteQQuickGraphsBarsNodeCall7)(const void *, QAbstract3DSeries *, int *);
typedef qsizetype (*CuteQQuickGraphsBarsNodeCall8)(const void *, QCustom3DItem *, int *);
typedef void (*CuteQQuickGraphsBarsNodeCall9)(const void *, int *);
typedef void (*CuteQQuickGraphsBarsNodeCall10)(const void *, QCustom3DItem *, int *);
typedef void (*CuteQQuickGraphsBarsNodeCall11)(const void *, const QVector3D *, int *);
typedef void (*CuteQQuickGraphsBarsNodeCall12)(const void *, QCustom3DItem *, int *);
typedef int (*CuteQQuickGraphsBarsNodeCall13)(const void *, int *);
typedef void * (*CuteQQuickGraphsBarsNodeCall14)(const void *, int *);
typedef qsizetype (*CuteQQuickGraphsBarsNodeCall15)(const void *, int *);
typedef void * (*CuteQQuickGraphsBarsNodeCall16)(const void *, int *);
typedef void (*CuteQQuickGraphsBarsNodeCall17)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickGraphsBarsNodeCall18)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickGraphsBarsNodeCall19)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
typedef void * (*CuteQQuickGraphsBarsNodeCall20)(const void *, QSSGRenderGraphObject *, int *);
typedef void (*CuteQQuickGraphsBarsNodeCall21)(const void *, int, const QQuick3DObject::ItemChangeData *, int *);
typedef void (*CuteQQuickGraphsBarsNodeCall22)(const void *, int *);
typedef void (*CuteQQuickGraphsBarsNodeCall23)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickGraphsBarsNodeCall24)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickGraphsBarsNodeCall25)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickGraphsBarsNodeCall26)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickGraphsBarsNodeCall27)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickGraphsBarsNodeCall28)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQQuickGraphsBarsNode : public QQuickGraphsBarsNode {
public:
  using QQuickGraphsBarsNode::QQuickGraphsBarsNode;
  void *taken[29] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN16QQuickGraphsNode14clearSelectionEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQuickGraphsNode9doPickingE7QPointF")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQuickGraphsNode12doRayPickingERK9QVector3DS2_")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQmlParserStatus17componentCompleteEv")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQuickGraphsNode16setSelectionModeE6QFlagsIN10QtGraphs3D13SelectionFlagEE")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQuickGraphsNode9hasSeriesEP17QAbstract3DSeries")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQuickGraphsNode17addSeriesInternalEP17QAbstract3DSeries")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQuickGraphsNode20removeSeriesInternalEP17QAbstract3DSeries")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQuickGraphsNode13addCustomItemEP13QCustom3DItem")) {
      taken[8] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQuickGraphsNode17removeCustomItemsEv")) {
      taken[9] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQuickGraphsNode16removeCustomItemEP13QCustom3DItem")) {
      taken[10] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQuickGraphsNode18removeCustomItemAtE9QVector3D")) {
      taken[11] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQuickGraphsNode17releaseCustomItemEP13QCustom3DItem")) {
      taken[12] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK16QQuickGraphsNode18selectedLabelIndexEv")) {
      taken[13] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK16QQuickGraphsNode12selectedAxisEv")) {
      taken[14] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK16QQuickGraphsNode23selectedCustomItemIndexEv")) {
      taken[15] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK16QQuickGraphsNode18selectedCustomItemEv")) {
      taken[16] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QQuick3DObject12markAllDirtyEv")) {
      taken[17] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[18] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[19] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN14QQuick3DObject17updateSpatialNodeEP21QSSGRenderGraphObject")) {
      taken[20] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QQuick3DObject10itemChangeENS_10ItemChangeERKNS_14ItemChangeDataE")) {
      taken[21] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQmlParserStatus10classBeginEv")) {
      taken[22] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QQuick3DObject7preSyncEv")) {
      taken[23] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[24] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[25] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[26] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[27] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[28] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

  //  void QQuickGraphsBarsNode::clearSelection()
  void clearSelection() override {
    if (taken[0]) {
      int handled = 0;
      CuteQQuickGraphsBarsNodeCall0 call = reinterpret_cast<CuteQQuickGraphsBarsNodeCall0>(taken[0]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickGraphsBarsNode::clearSelection();
  }

  //  bool QQuickGraphsBarsNode::doPicking(QPointF point)
  bool doPicking(QPointF point) override {
    if (taken[1]) {
      int handled = 0;
      CuteQQuickGraphsBarsNodeCall1 call = reinterpret_cast<CuteQQuickGraphsBarsNodeCall1>(taken[1]);
      bool given = call(this, &point, &handled);
      if (handled) return given;
    }
    return QQuickGraphsBarsNode::doPicking(point);
  }

  //  bool QQuickGraphsBarsNode::doRayPicking(const QVector3D &origin,
  //      const QVector3D &direction)
  bool doRayPicking(
      const QVector3D &origin,
      const QVector3D &direction) override {
    if (taken[2]) {
      int handled = 0;
      CuteQQuickGraphsBarsNodeCall2 call = reinterpret_cast<CuteQQuickGraphsBarsNodeCall2>(taken[2]);
      bool given = call(this, &origin, &direction, &handled);
      if (handled) return given;
    }
    return QQuickGraphsBarsNode::doRayPicking(origin, direction);
  }

  //  void QQuickGraphsBarsNode::componentComplete()
  void componentComplete() override {
    if (taken[3]) {
      int handled = 0;
      CuteQQuickGraphsBarsNodeCall3 call = reinterpret_cast<CuteQQuickGraphsBarsNodeCall3>(taken[3]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickGraphsBarsNode::componentComplete();
  }

  //  void QQuickGraphsNode::setSelectionMode(QtGraphs3D::SelectionFlags
  //      selectionMode)
  void setSelectionMode(QtGraphs3D::SelectionFlags selectionMode) override {
    if (taken[4]) {
      int handled = 0;
      CuteQQuickGraphsBarsNodeCall4 call = reinterpret_cast<CuteQQuickGraphsBarsNodeCall4>(taken[4]);
      call(this, static_cast<int>(selectionMode.toInt()), &handled);
      if (handled) return;
    }
    QQuickGraphsNode::setSelectionMode(selectionMode);
  }

  //  bool QQuickGraphsNode::hasSeries(QAbstract3DSeries *series)
  bool hasSeries(QAbstract3DSeries *series) override {
    if (taken[5]) {
      int handled = 0;
      CuteQQuickGraphsBarsNodeCall5 call = reinterpret_cast<CuteQQuickGraphsBarsNodeCall5>(taken[5]);
      bool given = call(this, series, &handled);
      if (handled) return given;
    }
    return QQuickGraphsNode::hasSeries(series);
  }

  //  void QQuickGraphsNode::addSeriesInternal(QAbstract3DSeries *series)
  void addSeriesInternal(QAbstract3DSeries *series) override {
    if (taken[6]) {
      int handled = 0;
      CuteQQuickGraphsBarsNodeCall6 call = reinterpret_cast<CuteQQuickGraphsBarsNodeCall6>(taken[6]);
      call(this, series, &handled);
      if (handled) return;
    }
    QQuickGraphsNode::addSeriesInternal(series);
  }

  //  void QQuickGraphsNode::removeSeriesInternal(QAbstract3DSeries
  //      *series)
  void removeSeriesInternal(QAbstract3DSeries *series) override {
    if (taken[7]) {
      int handled = 0;
      CuteQQuickGraphsBarsNodeCall7 call = reinterpret_cast<CuteQQuickGraphsBarsNodeCall7>(taken[7]);
      call(this, series, &handled);
      if (handled) return;
    }
    QQuickGraphsNode::removeSeriesInternal(series);
  }

  //  qsizetype QQuickGraphsNode::addCustomItem(QCustom3DItem *item)
  qsizetype addCustomItem(QCustom3DItem *item) override {
    if (taken[8]) {
      int handled = 0;
      CuteQQuickGraphsBarsNodeCall8 call = reinterpret_cast<CuteQQuickGraphsBarsNodeCall8>(taken[8]);
      qsizetype given = call(this, item, &handled);
      if (handled) return given;
    }
    return QQuickGraphsNode::addCustomItem(item);
  }

  //  void QQuickGraphsNode::removeCustomItems()
  void removeCustomItems() override {
    if (taken[9]) {
      int handled = 0;
      CuteQQuickGraphsBarsNodeCall9 call = reinterpret_cast<CuteQQuickGraphsBarsNodeCall9>(taken[9]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickGraphsNode::removeCustomItems();
  }

  //  void QQuickGraphsNode::removeCustomItem(QCustom3DItem *item)
  void removeCustomItem(QCustom3DItem *item) override {
    if (taken[10]) {
      int handled = 0;
      CuteQQuickGraphsBarsNodeCall10 call = reinterpret_cast<CuteQQuickGraphsBarsNodeCall10>(taken[10]);
      call(this, item, &handled);
      if (handled) return;
    }
    QQuickGraphsNode::removeCustomItem(item);
  }

  //  void QQuickGraphsNode::removeCustomItemAt(QVector3D position)
  void removeCustomItemAt(QVector3D position) override {
    if (taken[11]) {
      int handled = 0;
      CuteQQuickGraphsBarsNodeCall11 call = reinterpret_cast<CuteQQuickGraphsBarsNodeCall11>(taken[11]);
      call(this, &position, &handled);
      if (handled) return;
    }
    QQuickGraphsNode::removeCustomItemAt(position);
  }

  //  void QQuickGraphsNode::releaseCustomItem(QCustom3DItem *item)
  void releaseCustomItem(QCustom3DItem *item) override {
    if (taken[12]) {
      int handled = 0;
      CuteQQuickGraphsBarsNodeCall12 call = reinterpret_cast<CuteQQuickGraphsBarsNodeCall12>(taken[12]);
      call(this, item, &handled);
      if (handled) return;
    }
    QQuickGraphsNode::releaseCustomItem(item);
  }

  //  int QQuickGraphsNode::selectedLabelIndex() const
  int selectedLabelIndex() const override {
    if (taken[13]) {
      int handled = 0;
      CuteQQuickGraphsBarsNodeCall13 call = reinterpret_cast<CuteQQuickGraphsBarsNodeCall13>(taken[13]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return QQuickGraphsNode::selectedLabelIndex();
  }

  //  QAbstract3DAxis *QQuickGraphsNode::selectedAxis() const
  QAbstract3DAxis *selectedAxis() const override {
    if (taken[14]) {
      int handled = 0;
      CuteQQuickGraphsBarsNodeCall14 call = reinterpret_cast<CuteQQuickGraphsBarsNodeCall14>(taken[14]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QAbstract3DAxis *>(given);
    }
    return QQuickGraphsNode::selectedAxis();
  }

  //  qsizetype QQuickGraphsNode::selectedCustomItemIndex() const
  qsizetype selectedCustomItemIndex() const override {
    if (taken[15]) {
      int handled = 0;
      CuteQQuickGraphsBarsNodeCall15 call = reinterpret_cast<CuteQQuickGraphsBarsNodeCall15>(taken[15]);
      qsizetype given = call(this, &handled);
      if (handled) return given;
    }
    return QQuickGraphsNode::selectedCustomItemIndex();
  }

  //  QCustom3DItem *QQuickGraphsNode::selectedCustomItem() const
  QCustom3DItem *selectedCustomItem() const override {
    if (taken[16]) {
      int handled = 0;
      CuteQQuickGraphsBarsNodeCall16 call = reinterpret_cast<CuteQQuickGraphsBarsNodeCall16>(taken[16]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QCustom3DItem *>(given);
    }
    return QQuickGraphsNode::selectedCustomItem();
  }

  //  void QQuick3DNode::markAllDirty()
  void markAllDirty() override {
    if (taken[17]) {
      int handled = 0;
      CuteQQuickGraphsBarsNodeCall17 call = reinterpret_cast<CuteQQuickGraphsBarsNodeCall17>(taken[17]);
      call(this, &handled);
      if (handled) return;
    }
    QQuick3DNode::markAllDirty();
  }

#if !defined(QT_NO_QOBJECT)
  //  void QQuick3DNode::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[18]) {
      int handled = 0;
      CuteQQuickGraphsBarsNodeCall18 call = reinterpret_cast<CuteQQuickGraphsBarsNodeCall18>(taken[18]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QQuick3DNode::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QQuick3DNode::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[19]) {
      int handled = 0;
      CuteQQuickGraphsBarsNodeCall19 call = reinterpret_cast<CuteQQuickGraphsBarsNodeCall19>(taken[19]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QQuick3DNode::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

  //  QSSGRenderGraphObject
  //      *QQuick3DNode::updateSpatialNode(QSSGRenderGraphObject *node)
  QSSGRenderGraphObject *updateSpatialNode(
      QSSGRenderGraphObject *node) override {
    if (taken[20]) {
      int handled = 0;
      CuteQQuickGraphsBarsNodeCall20 call = reinterpret_cast<CuteQQuickGraphsBarsNodeCall20>(taken[20]);
      void * given = call(this, node, &handled);
      if (handled) return static_cast<QSSGRenderGraphObject *>(given);
    }
    return QQuick3DNode::updateSpatialNode(node);
  }

  //  void QQuick3DNode::itemChange(ItemChange a0, const ItemChangeData
  //      &a1)
  void itemChange(
      QQuick3DObject::ItemChange a0,
      const QQuick3DObject::ItemChangeData &a1) override {
    if (taken[21]) {
      int handled = 0;
      CuteQQuickGraphsBarsNodeCall21 call = reinterpret_cast<CuteQQuickGraphsBarsNodeCall21>(taken[21]);
      call(this, static_cast<int>(a0), &a1, &handled);
      if (handled) return;
    }
    QQuick3DNode::itemChange(a0, a1);
  }

  //  void QQuick3DObject::classBegin()
  void classBegin() override {
    if (taken[22]) {
      int handled = 0;
      CuteQQuickGraphsBarsNodeCall22 call = reinterpret_cast<CuteQQuickGraphsBarsNodeCall22>(taken[22]);
      call(this, &handled);
      if (handled) return;
    }
    QQuick3DObject::classBegin();
  }

  //  void QQuick3DObject::preSync()
  void preSync() override {
    if (taken[23]) {
      int handled = 0;
      CuteQQuickGraphsBarsNodeCall23 call = reinterpret_cast<CuteQQuickGraphsBarsNodeCall23>(taken[23]);
      call(this, &handled);
      if (handled) return;
    }
    QQuick3DObject::preSync();
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[24]) {
      int handled = 0;
      CuteQQuickGraphsBarsNodeCall24 call = reinterpret_cast<CuteQQuickGraphsBarsNodeCall24>(taken[24]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[25]) {
      int handled = 0;
      CuteQQuickGraphsBarsNodeCall25 call = reinterpret_cast<CuteQQuickGraphsBarsNodeCall25>(taken[25]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[26]) {
      int handled = 0;
      CuteQQuickGraphsBarsNodeCall26 call = reinterpret_cast<CuteQQuickGraphsBarsNodeCall26>(taken[26]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[27]) {
      int handled = 0;
      CuteQQuickGraphsBarsNodeCall27 call = reinterpret_cast<CuteQQuickGraphsBarsNodeCall27>(taken[27]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[28]) {
      int handled = 0;
      CuteQQuickGraphsBarsNodeCall28 call = reinterpret_cast<CuteQQuickGraphsBarsNodeCall28>(taken[28]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QQuickGraphsBarsNode::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK20QQuickGraphsBarsNode10metaObjectEv(
    const QQuickGraphsBarsNode *self) {
  return self->metaObject();
}

//  void *QQuickGraphsBarsNode::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN20QQuickGraphsBarsNode11qt_metacastEPKc(
    QQuickGraphsBarsNode *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QQuickGraphsBarsNode::qt_metacall(QMetaObject::Call a0, int a1, void
//      **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN20QQuickGraphsBarsNode11qt_metacallEN11QMetaObject4CallEiPPv(
    QQuickGraphsBarsNode *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QQuickGraphsBarsNode::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN20QQuickGraphsBarsNode2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuickGraphsBarsNode::tr(s, c, n));
}

//  QQuickGraphsBarsNode::QQuickGraphsBarsNode(QQuick3DNode *parent)
extern "C" Q_DECL_EXPORT
QQuickGraphsBarsNode *ritual_ZN20QQuickGraphsBarsNodeC1EP12QQuick3DNode(
    QQuick3DNode *parent) {
  return new CuteQQuickGraphsBarsNode(parent);
}

//  QQuickGraphsBarsNode::~QQuickGraphsBarsNode()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickGraphsBarsNodeD1Ev(QQuickGraphsBarsNode *self) {
  delete self;
}

//  void QQuickGraphsBarsNode::setRowAxis(QCategory3DAxis *axis)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickGraphsBarsNode10setRowAxisEP15QCategory3DAxis(
    QQuickGraphsBarsNode *self,
    QCategory3DAxis *axis) {
  self->setRowAxis(axis);
}

//  QCategory3DAxis *QQuickGraphsBarsNode::rowAxis() const
extern "C" Q_DECL_EXPORT
QCategory3DAxis *ritual_ZNK20QQuickGraphsBarsNode7rowAxisEv(
    const QQuickGraphsBarsNode *self) {
  return self->rowAxis();
}

//  void QQuickGraphsBarsNode::setValueAxis(QValue3DAxis *axis)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickGraphsBarsNode12setValueAxisEP12QValue3DAxis(
    QQuickGraphsBarsNode *self,
    QValue3DAxis *axis) {
  self->setValueAxis(axis);
}

//  QValue3DAxis *QQuickGraphsBarsNode::valueAxis() const
extern "C" Q_DECL_EXPORT
QValue3DAxis *ritual_ZNK20QQuickGraphsBarsNode9valueAxisEv(
    const QQuickGraphsBarsNode *self) {
  return self->valueAxis();
}

//  void QQuickGraphsBarsNode::setColumnAxis(QCategory3DAxis *axis)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickGraphsBarsNode13setColumnAxisEP15QCategory3DAxis(
    QQuickGraphsBarsNode *self,
    QCategory3DAxis *axis) {
  self->setColumnAxis(axis);
}

//  QCategory3DAxis *QQuickGraphsBarsNode::columnAxis() const
extern "C" Q_DECL_EXPORT
QCategory3DAxis *ritual_ZNK20QQuickGraphsBarsNode10columnAxisEv(
    const QQuickGraphsBarsNode *self) {
  return self->columnAxis();
}

//  void QQuickGraphsBarsNode::setMultiSeriesUniform(bool uniform)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickGraphsBarsNode21setMultiSeriesUniformEb(
    QQuickGraphsBarsNode *self,
    bool uniform) {
  self->setMultiSeriesUniform(uniform);
}

//  bool QQuickGraphsBarsNode::isMultiSeriesUniform() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK20QQuickGraphsBarsNode20isMultiSeriesUniformEv(
    const QQuickGraphsBarsNode *self) {
  return self->isMultiSeriesUniform();
}

//  void QQuickGraphsBarsNode::setBarThickness(float thickness)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickGraphsBarsNode15setBarThicknessEf(
    QQuickGraphsBarsNode *self,
    float thickness) {
  self->setBarThickness(thickness);
}

//  float QQuickGraphsBarsNode::barThickness() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK20QQuickGraphsBarsNode12barThicknessEv(
    const QQuickGraphsBarsNode *self) {
  return self->barThickness();
}

//  void QQuickGraphsBarsNode::setBarSpacing(QSizeF spacing)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickGraphsBarsNode13setBarSpacingE6QSizeF(
    QQuickGraphsBarsNode *self,
    const QSizeF *spacing) {
  self->setBarSpacing(*spacing);
}

//  QSizeF QQuickGraphsBarsNode::barSpacing() const
extern "C" Q_DECL_EXPORT
QSizeF *ritual_ZNK20QQuickGraphsBarsNode10barSpacingEv(
    const QQuickGraphsBarsNode *self) {
  return new QSizeF(self->barSpacing());
}

//  void QQuickGraphsBarsNode::setBarSpacingRelative(bool relative)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickGraphsBarsNode21setBarSpacingRelativeEb(
    QQuickGraphsBarsNode *self,
    bool relative) {
  self->setBarSpacingRelative(relative);
}

//  bool QQuickGraphsBarsNode::isBarSpacingRelative() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK20QQuickGraphsBarsNode20isBarSpacingRelativeEv(
    const QQuickGraphsBarsNode *self) {
  return self->isBarSpacingRelative();
}

//  void QQuickGraphsBarsNode::setBarSeriesMargin(QSizeF margin)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickGraphsBarsNode18setBarSeriesMarginE6QSizeF(
    QQuickGraphsBarsNode *self,
    const QSizeF *margin) {
  self->setBarSeriesMargin(*margin);
}

//  QSizeF QQuickGraphsBarsNode::barSeriesMargin() const
extern "C" Q_DECL_EXPORT
QSizeF *ritual_ZNK20QQuickGraphsBarsNode15barSeriesMarginEv(
    const QQuickGraphsBarsNode *self) {
  return new QSizeF(self->barSeriesMargin());
}

//  QBar3DSeries *QQuickGraphsBarsNode::selectedSeries() const
extern "C" Q_DECL_EXPORT
QBar3DSeries *ritual_ZNK20QQuickGraphsBarsNode14selectedSeriesEv(
    const QQuickGraphsBarsNode *self) {
  return self->selectedSeries();
}

//  void QQuickGraphsBarsNode::setPrimarySeries(QBar3DSeries *series)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickGraphsBarsNode16setPrimarySeriesEP12QBar3DSeries(
    QQuickGraphsBarsNode *self,
    QBar3DSeries *series) {
  self->setPrimarySeries(series);
}

//  QBar3DSeries *QQuickGraphsBarsNode::primarySeries() const
extern "C" Q_DECL_EXPORT
QBar3DSeries *ritual_ZNK20QQuickGraphsBarsNode13primarySeriesEv(
    const QQuickGraphsBarsNode *self) {
  return self->primarySeries();
}

//  void QQuickGraphsBarsNode::setFloorLevel(float floorLevel)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickGraphsBarsNode13setFloorLevelEf(
    QQuickGraphsBarsNode *self,
    float floorLevel) {
  self->setFloorLevel(floorLevel);
}

//  float QQuickGraphsBarsNode::floorLevel() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK20QQuickGraphsBarsNode10floorLevelEv(
    const QQuickGraphsBarsNode *self) {
  return self->floorLevel();
}

//  QList<QBar3DSeries *> QQuickGraphsBarsNode::barSeriesList()
extern "C" Q_DECL_EXPORT
QList<QBar3DSeries *> *ritual_ZN20QQuickGraphsBarsNode13barSeriesListEv(
    QQuickGraphsBarsNode *self) {
  return new QList<QBar3DSeries *>(self->barSeriesList());
}

//  QQmlListProperty<QBar3DSeries> QQuickGraphsBarsNode::seriesList()
extern "C" Q_DECL_EXPORT
QQmlListProperty<QBar3DSeries> *ritual_ZN20QQuickGraphsBarsNode10seriesListEv(
    QQuickGraphsBarsNode *self) {
  return new QQmlListProperty<QBar3DSeries>(self->seriesList());
}

//  void
//      QQuickGraphsBarsNode::appendSeriesFunc(QQmlListProperty<QBar3DSeries>
//      *list, QBar3DSeries *series)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickGraphsBarsNode16appendSeriesFuncEP16QQmlListPropertyI12QBar3DSeriesEPS1_(
    QQmlListProperty<QBar3DSeries> *list,
    QBar3DSeries *series) {
  QQuickGraphsBarsNode::appendSeriesFunc(list, series);
}

//  qsizetype
//      QQuickGraphsBarsNode::countSeriesFunc(QQmlListProperty<QBar3DSeries>
//      *list)
extern "C" Q_DECL_EXPORT
qsizetype ritual_ZN20QQuickGraphsBarsNode15countSeriesFuncEP16QQmlListPropertyI12QBar3DSeriesE(
    QQmlListProperty<QBar3DSeries> *list) {
  return QQuickGraphsBarsNode::countSeriesFunc(list);
}

//  QBar3DSeries
//      *QQuickGraphsBarsNode::atSeriesFunc(QQmlListProperty<QBar3DSeries>
//      *list, qsizetype index)
extern "C" Q_DECL_EXPORT
QBar3DSeries *ritual_ZN20QQuickGraphsBarsNode12atSeriesFuncEP16QQmlListPropertyI12QBar3DSeriesEx(
    QQmlListProperty<QBar3DSeries> *list,
    qsizetype index) {
  return QQuickGraphsBarsNode::atSeriesFunc(list, index);
}

//  void QQuickGraphsBarsNode::clearSeriesFunc(QQmlListProperty<QBar3DSeries>
//      *list)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickGraphsBarsNode15clearSeriesFuncEP16QQmlListPropertyI12QBar3DSeriesE(
    QQmlListProperty<QBar3DSeries> *list) {
  QQuickGraphsBarsNode::clearSeriesFunc(list);
}

//  void QQuickGraphsBarsNode::addSeries(QBar3DSeries *series)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickGraphsBarsNode9addSeriesEP12QBar3DSeries(
    QQuickGraphsBarsNode *self,
    QBar3DSeries *series) {
  self->addSeries(series);
}

//  void QQuickGraphsBarsNode::removeSeries(QBar3DSeries *series)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickGraphsBarsNode12removeSeriesEP12QBar3DSeries(
    QQuickGraphsBarsNode *self,
    QBar3DSeries *series) {
  self->removeSeries(series);
}

//  void QQuickGraphsBarsNode::insertSeries(qsizetype index, QBar3DSeries
//      *series)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickGraphsBarsNode12insertSeriesExP12QBar3DSeries(
    QQuickGraphsBarsNode *self,
    qsizetype index,
    QBar3DSeries *series) {
  self->insertSeries(index, series);
}

//  void QQuickGraphsBarsNode::clearSelection()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickGraphsBarsNode14clearSelectionEv(
    QQuickGraphsBarsNode *self) {
  self->clearSelection();
}

//  bool QQuickGraphsBarsNode::doPicking(QPointF point)
extern "C" Q_DECL_EXPORT
bool ritual_ZN20QQuickGraphsBarsNode9doPickingE7QPointF(
    QQuickGraphsBarsNode *self,
    const QPointF *point) {
  return self->doPicking(*point);
}

//  bool QQuickGraphsBarsNode::doRayPicking(const QVector3D &origin, const
//      QVector3D &direction)
extern "C" Q_DECL_EXPORT
bool ritual_ZN20QQuickGraphsBarsNode12doRayPickingERK9QVector3DS2_(
    QQuickGraphsBarsNode *self,
    const QVector3D *origin,
    const QVector3D *direction) {
  return self->doRayPicking(*origin, *direction);
}

//  void QQuickGraphsBarsNode::componentComplete()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickGraphsBarsNode17componentCompleteEv(
    QQuickGraphsBarsNode *self) {
  self->componentComplete();
}

//  void QQuickGraphsBarsNode::rowAxisChanged(QCategory3DAxis *axis)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickGraphsBarsNode14rowAxisChangedEP15QCategory3DAxis(
    QQuickGraphsBarsNode *self,
    QCategory3DAxis *axis) {
  self->rowAxisChanged(axis);
}

//  void QQuickGraphsBarsNode::valueAxisChanged(QValue3DAxis *axis)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickGraphsBarsNode16valueAxisChangedEP12QValue3DAxis(
    QQuickGraphsBarsNode *self,
    QValue3DAxis *axis) {
  self->valueAxisChanged(axis);
}

//  void QQuickGraphsBarsNode::columnAxisChanged(QCategory3DAxis *axis)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickGraphsBarsNode17columnAxisChangedEP15QCategory3DAxis(
    QQuickGraphsBarsNode *self,
    QCategory3DAxis *axis) {
  self->columnAxisChanged(axis);
}

//  void QQuickGraphsBarsNode::multiSeriesUniformChanged(bool uniform)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickGraphsBarsNode25multiSeriesUniformChangedEb(
    QQuickGraphsBarsNode *self,
    bool uniform) {
  self->multiSeriesUniformChanged(uniform);
}

//  void QQuickGraphsBarsNode::barThicknessChanged(float thicknessRatio)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickGraphsBarsNode19barThicknessChangedEf(
    QQuickGraphsBarsNode *self,
    float thicknessRatio) {
  self->barThicknessChanged(thicknessRatio);
}

//  void QQuickGraphsBarsNode::barSpacingChanged(QSizeF spacing)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickGraphsBarsNode17barSpacingChangedE6QSizeF(
    QQuickGraphsBarsNode *self,
    const QSizeF *spacing) {
  self->barSpacingChanged(*spacing);
}

//  void QQuickGraphsBarsNode::barSpacingRelativeChanged(bool relative)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickGraphsBarsNode25barSpacingRelativeChangedEb(
    QQuickGraphsBarsNode *self,
    bool relative) {
  self->barSpacingRelativeChanged(relative);
}

//  void QQuickGraphsBarsNode::barSeriesMarginChanged(QSizeF margin)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickGraphsBarsNode22barSeriesMarginChangedE6QSizeF(
    QQuickGraphsBarsNode *self,
    const QSizeF *margin) {
  self->barSeriesMarginChanged(*margin);
}

//  void QQuickGraphsBarsNode::primarySeriesChanged(QBar3DSeries *series)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickGraphsBarsNode20primarySeriesChangedEP12QBar3DSeries(
    QQuickGraphsBarsNode *self,
    QBar3DSeries *series) {
  self->primarySeriesChanged(series);
}

//  void QQuickGraphsBarsNode::selectedSeriesChanged(QBar3DSeries *series)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickGraphsBarsNode21selectedSeriesChangedEP12QBar3DSeries(
    QQuickGraphsBarsNode *self,
    QBar3DSeries *series) {
  self->selectedSeriesChanged(series);
}

//  void QQuickGraphsBarsNode::floorLevelChanged(float level)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickGraphsBarsNode17floorLevelChangedEf(
    QQuickGraphsBarsNode *self,
    float level) {
  self->floorLevelChanged(level);
}

//  QQuickGraphsBars *QQuickGraphsBarsNode::graphBars()
extern "C" Q_DECL_EXPORT
QQuickGraphsBars *ritual_ZN20QQuickGraphsBarsNode9graphBarsEv(
    QQuickGraphsBarsNode *self) {
  return self->graphBars();
}

//  const QQuickGraphsBars *QQuickGraphsBarsNode::graphBars() const
extern "C" Q_DECL_EXPORT
const QQuickGraphsBars *ritual_ZNK20QQuickGraphsBarsNode9graphBarsEv(
    const QQuickGraphsBarsNode *self) {
  return self->graphBars();
}

//  a Python function taken by a CuteQQuickGraphsBarsNode, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQuickGraphsBarsNode(
    QQuickGraphsBarsNode *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQuickGraphsBarsNode *>(self)->take(key, call);
}

//  void QQuickGraphsBarsNode::clearSelection()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN20QQuickGraphsBarsNode14clearSelectionEv(
    QQuickGraphsBarsNode *self) {
  self->QQuickGraphsBarsNode::clearSelection();
}

//  bool QQuickGraphsBarsNode::doPicking(QPointF point)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN20QQuickGraphsBarsNode9doPickingE7QPointF(
    QQuickGraphsBarsNode *self,
    const QPointF *point) {
  return self->QQuickGraphsBarsNode::doPicking(*point);
}

//  bool QQuickGraphsBarsNode::doRayPicking(const QVector3D &origin, const
//      QVector3D &direction)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN20QQuickGraphsBarsNode12doRayPickingERK9QVector3DS2_(
    QQuickGraphsBarsNode *self,
    const QVector3D *origin,
    const QVector3D *direction) {
  return self->QQuickGraphsBarsNode::doRayPicking(*origin, *direction);
}

//  void QQuickGraphsBarsNode::componentComplete()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN20QQuickGraphsBarsNode17componentCompleteEv(
    QQuickGraphsBarsNode *self) {
  static_cast<OwnQQuickGraphsBarsNode *>(self)->OwnQQuickGraphsBarsNode::componentComplete();
}

//  a QQmlListProperty<QBar3DSeries> a ritual of QQuickGraphsBarsNode gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QQuickGraphsBarsNode__QQmlListProperty_QBar3DSeries(
    QQmlListProperty<QBar3DSeries> *self) {
  delete self;
}

#endif  // (QT_CONFIG(graphs_3d)) && (!(!QT_CONFIG(graphs_3d_bars3d) && !QT_CONFIG(graphs_3d_scatter3d) && !QT_CONFIG(graphs_3d_surface3d))) && (QT_CONFIG(graphs_3d_bars3d))
