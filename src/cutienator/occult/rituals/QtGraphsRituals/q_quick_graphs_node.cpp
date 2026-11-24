//  Written by dev_tooling.RitualGenerator from the records of
//  QtGraphs/6.12.0/QtGraphs/private/qquickgraphsnode_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtGraphs/qgraphsglobal.h>
#include <QtGraphs/6.12.0/QtGraphs/private/qgraphsglobal_p.h>
#if !(!QT_CONFIG(graphs_3d_bars3d) && !QT_CONFIG(graphs_3d_scatter3d) && !QT_CONFIG(graphs_3d_surface3d))
#include <QtGraphs/6.12.0/QtGraphs/private/qgraphsglobal_p.h>
#include <QtGraphs/QtGraphs>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGraphs/6.12.0/QtGraphs/private/qquickgraphsnode_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qlocale.h>
#include <QtGui/qvectornd.h>
#include <QtGraphs/qabstract3dseries.h>
#include <QtCore/qpoint.h>
#include <QtCore/qmetaobject.h>
#include <QtQuick3D/qquick3dobject.h>
#include <QtCore/qlist.h>
#include <cstring>

//  A QQuickGraphsNode that Python can take functions over in. Every QQuickGraphsNode
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQQuickGraphsNodeCall0)(const void *, int *);
typedef void (*CuteQQuickGraphsNodeCall1)(const void *, int, int *);
typedef bool (*CuteQQuickGraphsNodeCall2)(const void *, QAbstract3DSeries *, int *);
typedef void (*CuteQQuickGraphsNodeCall3)(const void *, int *);
typedef void (*CuteQQuickGraphsNodeCall4)(const void *, QAbstract3DSeries *, int *);
typedef void (*CuteQQuickGraphsNodeCall5)(const void *, QAbstract3DSeries *, int *);
typedef qsizetype (*CuteQQuickGraphsNodeCall6)(const void *, QCustom3DItem *, int *);
typedef void (*CuteQQuickGraphsNodeCall7)(const void *, int *);
typedef void (*CuteQQuickGraphsNodeCall8)(const void *, QCustom3DItem *, int *);
typedef void (*CuteQQuickGraphsNodeCall9)(const void *, const QVector3D *, int *);
typedef void (*CuteQQuickGraphsNodeCall10)(const void *, QCustom3DItem *, int *);
typedef int (*CuteQQuickGraphsNodeCall11)(const void *, int *);
typedef void * (*CuteQQuickGraphsNodeCall12)(const void *, int *);
typedef qsizetype (*CuteQQuickGraphsNodeCall13)(const void *, int *);
typedef void * (*CuteQQuickGraphsNodeCall14)(const void *, int *);
typedef bool (*CuteQQuickGraphsNodeCall15)(const void *, const QPointF *, int *);
typedef bool (*CuteQQuickGraphsNodeCall16)(const void *, const QVector3D *, const QVector3D *, int *);
typedef void (*CuteQQuickGraphsNodeCall17)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickGraphsNodeCall18)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickGraphsNodeCall19)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
typedef void * (*CuteQQuickGraphsNodeCall20)(const void *, QSSGRenderGraphObject *, int *);
typedef void (*CuteQQuickGraphsNodeCall21)(const void *, int, const QQuick3DObject::ItemChangeData *, int *);
typedef void (*CuteQQuickGraphsNodeCall22)(const void *, int *);
typedef void (*CuteQQuickGraphsNodeCall23)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickGraphsNodeCall24)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickGraphsNodeCall25)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickGraphsNodeCall26)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickGraphsNodeCall27)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickGraphsNodeCall28)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQQuickGraphsNode : public QQuickGraphsNode {
public:
  using QQuickGraphsNode::QQuickGraphsNode;
  void *taken[29] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN16QQmlParserStatus17componentCompleteEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQuickGraphsNode16setSelectionModeE6QFlagsIN10QtGraphs3D13SelectionFlagEE")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQuickGraphsNode9hasSeriesEP17QAbstract3DSeries")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQuickGraphsNode14clearSelectionEv")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQuickGraphsNode17addSeriesInternalEP17QAbstract3DSeries")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQuickGraphsNode20removeSeriesInternalEP17QAbstract3DSeries")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQuickGraphsNode13addCustomItemEP13QCustom3DItem")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQuickGraphsNode17removeCustomItemsEv")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQuickGraphsNode16removeCustomItemEP13QCustom3DItem")) {
      taken[8] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQuickGraphsNode18removeCustomItemAtE9QVector3D")) {
      taken[9] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQuickGraphsNode17releaseCustomItemEP13QCustom3DItem")) {
      taken[10] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK16QQuickGraphsNode18selectedLabelIndexEv")) {
      taken[11] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK16QQuickGraphsNode12selectedAxisEv")) {
      taken[12] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK16QQuickGraphsNode23selectedCustomItemIndexEv")) {
      taken[13] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK16QQuickGraphsNode18selectedCustomItemEv")) {
      taken[14] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQuickGraphsNode9doPickingE7QPointF")) {
      taken[15] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQuickGraphsNode12doRayPickingERK9QVector3DS2_")) {
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

  //  void QQuickGraphsNode::componentComplete()
  void componentComplete() override {
    if (taken[0]) {
      int handled = 0;
      CuteQQuickGraphsNodeCall0 call = reinterpret_cast<CuteQQuickGraphsNodeCall0>(taken[0]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickGraphsNode::componentComplete();
  }

  //  void QQuickGraphsNode::setSelectionMode(QtGraphs3D::SelectionFlags
  //      selectionMode)
  void setSelectionMode(QtGraphs3D::SelectionFlags selectionMode) override {
    if (taken[1]) {
      int handled = 0;
      CuteQQuickGraphsNodeCall1 call = reinterpret_cast<CuteQQuickGraphsNodeCall1>(taken[1]);
      call(this, static_cast<int>(selectionMode.toInt()), &handled);
      if (handled) return;
    }
    QQuickGraphsNode::setSelectionMode(selectionMode);
  }

  //  bool QQuickGraphsNode::hasSeries(QAbstract3DSeries *series)
  bool hasSeries(QAbstract3DSeries *series) override {
    if (taken[2]) {
      int handled = 0;
      CuteQQuickGraphsNodeCall2 call = reinterpret_cast<CuteQQuickGraphsNodeCall2>(taken[2]);
      bool given = call(this, series, &handled);
      if (handled) return given;
    }
    return QQuickGraphsNode::hasSeries(series);
  }

  //  void QQuickGraphsNode::clearSelection()
  void clearSelection() override {
    if (taken[3]) {
      int handled = 0;
      CuteQQuickGraphsNodeCall3 call = reinterpret_cast<CuteQQuickGraphsNodeCall3>(taken[3]);
      call(this, &handled);
      if (handled) return;
    }
  }

  //  void QQuickGraphsNode::addSeriesInternal(QAbstract3DSeries *series)
  void addSeriesInternal(QAbstract3DSeries *series) override {
    if (taken[4]) {
      int handled = 0;
      CuteQQuickGraphsNodeCall4 call = reinterpret_cast<CuteQQuickGraphsNodeCall4>(taken[4]);
      call(this, series, &handled);
      if (handled) return;
    }
    QQuickGraphsNode::addSeriesInternal(series);
  }

  //  void QQuickGraphsNode::removeSeriesInternal(QAbstract3DSeries
  //      *series)
  void removeSeriesInternal(QAbstract3DSeries *series) override {
    if (taken[5]) {
      int handled = 0;
      CuteQQuickGraphsNodeCall5 call = reinterpret_cast<CuteQQuickGraphsNodeCall5>(taken[5]);
      call(this, series, &handled);
      if (handled) return;
    }
    QQuickGraphsNode::removeSeriesInternal(series);
  }

  //  qsizetype QQuickGraphsNode::addCustomItem(QCustom3DItem *item)
  qsizetype addCustomItem(QCustom3DItem *item) override {
    if (taken[6]) {
      int handled = 0;
      CuteQQuickGraphsNodeCall6 call = reinterpret_cast<CuteQQuickGraphsNodeCall6>(taken[6]);
      qsizetype given = call(this, item, &handled);
      if (handled) return given;
    }
    return QQuickGraphsNode::addCustomItem(item);
  }

  //  void QQuickGraphsNode::removeCustomItems()
  void removeCustomItems() override {
    if (taken[7]) {
      int handled = 0;
      CuteQQuickGraphsNodeCall7 call = reinterpret_cast<CuteQQuickGraphsNodeCall7>(taken[7]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickGraphsNode::removeCustomItems();
  }

  //  void QQuickGraphsNode::removeCustomItem(QCustom3DItem *item)
  void removeCustomItem(QCustom3DItem *item) override {
    if (taken[8]) {
      int handled = 0;
      CuteQQuickGraphsNodeCall8 call = reinterpret_cast<CuteQQuickGraphsNodeCall8>(taken[8]);
      call(this, item, &handled);
      if (handled) return;
    }
    QQuickGraphsNode::removeCustomItem(item);
  }

  //  void QQuickGraphsNode::removeCustomItemAt(QVector3D position)
  void removeCustomItemAt(QVector3D position) override {
    if (taken[9]) {
      int handled = 0;
      CuteQQuickGraphsNodeCall9 call = reinterpret_cast<CuteQQuickGraphsNodeCall9>(taken[9]);
      call(this, &position, &handled);
      if (handled) return;
    }
    QQuickGraphsNode::removeCustomItemAt(position);
  }

  //  void QQuickGraphsNode::releaseCustomItem(QCustom3DItem *item)
  void releaseCustomItem(QCustom3DItem *item) override {
    if (taken[10]) {
      int handled = 0;
      CuteQQuickGraphsNodeCall10 call = reinterpret_cast<CuteQQuickGraphsNodeCall10>(taken[10]);
      call(this, item, &handled);
      if (handled) return;
    }
    QQuickGraphsNode::releaseCustomItem(item);
  }

  //  int QQuickGraphsNode::selectedLabelIndex() const
  int selectedLabelIndex() const override {
    if (taken[11]) {
      int handled = 0;
      CuteQQuickGraphsNodeCall11 call = reinterpret_cast<CuteQQuickGraphsNodeCall11>(taken[11]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return QQuickGraphsNode::selectedLabelIndex();
  }

  //  QAbstract3DAxis *QQuickGraphsNode::selectedAxis() const
  QAbstract3DAxis *selectedAxis() const override {
    if (taken[12]) {
      int handled = 0;
      CuteQQuickGraphsNodeCall12 call = reinterpret_cast<CuteQQuickGraphsNodeCall12>(taken[12]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QAbstract3DAxis *>(given);
    }
    return QQuickGraphsNode::selectedAxis();
  }

  //  qsizetype QQuickGraphsNode::selectedCustomItemIndex() const
  qsizetype selectedCustomItemIndex() const override {
    if (taken[13]) {
      int handled = 0;
      CuteQQuickGraphsNodeCall13 call = reinterpret_cast<CuteQQuickGraphsNodeCall13>(taken[13]);
      qsizetype given = call(this, &handled);
      if (handled) return given;
    }
    return QQuickGraphsNode::selectedCustomItemIndex();
  }

  //  QCustom3DItem *QQuickGraphsNode::selectedCustomItem() const
  QCustom3DItem *selectedCustomItem() const override {
    if (taken[14]) {
      int handled = 0;
      CuteQQuickGraphsNodeCall14 call = reinterpret_cast<CuteQQuickGraphsNodeCall14>(taken[14]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QCustom3DItem *>(given);
    }
    return QQuickGraphsNode::selectedCustomItem();
  }

  //  bool QQuickGraphsNode::doPicking(QPointF point)
  bool doPicking(QPointF point) override {
    if (taken[15]) {
      int handled = 0;
      CuteQQuickGraphsNodeCall15 call = reinterpret_cast<CuteQQuickGraphsNodeCall15>(taken[15]);
      bool given = call(this, &point, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  bool QQuickGraphsNode::doRayPicking(const QVector3D &origin, const
  //      QVector3D &direction)
  bool doRayPicking(
      const QVector3D &origin,
      const QVector3D &direction) override {
    if (taken[16]) {
      int handled = 0;
      CuteQQuickGraphsNodeCall16 call = reinterpret_cast<CuteQQuickGraphsNodeCall16>(taken[16]);
      bool given = call(this, &origin, &direction, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  void QQuick3DNode::markAllDirty()
  void markAllDirty() override {
    if (taken[17]) {
      int handled = 0;
      CuteQQuickGraphsNodeCall17 call = reinterpret_cast<CuteQQuickGraphsNodeCall17>(taken[17]);
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
      CuteQQuickGraphsNodeCall18 call = reinterpret_cast<CuteQQuickGraphsNodeCall18>(taken[18]);
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
      CuteQQuickGraphsNodeCall19 call = reinterpret_cast<CuteQQuickGraphsNodeCall19>(taken[19]);
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
      CuteQQuickGraphsNodeCall20 call = reinterpret_cast<CuteQQuickGraphsNodeCall20>(taken[20]);
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
      CuteQQuickGraphsNodeCall21 call = reinterpret_cast<CuteQQuickGraphsNodeCall21>(taken[21]);
      call(this, static_cast<int>(a0), &a1, &handled);
      if (handled) return;
    }
    QQuick3DNode::itemChange(a0, a1);
  }

  //  void QQuick3DObject::classBegin()
  void classBegin() override {
    if (taken[22]) {
      int handled = 0;
      CuteQQuickGraphsNodeCall22 call = reinterpret_cast<CuteQQuickGraphsNodeCall22>(taken[22]);
      call(this, &handled);
      if (handled) return;
    }
    QQuick3DObject::classBegin();
  }

  //  void QQuick3DObject::preSync()
  void preSync() override {
    if (taken[23]) {
      int handled = 0;
      CuteQQuickGraphsNodeCall23 call = reinterpret_cast<CuteQQuickGraphsNodeCall23>(taken[23]);
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
      CuteQQuickGraphsNodeCall24 call = reinterpret_cast<CuteQQuickGraphsNodeCall24>(taken[24]);
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
      CuteQQuickGraphsNodeCall25 call = reinterpret_cast<CuteQQuickGraphsNodeCall25>(taken[25]);
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
      CuteQQuickGraphsNodeCall26 call = reinterpret_cast<CuteQQuickGraphsNodeCall26>(taken[26]);
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
      CuteQQuickGraphsNodeCall27 call = reinterpret_cast<CuteQQuickGraphsNodeCall27>(taken[27]);
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
      CuteQQuickGraphsNodeCall28 call = reinterpret_cast<CuteQQuickGraphsNodeCall28>(taken[28]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QQuickGraphsNode::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK16QQuickGraphsNode10metaObjectEv(
    const QQuickGraphsNode *self) {
  return self->metaObject();
}

//  QString QQuickGraphsNode::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN16QQuickGraphsNode2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuickGraphsNode::tr(s, c, n));
}

//  void QQuickGraphsNode::qt_qmlMarker_uncreatable()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickGraphsNode24qt_qmlMarker_uncreatableEv(
    QQuickGraphsNode *self) {
  self->qt_qmlMarker_uncreatable();
}

//  QQuickGraphsNode::~QQuickGraphsNode()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickGraphsNodeD1Ev(QQuickGraphsNode *self) {
  delete self;
}

//  void QQuickGraphsNode::componentComplete()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickGraphsNode17componentCompleteEv(
    QQuickGraphsNode *self) {
  self->componentComplete();
}

//  QtGraphs3D::ElementType QQuickGraphsNode::selectedElement() const
extern "C" Q_DECL_EXPORT
QtGraphs3D::ElementType ritual_ZNK16QQuickGraphsNode15selectedElementEv(
    const QQuickGraphsNode *self) {
  return self->selectedElement();
}

//  void QQuickGraphsNode::setSelectionMode(QtGraphs3D::SelectionFlags
//      selectionMode)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickGraphsNode16setSelectionModeE6QFlagsIN10QtGraphs3D13SelectionFlagEE(
    QQuickGraphsNode *self,
    int selectionMode) {
  self->setSelectionMode(
      QFlags<QtGraphs3D::SelectionFlag>::fromInt(selectionMode));
}

//  QtGraphs3D::SelectionFlags QQuickGraphsNode::selectionMode() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK16QQuickGraphsNode13selectionModeEv(
    const QQuickGraphsNode *self) {
  return static_cast<int>(self->selectionMode().toInt());
}

//  void QQuickGraphsNode::setTheme(QGraphsTheme *theme)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickGraphsNode8setThemeEP12QGraphsTheme(
    QQuickGraphsNode *self,
    QGraphsTheme *theme) {
  self->setTheme(theme);
}

//  QGraphsTheme *QQuickGraphsNode::theme() const
extern "C" Q_DECL_EXPORT
QGraphsTheme *ritual_ZNK16QQuickGraphsNode5themeEv(
    const QQuickGraphsNode *self) {
  return self->theme();
}

//  void QQuickGraphsNode::setAspectRatio(qreal aspectRatio)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickGraphsNode14setAspectRatioEd(
    QQuickGraphsNode *self,
    qreal aspectRatio) {
  self->setAspectRatio(aspectRatio);
}

//  qreal QQuickGraphsNode::aspectRatio() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK16QQuickGraphsNode11aspectRatioEv(
    const QQuickGraphsNode *self) {
  return self->aspectRatio();
}

//  void QQuickGraphsNode::setOptimizationHint(QtGraphs3D::OptimizationHint
//      optimizationHint)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickGraphsNode19setOptimizationHintEN10QtGraphs3D16OptimizationHintE(
    QQuickGraphsNode *self,
    QtGraphs3D::OptimizationHint optimizationHint) {
  self->setOptimizationHint(optimizationHint);
}

//  QtGraphs3D::OptimizationHint QQuickGraphsNode::optimizationHint() const
extern "C" Q_DECL_EXPORT
QtGraphs3D::OptimizationHint ritual_ZNK16QQuickGraphsNode16optimizationHintEv(
    const QQuickGraphsNode *self) {
  return self->optimizationHint();
}

//  void QQuickGraphsNode::setPolar(bool enabled)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickGraphsNode8setPolarEb(
    QQuickGraphsNode *self,
    bool enabled) {
  self->setPolar(enabled);
}

//  bool QQuickGraphsNode::isPolar() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK16QQuickGraphsNode7isPolarEv(const QQuickGraphsNode *self) {
  return self->isPolar();
}

//  void QQuickGraphsNode::setLabelMargin(float labelMargin)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickGraphsNode14setLabelMarginEf(
    QQuickGraphsNode *self,
    float labelMargin) {
  self->setLabelMargin(labelMargin);
}

//  float QQuickGraphsNode::labelMargin() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK16QQuickGraphsNode11labelMarginEv(
    const QQuickGraphsNode *self) {
  return self->labelMargin();
}

//  void QQuickGraphsNode::setRadialLabelOffset(float radialLabelOffset)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickGraphsNode20setRadialLabelOffsetEf(
    QQuickGraphsNode *self,
    float radialLabelOffset) {
  self->setRadialLabelOffset(radialLabelOffset);
}

//  float QQuickGraphsNode::radialLabelOffset() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK16QQuickGraphsNode17radialLabelOffsetEv(
    const QQuickGraphsNode *self) {
  return self->radialLabelOffset();
}

//  void QQuickGraphsNode::setHorizontalAspectRatio(qreal
//      horizontalAspectRatio)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickGraphsNode24setHorizontalAspectRatioEd(
    QQuickGraphsNode *self,
    qreal horizontalAspectRatio) {
  self->setHorizontalAspectRatio(horizontalAspectRatio);
}

//  qreal QQuickGraphsNode::horizontalAspectRatio() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK16QQuickGraphsNode21horizontalAspectRatioEv(
    const QQuickGraphsNode *self) {
  return self->horizontalAspectRatio();
}

//  void QQuickGraphsNode::setLocale(QLocale locale)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickGraphsNode9setLocaleE7QLocale(
    QQuickGraphsNode *self,
    const QLocale *locale) {
  self->setLocale(*locale);
}

