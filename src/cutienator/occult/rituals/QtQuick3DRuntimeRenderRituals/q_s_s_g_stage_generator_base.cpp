//  Written by dev_tooling.RitualGenerator from the records of QtQuick3DRunti
//  meRender/6.12.0/QtQuick3DRuntimeRender/private/qssgrendershadercodegenera
//  tor_p.h, Qt 6.12.0. Changes made here are lost.
#include <QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/private/qtquick3druntimerenderglobal_p.h>
#include <QtQuick3DRuntimeRender/QtQuick3DRuntimeRender>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/private/qssgrendershadercodegenerator_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qbytearray.h>
#include <cstring>

//  A QSSGStageGeneratorBase that Python can take functions over in. Every QSSGStageGeneratorBase
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQSSGStageGeneratorBaseCall0)(const void *, int, int *);
typedef void (*CuteQSSGStageGeneratorBaseCall1)(const void *, const QByteArray *, const QByteArray *, int *);
typedef void (*CuteQSSGStageGeneratorBaseCall2)(const void *, const QByteArray *, const QByteArray *, int *);
typedef void (*CuteQSSGStageGeneratorBaseCall3)(const void *, const QByteArray *, const QByteArray *, int *);
typedef void (*CuteQSSGStageGeneratorBaseCall4)(const void *, const QByteArray *, const QByteArray *, int *);
typedef void (*CuteQSSGStageGeneratorBaseCall5)(const void *, const QByteArray *, const QByteArray *, int *);
typedef void (*CuteQSSGStageGeneratorBaseCall6)(const void *, const QByteArray *, const QByteArray *, quint32, int *);
typedef void (*CuteQSSGStageGeneratorBaseCall7)(const void *, const QByteArray *, const QByteArray *, int *);
typedef void (*CuteQSSGStageGeneratorBaseCall8)(const void *, const QByteArray *, const QByteArray *, const QByteArray *, int *);
typedef void (*CuteQSSGStageGeneratorBaseCall9)(const void *, const QByteArray *, int *);
typedef void (*CuteQSSGStageGeneratorBaseCall10)(const void *, int *);
typedef void (*CuteQSSGStageGeneratorBaseCall11)(const void *, int *);
typedef void (*CuteQSSGStageGeneratorBaseCall12)(const void *, int *);
class CuteQSSGStageGeneratorBase : public QSSGStageGeneratorBase {
public:
  using QSSGStageGeneratorBase::QSSGStageGeneratorBase;
  CuteQSSGStageGeneratorBase(const QSSGStageGeneratorBase &other) : QSSGStageGeneratorBase(other) {}
  void *taken[13] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN22QSSGStageGeneratorBase5beginE6QFlagsI24QSSGShaderGeneratorStageE")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN22QSSGStageGeneratorBase11addIncomingERK10QByteArrayS2_")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN22QSSGStageGeneratorBase11addOutgoingERK10QByteArrayS2_")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN22QSSGStageGeneratorBase15addFlatIncomingERK10QByteArrayS2_")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN22QSSGStageGeneratorBase15addFlatOutgoingERK10QByteArrayS2_")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN22QSSGStageGeneratorBase10addUniformERK10QByteArrayS2_")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN22QSSGStageGeneratorBase15addUniformArrayERK10QByteArrayS2_j")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN22QSSGStageGeneratorBase17addConstantBufferERK10QByteArrayS2_")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN22QSSGStageGeneratorBase22addConstantBufferParamERK10QByteArrayS2_S2_")) {
      taken[8] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN22QSSGStageGeneratorBase6appendERK10QByteArray")) {
      taken[9] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN22QSSGStageGeneratorBase20addShaderIncomingMapEv")) {
      taken[10] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN22QSSGStageGeneratorBase19addShaderUniformMapEv")) {
      taken[11] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN22QSSGStageGeneratorBase20addShaderOutgoingMapEv")) {
      taken[12] = call;
      return true;
    }
    return false;
  }

  //  void QSSGStageGeneratorBase::begin(QSSGShaderGeneratorStageFlags
  //      inEnabledStages)
  void begin(QSSGShaderGeneratorStageFlags inEnabledStages) override {
    if (taken[0]) {
      int handled = 0;
      CuteQSSGStageGeneratorBaseCall0 call = reinterpret_cast<CuteQSSGStageGeneratorBaseCall0>(taken[0]);
      call(this, static_cast<int>(inEnabledStages.toInt()), &handled);
      if (handled) return;
    }
    QSSGStageGeneratorBase::begin(inEnabledStages);
  }

  //  void QSSGStageGeneratorBase::addIncoming(const QByteArray &name,
  //      const QByteArray &type)
  void addIncoming(const QByteArray &name, const QByteArray &type) override {
    if (taken[1]) {
      int handled = 0;
      CuteQSSGStageGeneratorBaseCall1 call = reinterpret_cast<CuteQSSGStageGeneratorBaseCall1>(taken[1]);
      call(this, &name, &type, &handled);
      if (handled) return;
    }
    QSSGStageGeneratorBase::addIncoming(name, type);
  }

  //  void QSSGStageGeneratorBase::addOutgoing(const QByteArray &name,
  //      const QByteArray &type)
  void addOutgoing(const QByteArray &name, const QByteArray &type) override {
    if (taken[2]) {
      int handled = 0;
      CuteQSSGStageGeneratorBaseCall2 call = reinterpret_cast<CuteQSSGStageGeneratorBaseCall2>(taken[2]);
      call(this, &name, &type, &handled);
      if (handled) return;
    }
    QSSGStageGeneratorBase::addOutgoing(name, type);
  }

  //  void QSSGStageGeneratorBase::addFlatIncoming(const QByteArray &name,
  //      const QByteArray &type)
  void addFlatIncoming(
      const QByteArray &name,
      const QByteArray &type) override {
    if (taken[3]) {
      int handled = 0;
      CuteQSSGStageGeneratorBaseCall3 call = reinterpret_cast<CuteQSSGStageGeneratorBaseCall3>(taken[3]);
      call(this, &name, &type, &handled);
      if (handled) return;
    }
    QSSGStageGeneratorBase::addFlatIncoming(name, type);
  }

  //  void QSSGStageGeneratorBase::addFlatOutgoing(const QByteArray &name,
  //      const QByteArray &type)
  void addFlatOutgoing(
      const QByteArray &name,
      const QByteArray &type) override {
    if (taken[4]) {
      int handled = 0;
      CuteQSSGStageGeneratorBaseCall4 call = reinterpret_cast<CuteQSSGStageGeneratorBaseCall4>(taken[4]);
      call(this, &name, &type, &handled);
      if (handled) return;
    }
    QSSGStageGeneratorBase::addFlatOutgoing(name, type);
  }

  //  void QSSGStageGeneratorBase::addUniform(const QByteArray &name, const
  //      QByteArray &type)
  void addUniform(const QByteArray &name, const QByteArray &type) override {
    if (taken[5]) {
      int handled = 0;
      CuteQSSGStageGeneratorBaseCall5 call = reinterpret_cast<CuteQSSGStageGeneratorBaseCall5>(taken[5]);
      call(this, &name, &type, &handled);
      if (handled) return;
    }
    QSSGStageGeneratorBase::addUniform(name, type);
  }

  //  void QSSGStageGeneratorBase::addUniformArray(const QByteArray &name,
  //      const QByteArray &type, quint32 size)
  void addUniformArray(
      const QByteArray &name,
      const QByteArray &type,
      quint32 size) override {
    if (taken[6]) {
      int handled = 0;
      CuteQSSGStageGeneratorBaseCall6 call = reinterpret_cast<CuteQSSGStageGeneratorBaseCall6>(taken[6]);
      call(this, &name, &type, size, &handled);
      if (handled) return;
    }
    QSSGStageGeneratorBase::addUniformArray(name, type, size);
  }

  //  void QSSGStageGeneratorBase::addConstantBuffer(const QByteArray
  //      &name, const QByteArray &layout)
  void addConstantBuffer(
      const QByteArray &name,
      const QByteArray &layout) override {
    if (taken[7]) {
      int handled = 0;
      CuteQSSGStageGeneratorBaseCall7 call = reinterpret_cast<CuteQSSGStageGeneratorBaseCall7>(taken[7]);
      call(this, &name, &layout, &handled);
      if (handled) return;
    }
    QSSGStageGeneratorBase::addConstantBuffer(name, layout);
  }

  //  void QSSGStageGeneratorBase::addConstantBufferParam(const QByteArray
  //      &cbName, const QByteArray &paramName, const QByteArray &type)
  void addConstantBufferParam(
      const QByteArray &cbName,
      const QByteArray &paramName,
      const QByteArray &type) override {
    if (taken[8]) {
      int handled = 0;
      CuteQSSGStageGeneratorBaseCall8 call = reinterpret_cast<CuteQSSGStageGeneratorBaseCall8>(taken[8]);
      call(this, &cbName, &paramName, &type, &handled);
      if (handled) return;
    }
    QSSGStageGeneratorBase::addConstantBufferParam(cbName, paramName, type);
  }

  //  void QSSGStageGeneratorBase::append(const QByteArray &data)
  void append(const QByteArray &data) override {
    if (taken[9]) {
      int handled = 0;
      CuteQSSGStageGeneratorBaseCall9 call = reinterpret_cast<CuteQSSGStageGeneratorBaseCall9>(taken[9]);
      call(this, &data, &handled);
      if (handled) return;
    }
    QSSGStageGeneratorBase::append(data);
  }

  //  void QSSGStageGeneratorBase::addShaderIncomingMap()
  void addShaderIncomingMap() override {
    if (taken[10]) {
      int handled = 0;
      CuteQSSGStageGeneratorBaseCall10 call = reinterpret_cast<CuteQSSGStageGeneratorBaseCall10>(taken[10]);
      call(this, &handled);
      if (handled) return;
    }
    QSSGStageGeneratorBase::addShaderIncomingMap();
  }

  //  void QSSGStageGeneratorBase::addShaderUniformMap()
  void addShaderUniformMap() override {
    if (taken[11]) {
      int handled = 0;
      CuteQSSGStageGeneratorBaseCall11 call = reinterpret_cast<CuteQSSGStageGeneratorBaseCall11>(taken[11]);
      call(this, &handled);
      if (handled) return;
    }
    QSSGStageGeneratorBase::addShaderUniformMap();
  }

  //  void QSSGStageGeneratorBase::addShaderOutgoingMap()
  void addShaderOutgoingMap() override {
    if (taken[12]) {
      int handled = 0;
      CuteQSSGStageGeneratorBaseCall12 call = reinterpret_cast<CuteQSSGStageGeneratorBaseCall12>(taken[12]);
      call(this, &handled);
      if (handled) return;
    }
    QSSGStageGeneratorBase::addShaderOutgoingMap();
  }
};

