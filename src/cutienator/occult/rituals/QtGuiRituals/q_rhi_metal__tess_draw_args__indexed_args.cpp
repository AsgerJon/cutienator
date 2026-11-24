//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/private/qrhimetal_p.h, Qt 6.12.0. Changes made here
//  are lost.
#include <QtGui/qtguiglobal.h>
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#if QT_CONFIG(metal)
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/private/qrhimetal_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  QRhiMetal::TessDrawArgs::IndexedArgs::~IndexedArgs()
extern "C" Q_DECL_EXPORT
void ritual_ZN9QRhiMetal12TessDrawArgs11IndexedArgsD1Ev(
    QRhiMetal::TessDrawArgs::IndexedArgs *self) {
  delete self;
}

#endif  // QT_CONFIG(metal)