//  QLocale QQuickGraphsNode::locale() const
extern "C" Q_DECL_EXPORT
QLocale *ritual_ZNK16QQuickGraphsNode6localeEv(
    const QQuickGraphsNode *self) {
  return new QLocale(self->locale());
}

//  QVector3D QQuickGraphsNode::queriedGraphPosition() const
extern "C" Q_DECL_EXPORT
QVector3D *ritual_ZNK16QQuickGraphsNode20queriedGraphPositionEv(
    const QQuickGraphsNode *self) {
  return new QVector3D(self->queriedGraphPosition());
}

//  void QQuickGraphsNode::setMargin(qreal margin)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickGraphsNode9setMarginEd(
    QQuickGraphsNode *self,
    qreal margin) {
  self->setMargin(margin);
}

//  qreal QQuickGraphsNode::margin() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK16QQuickGraphsNode6marginEv(const QQuickGraphsNode *self) {
  return self->margin();
}

//  QtGraphs3D::GridLineType QQuickGraphsNode::gridLineType() const
extern "C" Q_DECL_EXPORT
QtGraphs3D::GridLineType ritual_ZNK16QQuickGraphsNode12gridLineTypeEv(
    const QQuickGraphsNode *self) {
  return self->gridLineType();
}

//  bool QQuickGraphsNode::hasSeries(QAbstract3DSeries *series)
extern "C" Q_DECL_EXPORT
bool ritual_ZN16QQuickGraphsNode9hasSeriesEP17QAbstract3DSeries(
    QQuickGraphsNode *self,
    QAbstract3DSeries *series) {
  return self->hasSeries(series);
}