//  QSSGStageGeneratorBase::QSSGStageGeneratorBase(QSSGShaderGeneratorStage
//      inStage)
extern "C" Q_DECL_EXPORT
QSSGStageGeneratorBase *ritual_ZN22QSSGStageGeneratorBaseC1E24QSSGShaderGeneratorStage(
    QSSGShaderGeneratorStage inStage) {
  return new CuteQSSGStageGeneratorBase(inStage);
}

//  QSSGStageGeneratorBase::~QSSGStageGeneratorBase()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QSSGStageGeneratorBaseD1Ev(QSSGStageGeneratorBase *self) {
  delete self;
}

//  void QSSGStageGeneratorBase::begin(QSSGShaderGeneratorStageFlags
//      inEnabledStages)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QSSGStageGeneratorBase5beginE6QFlagsI24QSSGShaderGeneratorStageE(
    QSSGStageGeneratorBase *self,
    int inEnabledStages) {
  self->begin(QFlags<QSSGShaderGeneratorStage>::fromInt(inEnabledStages));
}

//  void QSSGStageGeneratorBase::addIncoming(const QByteArray &name, const
//      QByteArray &type)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QSSGStageGeneratorBase11addIncomingERK10QByteArrayS2_(
    QSSGStageGeneratorBase *self,
    const QByteArray *name,
    const QByteArray *type) {
  self->addIncoming(*name, *type);
}

