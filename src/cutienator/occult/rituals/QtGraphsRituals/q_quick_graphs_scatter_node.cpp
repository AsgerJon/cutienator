//  Written by dev_tooling.RitualGenerator from the records of
//  QtGraphs/6.12.0/QtGraphs/private/qquickgraphsscatternode_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtGraphs/qgraphsglobal.h>
#include <QtGraphs/6.12.0/QtGraphs/private/qgraphsglobal_p.h>
#if (QT_CONFIG(graphs_3d)) && (!(!QT_CONFIG(graphs_3d_bars3d) && !QT_CONFIG(graphs_3d_scatter3d) && !QT_CONFIG(graphs_3d_surface3d))) && (QT_CONFIG(graphs_3d_scatter3d))
#include <QtGraphs/6.12.0/QtGraphs/private/qgraphsglobal_p.h>
#include <QtGraphs/QtGraphs>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGraphs/6.12.0/QtGraphs/private/qquickgraphsscatternode_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#if (QT_CONFIG(graphs_3d)) && (!(!QT_CONFIG(graphs_3d_bars3d) && !QT_CONFIG(graphs_3d_scatter3d) && !QT_CONFIG(graphs_3d_surface3d))) && (QT_CONFIG(graphs_3d_scatter3d))
#include <QtGraphs/QtGraphs>
#include <QtGraphs/qscatter3dseries.h>
#endif
#include <QtCore/qpoint.h>
#include <QtGui/qvectornd.h>
#include <QtCore/qmetaobject.h>
#include <QtQuick3D/qquick3dobject.h>
#include <QtCore/qlist.h>
#include <cstring>
#include <QtQml/QQmlListProperty>
#include <QtGraphs/QScatter3DSeries>

//  Only a class built on QQuickGraphsScatterNode may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQQuickGraphsScatterNode : QQuickGraphsScatterNode {
  using QQuickGraphsScatterNode::componentComplete;
};

