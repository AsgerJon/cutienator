//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DRender/6.12.0/Qt3DRender/private/qshadernode_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <Qt3DRender/6.12.0/Qt3DRender/private/qt3drender_global_p.h>
#include <Qt3DRender/Qt3DRender>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DRender/6.12.0/Qt3DRender/private/qshadernode_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qbytearray.h>
#include <QtCore/qlist.h>

//  Qt3DRender::QShaderNode::Rule::Rule(const QByteArray &substitution, const
//      QByteArrayList &headerSnippets)
extern "C" Q_DECL_EXPORT
Qt3DRender::QShaderNode::Rule *ritual_ZN10Qt3DRender11QShaderNode4RuleC1ERK10QByteArrayRK5QListIS2_E(
    const QByteArray *substitution,
    const QList<QByteArray> *headerSnippets) {
  return new Qt3DRender::QShaderNode::Rule(*substitution, *headerSnippets);
}

//  Qt3DRender::QShaderNode::Rule::~Rule()
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender11QShaderNode4RuleD1Ev(
    Qt3DRender::QShaderNode::Rule *self) {
  delete self;
}