//  void QSSGStageGeneratorBase::addOutgoing(const QByteArray &name, const
//      QByteArray &type)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QSSGStageGeneratorBase11addOutgoingERK10QByteArrayS2_(
    QSSGStageGeneratorBase *self,
    const QByteArray *name,
    const QByteArray *type) {
  self->addOutgoing(*name, *type);
}

//  void QSSGStageGeneratorBase::addFlatIncoming(const QByteArray &name,
//      const QByteArray &type)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QSSGStageGeneratorBase15addFlatIncomingERK10QByteArrayS2_(
    QSSGStageGeneratorBase *self,
    const QByteArray *name,
    const QByteArray *type) {
  self->addFlatIncoming(*name, *type);
}

//  void QSSGStageGeneratorBase::addFlatOutgoing(const QByteArray &name,
//      const QByteArray &type)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QSSGStageGeneratorBase15addFlatOutgoingERK10QByteArrayS2_(
    QSSGStageGeneratorBase *self,
    const QByteArray *name,
    const QByteArray *type) {
  self->addFlatOutgoing(*name, *type);
}

//  void QSSGStageGeneratorBase::addUniform(const QByteArray &name, const
//      QByteArray &type)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QSSGStageGeneratorBase10addUniformERK10QByteArrayS2_(
    QSSGStageGeneratorBase *self,
    const QByteArray *name,
    const QByteArray *type) {
  self->addUniform(*name, *type);
}