//  A QQuickGraphsScatterNode that Python can take functions over in. Every QQuickGraphsScatterNode
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQQuickGraphsScatterNodeCall0)(const void *, int, int *);
typedef void (*CuteQQuickGraphsScatterNodeCall1)(const void *, int *);
typedef bool (*CuteQQuickGraphsScatterNodeCall2)(const void *, const QPointF *, int *);
typedef bool (*CuteQQuickGraphsScatterNodeCall3)(const void *, const QVector3D *, const QVector3D *, int *);
typedef void (*CuteQQuickGraphsScatterNodeCall4)(const void *, int *);
typedef bool (*CuteQQuickGraphsScatterNodeCall5)(const void *, QAbstract3DSeries *, int *);
typedef void (*CuteQQuickGraphsScatterNodeCall6)(const void *, QAbstract3DSeries *, int *);
typedef void (*CuteQQuickGraphsScatterNodeCall7)(const void *, QAbstract3DSeries *, int *);
typedef qsizetype (*CuteQQuickGraphsScatterNodeCall8)(const void *, QCustom3DItem *, int *);
typedef void (*CuteQQuickGraphsScatterNodeCall9)(const void *, int *);
typedef void (*CuteQQuickGraphsScatterNodeCall10)(const void *, QCustom3DItem *, int *);
typedef void (*CuteQQuickGraphsScatterNodeCall11)(const void *, const QVector3D *, int *);
typedef void (*CuteQQuickGraphsScatterNodeCall12)(const void *, QCustom3DItem *, int *);
typedef int (*CuteQQuickGraphsScatterNodeCall13)(const void *, int *);
typedef void * (*CuteQQuickGraphsScatterNodeCall14)(const void *, int *);
typedef qsizetype (*CuteQQuickGraphsScatterNodeCall15)(const void *, int *);
typedef void * (*CuteQQuickGraphsScatterNodeCall16)(const void *, int *);
typedef void (*CuteQQuickGraphsScatterNodeCall17)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickGraphsScatterNodeCall18)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickGraphsScatterNodeCall19)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
typedef void * (*CuteQQuickGraphsScatterNodeCall20)(const void *, QSSGRenderGraphObject *, int *);
typedef void (*CuteQQuickGraphsScatterNodeCall21)(const void *, int, const QQuick3DObject::ItemChangeData *, int *);
typedef void (*CuteQQuickGraphsScatterNodeCall22)(const void *, int *);
typedef void (*CuteQQuickGraphsScatterNodeCall23)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickGraphsScatterNodeCall24)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickGraphsScatterNodeCall25)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickGraphsScatterNodeCall26)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickGraphsScatterNodeCall27)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickGraphsScatterNodeCall28)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQQuickGraphsScatterNode : public QQuickGraphsScatterNode {
public:
  using QQuickGraphsScatterNode::QQuickGraphsScatterNode;
  void *taken[29] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN16QQuickGraphsNode16setSelectionModeE6QFlagsIN10QtGraphs3D13SelectionFlagEE")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQuickGraphsNode14clearSelectionEv")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQuickGraphsNode9doPickingE7QPointF")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQuickGraphsNode12doRayPickingERK9QVector3DS2_")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQmlParserStatus17componentCompleteEv")) {
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

  //  void
  //      QQuickGraphsScatterNode::setSelectionMode(QtGraphs3D::SelectionFl
  //      ags mode)
  void setSelectionMode(QtGraphs3D::SelectionFlags mode) override {
    if (taken[0]) {
      int handled = 0;
      CuteQQuickGraphsScatterNodeCall0 call = reinterpret_cast<CuteQQuickGraphsScatterNodeCall0>(taken[0]);
      call(this, static_cast<int>(mode.toInt()), &handled);
      if (handled) return;
    }
    QQuickGraphsScatterNode::setSelectionMode(mode);
  }

  //  void QQuickGraphsScatterNode::clearSelection()
  void clearSelection() override {
    if (taken[1]) {
      int handled = 0;
      CuteQQuickGraphsScatterNodeCall1 call = reinterpret_cast<CuteQQuickGraphsScatterNodeCall1>(taken[1]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickGraphsScatterNode::clearSelection();
  }

  //  bool QQuickGraphsScatterNode::doPicking(QPointF point)
  bool doPicking(QPointF point) override {
    if (taken[2]) {
      int handled = 0;
      CuteQQuickGraphsScatterNodeCall2 call = reinterpret_cast<CuteQQuickGraphsScatterNodeCall2>(taken[2]);
      bool given = call(this, &point, &handled);
      if (handled) return given;
    }
    return QQuickGraphsScatterNode::doPicking(point);
  }

  //  bool QQuickGraphsScatterNode::doRayPicking(const QVector3D &origin,
  //      const QVector3D &direction)
  bool doRayPicking(
      const QVector3D &origin,
      const QVector3D &direction) override {
    if (taken[3]) {
      int handled = 0;
      CuteQQuickGraphsScatterNodeCall3 call = reinterpret_cast<CuteQQuickGraphsScatterNodeCall3>(taken[3]);
      bool given = call(this, &origin, &direction, &handled);
      if (handled) return given;
    }
    return QQuickGraphsScatterNode::doRayPicking(origin, direction);
  }

  //  void QQuickGraphsScatterNode::componentComplete()
  void componentComplete() override {
    if (taken[4]) {
      int handled = 0;
      CuteQQuickGraphsScatterNodeCall4 call = reinterpret_cast<CuteQQuickGraphsScatterNodeCall4>(taken[4]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickGraphsScatterNode::componentComplete();
  }

  //  bool QQuickGraphsNode::hasSeries(QAbstract3DSeries *series)
  bool hasSeries(QAbstract3DSeries *series) override {
    if (taken[5]) {
      int handled = 0;
      CuteQQuickGraphsScatterNodeCall5 call = reinterpret_cast<CuteQQuickGraphsScatterNodeCall5>(taken[5]);
      bool given = call(this, series, &handled);
      if (handled) return given;
    }
    return QQuickGraphsNode::hasSeries(series);
  }

  //  void QQuickGraphsNode::addSeriesInternal(QAbstract3DSeries *series)
  void addSeriesInternal(QAbstract3DSeries *series) override {
    if (taken[6]) {
      int handled = 0;
      CuteQQuickGraphsScatterNodeCall6 call = reinterpret_cast<CuteQQuickGraphsScatterNodeCall6>(taken[6]);
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
      CuteQQuickGraphsScatterNodeCall7 call = reinterpret_cast<CuteQQuickGraphsScatterNodeCall7>(taken[7]);
      call(this, series, &handled);
      if (handled) return;
    }
    QQuickGraphsNode::removeSeriesInternal(series);
  }

  //  qsizetype QQuickGraphsNode::addCustomItem(QCustom3DItem *item)
  qsizetype addCustomItem(QCustom3DItem *item) override {
    if (taken[8]) {
      int handled = 0;
      CuteQQuickGraphsScatterNodeCall8 call = reinterpret_cast<CuteQQuickGraphsScatterNodeCall8>(taken[8]);
      qsizetype given = call(this, item, &handled);
      if (handled) return given;
    }
    return QQuickGraphsNode::addCustomItem(item);
  }

  //  void QQuickGraphsNode::removeCustomItems()
  void removeCustomItems() override {
    if (taken[9]) {
      int handled = 0;
      CuteQQuickGraphsScatterNodeCall9 call = reinterpret_cast<CuteQQuickGraphsScatterNodeCall9>(taken[9]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickGraphsNode::removeCustomItems();
  }

  //  void QQuickGraphsNode::removeCustomItem(QCustom3DItem *item)
  void removeCustomItem(QCustom3DItem *item) override {
    if (taken[10]) {
      int handled = 0;
      CuteQQuickGraphsScatterNodeCall10 call = reinterpret_cast<CuteQQuickGraphsScatterNodeCall10>(taken[10]);
      call(this, item, &handled);
      if (handled) return;
    }
    QQuickGraphsNode::removeCustomItem(item);
  }

  //  void QQuickGraphsNode::removeCustomItemAt(QVector3D position)
  void removeCustomItemAt(QVector3D position) override {
    if (taken[11]) {
      int handled = 0;
      CuteQQuickGraphsScatterNodeCall11 call = reinterpret_cast<CuteQQuickGraphsScatterNodeCall11>(taken[11]);
      call(this, &position, &handled);
      if (handled) return;
    }
    QQuickGraphsNode::removeCustomItemAt(position);
  }

  //  void QQuickGraphsNode::releaseCustomItem(QCustom3DItem *item)
  void releaseCustomItem(QCustom3DItem *item) override {
    if (taken[12]) {
      int handled = 0;
      CuteQQuickGraphsScatterNodeCall12 call = reinterpret_cast<CuteQQuickGraphsScatterNodeCall12>(taken[12]);
      call(this, item, &handled);
      if (handled) return;
    }
    QQuickGraphsNode::releaseCustomItem(item);
  }

  //  int QQuickGraphsNode::selectedLabelIndex() const
  int selectedLabelIndex() const override {
    if (taken[13]) {
      int handled = 0;
      CuteQQuickGraphsScatterNodeCall13 call = reinterpret_cast<CuteQQuickGraphsScatterNodeCall13>(taken[13]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return QQuickGraphsNode::selectedLabelIndex();
  }

  //  QAbstract3DAxis *QQuickGraphsNode::selectedAxis() const
  QAbstract3DAxis *selectedAxis() const override {
    if (taken[14]) {
      int handled = 0;
      CuteQQuickGraphsScatterNodeCall14 call = reinterpret_cast<CuteQQuickGraphsScatterNodeCall14>(taken[14]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QAbstract3DAxis *>(given);
    }
    return QQuickGraphsNode::selectedAxis();
  }

  //  qsizetype QQuickGraphsNode::selectedCustomItemIndex() const
  qsizetype selectedCustomItemIndex() const override {
    if (taken[15]) {
      int handled = 0;
      CuteQQuickGraphsScatterNodeCall15 call = reinterpret_cast<CuteQQuickGraphsScatterNodeCall15>(taken[15]);
      qsizetype given = call(this, &handled);
      if (handled) return given;
    }
    return QQuickGraphsNode::selectedCustomItemIndex();
  }

  //  QCustom3DItem *QQuickGraphsNode::selectedCustomItem() const
  QCustom3DItem *selectedCustomItem() const override {
    if (taken[16]) {
      int handled = 0;
      CuteQQuickGraphsScatterNodeCall16 call = reinterpret_cast<CuteQQuickGraphsScatterNodeCall16>(taken[16]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QCustom3DItem *>(given);
    }
    return QQuickGraphsNode::selectedCustomItem();
  }

  //  void QQuick3DNode::markAllDirty()
  void markAllDirty() override {
    if (taken[17]) {
      int handled = 0;
      CuteQQuickGraphsScatterNodeCall17 call = reinterpret_cast<CuteQQuickGraphsScatterNodeCall17>(taken[17]);
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
      CuteQQuickGraphsScatterNodeCall18 call = reinterpret_cast<CuteQQuickGraphsScatterNodeCall18>(taken[18]);
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
      CuteQQuickGraphsScatterNodeCall19 call = reinterpret_cast<CuteQQuickGraphsScatterNodeCall19>(taken[19]);
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
      CuteQQuickGraphsScatterNodeCall20 call = reinterpret_cast<CuteQQuickGraphsScatterNodeCall20>(taken[20]);
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
      CuteQQuickGraphsScatterNodeCall21 call = reinterpret_cast<CuteQQuickGraphsScatterNodeCall21>(taken[21]);
      call(this, static_cast<int>(a0), &a1, &handled);
      if (handled) return;
    }
    QQuick3DNode::itemChange(a0, a1);
  }

  //  void QQuick3DObject::classBegin()
  void classBegin() override {
    if (taken[22]) {
      int handled = 0;
      CuteQQuickGraphsScatterNodeCall22 call = reinterpret_cast<CuteQQuickGraphsScatterNodeCall22>(taken[22]);
      call(this, &handled);
      if (handled) return;
    }
    QQuick3DObject::classBegin();
  }

  //  void QQuick3DObject::preSync()
  void preSync() override {
    if (taken[23]) {
      int handled = 0;
      CuteQQuickGraphsScatterNodeCall23 call = reinterpret_cast<CuteQQuickGraphsScatterNodeCall23>(taken[23]);
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
      CuteQQuickGraphsScatterNodeCall24 call = reinterpret_cast<CuteQQuickGraphsScatterNodeCall24>(taken[24]);
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
      CuteQQuickGraphsScatterNodeCall25 call = reinterpret_cast<CuteQQuickGraphsScatterNodeCall25>(taken[25]);
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
      CuteQQuickGraphsScatterNodeCall26 call = reinterpret_cast<CuteQQuickGraphsScatterNodeCall26>(taken[26]);
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
      CuteQQuickGraphsScatterNodeCall27 call = reinterpret_cast<CuteQQuickGraphsScatterNodeCall27>(taken[27]);
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
      CuteQQuickGraphsScatterNodeCall28 call = reinterpret_cast<CuteQQuickGraphsScatterNodeCall28>(taken[28]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QQuickGraphsScatterNode::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK23QQuickGraphsScatterNode10metaObjectEv(
    const QQuickGraphsScatterNode *self) {
  return self->metaObject();
}

//  void *QQuickGraphsScatterNode::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN23QQuickGraphsScatterNode11qt_metacastEPKc(
    QQuickGraphsScatterNode *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QQuickGraphsScatterNode::qt_metacall(QMetaObject::Call a0, int a1,
//      void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN23QQuickGraphsScatterNode11qt_metacallEN11QMetaObject4CallEiPPv(
    QQuickGraphsScatterNode *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QQuickGraphsScatterNode::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN23QQuickGraphsScatterNode2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuickGraphsScatterNode::tr(s, c, n));
}

//  QQuickGraphsScatterNode::QQuickGraphsScatterNode(QQuick3DNode *parent)
extern "C" Q_DECL_EXPORT
QQuickGraphsScatterNode *ritual_ZN23QQuickGraphsScatterNodeC1EP12QQuick3DNode(
    QQuick3DNode *parent) {
  return new CuteQQuickGraphsScatterNode(parent);
}

//  QQuickGraphsScatterNode::~QQuickGraphsScatterNode()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuickGraphsScatterNodeD1Ev(QQuickGraphsScatterNode *self) {
  delete self;
}

//  QValue3DAxis *QQuickGraphsScatterNode::axisX() const
extern "C" Q_DECL_EXPORT
QValue3DAxis *ritual_ZNK23QQuickGraphsScatterNode5axisXEv(
    const QQuickGraphsScatterNode *self) {
  return self->axisX();
}

//  void QQuickGraphsScatterNode::setAxisX(QValue3DAxis *axis)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuickGraphsScatterNode8setAxisXEP12QValue3DAxis(
    QQuickGraphsScatterNode *self,
    QValue3DAxis *axis) {
  self->setAxisX(axis);
}

//  QValue3DAxis *QQuickGraphsScatterNode::axisY() const
extern "C" Q_DECL_EXPORT
QValue3DAxis *ritual_ZNK23QQuickGraphsScatterNode5axisYEv(
    const QQuickGraphsScatterNode *self) {
  return self->axisY();
}

//  void QQuickGraphsScatterNode::setAxisY(QValue3DAxis *axis)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuickGraphsScatterNode8setAxisYEP12QValue3DAxis(
    QQuickGraphsScatterNode *self,
    QValue3DAxis *axis) {
  self->setAxisY(axis);
}

//  QValue3DAxis *QQuickGraphsScatterNode::axisZ() const
extern "C" Q_DECL_EXPORT
QValue3DAxis *ritual_ZNK23QQuickGraphsScatterNode5axisZEv(
    const QQuickGraphsScatterNode *self) {
  return self->axisZ();
}

//  void QQuickGraphsScatterNode::setAxisZ(QValue3DAxis *axis)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuickGraphsScatterNode8setAxisZEP12QValue3DAxis(
    QQuickGraphsScatterNode *self,
    QValue3DAxis *axis) {
  self->setAxisZ(axis);
}

//  QScatter3DSeries *QQuickGraphsScatterNode::selectedSeries() const
extern "C" Q_DECL_EXPORT
QScatter3DSeries *ritual_ZNK23QQuickGraphsScatterNode14selectedSeriesEv(
    const QQuickGraphsScatterNode *self) {
  return self->selectedSeries();
}

//  void QQuickGraphsScatterNode::setSelectionMode(QtGraphs3D::SelectionFlags
//      mode)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuickGraphsScatterNode16setSelectionModeE6QFlagsIN10QtGraphs3D13SelectionFlagEE(
    QQuickGraphsScatterNode *self,
    int mode) {
  self->setSelectionMode(QFlags<QtGraphs3D::SelectionFlag>::fromInt(mode));
}

//  QList<QScatter3DSeries *> QQuickGraphsScatterNode::scatterSeriesList()
extern "C" Q_DECL_EXPORT
QList<QScatter3DSeries *> *ritual_ZN23QQuickGraphsScatterNode17scatterSeriesListEv(
    QQuickGraphsScatterNode *self) {
  return new QList<QScatter3DSeries *>(self->scatterSeriesList());
}

//  QQmlListProperty<QScatter3DSeries> QQuickGraphsScatterNode::seriesList()
extern "C" Q_DECL_EXPORT
QQmlListProperty<QScatter3DSeries> *ritual_ZN23QQuickGraphsScatterNode10seriesListEv(
    QQuickGraphsScatterNode *self) {
  return new QQmlListProperty<QScatter3DSeries>(self->seriesList());
}

//  void QQuickGraphsScatterNode::appendSeriesFunc(QQmlListProperty<QScatter3
//      DSeries> *list, QScatter3DSeries *series)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuickGraphsScatterNode16appendSeriesFuncEP16QQmlListPropertyI16QScatter3DSeriesEPS1_(
    QQmlListProperty<QScatter3DSeries> *list,
    QScatter3DSeries *series) {
  QQuickGraphsScatterNode::appendSeriesFunc(list, series);
}

//  qsizetype QQuickGraphsScatterNode::countSeriesFunc(QQmlListProperty<QScat
//      ter3DSeries> *list)
extern "C" Q_DECL_EXPORT
qsizetype ritual_ZN23QQuickGraphsScatterNode15countSeriesFuncEP16QQmlListPropertyI16QScatter3DSeriesE(
    QQmlListProperty<QScatter3DSeries> *list) {
  return QQuickGraphsScatterNode::countSeriesFunc(list);
}

//  QScatter3DSeries
//      *QQuickGraphsScatterNode::atSeriesFunc(QQmlListProperty<QScatter3DSer
//      ies> *list, qsizetype index)
extern "C" Q_DECL_EXPORT
QScatter3DSeries *ritual_ZN23QQuickGraphsScatterNode12atSeriesFuncEP16QQmlListPropertyI16QScatter3DSeriesEx(
    QQmlListProperty<QScatter3DSeries> *list,
    qsizetype index) {
  return QQuickGraphsScatterNode::atSeriesFunc(list, index);
}

//  void QQuickGraphsScatterNode::clearSeriesFunc(QQmlListProperty<QScatter3D
//      Series> *list)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuickGraphsScatterNode15clearSeriesFuncEP16QQmlListPropertyI16QScatter3DSeriesE(
    QQmlListProperty<QScatter3DSeries> *list) {
  QQuickGraphsScatterNode::clearSeriesFunc(list);
}

//  void QQuickGraphsScatterNode::addSeries(QScatter3DSeries *series)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuickGraphsScatterNode9addSeriesEP16QScatter3DSeries(
    QQuickGraphsScatterNode *self,
    QScatter3DSeries *series) {
  self->addSeries(series);
}

//  void QQuickGraphsScatterNode::removeSeries(QScatter3DSeries *series)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuickGraphsScatterNode12removeSeriesEP16QScatter3DSeries(
    QQuickGraphsScatterNode *self,
    QScatter3DSeries *series) {
  self->removeSeries(series);
}

//  void QQuickGraphsScatterNode::clearSelection()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuickGraphsScatterNode14clearSelectionEv(
    QQuickGraphsScatterNode *self) {
  self->clearSelection();
}

//  bool QQuickGraphsScatterNode::doPicking(QPointF point)
extern "C" Q_DECL_EXPORT
bool ritual_ZN23QQuickGraphsScatterNode9doPickingE7QPointF(
    QQuickGraphsScatterNode *self,
    const QPointF *point) {
  return self->doPicking(*point);
}

//  bool QQuickGraphsScatterNode::doRayPicking(const QVector3D &origin, const
//      QVector3D &direction)
extern "C" Q_DECL_EXPORT
bool ritual_ZN23QQuickGraphsScatterNode12doRayPickingERK9QVector3DS2_(
    QQuickGraphsScatterNode *self,
    const QVector3D *origin,
    const QVector3D *direction) {
  return self->doRayPicking(*origin, *direction);
}

//  void QQuickGraphsScatterNode::componentComplete()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuickGraphsScatterNode17componentCompleteEv(
    QQuickGraphsScatterNode *self) {
  self->componentComplete();
}

//  void QQuickGraphsScatterNode::axisXChanged(QValue3DAxis *axis)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuickGraphsScatterNode12axisXChangedEP12QValue3DAxis(
    QQuickGraphsScatterNode *self,
    QValue3DAxis *axis) {
  self->axisXChanged(axis);
}

