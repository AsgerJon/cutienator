//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/qprocess.h, Qt 6.12.0. Changes made here are lost.
#include <QtCore/qglobal.h>
#if (QT_CONFIG(processenvironment)) || (!QT_CONFIG(process))
#if QT_CONFIG(processenvironment)
#if QT_CONFIG(process)
#if defined(Q_OS_UNIX) || defined(Q_QDOC)
#include <QtCore/qprocess.h>

//  QProcess::UnixProcessParameters::~UnixProcessParameters()
extern "C" Q_DECL_EXPORT
void ritual_ZN8QProcess21UnixProcessParametersD1Ev(
    QProcess::UnixProcessParameters *self) {
  delete self;
}

#endif  // defined(Q_OS_UNIX) || defined(Q_QDOC)
#endif  // QT_CONFIG(process)
#endif  // QT_CONFIG(processenvironment)
#endif  // (QT_CONFIG(processenvironment)) || (!QT_CONFIG(process))