//  void QSSGStageGeneratorBase::addUniformArray(const QByteArray &name,
//      const QByteArray &type, quint32 size)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QSSGStageGeneratorBase15addUniformArrayERK10QByteArrayS2_j(
    QSSGStageGeneratorBase *self,
    const QByteArray *name,
    const QByteArray *type,
    quint32 size) {
  self->addUniformArray(*name, *type, size);
}

//  void QSSGStageGeneratorBase::addConstantBuffer(const QByteArray &name,
//      const QByteArray &layout)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QSSGStageGeneratorBase17addConstantBufferERK10QByteArrayS2_(
    QSSGStageGeneratorBase *self,
    const QByteArray *name,
    const QByteArray *layout) {
  self->addConstantBuffer(*name, *layout);
}

//  void QSSGStageGeneratorBase::addConstantBufferParam(const QByteArray
//      &cbName, const QByteArray &paramName, const QByteArray &type)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QSSGStageGeneratorBase22addConstantBufferParamERK10QByteArrayS2_S2_(
    QSSGStageGeneratorBase *self,
    const QByteArray *cbName,
    const QByteArray *paramName,
    const QByteArray *type) {
  self->addConstantBufferParam(*cbName, *paramName, *type);
}

//  void QSSGStageGeneratorBase::append(const QByteArray &data)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QSSGStageGeneratorBase6appendERK10QByteArray(
    QSSGStageGeneratorBase *self,
    const QByteArray *data) {
  self->append(*data);
}

//  QSSGShaderGeneratorStage QSSGStageGeneratorBase::stage() const
extern "C" Q_DECL_EXPORT
QSSGShaderGeneratorStage ritual_ZNK22QSSGStageGeneratorBase5stageEv(
    const QSSGStageGeneratorBase *self) {
  return self->stage();
}

//  void QSSGStageGeneratorBase::addShaderPass2Marker(ShaderItemType
//      itemType)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QSSGStageGeneratorBase20addShaderPass2MarkerENS_14ShaderItemTypeE(
    QSSGStageGeneratorBase *self,
    QSSGStageGeneratorBase::ShaderItemType itemType) {
  self->addShaderPass2Marker(itemType);
}

//  void QSSGStageGeneratorBase::addShaderIncomingMap()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QSSGStageGeneratorBase20addShaderIncomingMapEv(
    QSSGStageGeneratorBase *self) {
  self->addShaderIncomingMap();
}

//  void QSSGStageGeneratorBase::addShaderUniformMap()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QSSGStageGeneratorBase19addShaderUniformMapEv(
    QSSGStageGeneratorBase *self) {
  self->addShaderUniformMap();
}

