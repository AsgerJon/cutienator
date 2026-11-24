//  Written by dev_tooling.RitualGenerator from the records of
//  QtDesigner/6.12.0/QtDesigner/private/actionrepository_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtDesigner/QtDesigner>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtDesigner/6.12.0/QtDesigner/private/actionrepository_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtGui/qaction.h>
#include <QtCore/qlist.h>

//  const QMetaObject
//      *qdesigner_internal::ActionRepositoryMimeData::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK18qdesigner_internal24ActionRepositoryMimeData10metaObjectEv(
    const qdesigner_internal::ActionRepositoryMimeData *self) {
  return self->metaObject();
}

//  QString qdesigner_internal::ActionRepositoryMimeData::tr(const char *s,
//      const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN18qdesigner_internal24ActionRepositoryMimeData2trEPKcS2_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(
      qdesigner_internal::ActionRepositoryMimeData::tr(
          s,
          c,
          n));
}

//  const ActionList
//      &qdesigner_internal::ActionRepositoryMimeData::actionList() const
extern "C" Q_DECL_EXPORT
QList<QAction *> *ritual_ZNK18qdesigner_internal24ActionRepositoryMimeData10actionListEv(
    const qdesigner_internal::ActionRepositoryMimeData *self) {
  return new QList<QAction *>(self->actionList());
}
