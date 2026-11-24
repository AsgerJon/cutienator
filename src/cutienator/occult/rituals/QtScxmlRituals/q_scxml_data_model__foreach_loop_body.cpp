//  Written by dev_tooling.RitualGenerator from the records of
//  QtScxml/qscxmldatamodel.h, Qt 6.12.0. Changes made here are lost.
#include <QtScxml/qscxmldatamodel.h>

//  QScxmlDataModel::ForeachLoopBody::~ForeachLoopBody()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QScxmlDataModel15ForeachLoopBodyD1Ev(
    QScxmlDataModel::ForeachLoopBody *self) {
  delete self;
}

//  void QScxmlDataModel::ForeachLoopBody::run(bool *ok)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QScxmlDataModel15ForeachLoopBody3runEPb(
    QScxmlDataModel::ForeachLoopBody *self,
    bool *ok) {
  self->run(ok);
}