//  void QQuickGraphsNode::clearSelection()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickGraphsNode14clearSelectionEv(QQuickGraphsNode *self) {
  self->clearSelection();
}

//  void QQuickGraphsNode::addSeriesInternal(QAbstract3DSeries *series)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickGraphsNode17addSeriesInternalEP17QAbstract3DSeries(
    QQuickGraphsNode *self,
    QAbstract3DSeries *series) {
  self->addSeriesInternal(series);
}

//  void QQuickGraphsNode::insertSeries(qsizetype index, QAbstract3DSeries
//      *series)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickGraphsNode12insertSeriesExP17QAbstract3DSeries(
    QQuickGraphsNode *self,
    qsizetype index,
    QAbstract3DSeries *series) {
  self->insertSeries(index, series);
}

//  void QQuickGraphsNode::removeSeriesInternal(QAbstract3DSeries *series)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickGraphsNode20removeSeriesInternalEP17QAbstract3DSeries(
    QQuickGraphsNode *self,
    QAbstract3DSeries *series) {
  self->removeSeriesInternal(series);
}

//  QList<QAbstract3DSeries *> QQuickGraphsNode::seriesList()
extern "C" Q_DECL_EXPORT
QList<QAbstract3DSeries *> *ritual_ZN16QQuickGraphsNode10seriesListEv(
    QQuickGraphsNode *self) {
  return new QList<QAbstract3DSeries *>(self->seriesList());
}

