//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/6.12.0/QtQuick/private/qsgrhishadereffectnode_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qsgrhishadereffectnode_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  bool QSGRhiShaderLinker::Constant::operator==(const Constant &other)
//      const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK18QSGRhiShaderLinker8ConstanteqERKS0_(
    const QSGRhiShaderLinker::Constant *self,
    const QSGRhiShaderLinker::Constant *other) {
  return self->operator==(*other);
}

//  QSGRhiShaderLinker::Constant::~Constant()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QSGRhiShaderLinker8ConstantD1Ev(
    QSGRhiShaderLinker::Constant *self) {
  delete self;
}
