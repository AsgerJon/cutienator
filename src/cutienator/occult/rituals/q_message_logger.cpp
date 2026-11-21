//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/qlogging.h, Qt 6.12.0. Changes made here are lost.
#include <QtCore/QtCore>
#include <QtCore/qtestsupport_core.h>
#include <QtCore/qtmochelpers.h>
#include <QtCore/qdebug.h>

//  QMessageLogger::QMessageLogger()
extern "C" Q_DECL_EXPORT
QMessageLogger *ritual_ZN14QMessageLoggerC1Ev() {
  return new QMessageLogger();
}

//  QMessageLogger::QMessageLogger(const char *file, int line, const char
//      *function)
extern "C" Q_DECL_EXPORT
QMessageLogger *ritual_ZN14QMessageLoggerC1EPKciS1_(
    const char *file,
    int line,
    const char *function) {
  return new QMessageLogger(file, line, function);
}

//  QMessageLogger::QMessageLogger(const char *file, int line, const char
//      *function, const char *category)
extern "C" Q_DECL_EXPORT
QMessageLogger *ritual_ZN14QMessageLoggerC1EPKciS1_S1_(
    const char *file,
    int line,
    const char *function,
    const char *category) {
  return new QMessageLogger(file, line, function, category);
}

//  QDebug QMessageLogger::debug() const
extern "C" Q_DECL_EXPORT
QDebug *ritual_ZNK14QMessageLogger5debugEv(const QMessageLogger *self) {
  return new QDebug(self->debug());
}

//  QDebug QMessageLogger::info() const
extern "C" Q_DECL_EXPORT
QDebug *ritual_ZNK14QMessageLogger4infoEv(const QMessageLogger *self) {
  return new QDebug(self->info());
}

//  QDebug QMessageLogger::warning() const
extern "C" Q_DECL_EXPORT
QDebug *ritual_ZNK14QMessageLogger7warningEv(const QMessageLogger *self) {
  return new QDebug(self->warning());
}

//  QDebug QMessageLogger::critical() const
extern "C" Q_DECL_EXPORT
QDebug *ritual_ZNK14QMessageLogger8criticalEv(const QMessageLogger *self) {
  return new QDebug(self->critical());
}

//  QDebug QMessageLogger::fatal() const
extern "C" Q_DECL_EXPORT
QDebug *ritual_ZNK14QMessageLogger5fatalEv(const QMessageLogger *self) {
  return new QDebug(self->fatal());
}