//  qsizetype QQuickGraphsNode::addCustomItem(QCustom3DItem *item)
extern "C" Q_DECL_EXPORT
qsizetype ritual_ZN16QQuickGraphsNode13addCustomItemEP13QCustom3DItem(
    QQuickGraphsNode *self,
    QCustom3DItem *item) {
  return self->addCustomItem(item);
}

//  void QQuickGraphsNode::removeCustomItems()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickGraphsNode17removeCustomItemsEv(
    QQuickGraphsNode *self) {
  self->removeCustomItems();
}

//  void QQuickGraphsNode::removeCustomItem(QCustom3DItem *item)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickGraphsNode16removeCustomItemEP13QCustom3DItem(
    QQuickGraphsNode *self,
    QCustom3DItem *item) {
  self->removeCustomItem(item);
}

//  void QQuickGraphsNode::removeCustomItemAt(QVector3D position)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickGraphsNode18removeCustomItemAtE9QVector3D(
    QQuickGraphsNode *self,
    const QVector3D *position) {
  self->removeCustomItemAt(*position);
}

//  void QQuickGraphsNode::releaseCustomItem(QCustom3DItem *item)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickGraphsNode17releaseCustomItemEP13QCustom3DItem(
    QQuickGraphsNode *self,
    QCustom3DItem *item) {
  self->releaseCustomItem(item);
}

