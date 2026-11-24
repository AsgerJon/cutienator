//  Written by dev_tooling.RitualGenerator from the records of
//  QtDesigner/6.12.0/QtDesigner/private/actionrepository_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtDesigner/QtDesigner>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtDesigner/6.12.0/QtDesigner/private/actionrepository_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qabstractitemmodel.h>

//  const QMetaObject *qdesigner_internal::ActionModel::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK18qdesigner_internal11ActionModel10metaObjectEv(
    const qdesigner_internal::ActionModel *self) {
  return self->metaObject();
}

//  QString qdesigner_internal::ActionModel::tr(const char *s, const char *c,
//      int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN18qdesigner_internal11ActionModel2trEPKcS2_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(qdesigner_internal::ActionModel::tr(s, c, n));
}

//  void
//      qdesigner_internal::ActionModel::initialize(QDesignerFormEditorInterf
//      ace *core)
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal11ActionModel10initializeEP28QDesignerFormEditorInterface(
    qdesigner_internal::ActionModel *self,
    QDesignerFormEditorInterface *core) {
  self->initialize(core);
}

//  bool qdesigner_internal::ActionModel::dropMimeData(const QMimeData *data,
//      Qt::DropAction action, int row, int column, const QModelIndex
//      &parent)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN18qdesigner_internal11ActionModel12dropMimeDataEPK9QMimeDataN2Qt10DropActionEiiRK11QModelIndex(
    qdesigner_internal::ActionModel *self,
    const QMimeData *data,
    Qt::DropAction action,
    int row,
    int column,
    const QModelIndex *parent) {
  return self->qdesigner_internal::ActionModel::dropMimeData(
      data,
      action,
      row,
      column,
      *parent);
}