//  void QQuickGraphsScatterNode::axisYChanged(QValue3DAxis *axis)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuickGraphsScatterNode12axisYChangedEP12QValue3DAxis(
    QQuickGraphsScatterNode *self,
    QValue3DAxis *axis) {
  self->axisYChanged(axis);
}

//  void QQuickGraphsScatterNode::axisZChanged(QValue3DAxis *axis)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuickGraphsScatterNode12axisZChangedEP12QValue3DAxis(
    QQuickGraphsScatterNode *self,
    QValue3DAxis *axis) {
  self->axisZChanged(axis);
}

//  void QQuickGraphsScatterNode::selectedSeriesChanged(QScatter3DSeries
//      *series)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuickGraphsScatterNode21selectedSeriesChangedEP16QScatter3DSeries(
    QQuickGraphsScatterNode *self,
    QScatter3DSeries *series) {
  self->selectedSeriesChanged(series);
}

//  QQuickGraphsScatter *QQuickGraphsScatterNode::graphScatter()
extern "C" Q_DECL_EXPORT
QQuickGraphsScatter *ritual_ZN23QQuickGraphsScatterNode12graphScatterEv(
    QQuickGraphsScatterNode *self) {
  return self->graphScatter();
}

//  const QQuickGraphsScatter *QQuickGraphsScatterNode::graphScatter() const
extern "C" Q_DECL_EXPORT
const QQuickGraphsScatter *ritual_ZNK23QQuickGraphsScatterNode12graphScatterEv(
    const QQuickGraphsScatterNode *self) {
  return self->graphScatter();
}

