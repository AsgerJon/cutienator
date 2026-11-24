//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/private/qabstracttextdocumentlayout_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#include <QtGui/qabstracttextdocumentlayout.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/private/qabstracttextdocumentlayout_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qsize.h>

//  QAbstractTextDocumentLayout *QAbstractTextDocumentLayoutPrivate::q_func()
extern "C" Q_DECL_EXPORT
QAbstractTextDocumentLayout *ritual_ZN34QAbstractTextDocumentLayoutPrivate6q_funcEv(
    QAbstractTextDocumentLayoutPrivate *self) {
  return self->q_func();
}

//  const QAbstractTextDocumentLayout
//      *QAbstractTextDocumentLayoutPrivate::q_func() const
extern "C" Q_DECL_EXPORT
const QAbstractTextDocumentLayout *ritual_ZNK34QAbstractTextDocumentLayoutPrivate6q_funcEv(
    const QAbstractTextDocumentLayoutPrivate *self) {
  return self->q_func();
}

//  QAbstractTextDocumentLayoutPrivate::QAbstractTextDocumentLayoutPrivate()
extern "C" Q_DECL_EXPORT
QAbstractTextDocumentLayoutPrivate *ritual_ZN34QAbstractTextDocumentLayoutPrivateC1Ev() {
  return new QAbstractTextDocumentLayoutPrivate();
}

//  QAbstractTextDocumentLayoutPrivate::~QAbstractTextDocumentLayoutPrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN34QAbstractTextDocumentLayoutPrivateD1Ev(
    QAbstractTextDocumentLayoutPrivate *self) {
  delete self;
}

//  void QAbstractTextDocumentLayoutPrivate::setDocument(QTextDocument *doc)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QAbstractTextDocumentLayoutPrivate11setDocumentEP13QTextDocument(
    QAbstractTextDocumentLayoutPrivate *self,
    QTextDocument *doc) {
  self->setDocument(doc);
}

//  QAbstractTextDocumentLayoutPrivate
//      *QAbstractTextDocumentLayoutPrivate::get(QAbstractTextDocumentLayout
//      *layout)
extern "C" Q_DECL_EXPORT
QAbstractTextDocumentLayoutPrivate *ritual_ZN34QAbstractTextDocumentLayoutPrivate3getEP27QAbstractTextDocumentLayout(
    QAbstractTextDocumentLayout *layout) {
  return QAbstractTextDocumentLayoutPrivate::get(layout);
}

//  bool QAbstractTextDocumentLayoutPrivate::hasHandlers() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK34QAbstractTextDocumentLayoutPrivate11hasHandlersEv(
    const QAbstractTextDocumentLayoutPrivate *self) {
  return self->hasHandlers();
}

//  int QAbstractTextDocumentLayoutPrivate::_q_dynamicPageCountSlot() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK34QAbstractTextDocumentLayoutPrivate23_q_dynamicPageCountSlotEv(
    const QAbstractTextDocumentLayoutPrivate *self) {
  return self->_q_dynamicPageCountSlot();
}

//  QSizeF QAbstractTextDocumentLayoutPrivate::_q_dynamicDocumentSizeSlot()
//      const
extern "C" Q_DECL_EXPORT
QSizeF *ritual_ZNK34QAbstractTextDocumentLayoutPrivate26_q_dynamicDocumentSizeSlotEv(
    const QAbstractTextDocumentLayoutPrivate *self) {
  return new QSizeF(self->_q_dynamicDocumentSizeSlot());
}

//  void QAbstractTextDocumentLayoutPrivate::_q_handlerDestroyed(QObject
//      *obj)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QAbstractTextDocumentLayoutPrivate19_q_handlerDestroyedEP7QObject(
    QAbstractTextDocumentLayoutPrivate *self,
    QObject *obj) {
  self->_q_handlerDestroyed(obj);
}
