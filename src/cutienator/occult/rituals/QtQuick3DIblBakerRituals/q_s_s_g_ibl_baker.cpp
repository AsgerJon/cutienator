//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick3DIblBaker/6.12.0/QtQuick3DIblBaker/private/qssgiblbaker_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtQuick3DIblBaker/QtQuick3DIblBaker>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick3DIblBaker/6.12.0/QtQuick3DIblBaker/private/qssgiblbaker_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qlist.h>

//  const QStringList QSSGIblBaker::inputExtensions() const
extern "C" Q_DECL_EXPORT
QList<QString> *ritual_ZNK12QSSGIblBaker15inputExtensionsEv(
    const QSSGIblBaker *self) {
  return new QList<QString>(self->inputExtensions());
}

//  const QString QSSGIblBaker::outputExtension() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK12QSSGIblBaker15outputExtensionEv(
    const QSSGIblBaker *self) {
  return new QString(self->outputExtension());
}

//  QSSGIblBaker::~QSSGIblBaker()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QSSGIblBakerD1Ev(QSSGIblBaker *self) {
  delete self;
}
