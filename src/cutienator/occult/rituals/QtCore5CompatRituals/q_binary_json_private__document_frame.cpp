//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore5Compat/6.12.0/QtCore5Compat/private/qbinaryjson_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtCore5Compat/QtCore5Compat>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore5Compat/6.12.0/QtCore5Compat/private/qbinaryjson_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>

//  QBinaryJsonPrivate::DocumentFrame::DocumentFrame(const Base *b, QString
//      k)
extern "C" Q_DECL_EXPORT
QBinaryJsonPrivate::DocumentFrame *ritual_ZN18QBinaryJsonPrivate13DocumentFrameC1EPKNS_4BaseE7QString(
    const QBinaryJsonPrivate::Base *b,
    const QString *k) {
  return new QBinaryJsonPrivate::DocumentFrame(b, *k);
}

//  QBinaryJsonPrivate::DocumentFrame::~DocumentFrame()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QBinaryJsonPrivate13DocumentFrameD1Ev(
    QBinaryJsonPrivate::DocumentFrame *self) {
  delete self;
}
