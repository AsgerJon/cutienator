//  Written by dev_tooling.RitualGenerator from the records of
//  QtPdf/6.12.0/QtPdf/private/qpdflinkmodel_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtPdf/6.12.0/QtPdf/private/qtpdfglobal_p.h>
#include <QtPdf/qpdflinkmodel.h>
#include <QtPdf/QtPdf>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtPdf/6.12.0/QtPdf/private/qpdflinkmodel_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  QPdfLinkModel *QPdfLinkModelPrivate::q_func()
extern "C" Q_DECL_EXPORT
QPdfLinkModel *ritual_ZN20QPdfLinkModelPrivate6q_funcEv(
    QPdfLinkModelPrivate *self) {
  return self->q_func();
}

//  const QPdfLinkModel *QPdfLinkModelPrivate::q_func() const
extern "C" Q_DECL_EXPORT
const QPdfLinkModel *ritual_ZNK20QPdfLinkModelPrivate6q_funcEv(
    const QPdfLinkModelPrivate *self) {
  return self->q_func();
}

//  QPdfLinkModelPrivate::QPdfLinkModelPrivate(QPdfLinkModel *qq)
extern "C" Q_DECL_EXPORT
QPdfLinkModelPrivate *ritual_ZN20QPdfLinkModelPrivateC1EP13QPdfLinkModel(
    QPdfLinkModel *qq) {
  return new QPdfLinkModelPrivate(qq);
}

//  QPdfLinkModelPrivate::~QPdfLinkModelPrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QPdfLinkModelPrivateD1Ev(QPdfLinkModelPrivate *self) {
  delete self;
}