//  int QQuickGraphsNode::selectedLabelIndex() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK16QQuickGraphsNode18selectedLabelIndexEv(
    const QQuickGraphsNode *self) {
  return self->selectedLabelIndex();
}

//  QAbstract3DAxis *QQuickGraphsNode::selectedAxis() const
extern "C" Q_DECL_EXPORT
QAbstract3DAxis *ritual_ZNK16QQuickGraphsNode12selectedAxisEv(
    const QQuickGraphsNode *self) {
  return self->selectedAxis();
}

//  qsizetype QQuickGraphsNode::selectedCustomItemIndex() const
extern "C" Q_DECL_EXPORT
qsizetype ritual_ZNK16QQuickGraphsNode23selectedCustomItemIndexEv(
    const QQuickGraphsNode *self) {
  return self->selectedCustomItemIndex();
}

//  QCustom3DItem *QQuickGraphsNode::selectedCustomItem() const
extern "C" Q_DECL_EXPORT
QCustom3DItem *ritual_ZNK16QQuickGraphsNode18selectedCustomItemEv(
    const QQuickGraphsNode *self) {
  return self->selectedCustomItem();
}

//  bool QQuickGraphsNode::doPicking(QPointF point)
extern "C" Q_DECL_EXPORT
bool ritual_ZN16QQuickGraphsNode9doPickingE7QPointF(
    QQuickGraphsNode *self,
    const QPointF *point) {
  return self->doPicking(*point);
}

