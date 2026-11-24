//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/private/qtextobject_p.h, Qt 6.12.0. Changes made here
//  are lost.
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#include <QtGui/qtextobject.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/private/qtextobject_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  QTextObject *QTextObjectPrivate::q_func()
extern "C" Q_DECL_EXPORT
QTextObject *ritual_ZN18QTextObjectPrivate6q_funcEv(
    QTextObjectPrivate *self) {
  return self->q_func();
}

//  const QTextObject *QTextObjectPrivate::q_func() const
extern "C" Q_DECL_EXPORT
const QTextObject *ritual_ZNK18QTextObjectPrivate6q_funcEv(
    const QTextObjectPrivate *self) {
  return self->q_func();
}

//  QTextObjectPrivate::QTextObjectPrivate(QTextDocument *doc)
extern "C" Q_DECL_EXPORT
QTextObjectPrivate *ritual_ZN18QTextObjectPrivateC1EP13QTextDocument(
    QTextDocument *doc) {
  return new QTextObjectPrivate(doc);
}
