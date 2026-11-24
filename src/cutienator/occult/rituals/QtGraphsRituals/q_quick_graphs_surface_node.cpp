//  Written by dev_tooling.RitualGenerator from the records of
//  QtGraphs/6.12.0/QtGraphs/private/qquickgraphssurfacenode_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtGraphs/qgraphsglobal.h>
#include <QtGraphs/6.12.0/QtGraphs/private/qgraphsglobal_p.h>
#if (!(!QT_CONFIG(graphs_3d_bars3d) && !QT_CONFIG(graphs_3d_scatter3d) && !QT_CONFIG(graphs_3d_surface3d))) && (QT_CONFIG(graphs_3d_surface3d))
#include <QtGraphs/6.12.0/QtGraphs/private/qgraphsglobal_p.h>
#include <QtGraphs/QtGraphs>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGraphs/6.12.0/QtGraphs/private/qquickgraphssurfacenode_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtGraphs/qsurface3dseries.h>
#include <QtCore/qpoint.h>
#include <QtGui/qvectornd.h>
#include <QtCore/qmetaobject.h>
#include <QtQuick3D/qquick3dobject.h>
#include <QtCore/qlist.h>
#include <cstring>

//  Only a class built on QQuickGraphsSurfaceNode may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQQuickGraphsSurfaceNode : QQuickGraphsSurfaceNode {
  using QQuickGraphsSurfaceNode::componentComplete;
};