//  a Python function taken by a CuteQQuickGraphsScatterNode, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQuickGraphsScatterNode(
    QQuickGraphsScatterNode *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQuickGraphsScatterNode *>(self)->take(key, call);
}

//  void QQuickGraphsScatterNode::setSelectionMode(QtGraphs3D::SelectionFlags
//      mode)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN23QQuickGraphsScatterNode16setSelectionModeE6QFlagsIN10QtGraphs3D13SelectionFlagEE(
    QQuickGraphsScatterNode *self,
    int mode) {
  self->QQuickGraphsScatterNode::setSelectionMode(
      QFlags<QtGraphs3D::SelectionFlag>::fromInt(mode));
}

//  void QQuickGraphsScatterNode::clearSelection()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN23QQuickGraphsScatterNode14clearSelectionEv(
    QQuickGraphsScatterNode *self) {
  self->QQuickGraphsScatterNode::clearSelection();
}

//  bool QQuickGraphsScatterNode::doPicking(QPointF point)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN23QQuickGraphsScatterNode9doPickingE7QPointF(
    QQuickGraphsScatterNode *self,
    const QPointF *point) {
  return self->QQuickGraphsScatterNode::doPicking(*point);
}

//  bool QQuickGraphsScatterNode::doRayPicking(const QVector3D &origin, const
//      QVector3D &direction)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN23QQuickGraphsScatterNode12doRayPickingERK9QVector3DS2_(
    QQuickGraphsScatterNode *self,
    const QVector3D *origin,
    const QVector3D *direction) {
  return self->QQuickGraphsScatterNode::doRayPicking(*origin, *direction);
}

//  void QQuickGraphsScatterNode::componentComplete()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN23QQuickGraphsScatterNode17componentCompleteEv(
    QQuickGraphsScatterNode *self) {
  static_cast<OwnQQuickGraphsScatterNode *>(self)->OwnQQuickGraphsScatterNode::componentComplete();
}

//  a QQmlListProperty<QScatter3DSeries> a ritual of QQuickGraphsScatterNode
//      gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QQuickGraphsScatterNode__QQmlListProperty_QScatter3DSeries(
    QQmlListProperty<QScatter3DSeries> *self) {
  delete self;
}

#endif  // (QT_CONFIG(graphs_3d)) && (!(!QT_CONFIG(graphs_3d_bars3d) && !QT_CONFIG(graphs_3d_scatter3d) && !QT_CONFIG(graphs_3d_surface3d))) && (QT_CONFIG(graphs_3d_scatter3d))
