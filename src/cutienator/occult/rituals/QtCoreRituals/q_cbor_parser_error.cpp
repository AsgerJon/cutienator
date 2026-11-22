//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/qcborvalue.h, Qt 6.12.0. Changes made here are lost.
#include <QtCore/qcborvalue.h>
#include <QtCore/qstring.h>

//  QString QCborParserError::errorString() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK16QCborParserError11errorStringEv(
    const QCborParserError *self) {
  return new QString(self->errorString());
}

//  QCborParserError::~QCborParserError()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QCborParserErrorD1Ev(QCborParserError *self) {
  delete self;
}