//  A QQuickGraphsSurfaceNode that Python can take functions over in. Every QQuickGraphsSurfaceNode
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQQuickGraphsSurfaceNodeCall0)(const void *, int, int *);
typedef void (*CuteQQuickGraphsSurfaceNodeCall1)(const void *, int *);
typedef bool (*CuteQQuickGraphsSurfaceNodeCall2)(const void *, const QPointF *, int *);
typedef bool (*CuteQQuickGraphsSurfaceNodeCall3)(const void *, const QVector3D *, const QVector3D *, int *);
typedef void (*CuteQQuickGraphsSurfaceNodeCall4)(const void *, int *);
typedef bool (*CuteQQuickGraphsSurfaceNodeCall5)(const void *, QAbstract3DSeries *, int *);
typedef void (*CuteQQuickGraphsSurfaceNodeCall6)(const void *, QAbstract3DSeries *, int *);
typedef void (*CuteQQuickGraphsSurfaceNodeCall7)(const void *, QAbstract3DSeries *, int *);
typedef qsizetype (*CuteQQuickGraphsSurfaceNodeCall8)(const void *, QCustom3DItem *, int *);
typedef void (*CuteQQuickGraphsSurfaceNodeCall9)(const void *, int *);
typedef void (*CuteQQuickGraphsSurfaceNodeCall10)(const void *, QCustom3DItem *, int *);
typedef void (*CuteQQuickGraphsSurfaceNodeCall11)(const void *, const QVector3D *, int *);
typedef void (*CuteQQuickGraphsSurfaceNodeCall12)(const void *, QCustom3DItem *, int *);
typedef int (*CuteQQuickGraphsSurfaceNodeCall13)(const void *, int *);
typedef void * (*CuteQQuickGraphsSurfaceNodeCall14)(const void *, int *);
typedef qsizetype (*CuteQQuickGraphsSurfaceNodeCall15)(const void *, int *);
typedef void * (*CuteQQuickGraphsSurfaceNodeCall16)(const void *, int *);
typedef void (*CuteQQuickGraphsSurfaceNodeCall17)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickGraphsSurfaceNodeCall18)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickGraphsSurfaceNodeCall19)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
typedef void * (*CuteQQuickGraphsSurfaceNodeCall20)(const void *, QSSGRenderGraphObject *, int *);
typedef void (*CuteQQuickGraphsSurfaceNodeCall21)(const void *, int, const QQuick3DObject::ItemChangeData *, int *);
typedef void (*CuteQQuickGraphsSurfaceNodeCall22)(const void *, int *);
typedef void (*CuteQQuickGraphsSurfaceNodeCall23)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickGraphsSurfaceNodeCall24)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickGraphsSurfaceNodeCall25)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickGraphsSurfaceNodeCall26)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickGraphsSurfaceNodeCall27)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickGraphsSurfaceNodeCall28)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQQuickGraphsSurfaceNode : public QQuickGraphsSurfaceNode {
public:
  using QQuickGraphsSurfaceNode::QQuickGraphsSurfaceNode;
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
  //      QQuickGraphsSurfaceNode::setSelectionMode(QtGraphs3D::SelectionFl
  //      ags mode)
  void setSelectionMode(QtGraphs3D::SelectionFlags mode) override {
    if (taken[0]) {
      int handled = 0;
      CuteQQuickGraphsSurfaceNodeCall0 call = reinterpret_cast<CuteQQuickGraphsSurfaceNodeCall0>(taken[0]);
      call(this, static_cast<int>(mode.toInt()), &handled);
      if (handled) return;
    }
    QQuickGraphsSurfaceNode::setSelectionMode(mode);
  }

  //  void QQuickGraphsSurfaceNode::clearSelection()
  void clearSelection() override {
    if (taken[1]) {
      int handled = 0;
      CuteQQuickGraphsSurfaceNodeCall1 call = reinterpret_cast<CuteQQuickGraphsSurfaceNodeCall1>(taken[1]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickGraphsSurfaceNode::clearSelection();
  }

  //  bool QQuickGraphsSurfaceNode::doPicking(QPointF point)
  bool doPicking(QPointF point) override {
    if (taken[2]) {
      int handled = 0;
      CuteQQuickGraphsSurfaceNodeCall2 call = reinterpret_cast<CuteQQuickGraphsSurfaceNodeCall2>(taken[2]);
      bool given = call(this, &point, &handled);
      if (handled) return given;
    }
    return QQuickGraphsSurfaceNode::doPicking(point);
  }

  //  bool QQuickGraphsSurfaceNode::doRayPicking(const QVector3D &origin,
  //      const QVector3D &direction)
  bool doRayPicking(
      const QVector3D &origin,
      const QVector3D &direction) override {
    if (taken[3]) {
      int handled = 0;
      CuteQQuickGraphsSurfaceNodeCall3 call = reinterpret_cast<CuteQQuickGraphsSurfaceNodeCall3>(taken[3]);
      bool given = call(this, &origin, &direction, &handled);
      if (handled) return given;
    }
    return QQuickGraphsSurfaceNode::doRayPicking(origin, direction);
  }

  //  void QQuickGraphsSurfaceNode::componentComplete()
  void componentComplete() override {
    if (taken[4]) {
      int handled = 0;
      CuteQQuickGraphsSurfaceNodeCall4 call = reinterpret_cast<CuteQQuickGraphsSurfaceNodeCall4>(taken[4]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickGraphsSurfaceNode::componentComplete();
  }

  //  bool QQuickGraphsNode::hasSeries(QAbstract3DSeries *series)
  bool hasSeries(QAbstract3DSeries *series) override {
    if (taken[5]) {
      int handled = 0;
      CuteQQuickGraphsSurfaceNodeCall5 call = reinterpret_cast<CuteQQuickGraphsSurfaceNodeCall5>(taken[5]);
      bool given = call(this, series, &handled);
      if (handled) return given;
    }
    return QQuickGraphsNode::hasSeries(series);
  }

  //  void QQuickGraphsNode::addSeriesInternal(QAbstract3DSeries *series)
  void addSeriesInternal(QAbstract3DSeries *series) override {
    if (taken[6]) {
      int handled = 0;
      CuteQQuickGraphsSurfaceNodeCall6 call = reinterpret_cast<CuteQQuickGraphsSurfaceNodeCall6>(taken[6]);
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
      CuteQQuickGraphsSurfaceNodeCall7 call = reinterpret_cast<CuteQQuickGraphsSurfaceNodeCall7>(taken[7]);
      call(this, series, &handled);
      if (handled) return;
    }
    QQuickGraphsNode::removeSeriesInternal(series);
  }

  //  qsizetype QQuickGraphsNode::addCustomItem(QCustom3DItem *item)
  qsizetype addCustomItem(QCustom3DItem *item) override {
    if (taken[8]) {
      int handled = 0;
      CuteQQuickGraphsSurfaceNodeCall8 call = reinterpret_cast<CuteQQuickGraphsSurfaceNodeCall8>(taken[8]);
      qsizetype given = call(this, item, &handled);
      if (handled) return given;
    }
    return QQuickGraphsNode::addCustomItem(item);
  }

  //  void QQuickGraphsNode::removeCustomItems()
  void removeCustomItems() override {
    if (taken[9]) {
      int handled = 0;
      CuteQQuickGraphsSurfaceNodeCall9 call = reinterpret_cast<CuteQQuickGraphsSurfaceNodeCall9>(taken[9]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickGraphsNode::removeCustomItems();
  }

  //  void QQuickGraphsNode::removeCustomItem(QCustom3DItem *item)
  void removeCustomItem(QCustom3DItem *item) override {
    if (taken[10]) {
      int handled = 0;
      CuteQQuickGraphsSurfaceNodeCall10 call = reinterpret_cast<CuteQQuickGraphsSurfaceNodeCall10>(taken[10]);
      call(this, item, &handled);
      if (handled) return;
    }
    QQuickGraphsNode::removeCustomItem(item);
  }

  //  void QQuickGraphsNode::removeCustomItemAt(QVector3D position)
  void removeCustomItemAt(QVector3D position) override {
    if (taken[11]) {
      int handled = 0;
      CuteQQuickGraphsSurfaceNodeCall11 call = reinterpret_cast<CuteQQuickGraphsSurfaceNodeCall11>(taken[11]);
      call(this, &position, &handled);
      if (handled) return;
    }
    QQuickGraphsNode::removeCustomItemAt(position);
  }

  //  void QQuickGraphsNode::releaseCustomItem(QCustom3DItem *item)
  void releaseCustomItem(QCustom3DItem *item) override {
    if (taken[12]) {
      int handled = 0;
      CuteQQuickGraphsSurfaceNodeCall12 call = reinterpret_cast<CuteQQuickGraphsSurfaceNodeCall12>(taken[12]);
      call(this, item, &handled);
      if (handled) return;
    }
    QQuickGraphsNode::releaseCustomItem(item);
  }

  //  int QQuickGraphsNode::selectedLabelIndex() const
  int selectedLabelIndex() const override {
    if (taken[13]) {
      int handled = 0;
      CuteQQuickGraphsSurfaceNodeCall13 call = reinterpret_cast<CuteQQuickGraphsSurfaceNodeCall13>(taken[13]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return QQuickGraphsNode::selectedLabelIndex();
  }

  //  QAbstract3DAxis *QQuickGraphsNode::selectedAxis() const
  QAbstract3DAxis *selectedAxis() const override {
    if (taken[14]) {
      int handled = 0;
      CuteQQuickGraphsSurfaceNodeCall14 call = reinterpret_cast<CuteQQuickGraphsSurfaceNodeCall14>(taken[14]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QAbstract3DAxis *>(given);
    }
    return QQuickGraphsNode::selectedAxis();
  }

  //  qsizetype QQuickGraphsNode::selectedCustomItemIndex() const
  qsizetype selectedCustomItemIndex() const override {
    if (taken[15]) {
      int handled = 0;
      CuteQQuickGraphsSurfaceNodeCall15 call = reinterpret_cast<CuteQQuickGraphsSurfaceNodeCall15>(taken[15]);
      qsizetype given = call(this, &handled);
      if (handled) return given;
    }
    return QQuickGraphsNode::selectedCustomItemIndex();
  }

  //  QCustom3DItem *QQuickGraphsNode::selectedCustomItem() const
  QCustom3DItem *selectedCustomItem() const override {
    if (taken[16]) {
      int handled = 0;
      CuteQQuickGraphsSurfaceNodeCall16 call = reinterpret_cast<CuteQQuickGraphsSurfaceNodeCall16>(taken[16]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QCustom3DItem *>(given);
    }
    return QQuickGraphsNode::selectedCustomItem();
  }

  //  void QQuick3DNode::markAllDirty()
  void markAllDirty() override {
    if (taken[17]) {
      int handled = 0;
      CuteQQuickGraphsSurfaceNodeCall17 call = reinterpret_cast<CuteQQuickGraphsSurfaceNodeCall17>(taken[17]);
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
      CuteQQuickGraphsSurfaceNodeCall18 call = reinterpret_cast<CuteQQuickGraphsSurfaceNodeCall18>(taken[18]);
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
      CuteQQuickGraphsSurfaceNodeCall19 call = reinterpret_cast<CuteQQuickGraphsSurfaceNodeCall19>(taken[19]);
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
      CuteQQuickGraphsSurfaceNodeCall20 call = reinterpret_cast<CuteQQuickGraphsSurfaceNodeCall20>(taken[20]);
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
      CuteQQuickGraphsSurfaceNodeCall21 call = reinterpret_cast<CuteQQuickGraphsSurfaceNodeCall21>(taken[21]);
      call(this, static_cast<int>(a0), &a1, &handled);
      if (handled) return;
    }
    QQuick3DNode::itemChange(a0, a1);
  }

  //  void QQuick3DObject::classBegin()
  void classBegin() override {
    if (taken[22]) {
      int handled = 0;
      CuteQQuickGraphsSurfaceNodeCall22 call = reinterpret_cast<CuteQQuickGraphsSurfaceNodeCall22>(taken[22]);
      call(this, &handled);
      if (handled) return;
    }
    QQuick3DObject::classBegin();
  }

  //  void QQuick3DObject::preSync()
  void preSync() override {
    if (taken[23]) {
      int handled = 0;
      CuteQQuickGraphsSurfaceNodeCall23 call = reinterpret_cast<CuteQQuickGraphsSurfaceNodeCall23>(taken[23]);
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
      CuteQQuickGraphsSurfaceNodeCall24 call = reinterpret_cast<CuteQQuickGraphsSurfaceNodeCall24>(taken[24]);
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
      CuteQQuickGraphsSurfaceNodeCall25 call = reinterpret_cast<CuteQQuickGraphsSurfaceNodeCall25>(taken[25]);
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
      CuteQQuickGraphsSurfaceNodeCall26 call = reinterpret_cast<CuteQQuickGraphsSurfaceNodeCall26>(taken[26]);
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
      CuteQQuickGraphsSurfaceNodeCall27 call = reinterpret_cast<CuteQQuickGraphsSurfaceNodeCall27>(taken[27]);
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
      CuteQQuickGraphsSurfaceNodeCall28 call = reinterpret_cast<CuteQQuickGraphsSurfaceNodeCall28>(taken[28]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QQuickGraphsSurfaceNode::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK23QQuickGraphsSurfaceNode10metaObjectEv(
    const QQuickGraphsSurfaceNode *self) {
  return self->metaObject();
}

//  QString QQuickGraphsSurfaceNode::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN23QQuickGraphsSurfaceNode2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuickGraphsSurfaceNode::tr(s, c, n));
}

//  QQuickGraphsSurfaceNode::QQuickGraphsSurfaceNode(QQuick3DNode *parent)
extern "C" Q_DECL_EXPORT
QQuickGraphsSurfaceNode *ritual_ZN23QQuickGraphsSurfaceNodeC1EP12QQuick3DNode(
    QQuick3DNode *parent) {
  return new CuteQQuickGraphsSurfaceNode(parent);
}

//  QQuickGraphsSurfaceNode::~QQuickGraphsSurfaceNode()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuickGraphsSurfaceNodeD1Ev(QQuickGraphsSurfaceNode *self) {
  delete self;
}

//  QValue3DAxis *QQuickGraphsSurfaceNode::axisX() const
extern "C" Q_DECL_EXPORT
QValue3DAxis *ritual_ZNK23QQuickGraphsSurfaceNode5axisXEv(
    const QQuickGraphsSurfaceNode *self) {
  return self->axisX();
}

//  void QQuickGraphsSurfaceNode::setAxisX(QValue3DAxis *axis)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuickGraphsSurfaceNode8setAxisXEP12QValue3DAxis(
    QQuickGraphsSurfaceNode *self,
    QValue3DAxis *axis) {
  self->setAxisX(axis);
}

//  QValue3DAxis *QQuickGraphsSurfaceNode::axisY() const
extern "C" Q_DECL_EXPORT
QValue3DAxis *ritual_ZNK23QQuickGraphsSurfaceNode5axisYEv(
    const QQuickGraphsSurfaceNode *self) {
  return self->axisY();
}

//  void QQuickGraphsSurfaceNode::setAxisY(QValue3DAxis *axis)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuickGraphsSurfaceNode8setAxisYEP12QValue3DAxis(
    QQuickGraphsSurfaceNode *self,
    QValue3DAxis *axis) {
  self->setAxisY(axis);
}

//  QValue3DAxis *QQuickGraphsSurfaceNode::axisZ() const
extern "C" Q_DECL_EXPORT
QValue3DAxis *ritual_ZNK23QQuickGraphsSurfaceNode5axisZEv(
    const QQuickGraphsSurfaceNode *self) {
  return self->axisZ();
}

//  void QQuickGraphsSurfaceNode::setAxisZ(QValue3DAxis *axis)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuickGraphsSurfaceNode8setAxisZEP12QValue3DAxis(
    QQuickGraphsSurfaceNode *self,
    QValue3DAxis *axis) {
  self->setAxisZ(axis);
}

//  QSurface3DSeries *QQuickGraphsSurfaceNode::selectedSeries() const
extern "C" Q_DECL_EXPORT
QSurface3DSeries *ritual_ZNK23QQuickGraphsSurfaceNode14selectedSeriesEv(
    const QQuickGraphsSurfaceNode *self) {
  return self->selectedSeries();
}

//  void QQuickGraphsSurfaceNode::setSelectionMode(QtGraphs3D::SelectionFlags
//      mode)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuickGraphsSurfaceNode16setSelectionModeE6QFlagsIN10QtGraphs3D13SelectionFlagEE(
    QQuickGraphsSurfaceNode *self,
    int mode) {
  self->setSelectionMode(QFlags<QtGraphs3D::SelectionFlag>::fromInt(mode));
}

//  bool QQuickGraphsSurfaceNode::flipHorizontalGrid() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK23QQuickGraphsSurfaceNode18flipHorizontalGridEv(
    const QQuickGraphsSurfaceNode *self) {
  return self->flipHorizontalGrid();
}

//  void QQuickGraphsSurfaceNode::setFlipHorizontalGrid(bool flip)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuickGraphsSurfaceNode21setFlipHorizontalGridEb(
    QQuickGraphsSurfaceNode *self,
    bool flip) {
  self->setFlipHorizontalGrid(flip);
}

//  QList<QSurface3DSeries *> QQuickGraphsSurfaceNode::surfaceSeriesList()
extern "C" Q_DECL_EXPORT
QList<QSurface3DSeries *> *ritual_ZN23QQuickGraphsSurfaceNode17surfaceSeriesListEv(
    QQuickGraphsSurfaceNode *self) {
  return new QList<QSurface3DSeries *>(self->surfaceSeriesList());
}

//  void QQuickGraphsSurfaceNode::addSeries(QSurface3DSeries *series)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuickGraphsSurfaceNode9addSeriesEP16QSurface3DSeries(
    QQuickGraphsSurfaceNode *self,
    QSurface3DSeries *series) {
  self->addSeries(series);
}

//  void QQuickGraphsSurfaceNode::removeSeries(QSurface3DSeries *series)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuickGraphsSurfaceNode12removeSeriesEP16QSurface3DSeries(
    QQuickGraphsSurfaceNode *self,
    QSurface3DSeries *series) {
  self->removeSeries(series);
}

//  void QQuickGraphsSurfaceNode::clearSelection()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuickGraphsSurfaceNode14clearSelectionEv(
    QQuickGraphsSurfaceNode *self) {
  self->clearSelection();
}

//  bool QQuickGraphsSurfaceNode::doPicking(QPointF point)
extern "C" Q_DECL_EXPORT
bool ritual_ZN23QQuickGraphsSurfaceNode9doPickingE7QPointF(
    QQuickGraphsSurfaceNode *self,
    const QPointF *point) {
  return self->doPicking(*point);
}

//  bool QQuickGraphsSurfaceNode::doRayPicking(const QVector3D &origin, const
//      QVector3D &direction)
extern "C" Q_DECL_EXPORT
bool ritual_ZN23QQuickGraphsSurfaceNode12doRayPickingERK9QVector3DS2_(
    QQuickGraphsSurfaceNode *self,
    const QVector3D *origin,
    const QVector3D *direction) {
  return self->doRayPicking(*origin, *direction);
}

//  void QQuickGraphsSurfaceNode::componentComplete()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuickGraphsSurfaceNode17componentCompleteEv(
    QQuickGraphsSurfaceNode *self) {
  self->componentComplete();
}

//  QQuickGraphsSurface *QQuickGraphsSurfaceNode::graphSurface()
extern "C" Q_DECL_EXPORT
QQuickGraphsSurface *ritual_ZN23QQuickGraphsSurfaceNode12graphSurfaceEv(
    QQuickGraphsSurfaceNode *self) {
  return self->graphSurface();
}

//  const QQuickGraphsSurface *QQuickGraphsSurfaceNode::graphSurface() const
extern "C" Q_DECL_EXPORT
const QQuickGraphsSurface *ritual_ZNK23QQuickGraphsSurfaceNode12graphSurfaceEv(
    const QQuickGraphsSurfaceNode *self) {
  return self->graphSurface();
}

//  a Python function taken by a CuteQQuickGraphsSurfaceNode, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQuickGraphsSurfaceNode(
    QQuickGraphsSurfaceNode *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQuickGraphsSurfaceNode *>(self)->take(key, call);
}

//  void QQuickGraphsSurfaceNode::setSelectionMode(QtGraphs3D::SelectionFlags
//      mode)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN23QQuickGraphsSurfaceNode16setSelectionModeE6QFlagsIN10QtGraphs3D13SelectionFlagEE(
    QQuickGraphsSurfaceNode *self,
    int mode) {
  self->QQuickGraphsSurfaceNode::setSelectionMode(
      QFlags<QtGraphs3D::SelectionFlag>::fromInt(mode));
}

