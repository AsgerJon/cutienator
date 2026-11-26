//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qqmlirbuilder_p.h, Qt 6.12.0. Edited by hand
//  on 2026-11-25: added by hand, rituals for functions the generator leaves
//  out: 1. Kept as it is when the generator runs again.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qqmlirbuilder_p.h>
#include <cstring>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  void QmlIR::QmlUnitGenerator::generate(Document &output, const
//      QV4::CompiledData::DependentTypesHasher &dependencyHasher)
extern "C" Q_DECL_EXPORT
void ritual_ZN5QmlIR16QmlUnitGenerator8generateERNS_8DocumentERKSt8functionIF10QByteArrayvEE(
    QmlIR::QmlUnitGenerator *self,
    QmlIR::Document *output,
    const QV4::CompiledData::DependentTypesHasher *dependencyHasher) {
  self->generate(*output, *dependencyHasher);
}

//  QmlIR::QmlUnitGenerator::~QmlUnitGenerator()
extern "C" Q_DECL_EXPORT
void ritual_ZN5QmlIR16QmlUnitGeneratorD1Ev(QmlIR::QmlUnitGenerator *self) {
  delete self;
}

//  char *QmlIR::QmlUnitGenerator::writeBindings(char *bindingPtr, const
//      Object *o, BindingFilter filter) const
extern "C" Q_DECL_EXPORT
char *ritual_ZNK5QmlIR16QmlUnitGenerator13writeBindingsEPcPKNS_6ObjectEMNS_7BindingEKFbvE(
    const QmlIR::QmlUnitGenerator *self,
    char *bindingPtr,
    const QmlIR::Object *o,
    const char *filter) {
  static const struct {
    const char *name;
    QmlIR::QmlUnitGenerator::BindingFilter member;
  } known[] = {
      {"isValueBindingNoAlias", &QV4::CompiledData::Binding::isValueBindingNoAlias},
      {"isSignalHandler", &QV4::CompiledData::Binding::isSignalHandler},
      {"isAttachedProperty", &QV4::CompiledData::Binding::isAttachedProperty},
      {"isGroupProperty", &QV4::CompiledData::Binding::isGroupProperty},
      {"isValueBindingToAlias", &QV4::CompiledData::Binding::isValueBindingToAlias},
  };
  for (const auto &one : known) {
    if (!std::strcmp(one.name, filter)) {
      return self->writeBindings(bindingPtr, o, one.member);
    }
  }
  qFatal("no member function named %s here", filter);
}
