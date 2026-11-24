//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/private/qtextengine_p.h, Qt 6.12.0. Changes made here
//  are lost.
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/private/qtextengine_p.h>
#include <QtGui/6.12.0/QtGui/private/qfixed_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  QScriptItem::QScriptItem(int p, QScriptAnalysis a)
extern "C" Q_DECL_EXPORT
QScriptItem *ritual_ZN11QScriptItemC1Ei15QScriptAnalysis(
    int p,
    const QScriptAnalysis *a) {
  return new QScriptItem(p, *a);
}

//  QFixed QScriptItem::height() const
extern "C" Q_DECL_EXPORT
QFixed *ritual_ZNK11QScriptItem6heightEv(const QScriptItem *self) {
  return new QFixed(self->height());
}

//  QScriptItem::QScriptItem()
extern "C" Q_DECL_EXPORT
QScriptItem *ritual_ZN11QScriptItemC1Ev() {
  return new QScriptItem();
}

//  QScriptItem::~QScriptItem()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QScriptItemD1Ev(QScriptItem *self) {
  delete self;
}
