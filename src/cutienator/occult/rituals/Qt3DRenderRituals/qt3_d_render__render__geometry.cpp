//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DRender/6.12.0/Qt3DRender/private/geometry_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <Qt3DRender/6.12.0/Qt3DRender/private/qt3drender_global_p.h>
#include <Qt3DRender/Qt3DRender>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DRender/6.12.0/Qt3DRender/private/geometry_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DCore/qnodeid.h>
#include <QtGui/qvectornd.h>
#include <cstring>
#include <QtCore/QList>
#include <Qt3DCore/Qt3DCore>

//  A Qt3DRender::Render::Geometry that Python can take functions over in. Every Qt3DRender::Render::Geometry
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQt3DRender_Render_GeometryCall0)(const void *, const Qt3DCore::QNode *, bool, int *);
class CuteQt3DRender_Render_Geometry : public Qt3DRender::Render::Geometry {
public:
  using Qt3DRender::Render::Geometry::Geometry;
  void *taken[1] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN8Qt3DCore12QBackendNode16syncFromFrontEndEPKNS_5QNodeEb")) {
      taken[0] = call;
      return true;
    }
    return false;
  }

  //  void Qt3DRender::Render::Geometry::syncFromFrontEnd(const
  //      Qt3DCore::QNode *frontEnd, bool firstTime)
  void syncFromFrontEnd(
      const Qt3DCore::QNode *frontEnd,
      bool firstTime) override {
    if (taken[0]) {
      int handled = 0;
      CuteQt3DRender_Render_GeometryCall0 call = reinterpret_cast<CuteQt3DRender_Render_GeometryCall0>(taken[0]);
      call(this, frontEnd, firstTime, &handled);
      if (handled) return;
    }
    Qt3DRender::Render::Geometry::syncFromFrontEnd(frontEnd, firstTime);
  }
};

//  Qt3DRender::Render::Geometry::Geometry()
extern "C" Q_DECL_EXPORT
Qt3DRender::Render::Geometry *ritual_ZN10Qt3DRender6Render8GeometryC1Ev() {
  return new CuteQt3DRender_Render_Geometry();
}

//  Qt3DRender::Render::Geometry::~Geometry()
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender6Render8GeometryD1Ev(
    Qt3DRender::Render::Geometry *self) {
  delete self;
}

//  void Qt3DRender::Render::Geometry::cleanup()
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender6Render8Geometry7cleanupEv(
    Qt3DRender::Render::Geometry *self) {
  self->cleanup();
}

//  void Qt3DRender::Render::Geometry::syncFromFrontEnd(const Qt3DCore::QNode
//      *frontEnd, bool firstTime)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender6Render8Geometry16syncFromFrontEndEPKN8Qt3DCore5QNodeEb(
    Qt3DRender::Render::Geometry *self,
    const Qt3DCore::QNode *frontEnd,
    bool firstTime) {
  self->syncFromFrontEnd(frontEnd, firstTime);
}

//  QList<Qt3DCore::QNodeId> Qt3DRender::Render::Geometry::attributes() const
extern "C" Q_DECL_EXPORT
QList<Qt3DCore::QNodeId> *ritual_ZNK10Qt3DRender6Render8Geometry10attributesEv(
    const Qt3DRender::Render::Geometry *self) {
  return new QList<Qt3DCore::QNodeId>(self->attributes());
}

//  bool Qt3DRender::Render::Geometry::isDirty() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK10Qt3DRender6Render8Geometry7isDirtyEv(
    const Qt3DRender::Render::Geometry *self) {
  return self->isDirty();
}

//  Qt3DCore::QNodeId
//      Qt3DRender::Render::Geometry::boundingPositionAttribute() const
extern "C" Q_DECL_EXPORT
Qt3DCore::QNodeId *ritual_ZNK10Qt3DRender6Render8Geometry25boundingPositionAttributeEv(
    const Qt3DRender::Render::Geometry *self) {
  return new Qt3DCore::QNodeId(self->boundingPositionAttribute());
}

//  void Qt3DRender::Render::Geometry::unsetDirty()
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender6Render8Geometry10unsetDirtyEv(
    Qt3DRender::Render::Geometry *self) {
  self->unsetDirty();
}

//  QVector3D Qt3DRender::Render::Geometry::min() const
extern "C" Q_DECL_EXPORT
QVector3D *ritual_ZNK10Qt3DRender6Render8Geometry3minEv(
    const Qt3DRender::Render::Geometry *self) {
  return new QVector3D(self->min());
}

//  QVector3D Qt3DRender::Render::Geometry::max() const
extern "C" Q_DECL_EXPORT
QVector3D *ritual_ZNK10Qt3DRender6Render8Geometry3maxEv(
    const Qt3DRender::Render::Geometry *self) {
  return new QVector3D(self->max());
}

//  void Qt3DRender::Render::Geometry::updateExtent(const QVector3D &min,
//      const QVector3D &max)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender6Render8Geometry12updateExtentERK9QVector3DS4_(
    Qt3DRender::Render::Geometry *self,
    const QVector3D *min,
    const QVector3D *max) {
  self->updateExtent(*min, *max);
}

//  a Python function taken by a CuteQt3DRender_Render_Geometry, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_Qt3DRender_Render_Geometry(
    Qt3DRender::Render::Geometry *self,
    const char *key,
    void *call) {
  return static_cast<CuteQt3DRender_Render_Geometry *>(self)->take(key, call);
}

//  void Qt3DRender::Render::Geometry::syncFromFrontEnd(const Qt3DCore::QNode
//      *frontEnd, bool firstTime)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN10Qt3DRender6Render8Geometry16syncFromFrontEndEPKN8Qt3DCore5QNodeEb(
    Qt3DRender::Render::Geometry *self,
    const Qt3DCore::QNode *frontEnd,
    bool firstTime) {
  self->Qt3DRender::Render::Geometry::syncFromFrontEnd(frontEnd, firstTime);
}

//  a QList<Qt3DCore::QNodeId> a ritual of Qt3DRender::Render::Geometry gave
extern "C" Q_DECL_EXPORT
void ritual_drop_Qt3DRender_Render_Geometry__QList_Qt3DCore_QNodeId(
    QList<Qt3DCore::QNodeId> *self) {
  delete self;
}