//  bool QQuickGraphsNode::doRayPicking(const QVector3D &origin, const
//      QVector3D &direction)
extern "C" Q_DECL_EXPORT
bool ritual_ZN16QQuickGraphsNode12doRayPickingERK9QVector3DS2_(
    QQuickGraphsNode *self,
    const QVector3D *origin,
    const QVector3D *direction) {
  return self->doRayPicking(*origin, *direction);
}

//  void QQuickGraphsNode::setGraphParent()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickGraphsNode14setGraphParentEv(QQuickGraphsNode *self) {
  self->setGraphParent();
}

//  a Python function taken by a CuteQQuickGraphsNode, for the function named
//      by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQuickGraphsNode(
    QQuickGraphsNode *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQuickGraphsNode *>(self)->take(key, call);
}

//  void QQuickGraphsNode::componentComplete()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN16QQuickGraphsNode17componentCompleteEv(
    QQuickGraphsNode *self) {
  self->QQuickGraphsNode::componentComplete();
}

//  void QQuickGraphsNode::setSelectionMode(QtGraphs3D::SelectionFlags
//      selectionMode)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN16QQuickGraphsNode16setSelectionModeE6QFlagsIN10QtGraphs3D13SelectionFlagEE(
    QQuickGraphsNode *self,
    int selectionMode) {
  self->QQuickGraphsNode::setSelectionMode(
      QFlags<QtGraphs3D::SelectionFlag>::fromInt(selectionMode));
}