//  void QSSGStageGeneratorBase::addShaderOutgoingMap()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QSSGStageGeneratorBase20addShaderOutgoingMapEv(
    QSSGStageGeneratorBase *self) {
  self->addShaderOutgoingMap();
}

//  void QSSGStageGeneratorBase::appendShaderCode()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QSSGStageGeneratorBase16appendShaderCodeEv(
    QSSGStageGeneratorBase *self) {
  self->appendShaderCode();
}

//  void QSSGStageGeneratorBase::addInclude(const QByteArray &name)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QSSGStageGeneratorBase10addIncludeERK10QByteArray(
    QSSGStageGeneratorBase *self,
    const QByteArray *name) {
  self->addInclude(*name);
}

//  void QSSGStageGeneratorBase::buildShaderSourcePass1(QSSGShaderResourceMer
//      geContext *mergeContext)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QSSGStageGeneratorBase22buildShaderSourcePass1EP30QSSGShaderResourceMergeContext(
    QSSGStageGeneratorBase *self,
    QSSGShaderResourceMergeContext *mergeContext) {
  self->buildShaderSourcePass1(mergeContext);
}

//  QByteArray QSSGStageGeneratorBase::buildShaderSourcePass2(QSSGShaderResou
//      rceMergeContext *mergeContext)
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZN22QSSGStageGeneratorBase22buildShaderSourcePass2EP30QSSGShaderResourceMergeContext(
    QSSGStageGeneratorBase *self,
    QSSGShaderResourceMergeContext *mergeContext) {
  return new QByteArray(self->buildShaderSourcePass2(mergeContext));
}

//  void QSSGStageGeneratorBase::addFunction(const QByteArray &functionName)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QSSGStageGeneratorBase11addFunctionERK10QByteArray(
    QSSGStageGeneratorBase *self,
    const QByteArray *functionName) {
  self->addFunction(*functionName);
}

//  void QSSGStageGeneratorBase::addDefinition(const QByteArray &name, const
//      QByteArray &value)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QSSGStageGeneratorBase13addDefinitionERK10QByteArrayS2_(
    QSSGStageGeneratorBase *self,
    const QByteArray *name,
    const QByteArray *value) {
  self->addDefinition(*name, *value);
}

//  void QSSGStageGeneratorBase::addTypeDeclaration(const QByteArray
//      &typeName, const QByteArray &snippet)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QSSGStageGeneratorBase18addTypeDeclarationERK10QByteArrayS2_(
    QSSGStageGeneratorBase *self,
    const QByteArray *typeName,
    const QByteArray *snippet) {
  self->addTypeDeclaration(*typeName, *snippet);
}

//  void QSSGStageGeneratorBase::addPrefix(const QByteArray &data)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QSSGStageGeneratorBase9addPrefixERK10QByteArray(
    QSSGStageGeneratorBase *self,
    const QByteArray *data) {
  self->addPrefix(*data);
}

//  a Python function taken by a CuteQSSGStageGeneratorBase, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QSSGStageGeneratorBase(
    QSSGStageGeneratorBase *self,
    const char *key,
    void *call) {
  return static_cast<CuteQSSGStageGeneratorBase *>(self)->take(key, call);
}

//  void QSSGStageGeneratorBase::begin(QSSGShaderGeneratorStageFlags
//      inEnabledStages)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN22QSSGStageGeneratorBase5beginE6QFlagsI24QSSGShaderGeneratorStageE(
    QSSGStageGeneratorBase *self,
    int inEnabledStages) {
  self->QSSGStageGeneratorBase::begin(
      QFlags<QSSGShaderGeneratorStage>::fromInt(inEnabledStages));
}

//  void QSSGStageGeneratorBase::addIncoming(const QByteArray &name, const
//      QByteArray &type)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN22QSSGStageGeneratorBase11addIncomingERK10QByteArrayS2_(
    QSSGStageGeneratorBase *self,
    const QByteArray *name,
    const QByteArray *type) {
  self->QSSGStageGeneratorBase::addIncoming(*name, *type);
}

