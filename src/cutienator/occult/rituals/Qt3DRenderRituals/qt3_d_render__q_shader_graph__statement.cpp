//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DRender/6.12.0/Qt3DRender/private/qshadergraph_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <Qt3DRender/6.12.0/Qt3DRender/private/qt3drender_global_p.h>
#include <Qt3DRender/Qt3DRender>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DRender/6.12.0/Qt3DRender/private/qshadergraph_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/quuid.h>
#include <QtCore/qstring.h>

//  QUuid Qt3DRender::QShaderGraph::Statement::uuid() const
extern "C" Q_DECL_EXPORT
QUuid *ritual_ZNK10Qt3DRender12QShaderGraph9Statement4uuidEv(
    const Qt3DRender::QShaderGraph::Statement *self) {
  return new QUuid(self->uuid());
}

//  int
//      Qt3DRender::QShaderGraph::Statement::portIndex(QShaderNodePort::Direc
//      tion direction, const QString &portName) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK10Qt3DRender12QShaderGraph9Statement9portIndexENS_15QShaderNodePort9DirectionERK7QString(
    const Qt3DRender::QShaderGraph::Statement *self,
    Qt3DRender::QShaderNodePort::Direction direction,
    const QString *portName) {
  return self->portIndex(direction, *portName);
}

//  Qt3DRender::QShaderGraph::Statement::~Statement()
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender12QShaderGraph9StatementD1Ev(
    Qt3DRender::QShaderGraph::Statement *self) {
  delete self;
}
