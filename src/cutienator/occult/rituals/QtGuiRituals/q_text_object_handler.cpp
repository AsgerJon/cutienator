//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/private/qabstracttextdocumentlayout_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/private/qabstracttextdocumentlayout_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  QTextObjectHandler::QTextObjectHandler()
extern "C" Q_DECL_EXPORT
QTextObjectHandler *ritual_ZN18QTextObjectHandlerC1Ev() {
  return new QTextObjectHandler();
}

//  QTextObjectHandler::~QTextObjectHandler()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QTextObjectHandlerD1Ev(QTextObjectHandler *self) {
  delete self;
}
