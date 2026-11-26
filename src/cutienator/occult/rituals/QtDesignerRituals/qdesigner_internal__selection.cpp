//  Written by dev_tooling.RitualGenerator from the records of
//  QtDesigner/6.12.0/QtDesigner/private/qdesigner_objectinspector_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtDesigner/QtDesigner>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtDesigner/6.12.0/QtDesigner/private/qdesigner_objectinspector_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qobject.h>
#include <QtCore/qlist.h>

//  bool qdesigner_internal::Selection::empty() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK18qdesigner_internal9Selection5emptyEv(
    const qdesigner_internal::Selection *self) {
  return self->empty();
}

//  void qdesigner_internal::Selection::clear()
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal9Selection5clearEv(
    qdesigner_internal::Selection *self) {
  self->clear();
}

//  QObjectList qdesigner_internal::Selection::selection() const
extern "C" Q_DECL_EXPORT
QList<QObject *> *ritual_ZNK18qdesigner_internal9Selection9selectionEv(
    const qdesigner_internal::Selection *self) {
  return new QList<QObject *>(self->selection());
}

//  qdesigner_internal::Selection::~Selection()
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal9SelectionD1Ev(
    qdesigner_internal::Selection *self) {
  delete self;
}
