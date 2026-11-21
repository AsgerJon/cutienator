//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/qdebug.h, Qt 6.12.0. Changes made here are lost.
#include <QtCore/qdebug.h>

//  QDebug::QDebug(QIODevice *device)
extern "C" Q_DECL_EXPORT
QDebug *ritual_ZN6QDebugC1EP9QIODevice(QIODevice *device) {
  return new QDebug(device);
}

//  QDebug::QDebug(QString *string)
extern "C" Q_DECL_EXPORT
QDebug *ritual_ZN6QDebugC1EP7QString(QString *string) {
  return new QDebug(string);
}

//  QDebug::QDebug(QByteArray *bytes)
extern "C" Q_DECL_EXPORT
QDebug *ritual_ZN6QDebugC1EP10QByteArray(QByteArray *bytes) {
  return new QDebug(bytes);
}

//  QDebug::QDebug(QtMsgType t)
extern "C" Q_DECL_EXPORT
QDebug *ritual_ZN6QDebugC1E9QtMsgType(QtMsgType t) {
  return new QDebug(t);
}

//  QDebug::QDebug(const QDebug &o)
extern "C" Q_DECL_EXPORT
QDebug *ritual_ZN6QDebugC1ERKS_(const QDebug *o) {
  return new QDebug(*o);
}

//  QDebug::~QDebug()
extern "C" Q_DECL_EXPORT
void ritual_ZN6QDebugD1Ev(QDebug *self) {
  delete self;
}

//  int QDebug::verbosity() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK6QDebug9verbosityEv(const QDebug *self) {
  return self->verbosity();
}

//  void QDebug::setVerbosity(int verbosityLevel)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QDebug12setVerbosityEi(QDebug *self, int verbosityLevel) {
  self->setVerbosity(verbosityLevel);
}

//  bool QDebug::autoInsertSpaces() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK6QDebug16autoInsertSpacesEv(const QDebug *self) {
  return self->autoInsertSpaces();
}

//  void QDebug::setAutoInsertSpaces(bool b)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QDebug19setAutoInsertSpacesEb(QDebug *self, bool b) {
  self->setAutoInsertSpaces(b);
}

//  bool QDebug::quoteStrings() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK6QDebug12quoteStringsEv(const QDebug *self) {
  return self->quoteStrings();
}

//  void QDebug::setQuoteStrings(bool b)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QDebug15setQuoteStringsEb(QDebug *self, bool b) {
  self->setQuoteStrings(b);
}
