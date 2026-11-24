//  Written by dev_tooling.RitualGenerator from the records of
//  QtDesigner/6.12.0/QtDesigner/private/qdesigner_utils_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtDesigner/QtDesigner>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtDesigner/6.12.0/QtDesigner/private/qdesigner_utils_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>

//  qdesigner_internal::DesignerMetaEnum::DesignerMetaEnum()
extern "C" Q_DECL_EXPORT
qdesigner_internal::DesignerMetaEnum *ritual_ZN18qdesigner_internal16DesignerMetaEnumC1Ev() {
  return new qdesigner_internal::DesignerMetaEnum();
}

//  int qdesigner_internal::DesignerMetaEnum::parseEnum(const QString &s,
//      bool *ok) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK18qdesigner_internal16DesignerMetaEnum9parseEnumERK7QStringPb(
    const qdesigner_internal::DesignerMetaEnum *self,
    const QString *s,
    bool *ok) {
  return self->parseEnum(*s, ok);
}

//  qdesigner_internal::DesignerMetaEnum::~DesignerMetaEnum()
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal16DesignerMetaEnumD1Ev(
    qdesigner_internal::DesignerMetaEnum *self) {
  delete self;
}
