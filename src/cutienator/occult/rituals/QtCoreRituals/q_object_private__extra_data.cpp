//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/6.12.0/QtCore/private/qobject_p.h, Qt 6.12.0. Changes made here
//  are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtCore/QtCore>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/6.12.0/QtCore/private/qobject_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>

//  QObjectPrivate::ExtraData::ExtraData(QObjectPrivate *ptr)
extern "C" Q_DECL_EXPORT
QObjectPrivate::ExtraData *ritual_ZN14QObjectPrivate9ExtraDataC1EPS_(
    QObjectPrivate *ptr) {
  return new QObjectPrivate::ExtraData(ptr);
}

//  void QObjectPrivate::ExtraData::setObjectNameForwarder(const QString
//      &name)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QObjectPrivate9ExtraData22setObjectNameForwarderERK7QString(
    QObjectPrivate::ExtraData *self,
    const QString *name) {
  self->setObjectNameForwarder(*name);
}

//  void QObjectPrivate::ExtraData::nameChangedForwarder(const QString &name)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QObjectPrivate9ExtraData20nameChangedForwarderERK7QString(
    QObjectPrivate::ExtraData *self,
    const QString *name) {
  self->nameChangedForwarder(*name);
}

//  QObjectPrivate::ExtraData::~ExtraData()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QObjectPrivate9ExtraDataD1Ev(
    QObjectPrivate::ExtraData *self) {
  delete self;
}