//  void QQuickGraphsSurfaceNode::clearSelection()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN23QQuickGraphsSurfaceNode14clearSelectionEv(
    QQuickGraphsSurfaceNode *self) {
  self->QQuickGraphsSurfaceNode::clearSelection();
}

//  bool QQuickGraphsSurfaceNode::doPicking(QPointF point)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN23QQuickGraphsSurfaceNode9doPickingE7QPointF(
    QQuickGraphsSurfaceNode *self,
    const QPointF *point) {
  return self->QQuickGraphsSurfaceNode::doPicking(*point);
}

//  bool QQuickGraphsSurfaceNode::doRayPicking(const QVector3D &origin, const
//      QVector3D &direction)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN23QQuickGraphsSurfaceNode12doRayPickingERK9QVector3DS2_(
    QQuickGraphsSurfaceNode *self,
    const QVector3D *origin,
    const QVector3D *direction) {
  return self->QQuickGraphsSurfaceNode::doRayPicking(*origin, *direction);
}

//  void QQuickGraphsSurfaceNode::componentComplete()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN23QQuickGraphsSurfaceNode17componentCompleteEv(
    QQuickGraphsSurfaceNode *self) {
  static_cast<OwnQQuickGraphsSurfaceNode *>(self)->OwnQQuickGraphsSurfaceNode::componentComplete();
}

#endif  // (!(!QT_CONFIG(graphs_3d_bars3d) && !QT_CONFIG(graphs_3d_scatter3d) && !QT_CONFIG(graphs_3d_surface3d))) && (QT_CONFIG(graphs_3d_surface3d))