//  bool QQuickGraphsNode::hasSeries(QAbstract3DSeries *series)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN16QQuickGraphsNode9hasSeriesEP17QAbstract3DSeries(
    QQuickGraphsNode *self,
    QAbstract3DSeries *series) {
  return self->QQuickGraphsNode::hasSeries(series);
}

//  void QQuickGraphsNode::addSeriesInternal(QAbstract3DSeries *series)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN16QQuickGraphsNode17addSeriesInternalEP17QAbstract3DSeries(
    QQuickGraphsNode *self,
    QAbstract3DSeries *series) {
  self->QQuickGraphsNode::addSeriesInternal(series);
}

//  void QQuickGraphsNode::removeSeriesInternal(QAbstract3DSeries *series)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN16QQuickGraphsNode20removeSeriesInternalEP17QAbstract3DSeries(
    QQuickGraphsNode *self,
    QAbstract3DSeries *series) {
  self->QQuickGraphsNode::removeSeriesInternal(series);
}

//  qsizetype QQuickGraphsNode::addCustomItem(QCustom3DItem *item)
extern "C" Q_DECL_EXPORT
qsizetype ritual_own_ZN16QQuickGraphsNode13addCustomItemEP13QCustom3DItem(
    QQuickGraphsNode *self,
    QCustom3DItem *item) {
  return self->QQuickGraphsNode::addCustomItem(item);
}

