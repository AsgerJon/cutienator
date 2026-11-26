//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DRender/6.12.0/Qt3DRender/private/qframegraphnode_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <Qt3DRender/6.12.0/Qt3DRender/private/qt3drender_global_p.h>
#include <Qt3DRender/Qt3DRender>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DRender/6.12.0/Qt3DRender/private/qframegraphnode_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qlist.h>
#include <cstring>
#include <QtCore/QList>

//  A Qt3DRender::QFrameGraphNodePrivate that Python can take functions over in. Every Qt3DRender::QFrameGraphNodePrivate
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQt3DRender_QFrameGraphNodePrivateCall0)(const void *, Qt3DCore::QScene *, int *);
typedef void (*CuteQt3DRender_QFrameGraphNodePrivateCall1)(const void *, int *);
class CuteQt3DRender_QFrameGraphNodePrivate : public Qt3DRender::QFrameGraphNodePrivate {
public:
  using Qt3DRender::QFrameGraphNodePrivate::QFrameGraphNodePrivate;
  void *taken[2] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN8Qt3DCore12QNodePrivate8setSceneEPNS_6QSceneE")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN8Qt3DCore12QNodePrivate6updateEv")) {
      taken[1] = call;
      return true;
    }
    return false;
  }

  //  void Qt3DCore::QNodePrivate::setScene(QScene *scene)
  void setScene(Qt3DCore::QScene *scene) override {
    if (taken[0]) {
      int handled = 0;
      CuteQt3DRender_QFrameGraphNodePrivateCall0 call = reinterpret_cast<CuteQt3DRender_QFrameGraphNodePrivateCall0>(taken[0]);
      call(this, scene, &handled);
      if (handled) return;
    }
    Qt3DCore::QNodePrivate::setScene(scene);
  }

  //  void Qt3DCore::QNodePrivate::update()
  void update() override {
    if (taken[1]) {
      int handled = 0;
      CuteQt3DRender_QFrameGraphNodePrivateCall1 call = reinterpret_cast<CuteQt3DRender_QFrameGraphNodePrivateCall1>(taken[1]);
      call(this, &handled);
      if (handled) return;
    }
    Qt3DCore::QNodePrivate::update();
  }
};

//  Qt3DRender::QFrameGraphNodePrivate::QFrameGraphNodePrivate()
extern "C" Q_DECL_EXPORT
Qt3DRender::QFrameGraphNodePrivate *ritual_ZN10Qt3DRender22QFrameGraphNodePrivateC1Ev() {
  return new CuteQt3DRender_QFrameGraphNodePrivate();
}

//  QList<QFrameGraphNode *>
//      Qt3DRender::QFrameGraphNodePrivate::childFrameGraphNodes() const
extern "C" Q_DECL_EXPORT
QList<Qt3DRender::QFrameGraphNode *> *ritual_ZNK10Qt3DRender22QFrameGraphNodePrivate20childFrameGraphNodesEv(
    const Qt3DRender::QFrameGraphNodePrivate *self) {
  return new QList<Qt3DRender::QFrameGraphNode *>(
      self->childFrameGraphNodes());
}

//  QFrameGraphNodePrivate
//      *Qt3DRender::QFrameGraphNodePrivate::get(QFrameGraphNode *node)
extern "C" Q_DECL_EXPORT
Qt3DRender::QFrameGraphNodePrivate *ritual_ZN10Qt3DRender22QFrameGraphNodePrivate3getEPNS_15QFrameGraphNodeE(
    Qt3DRender::QFrameGraphNode *node) {
  return Qt3DRender::QFrameGraphNodePrivate::get(node);
}

//  const QFrameGraphNodePrivate
//      *Qt3DRender::QFrameGraphNodePrivate::get(const QFrameGraphNode *node)
extern "C" Q_DECL_EXPORT
const Qt3DRender::QFrameGraphNodePrivate *ritual_ZN10Qt3DRender22QFrameGraphNodePrivate3getEPKNS_15QFrameGraphNodeE(
    const Qt3DRender::QFrameGraphNode *node) {
  return Qt3DRender::QFrameGraphNodePrivate::get(node);
}

//  QString Qt3DRender::QFrameGraphNodePrivate::dumpFrameGraph() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK10Qt3DRender22QFrameGraphNodePrivate14dumpFrameGraphEv(
    const Qt3DRender::QFrameGraphNodePrivate *self) {
  return new QString(self->dumpFrameGraph());
}

//  QStringList Qt3DRender::QFrameGraphNodePrivate::dumpFrameGraphPaths()
//      const
extern "C" Q_DECL_EXPORT
QList<QString> *ritual_ZNK10Qt3DRender22QFrameGraphNodePrivate19dumpFrameGraphPathsEv(
    const Qt3DRender::QFrameGraphNodePrivate *self) {
  return new QList<QString>(self->dumpFrameGraphPaths());
}

//  QStringList
//      Qt3DRender::QFrameGraphNodePrivate::dumpFrameGraphFilterState() const
extern "C" Q_DECL_EXPORT
QList<QString> *ritual_ZNK10Qt3DRender22QFrameGraphNodePrivate25dumpFrameGraphFilterStateEv(
    const Qt3DRender::QFrameGraphNodePrivate *self) {
  return new QList<QString>(self->dumpFrameGraphFilterState());
}

//  QFrameGraphNode *Qt3DRender::QFrameGraphNodePrivate::q_func()
extern "C" Q_DECL_EXPORT
Qt3DRender::QFrameGraphNode *ritual_ZN10Qt3DRender22QFrameGraphNodePrivate6q_funcEv(
    Qt3DRender::QFrameGraphNodePrivate *self) {
  return self->q_func();
}

//  const QFrameGraphNode *Qt3DRender::QFrameGraphNodePrivate::q_func() const
extern "C" Q_DECL_EXPORT
const Qt3DRender::QFrameGraphNode *ritual_ZNK10Qt3DRender22QFrameGraphNodePrivate6q_funcEv(
    const Qt3DRender::QFrameGraphNodePrivate *self) {
  return self->q_func();
}

//  a Python function taken by a CuteQt3DRender_QFrameGraphNodePrivate, for
//      the function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_Qt3DRender_QFrameGraphNodePrivate(
    Qt3DRender::QFrameGraphNodePrivate *self,
    const char *key,
    void *call) {
  return static_cast<CuteQt3DRender_QFrameGraphNodePrivate *>(self)->take(key, call);
}

//  a QList<Qt3DRender::QFrameGraphNode *> a ritual of
//      Qt3DRender::QFrameGraphNodePrivate gave
extern "C" Q_DECL_EXPORT
void ritual_drop_Qt3DRender_QFrameGraphNodePrivate__QList_Qt3DRender_QFrameGraphNode(
    QList<Qt3DRender::QFrameGraphNode *> *self) {
  delete self;
}
