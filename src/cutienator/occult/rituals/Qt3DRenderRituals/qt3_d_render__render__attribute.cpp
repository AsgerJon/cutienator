//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DRender/6.12.0/Qt3DRender/private/attribute_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <Qt3DRender/6.12.0/Qt3DRender/private/qt3drender_global_p.h>
#include <Qt3DRender/Qt3DRender>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DRender/6.12.0/Qt3DRender/private/attribute_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DCore/qnodeid.h>
#include <QtCore/qstring.h>
#include <cstring>

//  A Qt3DRender::Render::Attribute that Python can take functions over in. Every Qt3DRender::Render::Attribute
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQt3DRender_Render_AttributeCall0)(const void *, const Qt3DCore::QNode *, bool, int *);
class CuteQt3DRender_Render_Attribute : public Qt3DRender::Render::Attribute {
public:
  using Qt3DRender::Render::Attribute::Attribute;
  void *taken[1] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN8Qt3DCore12QBackendNode16syncFromFrontEndEPKNS_5QNodeEb")) {
      taken[0] = call;
      return true;
    }
    return false;
  }

  //  void Qt3DRender::Render::Attribute::syncFromFrontEnd(const
  //      Qt3DCore::QNode *frontEnd, bool firstTime)
  void syncFromFrontEnd(
      const Qt3DCore::QNode *frontEnd,
      bool firstTime) override {
    if (taken[0]) {
      int handled = 0;
      CuteQt3DRender_Render_AttributeCall0 call = reinterpret_cast<CuteQt3DRender_Render_AttributeCall0>(taken[0]);
      call(this, frontEnd, firstTime, &handled);
      if (handled) return;
    }
    Qt3DRender::Render::Attribute::syncFromFrontEnd(frontEnd, firstTime);
  }
};

//  Qt3DRender::Render::Attribute::Attribute()
extern "C" Q_DECL_EXPORT
Qt3DRender::Render::Attribute *ritual_ZN10Qt3DRender6Render9AttributeC1Ev() {
  return new CuteQt3DRender_Render_Attribute();
}

//  Qt3DRender::Render::Attribute::~Attribute()
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender6Render9AttributeD1Ev(
    Qt3DRender::Render::Attribute *self) {
  delete self;
}

//  void Qt3DRender::Render::Attribute::cleanup()
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender6Render9Attribute7cleanupEv(
    Qt3DRender::Render::Attribute *self) {
  self->cleanup();
}

//  void Qt3DRender::Render::Attribute::syncFromFrontEnd(const
//      Qt3DCore::QNode *frontEnd, bool firstTime)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender6Render9Attribute16syncFromFrontEndEPKN8Qt3DCore5QNodeEb(
    Qt3DRender::Render::Attribute *self,
    const Qt3DCore::QNode *frontEnd,
    bool firstTime) {
  self->syncFromFrontEnd(frontEnd, firstTime);
}

//  Qt3DCore::QNodeId Qt3DRender::Render::Attribute::bufferId() const
extern "C" Q_DECL_EXPORT
Qt3DCore::QNodeId *ritual_ZNK10Qt3DRender6Render9Attribute8bufferIdEv(
    const Qt3DRender::Render::Attribute *self) {
  return new Qt3DCore::QNodeId(self->bufferId());
}

//  QString Qt3DRender::Render::Attribute::name() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK10Qt3DRender6Render9Attribute4nameEv(
    const Qt3DRender::Render::Attribute *self) {
  return new QString(self->name());
}

//  int Qt3DRender::Render::Attribute::nameId() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK10Qt3DRender6Render9Attribute6nameIdEv(
    const Qt3DRender::Render::Attribute *self) {
  return self->nameId();
}

//  Qt3DCore::QAttribute::VertexBaseType
//      Qt3DRender::Render::Attribute::vertexBaseType() const
extern "C" Q_DECL_EXPORT
Qt3DCore::QAttribute::VertexBaseType ritual_ZNK10Qt3DRender6Render9Attribute14vertexBaseTypeEv(
    const Qt3DRender::Render::Attribute *self) {
  return self->vertexBaseType();
}

//  uint Qt3DRender::Render::Attribute::vertexSize() const
extern "C" Q_DECL_EXPORT
uint ritual_ZNK10Qt3DRender6Render9Attribute10vertexSizeEv(
    const Qt3DRender::Render::Attribute *self) {
  return self->vertexSize();
}

//  uint Qt3DRender::Render::Attribute::count() const
extern "C" Q_DECL_EXPORT
uint ritual_ZNK10Qt3DRender6Render9Attribute5countEv(
    const Qt3DRender::Render::Attribute *self) {
  return self->count();
}

//  uint Qt3DRender::Render::Attribute::byteStride() const
extern "C" Q_DECL_EXPORT
uint ritual_ZNK10Qt3DRender6Render9Attribute10byteStrideEv(
    const Qt3DRender::Render::Attribute *self) {
  return self->byteStride();
}

//  uint Qt3DRender::Render::Attribute::byteOffset() const
extern "C" Q_DECL_EXPORT
uint ritual_ZNK10Qt3DRender6Render9Attribute10byteOffsetEv(
    const Qt3DRender::Render::Attribute *self) {
  return self->byteOffset();
}

//  uint Qt3DRender::Render::Attribute::divisor() const
extern "C" Q_DECL_EXPORT
uint ritual_ZNK10Qt3DRender6Render9Attribute7divisorEv(
    const Qt3DRender::Render::Attribute *self) {
  return self->divisor();
}

//  Qt3DCore::QAttribute::AttributeType
//      Qt3DRender::Render::Attribute::attributeType() const
extern "C" Q_DECL_EXPORT
Qt3DCore::QAttribute::AttributeType ritual_ZNK10Qt3DRender6Render9Attribute13attributeTypeEv(
    const Qt3DRender::Render::Attribute *self) {
  return self->attributeType();
}

//  bool Qt3DRender::Render::Attribute::isDirty() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK10Qt3DRender6Render9Attribute7isDirtyEv(
    const Qt3DRender::Render::Attribute *self) {
  return self->isDirty();
}

//  void Qt3DRender::Render::Attribute::unsetDirty()
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender6Render9Attribute10unsetDirtyEv(
    Qt3DRender::Render::Attribute *self) {
  self->unsetDirty();
}

//  a Python function taken by a CuteQt3DRender_Render_Attribute, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_Qt3DRender_Render_Attribute(
    Qt3DRender::Render::Attribute *self,
    const char *key,
    void *call) {
  return static_cast<CuteQt3DRender_Render_Attribute *>(self)->take(key, call);
}

//  void Qt3DRender::Render::Attribute::syncFromFrontEnd(const
//      Qt3DCore::QNode *frontEnd, bool firstTime)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN10Qt3DRender6Render9Attribute16syncFromFrontEndEPKN8Qt3DCore5QNodeEb(
    Qt3DRender::Render::Attribute *self,
    const Qt3DCore::QNode *frontEnd,
    bool firstTime) {
  self->Qt3DRender::Render::Attribute::syncFromFrontEnd(frontEnd, firstTime);
}
