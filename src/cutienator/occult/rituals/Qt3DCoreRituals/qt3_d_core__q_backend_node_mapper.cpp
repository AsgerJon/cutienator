//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DCore/qbackendnode.h, Qt 6.12.0. Changes made here are lost.
#include <Qt3DCore/qbackendnode.h>
#include <Qt3DCore/qnodeid.h>
#include <cstring>

//  A Qt3DCore::QBackendNodeMapper that Python can take functions over in. Every Qt3DCore::QBackendNodeMapper
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void * (*CuteQt3DCore_QBackendNodeMapperCall0)(const void *, const Qt3DCore::QNodeId *, int *);
typedef void * (*CuteQt3DCore_QBackendNodeMapperCall1)(const void *, const Qt3DCore::QNodeId *, int *);
typedef void (*CuteQt3DCore_QBackendNodeMapperCall2)(const void *, const Qt3DCore::QNodeId *, int *);
class CuteQt3DCore_QBackendNodeMapper : public Qt3DCore::QBackendNodeMapper {
public:
  using Qt3DCore::QBackendNodeMapper::QBackendNodeMapper;
  void *taken[3] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZNK8Qt3DCore18QBackendNodeMapper6createENS_7QNodeIdE")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK8Qt3DCore18QBackendNodeMapper3getENS_7QNodeIdE")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK8Qt3DCore18QBackendNodeMapper7destroyENS_7QNodeIdE")) {
      taken[2] = call;
      return true;
    }
    return false;
  }

  //  QBackendNode *Qt3DCore::QBackendNodeMapper::create(QNodeId id) const
  Qt3DCore::QBackendNode *create(Qt3DCore::QNodeId id) const override {
    if (taken[0]) {
      int handled = 0;
      CuteQt3DCore_QBackendNodeMapperCall0 call = reinterpret_cast<CuteQt3DCore_QBackendNodeMapperCall0>(taken[0]);
      void * given = call(this, &id, &handled);
      if (handled) return static_cast<Qt3DCore::QBackendNode *>(given);
    }
    return {};
  }

  //  QBackendNode *Qt3DCore::QBackendNodeMapper::get(QNodeId id) const
  Qt3DCore::QBackendNode *get(Qt3DCore::QNodeId id) const override {
    if (taken[1]) {
      int handled = 0;
      CuteQt3DCore_QBackendNodeMapperCall1 call = reinterpret_cast<CuteQt3DCore_QBackendNodeMapperCall1>(taken[1]);
      void * given = call(this, &id, &handled);
      if (handled) return static_cast<Qt3DCore::QBackendNode *>(given);
    }
    return {};
  }

  //  void Qt3DCore::QBackendNodeMapper::destroy(QNodeId id) const
  void destroy(Qt3DCore::QNodeId id) const override {
    if (taken[2]) {
      int handled = 0;
      CuteQt3DCore_QBackendNodeMapperCall2 call = reinterpret_cast<CuteQt3DCore_QBackendNodeMapperCall2>(taken[2]);
      call(this, &id, &handled);
      if (handled) return;
    }
  }
};

//  Qt3DCore::QBackendNodeMapper::~QBackendNodeMapper()
extern "C" Q_DECL_EXPORT
void ritual_ZN8Qt3DCore18QBackendNodeMapperD1Ev(
    Qt3DCore::QBackendNodeMapper *self) {
  delete self;
}

//  QBackendNode *Qt3DCore::QBackendNodeMapper::create(QNodeId id) const
extern "C" Q_DECL_EXPORT
Qt3DCore::QBackendNode *ritual_ZNK8Qt3DCore18QBackendNodeMapper6createENS_7QNodeIdE(
    const Qt3DCore::QBackendNodeMapper *self,
    const Qt3DCore::QNodeId *id) {
  return self->create(*id);
}

//  QBackendNode *Qt3DCore::QBackendNodeMapper::get(QNodeId id) const
extern "C" Q_DECL_EXPORT
Qt3DCore::QBackendNode *ritual_ZNK8Qt3DCore18QBackendNodeMapper3getENS_7QNodeIdE(
    const Qt3DCore::QBackendNodeMapper *self,
    const Qt3DCore::QNodeId *id) {
  return self->get(*id);
}

//  void Qt3DCore::QBackendNodeMapper::destroy(QNodeId id) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK8Qt3DCore18QBackendNodeMapper7destroyENS_7QNodeIdE(
    const Qt3DCore::QBackendNodeMapper *self,
    const Qt3DCore::QNodeId *id) {
  self->destroy(*id);
}

//  a Python function taken by a CuteQt3DCore_QBackendNodeMapper, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_Qt3DCore_QBackendNodeMapper(
    Qt3DCore::QBackendNodeMapper *self,
    const char *key,
    void *call) {
  return static_cast<CuteQt3DCore_QBackendNodeMapper *>(self)->take(key, call);
}