//  void QQuickGraphsNode::removeCustomItems()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN16QQuickGraphsNode17removeCustomItemsEv(
    QQuickGraphsNode *self) {
  self->QQuickGraphsNode::removeCustomItems();
}

//  void QQuickGraphsNode::removeCustomItem(QCustom3DItem *item)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN16QQuickGraphsNode16removeCustomItemEP13QCustom3DItem(
    QQuickGraphsNode *self,
    QCustom3DItem *item) {
  self->QQuickGraphsNode::removeCustomItem(item);
}

//  void QQuickGraphsNode::removeCustomItemAt(QVector3D position)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN16QQuickGraphsNode18removeCustomItemAtE9QVector3D(
    QQuickGraphsNode *self,
    const QVector3D *position) {
  self->QQuickGraphsNode::removeCustomItemAt(*position);
}

//  void QQuickGraphsNode::releaseCustomItem(QCustom3DItem *item)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN16QQuickGraphsNode17releaseCustomItemEP13QCustom3DItem(
    QQuickGraphsNode *self,
    QCustom3DItem *item) {
  self->QQuickGraphsNode::releaseCustomItem(item);
}

//  int QQuickGraphsNode::selectedLabelIndex() const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK16QQuickGraphsNode18selectedLabelIndexEv(
    const QQuickGraphsNode *self) {
  return self->QQuickGraphsNode::selectedLabelIndex();
}

//  QAbstract3DAxis *QQuickGraphsNode::selectedAxis() const
extern "C" Q_DECL_EXPORT
QAbstract3DAxis *ritual_own_ZNK16QQuickGraphsNode12selectedAxisEv(
    const QQuickGraphsNode *self) {
  return self->QQuickGraphsNode::selectedAxis();
}

//  qsizetype QQuickGraphsNode::selectedCustomItemIndex() const
extern "C" Q_DECL_EXPORT
qsizetype ritual_own_ZNK16QQuickGraphsNode23selectedCustomItemIndexEv(
    const QQuickGraphsNode *self) {
  return self->QQuickGraphsNode::selectedCustomItemIndex();
}

//  QCustom3DItem *QQuickGraphsNode::selectedCustomItem() const
extern "C" Q_DECL_EXPORT
QCustom3DItem *ritual_own_ZNK16QQuickGraphsNode18selectedCustomItemEv(
    const QQuickGraphsNode *self) {
  return self->QQuickGraphsNode::selectedCustomItem();
}

#endif  // !(!QT_CONFIG(graphs_3d_bars3d) && !QT_CONFIG(graphs_3d_scatter3d) && !QT_CONFIG(graphs_3d_surface3d))