//  void QSSGStageGeneratorBase::addOutgoing(const QByteArray &name, const
//      QByteArray &type)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN22QSSGStageGeneratorBase11addOutgoingERK10QByteArrayS2_(
    QSSGStageGeneratorBase *self,
    const QByteArray *name,
    const QByteArray *type) {
  self->QSSGStageGeneratorBase::addOutgoing(*name, *type);
}

//  void QSSGStageGeneratorBase::addFlatIncoming(const QByteArray &name,
//      const QByteArray &type)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN22QSSGStageGeneratorBase15addFlatIncomingERK10QByteArrayS2_(
    QSSGStageGeneratorBase *self,
    const QByteArray *name,
    const QByteArray *type) {
  self->QSSGStageGeneratorBase::addFlatIncoming(*name, *type);
}

//  void QSSGStageGeneratorBase::addFlatOutgoing(const QByteArray &name,
//      const QByteArray &type)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN22QSSGStageGeneratorBase15addFlatOutgoingERK10QByteArrayS2_(
    QSSGStageGeneratorBase *self,
    const QByteArray *name,
    const QByteArray *type) {
  self->QSSGStageGeneratorBase::addFlatOutgoing(*name, *type);
}

//  void QSSGStageGeneratorBase::addUniform(const QByteArray &name, const
//      QByteArray &type)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN22QSSGStageGeneratorBase10addUniformERK10QByteArrayS2_(
    QSSGStageGeneratorBase *self,
    const QByteArray *name,
    const QByteArray *type) {
  self->QSSGStageGeneratorBase::addUniform(*name, *type);
}

//  void QSSGStageGeneratorBase::addUniformArray(const QByteArray &name,
//      const QByteArray &type, quint32 size)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN22QSSGStageGeneratorBase15addUniformArrayERK10QByteArrayS2_j(
    QSSGStageGeneratorBase *self,
    const QByteArray *name,
    const QByteArray *type,
    quint32 size) {
  self->QSSGStageGeneratorBase::addUniformArray(*name, *type, size);
}

//  void QSSGStageGeneratorBase::addConstantBuffer(const QByteArray &name,
//      const QByteArray &layout)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN22QSSGStageGeneratorBase17addConstantBufferERK10QByteArrayS2_(
    QSSGStageGeneratorBase *self,
    const QByteArray *name,
    const QByteArray *layout) {
  self->QSSGStageGeneratorBase::addConstantBuffer(*name, *layout);
}

//  void QSSGStageGeneratorBase::addConstantBufferParam(const QByteArray
//      &cbName, const QByteArray &paramName, const QByteArray &type)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN22QSSGStageGeneratorBase22addConstantBufferParamERK10QByteArrayS2_S2_(
    QSSGStageGeneratorBase *self,
    const QByteArray *cbName,
    const QByteArray *paramName,
    const QByteArray *type) {
  self->QSSGStageGeneratorBase::addConstantBufferParam(
      *cbName,
      *paramName,
      *type);
}

//  void QSSGStageGeneratorBase::append(const QByteArray &data)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN22QSSGStageGeneratorBase6appendERK10QByteArray(
    QSSGStageGeneratorBase *self,
    const QByteArray *data) {
  self->QSSGStageGeneratorBase::append(*data);
}

//  void QSSGStageGeneratorBase::addShaderIncomingMap()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN22QSSGStageGeneratorBase20addShaderIncomingMapEv(
    QSSGStageGeneratorBase *self) {
  self->QSSGStageGeneratorBase::addShaderIncomingMap();
}

//  void QSSGStageGeneratorBase::addShaderUniformMap()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN22QSSGStageGeneratorBase19addShaderUniformMapEv(
    QSSGStageGeneratorBase *self) {
  self->QSSGStageGeneratorBase::addShaderUniformMap();
}

//  void QSSGStageGeneratorBase::addShaderOutgoingMap()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN22QSSGStageGeneratorBase20addShaderOutgoingMapEv(
    QSSGStageGeneratorBase *self) {
  self->QSSGStageGeneratorBase::addShaderOutgoingMap();
}
