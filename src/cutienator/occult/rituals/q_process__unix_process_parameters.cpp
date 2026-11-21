//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/qprocess.h, Qt 6.12.0. Changes made here are lost.
#include <QtCore/qprocess.h>

//  QProcess::UnixProcessParameters::~UnixProcessParameters()
extern "C" Q_DECL_EXPORT
void ritual_ZN8QProcess21UnixProcessParametersD1Ev(
    QProcess::UnixProcessParameters *self) {
  delete self;
}
